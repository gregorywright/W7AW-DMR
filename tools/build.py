#!/usr/bin/env python3
"""Build the W7AW DM-32UV cheat sheet (HTML) from the decoded codeplug data."""
import json
from html import escape as e

import sys
SRC = sys.argv[1] if len(sys.argv) > 1 else 'build/sheet.json'
DST = sys.argv[2] if len(sys.argv) > 2 else 'build/cheatsheet.html'
D = json.load(open(SRC))
ZONES = {z['num']: z for z in D['zones']}
TGS = D['tgs']

FOOT = "W7AW codeplug <b>BaofengDM32UV_NWDMR</b> by Tom N7OEP &middot; data read from the codeplug file 2026-11-24"


def mhz(f):
    s = f"{f:.4f}".rstrip('0')
    if len(s.split('.')[1]) < 3:
        s = f"{f:.3f}"
    return s


def offset(c):
    d = round(c['tx'] - c['rx'], 4)
    if abs(d) < 1e-6:
        return '<span class="simp">simplex</span>'
    if abs(abs(d) - 5) < 1e-6 or abs(abs(d) - 0.6) < 1e-6 or abs(abs(d) - 1.0) < 1e-6 or abs(abs(d) - 9) < 1e-6:
        sign = '+' if d > 0 else '&minus;'
        v = f"{abs(d):g}"
        return f'<span class="off">{sign}{v}</span>'
    return f'<span class="off">TX {mhz(c["tx"])}</span>'


def tone(c):
    t = c.get('txt')
    if not t:
        return '<span class="none">&mdash;</span>'
    label = f"DCS {t[1:]}" if t.startswith('D') else t
    sq = ' <span class="sq">SQ</span>' if c.get('rxt') else ''
    return f'<span class="tone">{label}</span>{sq}'


def page(n, title, sub, body, accent='navy'):
    return f'''
<section class="page">
  <header class="band {accent}">
    <div class="ttl">{title}</div>
    <div class="sub">{sub}</div>
  </header>
  <main>{body}</main>
  <footer><span>{FOOT}</span><span class="pg">Page {n} of 5</span></footer>
</section>'''



DESC = {'V/M': 'Channel &harr; frequency mode', 'Monitor': 'Monitor (open squelch)',
        'Power Select': 'Power L &rarr; M &rarr; H', 'GPS Information': 'GPS info',
        'Zone Up': 'Next zone', 'Zone Down': 'Previous zone', 'Scan': 'Scan &sup1;', 'Flashlight': 'Flashlight &sup2;'}


def keys_table():
    k = {(b['key'], b['press']): b['func'] for b in D['keys']['buttons']}
    lp = D['keys']['long_press_s']
    rows = ''.join(f'<tr><td><span class="key">{key}</span></td><td>{DESC.get(k[(key, "short")], k[(key, "short")])}</td>'
                   f'<td>{DESC.get(k[(key, "long")], k[(key, "long")])}</td></tr>' for key in ('SK1', 'SK2', 'P1', 'P2'))
    return (f'<table class="keys"><tr class="kh"><th>Key</th><th>Short press</th><th>Long press<br>'
            f'<span class="h2n">hold {lp} s</span></th></tr>{rows}'
            f'<tr><td><span class="key">&#9650;</span><span class="key">&#9660;</span></td><td colspan="2">Channel up / down (or turn the top knob)</td></tr></table>'
            '<p class="fn">SK1 is just below PTT, SK2 below it. P1 and P2 are left and right of the rocker under the screen.<br>'
            '&sup1; Scan starts only after a scan list is chosen in the radio menu. '
            '&sup2; The manual shows no flashlight on this radio, so this may do nothing.</p>')

