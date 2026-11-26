#!/usr/bin/env python3
"""Decode a Baofeng DM-32UV CPS codeplug (.data) into JSON for the cheat sheet.

Usage: decode.py <codeplug.data> <out.json>

The .data format is Baofeng's undocumented binary. The layout below was worked
out by hand from one file (firmware string DM32.00.01.048, CPS read 2026-11) and
checked against the CPS, the W7AW repeater page and SeattleDMR.org's CSVs.
See AGENTS.md -> "Codeplug format notes" before changing anything here.
"""
import json
import re
import struct
import sys

# ---- channels -------------------------------------------------------------
CH_PAGE0 = 0x21000      # u16 channel count at +0, records start at +0x10
CH_REC = 0x30           # 48-byte channel record
CH_PAGE0_N = 84         # records in the first page (after the header)
CH_PER_PAGE = 85        # records in each later 4 KiB page (0x22000, 0x23000, ...)

# ---- zones ----------------------------------------------------------------
ZONE_PAGE0 = 0x11010    # first page has a 16-byte header
ZONE_PAGES = range(0x12000, 0x15000, 0x1000)   # later pages start at +0
ZONE_REC = 0x91         # 16 name + 1 count + 64 x u16 channel numbers
ZONES_PER_PAGE = 28

# ---- talkgroups / contacts -------------------------------------------------
TG_PAGE0 = 0x1c000      # first page has a 2-byte header
TG_END = 0x20000
TG_REC = 0x18           # 16 name + 1 pad + 3-byte LE ID + 4 bytes flags


def bcd_mhz(b):
    """4 bytes little-endian BCD in 10 Hz units -> MHz float, or None."""
    h = b[::-1].hex()
    return int(h) / 1e5 if re.fullmatch(r'[0-9]{8}', h) else None


def tone(b):
    """2-byte LE tone field -> '141.3', 'D172' (DCS, high nibble set) or None."""
    if b == b'\xff\xff':
        return None
    h = b[::-1].hex()
    if h[0] in '89abcdef':
        return 'D' + h[1:]          # DCS -- only one example seen (V71 Lynwood); verify in CPS
    return f"{int(h) / 10:.1f}"


def name(b):
    return b.split(b'\0')[0].decode('latin1').strip()


def ch_offset(i):
    if i <= CH_PAGE0_N:
        return CH_PAGE0 + 0x10 + (i - 1) * CH_REC
    k = i - CH_PAGE0_N - 1
    return CH_PAGE0 + 0x1000 + (k // CH_PER_PAGE) * 0x1000 + (k % CH_PER_PAGE) * CH_REC


def channels(d):
    n = struct.unpack_from('<H', d, CH_PAGE0)[0]
    out = {}
    for i in range(1, n + 1):
        o = ch_offset(i)
        r = d[o + 24:o + 48]
        c = dict(name=name(d[o:o + 16]), rx=bcd_mhz(d[o + 16:o + 20]), tx=bcd_mhz(d[o + 20:o + 24]))
        c['dig'] = bool(r[0] & 0x10)
        if c['dig']:
            c['cc'] = r[5] & 0x0f
            c['slot'] = 2 if r[5] & 0x10 else 1
        else:
            c['rxt'] = tone(r[9:11])        # tone required to unmute (tone squelch)
            c['txt'] = tone(r[11:13])       # tone transmitted
        out[i] = c
    return out


def zones(d):
    out = []
    starts = [(ZONE_PAGE0, ZONE_PAGE0 & ~0xfff)] + [(p, p) for p in ZONE_PAGES]
    for start, page in starts:
        for k in range(ZONES_PER_PAGE):
            z = start + k * ZONE_REC
            if z + ZONE_REC > page + 0x1000:
                break
            nm = d[z:z + 16].split(b'\0')[0]
            if not nm or nm[0] == 0xff:
                continue
            if not all(32 <= c < 127 for c in nm):
                return out          # past the last real zone: stale bytes follow
            cnt = d[z + 0x10]
            mem = [struct.unpack_from('<H', d, z + 0x11 + 2 * i)[0] for i in range(cnt)]
            out.append(dict(name=nm.decode('latin1'), mem=mem))
    return out


def talkgroups(d):
    tgs = {}
    for page in range(TG_PAGE0, TG_END, 0x1000):
        o = page + 2 if page == TG_PAGE0 else page
        while o + TG_REC <= page + 0x1000:
            nm = d[o:o + 16].split(b'\0')[0]
            if nm and nm[0] != 0xff and all(32 <= c < 127 for c in nm):
                tgs[nm.decode()] = int.from_bytes(d[o + 17:o + 20], 'little')
            o += TG_REC
    return tgs


# ---- programmable keys (radio settings page) --------------------------------
# Offsets from infamy/DM32-Protocol-Spec 05-DATA-STRUCTURES.md ("Key lock and button
# functions", block 0x04 +0x085..0x093). In this .data file that block is the page at 0x5000.
SETTINGS = 0x5000
KEY_SLOTS = [('SK1', 'short', 0x87), ('SK1', 'long', 0x88), ('SK2', 'short', 0x89), ('SK2', 'long', 0x8a),
             ('P1', 'short', 0x8d), ('P1', 'long', 0x8e), ('P2', 'short', 0x8f), ('P2', 'long', 0x90)]
LONG_PRESS = 0x93       # stored 0-4, shown 1-5 s (spec); Baofeng's Part 6 guide says the default is 3 s
KEY_FUNCS = ("None,Power Select,Volt,Talkaround,Digital Encrypt,Call,VOX,V/M,Alarm,One Touch Call 1,"
             "One Touch Call 2,One Touch Call 3,One Touch Call 4,One Touch Call 5,SMS,CSV Contacts,Zone Up,"
             "Zone Down,Scan,Record Switch,Previous Record,Next Record,FM Radio,FM Search,GPS Information,"
             "Monitor,Switch Main Channel,Lone Work,Keypad Lock,Nuisance Channel Delete,TBST Send,APRS Send,"
             "Channel Type,Display Mode,CTC Scan,CTC Setting,Silent Tone,Roaming,Sub-PTT,"
             "Analog Scramble Switch,One Key Scan Freq,Flashlight,Man Down Alarm").split(',')


def keys(d):
    out = []
    for key, press, off in KEY_SLOTS:
        v = d[SETTINGS + off]
        out.append(dict(key=key, press=press, code=v, func=KEY_FUNCS[v] if v < len(KEY_FUNCS) else f'?{v}'))
    raw = d[SETTINGS + LONG_PRESS]
    return dict(buttons=out, long_press_raw=raw, long_press_s=raw + 1 if raw <= 4 else None)


def main(src, dst):
    d = open(src, 'rb').read()
    ch = channels(d)
    zs = zones(d)
    out = []
    for i, z in enumerate(zs, 1):
        cs = [ch[m] for m in z['mem']]
        nd = sum(c['dig'] for c in cs)
        kind = 'DMR' if nd == len(cs) else ('FM' if nd == 0 else 'Mixed')
        out.append(dict(num=i, name=z['name'], kind=kind, chans=cs))
    fw = re.search(rb'DM32\.[0-9.]+', d[:0x100])
    meta = dict(source=src.rsplit('/', 1)[-1], firmware=fw.group().decode() if fw else None,
                channels=len(ch), zones=len(out))
    json.dump(dict(meta=meta, zones=out, tgs=talkgroups(d), keys=keys(d)), open(dst, 'w'), indent=1)
    print(f"{meta['source']}: firmware {meta['firmware']}, {len(ch)} channels, {len(out)} zones -> {dst}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
