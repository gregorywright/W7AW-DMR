# Plan: W7AW DM-32UV Starter Guide

Status: **planning only, not built yet.** Content decisions come from Greg (2026-11-26). Research checks from
2026-11-26 are folded in below (see "Where the facts come from" at the end).
While the Starter Guide is being built, **leave the existing 5-page Reference Sheet unchanged.**

## Title (decided 2026-11-26)

**W7AW DM-32UV Starter Guide.** The existing 5 pages are the **Reference Sheet**, for people who already use the radio.

## Goal, audience and format

- **Goal:** get a new owner's radio tuned and make a first contact, without overwhelming them. Fine detail goes later in
  the guide, or stays on the Reference Sheet.
- **Readers:** licensed hams who already know how to work a repeater, but who are **new to this radio, to DMR, or both**.
  Greg is the model reader. **Don't** explain basic ham operating (net check-in, what a repeater is).
- **Format:** most readers will view it on a phone or computer, so there is **no page limit**. **Page 1 carries only
  what matters most** to someone new to DMR and to this radio. Keep tiny details off the first pages.
- **Don't assume two channels on screen.** Some readers set the radio to show one channel at a time. Mention the red
  A/B (⌂) key only as "if your screen shows two channels".
- Legibility rules as on the Reference Sheet: large type, high contrast, colour plus bold. Same colours: blue = DMR,
  green = analog FM, gold = W7AW. Letter paper.

## Proposed outline (for Greg to agree)

Ordered the way a first-time owner goes. Each section: its purpose, then at most five key points.
Details and sources for each section are in "Section details" below.

**Page 1: Start here** (page 1 holds this and nothing else)
Purpose: show the whole path to a first contact on one page, plus the things that can't wait.
- The steps, one line each: open the box and charge; get your FCC license copy and DMR ID; get the club codeplug
  installed; check the radio shows your own ID; learn the few basics; make your first contacts. Each line points to its section.
- **Start your DMR ID while the battery charges.** RadioID approval often comes within an hour or so, but it can take longer.
- **Screw the antenna on before you ever press PTT** (the longest one, if the radio came with more than one).
- **The easy way:** bring the charged radio, your callsign and your DMR ID to the Elmers' Breakfast and get the club codeplug put in.
- **Don't update the firmware** until the radio works (one line; the full warning is section 10).

**1. Open the box, charge, fit the antenna**
Purpose: a charged radio with its antenna on.
- The battery comes uncharged. Charge it with the **radio off**, in the desk charger or from the USB-C port on the back of the battery.
- Desk charger light: red = charging, green = full.
- Antenna: if the radio came with more than one, start with the **longest** for the best chance of reception; switch to a
  shorter one later, once the radio works, if you like. Screw it on clockwise, finger tight. Never transmit without it.
- Turn on: turn the power/volume knob (right edge) clockwise until it clicks.
- Keys do nothing? The keypad is locked: press Menu, then `*`.