# ---------------------------------------------------------------- page 1
def page1():
    west = ZONES[11]['chans']
    key = [15, 17, 18, 12, 13]
    rows = ''
    use = {15: 'Echo test &mdash; hear yourself played back',
           17: 'City-wide Seattle calling channel',
           18: 'City-wide Seattle, second slot',
           12: 'Local talkgroup 1',
           13: 'Local talkgroup 2'}
    for k in key:
        c = west[k - 1]
        tg = c['name'].rsplit(' ', 1)[0]
        hl = ' class="hl"' if k in (15, 17) else ''
        rows += (f'<tr{hl}><td class="chn">{k}</td><td class="nm">{e(c["name"])}</td>'
                 f'<td><span class="ts ts{c["slot"]}">TS{c["slot"]}</span></td>'
                 f'<td class="mono">{TGS[tg]}</td><td>{use[k]}</td></tr>')
    u11 = ZONES[1]['chans'][10]
    v04 = ZONES[3]['chans'][4]
    return page(1, 'W7AW &middot; West Seattle ARC &mdash; DM-32UV Quick Card',
                'Your club repeaters, where they are in the radio, and how to get there', f'''
<div class="cards">
  <div class="card dmr">
    <div class="ctag">DMR &middot; 70 cm</div>
    <div class="cname">W7AW DMR repeater</div>
    <div class="where">Zone <b class="big">11</b> <span class="zn">Seattle/West</span></div>
    <div class="spec mono">440.975 &nbsp;+5.000 &nbsp;CC 2</div>
    <div class="note">Channels end in <b>SWE</b> &middot; Myrtle Reservoir Park</div>
  </div>
  <div class="card fm">
    <div class="ctag">Analog FM &middot; 70 cm</div>
    <div class="cname">W7AW 70 cm repeater</div>
    <div class="where">Zone <b class="big">1</b> <span class="zn">ACS UHF</span> &middot; Ch <b class="big">11</b></div>
    <div class="spec mono">{mhz(u11['rx'])} &nbsp;+5.000 &nbsp;{u11['txt']} Hz</div>
    <div class="note">Channel <b>{e(u11['name'])}</b> &middot; tone sent and required</div>
  </div>
  <div class="card fm">
    <div class="ctag">Analog FM &middot; 2 m</div>
    <div class="cname">W7AW 2 m repeater</div>
    <div class="where">Zone <b class="big">3</b> <span class="zn">ACS VHF</span> &middot; Ch <b class="big">5</b></div>
    <div class="spec mono">{mhz(v04['rx'])} &nbsp;&minus;0.600 &nbsp;{v04['txt']} Hz</div>
    <div class="note">Channel <b>{e(v04['name'])}</b> &middot; tone sent only</div>
  </div>
</div>

<div class="net">
  <b>Weekly Net:</b> every <b>Monday 6:30 pm</b> (early check-in 6:15) on the linked
  <b>70 cm, 2 m and 6 m</b> analog repeaters. The DMR repeater is <u>not</u> linked to them.
  The 6 m repeater (53.290) is outside this radio&rsquo;s range.
</div>

<h2 class="dmrh">Key DMR channels &mdash; Zone 11 Seattle/West</h2>
<table class="grid">
  <thead><tr><th>Ch</th><th>Channel name</th><th>Slot</th><th>TG ID</th><th>What it&rsquo;s for</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<p class="small">All 21 DMR channels are on page 2. The same channel numbers work in every Seattle DMR zone.</p>

<div class="two">
  <div>
    <h2>Getting to a channel</h2>
    <ol class="steps">
      <li>If you see a bare frequency, short-press <span class="key">SK1</span> to switch to channel mode.</li>
      <li>Short-press <span class="key">P1</span> (next zone, 12&rarr;13) or <span class="key">P2</span> (previous zone) until the <b>zone name</b> is right.</li>
      <li>Turn the <b>top knob</b> (or <span class="key">&#9650;</span>/<span class="key">&#9660;</span>) to the <b>channel number</b>.</li>
      <li>The <b>&gt;</b> marks the half of the screen you control. Switch halves with the red <b>&#8962; Back</b> key on the right (house icon).</li>
    </ol>
    <h2>Parrot test (DMR)</h2>
    <ol class="steps">
      <li>Zone 11, <b>Ch 15 Parrot 1 SWE</b>.</li>
      <li>Hold PTT, <b>wait &frac12; second</b>, give your call, release.</li>
      <li>You should hear yourself played back.</li>
    </ol>
    <div class="tip warn"><b>Before transmitting on DMR</b>, your own Radio ID from
      RadioID.net must be in <b>Digital &rarr; DMR ID</b> (row 1) in the CPS.</div>
  </div>
  <div>
    <h2>Buttons <span class="h2n">(as set in this codeplug)</span></h2>
    {keys_table()}
    <div class="tip"><b>Dual display:</b> Menu &rarr; Settings &rarr; Radio settings &rarr;
      Display Func &rarr; Dual Watch &rarr; <b>Double Wait</b></div>
  </div>
</div>
''')


