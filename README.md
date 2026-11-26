# W7AW DMR: Baofeng DM-32UV reference sheets

Printable guides for **West Seattle Amateur Radio Club ([W7AW](https://w7aw.org))** members using the
**Baofeng DM-32UV** with the club codeplug by Tom N7OEP ([club codeplug page](https://w7aw.org/dmr-code-plug/)).

- **Reference Sheet** (5 pages, built from the codeplug): [`output/W7AW-DM32UV-Cheat-Sheet.pdf`](output/W7AW-DM32UV-Cheat-Sheet.pdf)
- **W7AW DM-32UV Starter Guide**: in planning, see [`GETTING-STARTED-PLAN.md`](GETTING-STARTED-PLAN.md)

## Getting the codeplug

The codeplug isn't in this repository. Download Tom N7OEP's **Baofeng DM-32UV codeplug** (`BaofengDM32UV_NWDMR.data`)
from the club's [DMR Code Plug page](https://w7aw.org/dmr-code-plug/) (the "DOWNLOAD" link goes to the W7AW Google Drive).
Open it in the Baofeng CPS and put your own DMR ID and callsign in **Digital → DMR ID** before you write it to your radio.

## Rebuilding the PDF

Save the codeplug in `codeplug/`, then run `./make.sh codeplug/BaofengDM32UV_NWDMR.data`
(with no argument, it uses `codeplug/Gregs-BaofengDM32UV_NWDMR.data`). You need python3, a headless Chromium and poppler.
Project notes, sources, the fact-check table and the codeplug format notes are in [`AGENTS.md`](AGENTS.md).

No warranty. Check everything against your own radio.