**2. Your FCC license copy and DMR ID**
Purpose: get the DMR ID the radio needs before it transmits on DMR.
- Download the **official copy** of your license from the FCC License Manager. A screenshot isn't accepted.
- If nothing downloads, allow pop-ups for fcc.gov (Greg's problem was an ad blocker).
- Register at RadioID.net and upload the PDF. Approval often comes within an hour or so (Greg's took about an hour).
- Answer RadioID's yearly email, or your ID will eventually stop working.

**3. Get the club codeplug installed**
Purpose: Tom N7OEP's club codeplug in the radio, with your own ID in it.
- The easy way: the Elmers' Breakfast (1st Saturday) or the club meeting (3rd Saturday). Check the calendar for times.
- Bring the charged radio, your callsign and your DMR ID.
- Doing it yourself: a short box (Windows, the official CPS, the cable in the speaker-mic jack, read and save first).

**4. Check the radio shows your own ID**
Purpose: make sure you never transmit on DMR as someone else.
- The club file holds a placeholder ID, **1234567 "BLANK"**. Your radio must show your own DMR ID instead.
- Where to look: Menu → Settings → Device Info → Device Info → DMR ID ("Device Info" twice).
- If you see 1234567, don't transmit on DMR until your ID is put in.

**5. The few basics**
Purpose: enough to pick a channel and talk.
- Facing the screen: antenna on the left, **channel knob** in the middle (it also scrolls menus), **power/volume knob** at the right edge.
- **Zone:** P1 = next zone, P2 = previous. **Channel:** the channel knob or ▲/▼.
- **On DMR, press PTT and pause about 1 second before you talk.**
- SK1 (one ridge) and SK2 (two ridges) are below PTT: find them by feel. SK2 sets the power (L/M/H).
- If your screen shows two channels: the red ▶ marks the one you talk on. Press the red A/B (⌂) key briefly to switch.

**6. First contacts**
Purpose: hear something first, then talk.
- **NOAA weather** (receive only): zone NOAA (zone 5), WX4 162.425. Try other WX channels if it doesn't come in.
- **DMR parrot:** zone 11, ch 15 **Parrot 1 SWE**. Talk, release, and hear yourself played back.
- **Monday net** (analog), 6:30 pm, early check-in 6:15: **U11 West Sea** (zone 1, ch 11) or **V04 WEST SEA** (zone 3, ch 5).
- **DMR Gathering** right after the net, Mondays about 7 pm: **Seattle 1 SWE** (zone 11, ch 17).

**Later sections**

**7. Troubleshooting**
Purpose: fix the common first-week problems.
- A bare frequency and no channel name: get back to channel mode.
- DMR: can't get into the repeater, or hear nothing.
- First words cut off.
- No sound; blank screen at power-on (the programming cable).
- An analog channel is silent (it needs a tone).

**8. Reading the screen**
Purpose: a cleaned-up screen drawing with callouts, so readers know what they're looking at.
- The red ▶ marks the active channel (check how it looks on a one-channel screen).
- L/M/H power; N narrowband; |+| / |-| repeater offset direction.
- CTC: probably "this channel listens for a tone" (inferred, not confirmed).
- DIG/ANA: red idle, blue receiving; the bar is a relative signal meter.

**9. Labeled drawing of the radio**
Purpose: find every key and port.
- PTT, SK1, SK2, P1, P2, Menu, ▲/▼, red A/B (⌂) key, the two knobs.
- Speaker-mic jack (also the programming cable), USB-C on the battery (charging only), top LED.
- Each key's short-press and press-and-hold (about a second) function in the club codeplug.

**10. Firmware: a warning box**
Purpose: stop new owners from soft-bricking the radio.
- Get the radio working first.
- More than one kind of DM-32UV exists; firmware for the other kind can soft-brick it.
- If you update later, know exactly which firmware your radio needs. How to see your version.

**11. Where to get help**
Purpose: people to ask, without naming anyone.
- Ask on the air at the Monday net, at the Elmers' Breakfast or at the club meeting.
- The club website and calendar. The Reference Sheet for everything else.

**12. QR codes**
Purpose: one tap from a printed copy to the sites, without scrolling.
- Each section that names a site carries its codes (Greg, 2026-11-26): section 2 FCC License Manager and RadioID.net;
  section 3 codeplug page, calendar and Baofeng's CPS download page; the Monday page repeaters, calendar and club home;
  help calendar, club home and codeplug page. None on page 1.
- The full set is also on its own last page. Scan each with a phone before printing.

**Ordering questions for Greg**
- **DMR ID first?** An owner can start the DMR ID before the radio even arrives. The outline keeps it second, as you
  open the box, with "start it while the battery charges" on page 1.
- **Firmware line on page 1?** The outline puts one line there because a soft-brick is the worst first-week mistake. The
  alternative is to keep all firmware text in section 10.
- **Radio drawing earlier?** Section 5 names keys before the drawing (section 9) shows them. Moving the drawing next to
  section 5 helps first-time readers but makes the opening longer.
- **The do-it-yourself box:** inside section 3 (as now) or moved to a later section, so page-1 readers aren't put off.

## Section details

Layout notes for the draft (2026-11-26): section 4 shares a page with section 5, and the Monday net / DMR Gathering part
of section 6 has its own page, so the in-context QR codes fit without small text. Footer on every page, exactly:
"W7AW DM-32UV Starter Guide for the club codeplug by Tom N7OEP · check everything against your own radio".

### Page 1 and section 1: open the box, charge, antenna
- Box contents: the manual's §1 packing list. Baofeng's product page shows a drop-in desk charger. Check both against Greg's box before printing.
- Battery: Li-ion, not charged at the factory (manual §3.1, Appendix B).
- Charging: **USB-C is on the back of the battery and only charges it** (manual §3.6, §4.1 item 14: "Type-C charge port").
  The old plan said the radio "charges through the USB-C port" and put USB-C on the radio drawing as a port; both are corrected.
  Charge with the radio off, because the charger light may never turn green with it on (manual §3.4). Charger light: red = charging, green = full (§3.5).
- Antenna: clockwise, finger tight (manual §2.1). Leave the connector type off: it's SMA by a single retailer source.
- **More than one antenna:** Greg's radio came with short, medium and long antennas (2026-11-26). Single source (one radio): print "for example short, medium and long". Tell readers to start
  with the longest for the best chance of reception and switch to a shorter one later, once they know the radio works.
- Power on/off: power/volume knob clockwise to the click, beep after about 3 s; counter-clockwise to the click = off (manual §5.1).
- Keypad lock: holding `*` locks the keypad; unlock with Menu, then `*` (manual §4.2, §5.17). The manual's §9 says radios
  ship keypad-locked (single source). The club codeplug has auto-lock off.

### Section 2: FCC license copy and DMR ID
Your own DMR ID is required before you transmit on DMR. It's free.
1. Get an **official copy** of your FCC license (a PDF). A screenshot or the public ULS search page is not accepted.
   - Sign in to the [FCC ULS License Manager](https://wireless2.fcc.gov/UlsEntry/licManager/login.jsp) with your
     **FRN** and password. If you've forgotten your FRN, look up your callsign in the
     [ULS license search](https://wireless2.fcc.gov/UlsApp/UlsSearch/searchLicense.jsp) (unverified: fcc.gov blocked automated reads).
   - Click **Download Electronic Authorizations**, add your callsign, and click **Download**.
   - The official copy has the FCC logo and an "Official Copy" watermark on each page.
   - **If nothing downloads,** the browser's **pop-up blocker** or ad blocker is probably stopping it. Allow
     pop-ups for fcc.gov and try again. (Greg's cause was an ad blocker, not a VPN or iCloud Private Relay.)
   - FCC help line: 877-480-3201, Mon–Fri 8–6 Eastern, option 2.
   - The FCC steps come from ARRL's guide (secondary); the FCC site itself blocked the research reads.
2. Go to [RadioID.net](https://radioid.net), register, and upload the license PDF.
3. **Approval:** "often within an hour or so". Greg's took about an hour after he uploaded the official copy (reported 2026-11-26).
   One older DMR slide deck from another club (WCARES, 2021) says 1–2 days; the old plan's "about a day" is replaced.
4. **Yearly re-verification:** since July 1, 2026, RadioID sends a yearly email on the account anniversary. No reply means
   the ID is marked unvalidated in year 1 and stops working in year 2 (single secondary source: ARRL New England Division).
   Print only "answer RadioID's yearly email, or your ID will eventually stop working."
5. Bring the ID with you to get the codeplug installed.

### Section 3: get the club codeplug installed
- **The easy way:** bring the **charged radio, your callsign and your DMR ID** to the **Elmers' Breakfast** (1st Saturday)
  or the **club meeting** (3rd Saturday). Ham Jam (1st Monday) might also work; ask the club first.
  Link the [club calendar](https://w7aw.org/calendar/) for current times and places.
- **Doing it yourself (short box),** from Baofeng's Parts One and Two and the firmware research:
  1. You need Windows and the programming cable. The cable goes into the **speaker-mic jack**; the USB-C port can't program the radio.
  2. Get the CPS **only** from Baofeng's [download page](https://www.baofengradio.com/pages/download). Don't print the CPS version.
  3. **Turn the radio on first, then plug in the cable** (with the cable already in, the radio powers up to a blank screen).
     Baofeng's Part Two says cable first; Greg's radio shows why not.
  4. **Program → Read data**, save it as "my radio original", and never change that file. If a read fails, try once more.
  5. Open the club file from the [club codeplug page](https://w7aw.org/dmr-code-plug/). In **Digital → DMR ID**, replace the
     placeholder **1234567 "BLANK"** with your own DMR ID and callsign. **Save As** a new name.
     (The club file is confirmed working only on Greg's firmware; see Open questions.)
  6. **Program → Write data.**
  7. Don't use **File → New** in the CPS: it switches menus to Chinese (confirmed for CPS 1.45; unknown for newer versions).
  - Fine print for the box or the Reference Sheet: port speed 115200 baud (what worked for Greg; the manual's §9 says 256000).
    One CHIRP author saw corrupted reads with CH340 cables (single source), another reason to keep the first backup and verify it
    (the source doesn't say how; a second read compared with the first is one way, untested).

### Section 4: check the radio shows your own ID
- The club codeplug's Radio ID list has one entry, **1234567 "BLANK"** (decoded from the club file downloaded 2026-11-26).
  Anyone who writes the club file without editing it transmits as 1234567.
- **Where to look (Greg's radio, 2026-11-26):** Menu → Settings → Device Info → Device Info → **DMR ID**. "Device Info"
  appears twice in the path; say so on the sheet.

### Section 5: the few basics
- Knob layout, facing the screen (Greg's radio): antenna left, channel knob middle (it also scrolls menus), power/volume knob at the right edge.
- Volume: the power/volume knob (manual §5.2).
- Zone: P1 short = next zone number, P2 short = previous (codeplug; confirmed on Greg's radio).
- Channel: the channel knob, or ▲/▼ in channel mode (manual §4.2, §5.7).
- Power: SK2 short = L/M/H (codeplug).
- Finding SK1 and SK2: SK1 has one ridge, SK2 two (Greg's radio). Say "find them by feel". Don't print the
  ridged-versus-smooth firmware tell.
- **Press and hold = about a second.** Greg found a long press registers after about 1 second on every key he tried
  (2026-11-26). The codeplug value (`0x5093` = 2) was read as 3 s by the protocol spec's scaling, and that reading is
  now in doubt. The guide says "press and hold (about a second)".
- **DMR: press PTT, pause about 1 second, then talk.** The club codeplug has **Talk Permit off**, so there's no go-ahead
  beep (decoded from the file; confirmed by Greg 2026-11-26). The setting is at Menu → Settings → Radio Settings →
  Voice Func → Talk Permit (manual §7.6.1.1).
  PNWDigital puts the repeater's acknowledgement at 0.5–1.5 s, so the old "½ second" was too short.
  **Open decision for Greg:** whether to tell readers they can turn Talk Permit **On**.
- **If your screen shows two channels:** there is one red right-pointing ▶, on the active half; PTT and the knob work on
  that half (manual §4.3, §5.19). **Press** the red A/B (⌂) key briefly to switch halves (manual §5.3). **Holding** ⌂
  switches to frequency (VFO) mode (manual §4.2), which belongs in troubleshooting, not here.

### Section 6: first contacts
1. **NOAA weather, which teaches zones and channels.** Press P1/P2 until the zone reads **NOAA** (zone 5), then turn the
   channel knob until the screen shows **162.42500 / NOAA CH 4** (WX4), as on Greg's radio. In West Seattle WX4 comes in
   best for Greg; if it doesn't come in, try the other WX channels. Receive only.
   weather.gov: 162.425 is **WWG24 "Puget Sound Marine"** (near Port Townsend); 162.550 (WX1) is **KHB60 Seattle** (Cougar Mtn).
2. **DMR parrot:** **Parrot 1 SWE** (zone 11, ch 15, TG 9998). Just talk and it plays you back, with no keys needed.
3. **Monday net (analog):** 6:30 pm, early check-in 6:15, on **U11 West Sea** (zone 1, ch 11) or **V04 WEST SEA**
   (zone 3, ch 5). The net is on the linked analog repeaters, not the DMR repeater.
4. **W7AW DMR Gathering** on the **Seattle 1** talkgroup, Mondays 7:00–7:30 pm, right after the net: **Seattle 1 SWE**
   (zone 11, ch 17). Single source: the club calendar feed (entry updated 2026-11-04). Print "about 7 pm" and "check the calendar".

### Section 7: troubleshooting (ranked)
From the pitfalls research, with long presses changed to "about a second":
1. **A bare frequency shows and the channel name is gone** (frequency/VFO mode): short-press SK1 (V/M), or hold the red ⌂
   key about a second, to get back to channel mode. INFERRED from the codeplug and manual; no forum report found.
2. **DMR: can't get into the repeater:** set power to H (SK2); pick a zone for a repeater you can hear; make sure your own
   Radio ID replaced 1234567.
3. **DMR: you hear nothing:** the radio plays only the talkgroup on the channel you chose. Try Parrot 1 SWE (zone 11, ch 15).
4. **First words cut off, or a "bonk" tone:** pause about 1 second after PTT. A bonk means the slot or talkgroup is busy:
   wait and try again. (PNWDigital and BridgeCom describe the bonk for DMR in general; not yet heard on this radio with the club codeplug.)
5. **No sound from the speaker:** unplug the programming cable (single forum report); check the volume.
6. **Blank screen at power-on:** the cable was plugged in. Unplug it, turn the radio on, then plug it back in.
7. **An analog channel is silent:** the channel needs the repeater's tone (shown as SQ on the Reference Sheet). Hold SK1
   about a second (Monitor) to hear whether anything is there.
8. **Keys do nothing:** the keypad is locked: press Menu, then `*`. For long-press functions, hold about a second.
- "Menus switched to Chinese" moves to the do-it-yourself box (section 3), since most readers get the codeplug put in for them.

### Section 8: reading the screen
Greg's photos of the screen (Dual Watch on, 2026-11-26):

```
 [GPS]          DW          [battery]      status bar
 ▶ L    N |+|          DIG                 top half (▶ = the active half)
     Seattle 1 SWE                         channel name
       440.97500                           receive frequency
 Seattle/West          CH 17               zone · channel number
 A ||||||||||||||||||||||||                top half's signal bar
   L CTC  |+|          ANA                 bottom half
     U11 West Sea / 441.80000 / ACS UHF  CH 11
 B ||||||||||||||||||||||||
 2026/11/26   07:07                        date/time (set from GPS)
 Menu                  A/B                 labels for the two keys under the screen
```

| Icon | Meaning | How confirmed |
|---|---|---|
| red **▶** | the active half: PTT and the knob work on it. There is only one, on the active half. Unverified: whether it shows on a one-channel screen | manual §4.3, §5.3 + Greg's radio |
| **L / M / H** | transmit power | manual §4.3 |
| **N** | narrowband (12.5 kHz) channel | manual §4.3 ("Analog mode"); Greg sees it on DMR channels too. Matches the codeplug bandwidth bit |
| **\|+\| / \|-\|** | the repeater's **offset direction**: transmit above (+) or below (−) the receive frequency. None on simplex | Greg's radio: U11 shows \|+\|, V04 WEST SEA (−0.6) shows \|-\|, simplex WX4 shows neither. The manual also has a separate repeater icon, not seen so far |
| **CTC** | INFERRED: **this channel listens for a tone** (tone squelch) | Greg's radio: shown on U11 (tone both ways), not on V04 (transmit-only tone). Manual draws it as "CT" |
| **DIG / ANA** | digital (DMR) or analog channel. Red = idle, blue = receiving now | manual + Greg's radio only |
| **DW** | Dual Watch (Double Wait) on | manual |
| pin-in-circle | GPS. The manual has two similar pins: one for a fix, one for "GPS on, no fix yet" | manual §4.3 |
| **A / B** + long bar | which half; the bar is a relative signal meter that fills solid blue on receive | Greg's radio |
| **Menu / A/B** labels | on-screen labels for the keys below them. A/B is the red ⌂ key | Greg's radio; manual §5.3 |

- Keys under the screen (Greg's photo): blue **Menu** key (☰) far left, **P1**, the **▲/▼** rocker, **P2**, the red **⌂** key far right.
- Describe the signal bar only as a relative strength indicator, not as S-units (community notes say it isn't calibrated).
- Use a cleaned-up drawing of the screen, not the photo. Show the single-channel view too, or say the second half may not be there.
- Greg could keep his screen photos for reference **outside the repo** (phone photos carry location data, and `docs/photos/` isn't ignored by git).

### Section 9: labeled drawing of the radio
A line drawing (SVG, theme colours, no photo), checked against Greg's radio before printing, with:
- Left side: PTT, SK1 (one ridge) just below, SK2 (two ridges) below SK1 (manual §4.1; Baofeng Part 6).
- Top, facing the screen: antenna left, channel knob middle, power/volume knob right edge. The **top LED**: red = transmit,
  green = receive, slow orange = scanning (manual §4.3).
- Under the screen: Menu, P1, ▲/▼, P2, red ⌂ (A/B).
- Right side: **speaker-mic jack**, labeled "speaker-mic / programming cable" (manual §4.1 item 13).
- Back: rear speaker; **USB-C on the battery, labeled "charging only"**.
- Each key's club-codeplug function, short press and press-and-hold: SK1 V/M / Monitor, SK2 Power / GPS, P1 Zone Up / Scan,
  P2 Zone Down / (nothing useful). Scan needs a scan list chosen in the radio menu first (Baofeng Part 6; AGENTS.md), so say so next to it. **P2 press-and-hold does nothing but beep** on Greg's radio, so the flashlight is left off.
  INFERRED from the decoded key table: no key has the emergency Alarm function in the club codeplug, so no emergency key is drawn.

### Section 10: firmware warning box
Greg's direction: say what we found, get the radio working first, and if you do update, know exactly what you need.
Print no version numbers and no firmware family names. Suggested wording:

> **Firmware: get the radio working first.** Don't update the firmware until the radio works with the club
> codeplug. More than one kind of DM-32UV exists. They look alike and report the same model, and
> firmware meant for the other kind can "soft-brick" the radio (it can be recovered, but you need a computer and the right file).
> If you do decide to update later, **make sure you know exactly which firmware your radio needs** before you start. Ask
> at an Elmers' Breakfast if you're unsure.
>
> **See your version:** blue Menu key → **Settings → Device Info → Versions** (the radio spells it "VerSions").

Background, not for printing (firmware research; community sources that disagree, MEDIUM confidence):
- Families seen: **DM32.01.*** (most common), **DM32.NRF.*** (kept in the same community archive branch as 01.*) and
  **DM32.00.***. 00 and 01 carry mutual soft-brick warnings in the archive.
- **Corrected:** "00.* = HR Vocoder" is wrong as a rule. The HR Vocoder files are particular 00.01 builds, and owners
  report `DM32.00.01.048` (the club file's header string) as a real firmware that took 01.* updates without bricking.
- Baofeng's own download page offers an 01.L01.048 build marked "No Record". The research reads that as "an update can
  remove features" (inferred), one more reason to wait.
- Unofficial firmware and flash tools can erase data unique to the radio (community sources).
- Recovery (two sources): battery out, hold SK1 + PTT, reattach the battery and power on, then reflash the correct file.
- Greg's radio shows `DM32.NRF.01.048`; no public source lists an NRF 048 build. Whether the file header records the
  firmware of the radio it was read from is unknown (inferred from Baofeng's sample file).

### Section 11: where to get help
- The weekly **Monday net** on the air (6:30 pm, early check-in 6:15).
- The **Elmers' Breakfast** (1st Saturday) and the **monthly club meeting** (3rd Saturday).
- The [club website](https://w7aw.org) and the [calendar](https://w7aw.org/calendar/). The Reference Sheet for zones and channels.
- **Don't list Tom N7OEP (or anyone else) as a support contact** until they've agreed to it. Greg will ask Tom first.

### Section 12: QR codes
Club home page, calendar, codeplug page and repeater page (all answer directly, no redirect), and **RadioID.net's home
page** (its Register link is there). The FCC License Manager is included (Greg's request), and so is Baofeng's CPS
[download page](https://www.baofengradio.com/pages/download) (the official CPS source). A short label and the URL under each.
In-context codes are 1.25 in wide, the full set on the last page 1.4 in, each with a 4-module quiet zone.
Generated by `segno` from the project's `.venv` (see AGENTS.md "Python setup"); check each with a phone before printing.

## Club events (checked 2026-11-26)
Always print "check the calendar for current details". **The club's own pages disagree** (open question):
- **Elmers' Breakfast & Help Session:** 1st Saturday at Taste & Best Indo-American Bar & Grill. Monthly Events says
  8:30 am at 4752 California Ave SW; the calendar says 8:00–11:00 at 4727. The restaurant's own site says 4752 and opens at 8:00.
- **Club meeting:** 3rd Saturday, Salvation Army White Center. Monthly Events says 9–11 am; the calendar says 9:30–11:30
  (meeting at 10:00), 9050 16th Ave SW. December and January meetings often move.
- **Ham Jam:** 1st Monday, 5:45–7 pm, Center for Active Living, 4217 SW Oregon St, 2nd floor.
- **Monday Net:** 6:30 pm (early check-in 6:15) on the linked 70 cm, 2 m and 6 m analog repeaters.
- **DMR Gathering:** Mondays 7:00–7:30 pm on Seattle 1 (calendar only).
- Leave off: the 10 m gathering (this radio can't do HF; the club pages also disagree on its day).

## Open questions
- **Talk Permit:** tell readers they can turn it On (Menu → Settings → Radio Settings → Voice Func → Talk Permit)? Default: don't; say "pause about 1 second".
- **Event times and addresses** (above). Default: print the day and the restaurant or hall name only (no times or street numbers), plus "check the calendar".
- **Club codeplug updates:** the codeplug page now says "Updates 9-17-2026 > 11-25-2026". Is Greg's file older than the
  current one? Default: build from the current download once Greg has it.
- **The club page links this project's v1 sheet** as "W7AW Baofeng DM-32UV Reference Guide by Tom N7OEP 11-24-2026" (the
  PDF's title is "W7AW DM-32UV Cheat Sheet"). Default: once the Starter Guide and the fixed Reference Sheet exist, Greg asks
  Tom to update the link.
- **Box contents** (section 1). Default: list only what Greg's box held.
- **Does the club codeplug work on every firmware?** Confirmed only on Greg's radio (`DM32.NRF.01.048`, parrot test);
  no source says either way for other builds. Default: the guide says to get the radio working with the club file first
  and to ask at the Elmers' Breakfast if it misbehaves; it doesn't promise the file fits every radio.
- Does P1 wrap from zone 102 back to zone 1? One user reports a freeze on older firmware. Default: left off the guide.

## Not changed here: fixes for the Reference Sheet and AGENTS.md (Greg's call)
These came out of the research and Greg's checks. This plan doesn't touch either file.
- **Long press:** the Reference Sheet and AGENTS.md say "hold 3 s". Greg's radio registers a long press at about 1 second.
- **"Wait ½ s" after PTT** (Reference Sheet parrot test): about 1 second, since Talk Permit is off.
- **P2 long = Flashlight:** on Greg's radio it does nothing but beep.
- **AGENTS.md fact-check row "Parrot: wait ½ s after PTT"**: about 1 second.
- **AGENTS.md "Starter Guide (new, 1–2 pages)"**: Greg has since dropped the page limit.
- **AGENTS.md:** the manual *does* describe the ⌂ key's A/B use (§5.3); and the |+| icon is the offset direction, not "repeater/duplex".

## Decided NOT to include (for now)
- **A script for checking into the net.** The readers are licensed hams.
- **APRS.** Greg will learn how it works on SeattleDMR from Tom first. Technical notes are in AGENTS.md.
- **Tom (or anyone) as a named support contact** (see section 11).
- **The flashlight:** there isn't one (P2 press-and-hold only beeps).
- **The ridged-versus-smooth button tell** for firmware type, and **firmware version numbers**.

Left out by the planner, not by Greg (he may add them back): "your DMR ID doesn't replace giving your call sign" (basic
operating); the battery screws and the antenna connector type (tiny details).

## Reference Sheet: page 6 ideas (later; don't change the Reference Sheet yet)
- Alan's analog parrot steps (key "12", details in AGENTS.md), clearly labeled analog-only.
- How to set up scanning: scan lists, with 16 entries per list.
- EchoLink node 56575.
- The codeplug version and date, and how to get the latest.
- APRS, once it's understood.

## Where the facts come from
- Greg's decisions and on-radio checks (2026-11-26) override the research where they differ.
- Four research notes from 2026-11-26, kept outside the repo with the Project Agent's evidence: **hardware** (keys, ports,
  screen; manual page images), **firmware** (families, CPS, cable), **onboarding** (FCC, RadioID, club events, NOAA) and
  **pitfalls** (troubleshooting, plus a read-only decode of the club codeplug). Each has a FINDINGS.md with its sources.
- Manual: Baofeng's DM-32UV user manual (the Shopify-hosted copy dated 2024-12-18 was used where the 2025-02-10 file
  couldn't be fetched; section numbers match). Baofeng's "Programming the DM-32UV" Parts 1–7. AGENTS.md for the decoded codeplug.
- Web sources behind the newer claims (secondary unless noted; the guide marks them that way):
  [PNWDigital talk-permit FAQ](https://pnwdigital.net/ufaq/talk-permit-call-tone-why-are-they-essential/) (0.5–1.5 s);
  [ARRL New England Division](https://nediv.arrl.org/category/all/operating/) (RadioID yearly email);
  [ARRL license copy guide](https://www.arrl.org/obtain-license-copy) (FCC steps);
  [M7OCM DM-32UV discussions](https://github.com/M7OCM/DM-32UV/discussions) #5, #8, #16, #22 and READMEs (firmware families, recovery);
  [dm32-info FIRMWARE.md](https://github.com/Chicago-Offline/dm32-info/blob/main/FIRMWARE.md) (firmware, blank screen);
  [club Monthly Events](https://w7aw.org/about-wsarc/monthly-events/) and [calendar](https://w7aw.org/calendar/) (events, DMR Gathering; primary);
  [Baofeng download page](https://www.baofengradio.com/pages/download) (CPS); weather.gov NWR station data (WWG24, KHB60; primary).