# ---------------------------------------------------------------- page 2
USE = {
    'Audio Test 2': 'Audio test', 'BEARS 1': 'Boeing BEARS group', 'BEARS 2': 'Boeing BEARS group',
    'Baynet 2': 'BayNet', 'King County': 'King County',
    'Link 1': 'Spare link &dagger;', 'Link 2': 'Spare link &dagger;', 'Link 3': 'Spare link &dagger;',
    'Link 4': 'Spare link &dagger;', 'Link 5': 'Spare link &dagger;', 'Link 6': 'Spare link &dagger;',
    'Local 1': 'Local', 'Local 2': 'Local', 'PNW Rgnl 2': 'Pacific Northwest region',
    'Parrot 1': '<b>Echo test &mdash; hear yourself</b>', 'Puget Sound': 'Puget Sound area',
    'Seattle 1': '<b>Seattle city-wide &mdash; start here</b>', 'Seattle 2': '<b>Seattle city-wide</b>',
    'TAC 313-2': 'Tactical (move a QSO here)', 'Washington 1': 'Washington statewide',
    'Washington 2': 'Washington statewide',
}


def page2():
    zinfo = [
        (11, 'Seattle/West', 'SWE', 'W7AW &middot; Myrtle Res.', True),
        (9, 'Seattle/Central', 'SCE', 'PSRG &middot; Capitol Hill', False),
        (10, 'Seattle/North', 'LFP', 'ACS &middot; Lake Forest Pk', False),
        (8, 'BEARS W.Tiger', 'BWT', 'BEARS &middot; W. Tiger Mtn', False),
        (12, 'SeattleDMR', 'HOT', 'Personal hotspot', False),
    ]
    cards = ''
    for num, name, suf, where, club in zinfo:
        c = ZONES[num]['chans'][0]
        cards += (f'<div class="zc{" club" if club else ""}"><div class="zcn">Zone <b>{num}</b></div>'
                  f'<div class="zcname">{name}</div><div class="mono zcf">{mhz(c["rx"])}</div>'
                  f'<div class="zcw">{where}</div><div class="zcs">ends in <b class="mono">{suf}</b></div></div>')
    rows = ''
    for i, c in enumerate(ZONES[11]['chans'], 1):
        tg = c['name'].rsplit(' ', 1)[0]
        hl = ' class="hl"' if tg in ('Seattle 1', 'Seattle 2', 'Parrot 1') else ''
        rows += (f'<tr{hl}><td class="chn">{i}</td><td class="nm">{e(tg)}</td>'
                 f'<td class="mono r">{TGS[tg]}</td><td><span class="ts ts{c["slot"]}">TS{c["slot"]}</span></td>'
                 f'<td>{USE.get(tg, "")}</td></tr>')
    return page(2, 'Seattle DMR &mdash; same channels in every zone',
                'Pick the zone for the repeater you can reach; the channel numbers stay the same', f'''
<div class="zcards">{cards}</div>
<p class="small c">All five zones: color code <b>2</b>, offset <b>+5 MHz</b> (hotspot: TX 439.4375).
 The channel name is the talkgroup plus the zone&rsquo;s 3-letter ending, e.g. <b class="mono">Seattle 1 SWE</b>.</p>
<table class="grid big2">
  <thead><tr><th>Ch</th><th>Talkgroup</th><th class="r">TG ID</th><th>Slot</th><th>Who hears you / use</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<div class="two tight">
  <div class="tip"><b>Time slots:</b> <span class="ts ts1">TS1</span> and <span class="ts ts2">TS2</span> are two
    separate conversations on the same repeater. The radio picks the slot for you from the channel.</div>
  <div class="tip">&dagger; <b>Link 1&ndash;6</b> are spare SeattleDMR talkgroups that an administrator can patch to other
    networks when needed. TG IDs and slots match SeattleDMR.org&rsquo;s list.</div>
</div>

''', accent='blue')


