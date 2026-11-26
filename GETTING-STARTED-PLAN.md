# Plan: "Getting Started" sheet for the DM-32UV

Status: **planning only, not built yet** (2026-11-26). Content decisions below come from Greg.
While this sheet is being built, **leave the existing 5-page reference sheet unchanged.**

## Title (decided 2026-11-26)

**W7AW DM-32UV Starter Guide.** The existing 5 pages are the **Reference Sheet**, for people who already use the radio.

## Audience

- **Licensed hams** who already know how to operate on a repeater, but who are **new to this radio,
  to DMR, or both**. Greg is the model reader.
- **Don't** explain basic ham operating, such as how to check into a net or what a repeater is.
- Most readers are older, so use the same legibility rules as the reference sheet: large type, high contrast, colour plus bold.
- Use the same style: blue = DMR, green = analog FM, gold = W7AW. 1–2 pages, letter paper.

## Content (in rough page order)

### 1. Before you start: checklist
- Your amateur license, and your **DMR ID** (see section 2).
- A charged battery (charges through the USB-C port).
- **Antenna on.** Never transmit without it.

### 2. Get your DMR ID (RadioID.net): simple steps
Your own DMR ID is required before you transmit on DMR. It's free, and approval can take about a day.
1. Get an **official copy** of your FCC license (a PDF). A screenshot or the public ULS search page is not accepted.
   - Sign in to the [FCC ULS License Manager](https://wireless2.fcc.gov/UlsEntry/licManager/login.jsp) with your
     **FRN** and password. If you've forgotten your FRN, look up your callsign in the
     [ULS license search](https://wireless2.fcc.gov/UlsApp/UlsSearch/searchLicense.jsp).
   - Click **Download Electronic Authorizations**, add your callsign, and click **Download**.
   - The official copy has the FCC logo and an "Official Copy" watermark on each page.
   - **If nothing downloads,** your browser's **pop-up blocker** or ad blocker is probably stopping it. Allow
     pop-ups for fcc.gov and try again. (This happened to Greg. The cause was an ad blocker, not a VPN.)
   - FCC help line: 877-480-3201.
2. Go to [RadioID.net](https://radioid.net), register, and upload the license PDF.
3. When the ID arrives by email, bring it with you to get the codeplug installed (section 3).

### 3. Get the club codeplug installed
- **The easy way:** bring the **charged radio, your callsign and your DMR ID** to the
  **Elmers' Breakfast** (1st Saturday) or the **club meeting** (3rd Saturday). Ham Jam (1st Monday)
  might also work; ask the club first.
- **Doing it yourself (short box):** see the [club codeplug page](https://w7aw.org/dmr-code-plug/).
  You need Windows and the programming cable. **Turn the radio on first, then plug in the cable.** The port runs at 115200 baud.
  Read and save the radio's original settings before writing anything to it.
- Link to the [club calendar](https://w7aw.org/calendar/) for current times and locations.

### 4. Labeled drawing of the radio
A line drawing (SVG, theme colours, no photo) with these labeled: PTT, SK1 (just below PTT), SK2, P1 and P2
(left and right of the rocker under the screen), the **red ⌂ Back key** (right side, house icon with a return
arrow, switches the top and bottom halves of the screen), the ▲/▼ rocker, the channel knob, the power/volume
knob, the mic/speaker jack and the USB-C port. Add each key's function as set by the club codeplug (short/long press).
Check the drawing against Greg's radio before printing.

### 5. Reading the screen (confirmed from Greg's photos, 2026-11-26)
Greg's two photos of the screen (Dual Watch on):

```
 [GPS]          DW          [battery]      status bar
 ▶ L    N |+|          DIG                 band A (▶ = the half you control)
     Seattle 1 SWE                         channel name
       440.97500                           receive frequency
 Seattle/West          CH 17               zone · channel number
 A ||||||||||||||||||||||||                band A bar
   L CTC  |+|          ANA                 band B
     U11 West Sea / 441.80000 / ACS UHF  CH 11
 B ||||||||||||||||||||||||
 2026/11/26   07:07                        date/time (set from GPS)
 Menu                  A/B                 labels for the two keys under the screen
```

| Icon | Meaning | How confirmed |
|---|---|---|
| red **▶** | the half PTT and the knob control (the "main band") | manual §4.3 + radio |
| **L / M / H** | transmit power | manual |
| **N** | **narrowband** (12.5 kHz) channel | manual says N = narrowband. Codeplug bandwidth bit: Seattle 1 SWE and WX4 are narrow (N shown); U11 and V04 are wide (no N). **Matches.** |
| **CTC** | CTCSS tone on this channel (manual shows it as "CT") | U11 uses 141.3 |
| **\|+\|** | **repeater (duplex) channel**. The manual draws it as bar-arrow-bar; on the radio it looks like `\|+\|` | it's there on Seattle 1 SWE and U11 and **gone on WX4 (simplex)** |
| **DIG / ANA** badge | digital (DMR) or analog channel. **Red = idle, blue = receiving a signal right now** | manual + Greg's radio (WX4 is always transmitting, so it showed a blue ANA) |
| **DW** | Dual Watch (Double Wait) on | manual |
| pin-in-circle icon | GPS has a position fix | manual ("positioned successfully") |
| **A / B** + long bar | band A (top) / band B (bottom). The screen-wide bar beside each is that band's **signal-strength meter**. When nothing is received it shows empty outlined ticks; when a signal comes in, segments fill in solid **blue** and rise and fall with the signal | Greg's radio, 2026-11-26 (photo: WX4 with band A's bar partly solid blue) |
| **Menu / A/B** | on-screen labels for the keys below the screen. **A/B is the red ⌂ key**, which switches the main band | matches Greg's earlier finding and the club page |

No separate `+`/`−`
offset icon was seen on these channels.
Keys under the screen (from Greg's third photo): **blue Menu key** (☰ list icon) at the far left, **P1**, the **▲** rocker,
**P2**, and the **orange/red ⌂ key** at the far right. The on-screen "Menu" and "A/B" labels sit right above the
two outer keys. Use this for the labeled radio drawing (§4).
Describe the signal bar only as a relative strength indicator, not as S-units. Community notes say the stock S-meter isn't calibrated.
Idea: use a cleaned-up drawing of this screen (not the photo) on the Starter Guide, with callouts.
Greg could save his photos to `docs/photos/` for reference.

### 6. The basics on this radio
Volume, choosing a zone (P1 = next, P2 = previous), choosing a channel (knob or ▲/▼), power (SK2), the top/bottom
halves (⌂ Back), and **waiting ½ second after pressing PTT on DMR** before you talk.
Long-press functions need a **3-second hold**.

### 7. First three things to try (also your first training)
1. **NOAA weather, which teaches zones and channels.** A step-by-step walkthrough:
   press **P1/P2** until the zone reads **NOAA** (zone 5), then turn the knob until the screen shows
   **162.42500 / NOAA CH 4** (WX4). This is how it appears on Greg's radio.
   In West Seattle, **WX4 comes in best** for Greg. If it doesn't come in for you, try the other WX channels. Receive only.
   Per weather.gov's SEW transmitter list, 162.425 is **WWG24, "Puget Sound Marine"** (marine-focused). 162.550 (WX1) is
   **KHB60 Seattle**. Both could be mentioned.
2. **Analog: listen to or check into the Monday net** on **U11 West Sea** (zone 1, ch 11) or
   **V04 WEST SEA** (zone 3, ch 5).
3. **DMR: parrot test** on **Parrot 1 SWE** (zone 11, ch 15). Just talk and it plays you back, with no keys needed.

### 8. Troubleshooting (top items)
- No audio from the speaker: unplug the programming cable.
- Blank screen at power-on: the cable was plugged in. Unplug it, turn the radio on, then plug it back in.
- Silence on an analog channel: that channel needs the repeater's tone (shown as SQ on the reference sheet).
- A long press seems to do nothing: hold it for 3 seconds.
- Can't reach the repeater: raise the power (SK2) to H.
- Menus switched to Chinese: don't use **File → New** in the CPS. Start from a read of your radio or from the club file.

### 9. Firmware: a warning box
Greg's direction: say what we found, **get the radio working first**, and if you do update, make sure you know what you're doing.
Suggested wording:

> **Firmware: get the radio working first.** Don't update the firmware until the radio works with the club
> codeplug. More than one kind of DM-32UV exists. They look alike and report the same model, and
> firmware meant for the other kind can "soft-brick" the radio (it can be recovered, but you need a computer and the right file).
> If you do decide to update later, **make sure you know exactly which firmware your radio needs** before you start. Ask
> at an Elmers' Breakfast if you're unsure.
>
> **See your version:** blue menu button → **Settings → Device Info → Versions** (the radio spells it "VerSions").

Background (from the [dm32-info community notes](https://github.com/Chicago-Offline/dm32-info/blob/main/FIRMWARE.md)):
- Firmware comes in families: **DM32.01.*** (most common), **DM32.NRF.*** (Taiwan-sourced builds, kept in the same
  archive branch as 01.*) and **DM32.00.*** ("HR Vocoder"). 00 and 01 carry mutual soft-brick warnings.
- Recovery: remove the battery, hold SK1 + PTT, reattach the battery and power on, then reflash the correct file.
- A possible way to tell them apart: ridged SK1/SK2 = the common type, smooth = HR Vocoder. This comes from a single source.
- That source's own radios stay on **048**. Baofeng's guides were written on DM32.01.L01.048.
- **Greg's radio shows `DM32.NRF.01.048`** (2026-11-26). The community list only shows NRF builds at 049, so 048 NRF
  isn't listed there. Tom's codeplug file header says `DM32.00.01.048`, and it's unknown what that header means.
  Club radios may well run different firmware. Don't print version numbers.

### 10. Where to get help
- The weekly **Monday net** on the air (6:30 pm, early check-in 6:15).
- The **Elmers' Breakfast** (1st Saturday) and the **monthly club meeting** (3rd Saturday).
- The [club website](https://w7aw.org) and the [calendar](https://w7aw.org/calendar/).
- **Don't list Tom N7OEP (or anyone else) as a support contact** until they've agreed to it. Greg will ask Tom first.

### 11. QR codes
Add QR codes for: the club home page, the calendar, the codeplug page, the repeater page and RadioID.net (and maybe the FCC
License Manager). Put a short label under each. They're generated locally. Candidate tools are the Python `segno`
package or `qrencode` from Homebrew. Check them with a phone before printing.

## Club events (checked on [Monthly Events](https://w7aw.org/about-wsarc/monthly-events/), 2026-11-26)
Always print "check the calendar for current details".
- **Elmers' Breakfast & Help Session:** 1st Saturday, 8:30 am, Taste & Best Indo-American Bar & Grill,
  4752 California Ave SW. Introductions and Q&A around 9:30.
- **Club Meeting:** 3rd Saturday, 9–11 am, Salvation Army White Center.
- **Ham Jam:** 1st Monday, 5:45–7 pm, Center for Active Living, 4217 SW Oregon St, 2nd floor.
- **Monday Net:** 6:30 pm (early check-in 6:15) on the linked 70 cm, 2 m and 6 m analog repeaters.
- Leave off: the Sunday 10 m gathering, because this radio can't do HF.

## Decided NOT to include (for now)
- **A script for checking into the net.** The readers are licensed hams.
- **APRS.** Greg will learn how it works on SeattleDMR from Tom first. Technical notes are in AGENTS.md.
- Tom as a named support contact (see section 10).

## Reference sheet: page 6 ideas (later; don't change the reference sheet yet)
- Alan's analog parrot steps (key "12", details in AGENTS.md), clearly labeled analog-only.
- How to set up scanning: scan lists, with 16 entries per list.
- EchoLink node 56575.
- The codeplug version and date, and how to get the latest.
- APRS, once it's understood.