# ---------------------------------------------------------------- pages 3/4
def fm_table(chans, start, hl_names=()):
    rows = ''
    for i, c in enumerate(chans, start):
        hl = ' class="hl"' if c['name'] in hl_names else ''
        rows += (f'<tr{hl}><td class="chn">{i}</td><td class="nm">{e(c["name"])}</td>'
                 f'<td class="mono r">{mhz(c["rx"])}</td><td class="mono">{offset(c)}</td><td class="mono">{tone(c)}</td></tr>')
    return (f'<table class="grid fmt"><colgroup><col style="width:8.5%"><col style="width:34%"><col style="width:18%"><col style="width:16%"><col style="width:23.5%"></colgroup>'
            f'<thead><tr><th>Ch</th><th>Name</th><th class="r">RX</th>'
            f'<th>Offset</th><th>Tone</th></tr></thead><tbody>{rows}</tbody></table>')


LEGEND = ('<p class="small legend"><b>Tone</b> = CTCSS tone sent (Hz). <span class="sq">SQ</span> = radio also '
          'requires that tone to unmute. <span class="simp">simplex</span> = transmit and receive on the same frequency. '
          '<span class="hlbox">Highlighted</span> = W7AW repeater.</p>')


def page3():
    ch = ZONES[1]['chans']
    hl = ('U11 West Sea',)
    return page(3, 'Zone 1 &middot; ACS UHF &mdash; Seattle-area 70 cm analog',
                '64 channels &middot; Seattle ACS channel plan &middot; U = UHF channel number', f'''
{LEGEND}
<div class="two cols">{fm_table(ch[:32], 1, hl)}{fm_table(ch[32:], 33, hl)}</div>
''', accent='green')


def page4():
    ch = ZONES[3]['chans']
    hl = ('V04 WEST SEA',)
    wx = ZONES[5]['chans']
    return page(4, 'Zone 3 &middot; ACS VHF &mdash; Seattle-area 2 m analog',
                '47 channels &middot; plus NOAA weather (Zone 5)', f'''
{LEGEND}
<div class="two cols">{fm_table(ch[:24], 1, hl)}{fm_table(ch[24:], 25, hl)}</div>
<div class="two cols wxrow">
  <div class="tip fmtip"><b>Zone 5 &middot; NOAA weather</b> (receive only)<br>
    <span class="mono wx">{" &middot; ".join(f"<b>{e(c['name'])}</b> {mhz(c['rx'])}" for c in wx)}</span><br>
    Seattle&rsquo;s station KHB60 is <b>WX1</b> 162.550.</div>
  <div class="tip fmtip"><b>Data zones (not for voice):</b> Zone 2 ACS UHF Data and Zone 4 ACS VHF Data hold packet,
    APRS and Winlink frequencies, e.g. <span class="mono">439.850 W7AW-10</span>, <span class="mono">144.390 APRS</span>.</div>
</div>
''', accent='green')


# ---------------------------------------------------------------- page 5
def page5():
    zs = D['zones']
    club = {1, 3, 11}
    seattle = {6, 8, 9, 10, 12, 25, 26, 81, 82, 84, 90, 91, 92, 93}
    per = 34
    cols = ''
    for k in range(3):
        rows = ''
        for z in zs[k * per:(k + 1) * per]:
            cls = 'club' if z['num'] in club else ('sea' if z['num'] in seattle else '')
            tag = f'<span class="kt {z["kind"].lower()}">{z["kind"]}</span>'
            rows += (f'<tr class="{cls}"><td class="chn">{z["num"]}</td><td class="nm">{e(z["name"])}</td>'
                     f'<td>{tag}</td><td class="r mono">{len(z["chans"])}</td></tr>')
        cols += (f'<table class="grid zi"><colgroup><col style="width:12.5%"><col style="width:59%"><col style="width:16.5%"><col style="width:12%"></colgroup><thead><tr><th>#</th><th>Zone</th><th>Type</th><th class="r">Ch</th>'
                 f'</tr></thead><tbody>{rows}</tbody></table>')
    return page(5, 'Zone index &mdash; all 102 zones in P1/P2 order',
                'P1 short = next zone (e.g. 12 &rarr; 13) &middot; P2 short = previous zone', f'''
<p class="small legend"><span class="hlbox">Gold</span> = W7AW repeaters &nbsp;
<span class="seabox">Blue</span> = other Seattle-area zones &nbsp;
<span class="kt dmr">DMR</span> digital &nbsp; <span class="kt fm">FM</span> analog.
Most DMR zones hold one repeater with its talkgroups.</p>
<div class="three">{cols}</div>
''', accent='navy')


CSS = '''
@page { size: letter; margin: 0; }
:root { --navy:#1f3a5f; --blue:#1e5aa8; --green:#2e7d4f; --gold:#f6d77a; --goldbg:#fff4cc;
        --ink:#1b1f24; --muted:#5b6470; --line:#c9d1db; --stripe:#f2f5f9; --ts1:#1e5aa8; --ts2:#c25e00; }
* { box-sizing:border-box; }
html,body { margin:0; padding:0; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color:var(--ink); font-size:13pt; line-height:1.3; }
.mono { font-family: Menlo, "SF Mono", Consolas, monospace; }
.page { width:8.5in; height:11in; padding:0.35in 0.35in 0.5in; position:relative; page-break-after:always; overflow:hidden; }
.page:last-child { page-break-after:auto; }
.band { color:#fff; border-radius:10px; padding:10px 16px 9px; margin-bottom:12px; }
.band.navy { background:var(--navy); } .band.blue { background:var(--blue); } .band.green { background:var(--green); }
.ttl { font-size:21pt; font-weight:800; letter-spacing:.2px; }
.sub { font-size:12pt; opacity:.92; margin-top:2px; }
h2 { font-size:14pt; margin:9px 0 5px; color:var(--navy); border-bottom:2px solid var(--line); padding-bottom:2px; }
h2.dmrh { color:var(--blue); } h2.fmh { color:var(--green); }
footer { position:absolute; left:0.35in; right:0.35in; bottom:0.2in; font-size:8.5pt; color:var(--muted);
         display:flex; justify-content:space-between; gap:12px; border-top:1px solid var(--line); padding-top:4px; }
footer .pg { white-space:nowrap; font-weight:700; }
.small { font-size:10.5pt; color:var(--muted); margin:5px 0; } .c { text-align:center; }
.r { text-align:right; }
/* cards */
.cards { display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; }
.card { border:2px solid var(--line); border-radius:10px; padding:7px 9px; background:#fff; }
.card.dmr { border-color:var(--blue); background:#eef4fc; } .card.fm { border-color:var(--green); background:#eef7f1; }
.ctag { font-size:10pt; font-weight:800; text-transform:uppercase; letter-spacing:.6px; }
.dmr .ctag { color:var(--blue); } .fm .ctag { color:var(--green); }
.cname { font-size:13pt; font-weight:700; margin:2px 0 4px; }
.where { font-size:12pt; white-space:nowrap; } .where .big { font-size:17pt; } .zn { font-weight:700; }
.spec { white-space:nowrap; font-size:10.5pt; font-weight:700; margin-top:3px; background:#fff; border:1px solid var(--line); border-radius:6px; padding:2px 6px; display:inline-block; }
.note { font-size:10.5pt; color:var(--muted); margin-top:4px; }
.net { margin:9px 0 0; background:var(--goldbg); border-left:6px solid #d9a400; padding:5px 9px; border-radius:6px; font-size:11pt; }
/* tables */
table.grid { border-collapse:separate; border-spacing:0; width:100%; border:1.5px solid #9aa7b6; border-radius:8px; overflow:hidden; }
table.grid th { background:#e3e9f1; color:var(--navy); text-align:left; font-size:11pt; padding:5px 8px; border-bottom:1.5px solid #9aa7b6; }
table.grid td { padding:3px 8px; border-bottom:1px solid #dde3ea; vertical-align:middle; }
table.grid tbody tr:nth-child(even) td { background:var(--stripe); }
table.grid tbody tr:last-child td { border-bottom:none; }
table.grid tr.hl td { background:var(--goldbg) !important; font-weight:700; }
td.chn { font-weight:800; text-align:center; width:2.2em; color:var(--navy); }
td.nm { font-weight:600; }
.big2 td { font-size:12.5pt; padding:2px 9px; }
.ts { display:inline-block; font-family:Menlo,monospace; font-weight:800; font-size:10.5pt; color:#fff; border-radius:5px; padding:0 6px; }
.ts1 { background:var(--ts1); } .ts2 { background:var(--ts2); }
.two { display:grid; grid-template-columns:1fr 1fr; gap:16px; } .two.tight { gap:10px; margin-top:8px; }
.two.cols { gap:9px; align-items:start; }
.three { display:grid; grid-template-columns:1fr 1fr 1fr; gap:7px; align-items:start; }
.steps { margin:3px 0 0 0; padding-left:20px; font-size:11.5pt; } .steps li { margin-bottom:2px; }
.key { display:inline-block; font-family:Menlo,monospace; font-weight:800; font-size:10.5pt; border:1.5px solid #6b7785;
       border-bottom-width:3px; border-radius:5px; padding:0 5px; background:#fafbfc; }
table.keys { border-collapse:collapse; width:100%; font-size:11.5pt; }
table.keys td { padding:2.5px 5px; border-bottom:1px solid #dde3ea; } table.keys tr:nth-child(even) td { background:var(--stripe); }
table.keys td:first-child { white-space:nowrap; width:18%; } table.keys th { text-align:left; font-size:10.5pt; color:var(--navy); background:#e3e9f1; padding:3px 5px; line-height:1.1; }
.h2n { font-size:9.5pt; font-weight:400; color:var(--muted); } .fn { font-size:9.5pt; color:var(--muted); margin:4px 0 0; line-height:1.25; }
.tip { margin-top:7px; background:#eef4fc; border-left:5px solid var(--blue); padding:5px 9px; border-radius:6px; font-size:11pt; }
.tip.warn { background:#fdecea; border-left-color:#c62828; }
/* page 2 zone cards */
.zcards { display:grid; grid-template-columns:repeat(5,1fr); gap:7px; }
.zc { border:1.5px solid var(--blue); border-radius:8px; padding:6px 7px; background:#eef4fc; text-align:center; }
.zc.club { background:var(--goldbg); border-color:#d9a400; border-width:2.5px; }
.zcn { font-size:10.5pt; color:var(--muted); } .zcn b { font-size:15pt; color:var(--ink); }
.zcname { font-weight:800; font-size:11.5pt; } .zcf { font-weight:700; font-size:12pt; color:var(--blue); }
.zcw { font-size:9.5pt; color:var(--muted); line-height:1.15; margin-top:2px; } .zcs { font-size:10pt; margin-top:2px; }
/* FM tables */
.two > *, .three > * { min-width:0; }
table.grid.fmt, table.grid.zi { table-layout:fixed; width:100%; }
.fmt td, .zi td { overflow:hidden; white-space:nowrap; } .zi td.nm { font-size:9.8pt; letter-spacing:-0.1px; }
.fmtip { background:#eef7f1; border-left-color:var(--green); margin-top:0; }
.wx { font-size:10pt; line-height:1.5; }
.fmt td { font-size:11pt; padding:2px 3px; line-height:1.18; } .fmt td.mono { font-size:10pt; } .fmt th { font-size:9.5pt; padding:3px 3px; } .fmt td.chn { font-size:10.5pt; }
.fmt td.nm { white-space:nowrap; }
.tone { font-weight:700; color:var(--green); } .sq { display:inline-block; font-size:7.5pt; font-weight:800; color:#fff; background:#7a4fb3; border-radius:4px; padding:0 4px; font-family:Helvetica,Arial,sans-serif; vertical-align:1px; }
.simp { color:#b26a00; font-weight:700; font-size:9pt; } .off { font-weight:600; } .none { color:#aab3bd; }
.legend { color:var(--ink); }
.hlbox { background:var(--goldbg); border:1px solid #d9a400; padding:0 5px; border-radius:4px; font-weight:700; }
.seabox { background:#dbe8f8; border:1px solid var(--blue); padding:0 5px; border-radius:4px; font-weight:700; }
.wxrow { margin-top:6px; }
/* zone index */
.zi td { font-size:10pt; padding:1.6px 3px; line-height:1.15; } .zi th { font-size:9.5pt; padding:3px 3px; } .zi td.chn{width:auto}
.zi td.nm { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:1.55in; }
.zi tr.club td { background:var(--goldbg) !important; font-weight:800; }
.zi tr.sea td { background:#dbe8f8 !important; }
.kt { display:inline-block; font-size:8.5pt; font-weight:800; border-radius:4px; padding:0 4px; color:#fff; }
.kt.dmr { background:var(--blue); } .kt.fm { background:var(--green); } .kt.mixed { background:#777; }
'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>W7AW DM-32UV Cheat Sheet</title>
<style>{CSS}</style></head><body>
{page1()}{page2()}{page3()}{page4()}{page5()}
</body></html>'''
open(DST, 'w').write(html)
print(f'wrote {DST}')
