#!/usr/bin/env python3
"""Build the W7AW DM-32UV Starter Guide (HTML).

Content follows GETTING-STARTED-PLAN.md ("Proposed outline" and "Section details").
The look follows tools/build.py (the Reference Sheet). Unlike the Reference Sheet, nothing
here is read from the codeplug: every fact is typed in from the plan, so check the plan first.
Usage: .venv/bin/python tools/build_starter.py [out.html]
"""
import io
import sys

import segno  # QR codes; installed in .venv (see AGENTS.md "Python setup")

DST = sys.argv[1] if len(sys.argv) > 1 else 'build/starter.html'

FOOT = 'W7AW DM-32UV Starter Guide for the club codeplug by Tom N7OEP &middot; check everything against your own radio'

PAGES = []


def page(title, sub, body, accent='navy', key=None):
    PAGES.append((title, sub, body, accent, key))


def ref(k):
    """Placeholder for the page number of the page registered with key k (filled in by render)."""
    return f'@@{k}@@'


def render():
    n = len(PAGES)
    nums = {key: i for i, (*_, key) in enumerate(PAGES, 1) if key}
    out = ''
    for i, (title, sub, body, accent, _) in enumerate(PAGES, 1):
        for k, v in nums.items():
            body = body.replace(f'@@{k}@@', str(v))
        assert '@@' not in body, f'unknown page reference on page {i}'
        out += f'''
<section class="page">
  <header class="band {accent}">
    <div class="ttl">{title}</div>
    <div class="sub">{sub}</div>
  </header>
  <main>{body}</main>
  <footer><span>{FOOT}</span><span class="pg">Page {i} of {n}</span></footer>
</section>'''
    return out


# ---------------------------------------------------------------- QR codes
QR = [
    ('W7AW club home', 'https://w7aw.org'),
    ('Club calendar', 'https://w7aw.org/calendar/'),
    ('Club codeplug page', 'https://w7aw.org/dmr-code-plug/'),
    ('Club repeaters', 'https://w7aw.org/echolink-irlp/'),
    ('RadioID.net', 'https://radioid.net'),
    ('FCC License Manager', 'https://wireless2.fcc.gov/UlsEntry/licManager/login.jsp'),
    ('Baofeng CPS download', 'https://www.baofengradio.com/pages/download'),
]
QR_URL = dict(QR)


def qr_svg(url):
    """Inline SVG QR code (error correction M, 4-module quiet zone, black on white)."""
    buf = io.BytesIO()
    segno.make(url, error='m', micro=False).save(buf, kind='svg', border=4, xmldecl=False, svgns=True,
                                                    omitsize=True, dark='#000', light='#fff', svgclass='qrsvg')
    return buf.getvalue().decode()


def qr_card(label):
    u = QR_URL[label]
    # Plain ASCII hyphens so a copied URL works; each path segment is kept on one line, breaks only after a slash.
    parts = u.replace('https://', '').replace('www.', '').split('/')
    shown = '/<wbr>'.join(f'<span class="nw">{p}</span>' for p in parts)
    return (f'<a class="qr" href="{u}">{qr_svg(u)}<div class="ql">{label}</div>'
            f'<div class="mono qu">{shown}</div></a>')


def qr_strip(*labels):
    """A row of QR codes for the sites a section mentions."""
    return f'<div class="qrstrip">{"".join(qr_card(t) for t in labels)}</div>'


def key(k, cls=''):
    return f'<span class="key {cls}">{k}</span>'



# ---------------------------------------------------------------- page 1: start here
page('W7AW DM-32UV Starter Guide', 'Start here: from the box to your first contact', f'''
<p class="lead">This guide is for licensed hams who are new to the Baofeng DM-32UV, to DMR, or both.
It gets your radio set up with the W7AW club codeplug and on the air, in six steps.</p>

<ol class="road">
  <li><span class="rn">1</span><div><b>Open the box, charge, fit the antenna.</b> <span class="pref">Page {ref("box")}</span></div></li>
  <li><span class="rn">2</span><div><b>Get your FCC license copy and DMR ID.</b> <span class="pref">Page {ref("box")}</span></div></li>
  <li><span class="rn">3</span><div><b>Get the club codeplug installed.</b> <span class="pref">Page {ref("cp")}</span></div></li>
  <li><span class="rn">4</span><div><b>Check the radio shows your own ID.</b> <span class="pref">Page {ref("basics")}</span></div></li>
  <li><span class="rn">5</span><div><b>Learn the few basics.</b> <span class="pref">Page {ref("basics")}</span></div></li>
  <li><span class="rn">6</span><div><b>Make your first contacts.</b> <span class="pref">Page {ref("fc")}</span></div></li>
</ol>

<div class="box dmr"><div class="bh">Start your DMR ID while the battery charges</div>
  You need your own DMR ID before you talk on DMR. Approval from RadioID.net often comes within an hour or so,
  but it can take longer.</div>
<div class="box warn"><div class="bh">Screw the antenna on before you ever press PTT</div>
  If your radio came with more than one, start with the longest. Never transmit without it.</div>
<div class="box gold"><div class="bh">The easy way</div>
  Bring the <b>charged radio</b>, your <b>callsign</b> and your <b>DMR ID</b> to the club&rsquo;s
  <b>Elmers&rsquo; Breakfast</b> (1st Saturday; check the club calendar), and get the club codeplug put in for you.</div>
<div class="box warn"><div class="bh">Don&rsquo;t update the firmware</div>
  &hellip;until the radio works with the club codeplug. See page {ref("fw")}.</div>
''', accent='navy', key='start')

# ---------------------------------------------------------------- page 2: box + DMR ID
page('1 &amp; 2 &middot; Charge the radio, and get your DMR ID', 'Do these two at the same time', f'''
<h2>1. Open the box, charge, fit the antenna</h2>
<ul class="pts">
  <li>The battery comes <b>uncharged</b>. Charge it with the <b>radio turned off</b>, in the desk charger or with a USB-C
    cable in the port on the <b>back of the battery</b>. That port only charges; it can&rsquo;t program the radio.</li>
  <li>Desk charger light: <b class="red">red</b> = charging, <b class="grn">green</b> = full.</li>
  <li><b>Antenna:</b> some radios come with more than one (for example short, medium and long). <b>Start with the longest</b>
    for the best chance of reception; once you know the radio works you can switch to a shorter one if you like.
    Screw it on clockwise, finger tight. Never transmit without it.</li>
  <li><b>Turn on:</b> turn the power/volume knob (at the right edge) clockwise until it clicks.</li>
  <li><b>Keys do nothing?</b> The keypad is locked. Press {key('Menu')}, then {key('*')}.</li>
</ul>

<h2>2. Your FCC license copy and DMR ID</h2>
<ol class="steps">
  <li><b>Get the official copy of your license.</b> Sign in to the FCC <b>ULS License Manager</b> with your FRN and
    password. Click <b>Download Electronic Authorizations</b>, add your callsign, and click <b>Download</b>.
    The official copy is a PDF with the FCC logo and an &ldquo;Official Copy&rdquo; watermark. A screenshot is not accepted.</li>
  <li><b>Nothing downloads?</b> A pop-up or ad blocker is probably stopping it. Allow pop-ups for fcc.gov and try again.
    FCC help line: <span class="mono">877-480-3201</span> (option 2, weekdays).</li>
  <li><b>Register at RadioID.net</b> and upload the license PDF. Your DMR ID comes by email, often within an hour or so, but it can take longer.</li>
  <li><b>Answer RadioID&rsquo;s yearly email,</b> or your ID will eventually stop working.</li>
</ol>
{qr_strip('FCC License Manager', 'RadioID.net')}
''', accent='navy', key='box')

# ---------------------------------------------------------------- page 3: codeplug
page('3 &middot; The club codeplug', 'The codeplug is the radio&rsquo;s list of zones and channels', f'''
<h2>3. Get the club codeplug installed</h2>
<div class="box gold"><div class="bh">The easy way</div>
  Bring the <b>charged radio</b>, your <b>callsign</b> and your <b>DMR ID</b> to the <b>Elmers&rsquo; Breakfast</b>
  (1st Saturday, Taste &amp; Best restaurant) or the <b>club meeting</b> (3rd Saturday, Salvation Army White Center).
  <b>Check the club calendar</b> for times and places.</div>

<div class="box plain"><div class="bh">Doing it yourself</div>
<ol class="steps tight">
  <li>You need a <b>Windows</b> computer and the programming cable. The cable goes into the <b>speaker-mic jack</b>.</li>
  <li>Get the Baofeng CPS programming software <b>only</b> from Baofeng&rsquo;s download page,
    <span class="mono">baofengradio.com/pages/download</span>.</li>
  <li><b>Turn the radio on first, then plug in the cable.</b> With the cable already in, the radio starts with a blank screen.</li>
  <li><b>Program &rarr; Read data.</b> Save it as &ldquo;my radio original&rdquo; and never change that file.</li>
  <li>Open the club file from the W7AW codeplug page. In <b>Digital &rarr; DMR ID</b>, row 1, <b>replace</b> the
    placeholder <span class="mono">1234567 BLANK</span> with <b>your own DMR ID and callsign</b>. <b>Save As</b> a new name.</li>
  <li><b>Program &rarr; Write data.</b></li>
</ol>
<p>Don&rsquo;t use <b>File &rarr; New</b> in the CPS (it can switch the menus to Chinese). If your radio misbehaves
with the club file, ask at the Elmers&rsquo; Breakfast.</p></div>

{qr_strip('Club codeplug page', 'Club calendar', 'Baofeng CPS download')}
''', accent='navy', key='cp')

# ---------------------------------------------------------------- page 4: own ID + basics
page('4 &amp; 5 &middot; Your own ID, and the few basics', 'Check the ID first, then learn enough to pick a channel and talk', f'''
<h2>4. Check the radio shows your own ID</h2>
<div class="box warn"><div class="bh">The club file holds a placeholder ID: <span class="mono">1234567 &ldquo;BLANK&rdquo;</span></div>
  Look: blue {key('Menu')} key &rarr; <b>Settings &rarr; Device Info &rarr; Device Info &rarr; DMR ID</b>
  (&ldquo;Device Info&rdquo; comes twice). It must show <b>your own DMR ID</b>. If it shows 1234567, don&rsquo;t transmit
  on DMR until your ID is put in.</div>

<h2>5. The few basics</h2>
<table class="grid basics">
  <thead><tr><th style="width:32%">To do this</th><th>Do this</th></tr></thead>
  <tbody>
  <tr><td class="nm">Find the knobs</td><td>Facing the screen: the <b>antenna</b> is on the left, the <b>channel knob</b> in the
    middle (it also scrolls menus), the <b>power/volume knob</b> at the right edge. Drawing: page {ref("radio")}.</td></tr>
  <tr><td class="nm">Change the volume</td><td>Turn the power/volume knob.</td></tr>
  <tr><td class="nm">Change zone</td><td>{key('P1')} = next zone, {key('P2')} = previous zone. They are left and right of the
    {key('&#9650;')}{key('&#9660;')} keys under the screen.</td></tr>
  <tr><td class="nm">Change channel</td><td>Turn the channel knob, or press {key('&#9650;')} / {key('&#9660;')}.</td></tr>
  <tr><td class="nm">Find SK1 and SK2</td><td>They are below PTT on the left side. Find them by feel:
    <b>SK1 has one ridge</b>, <b>SK2 has two</b>.</td></tr>
  <tr><td class="nm">Change transmit power</td><td>Press {key('SK2')}: L &rarr; M &rarr; H.</td></tr>
  <tr><td class="nm">&ldquo;Press and hold&rdquo;</td><td>Hold the key for <b>about a second</b>.</td></tr>
  </tbody>
</table>

<div class="box dmr"><div class="bh">Talking on DMR: press PTT, pause about 1 second, then talk</div>
  The radio and the repeater need a moment to connect. The club codeplug gives no go-ahead beep, so count
  &ldquo;one&rdquo; before you speak.</div>

<div class="box plain"><div class="bh">If your screen shows two channels</div>
  The red {'<span class="tri">&#9654;</span>'} marks the one you talk on. Press the red {key('&#8962;', 'home')} (A/B) key
  <b>briefly</b> to switch.</div>

''', accent='navy', key='basics')

# ---------------------------------------------------------------- pages 5-6: first contacts, every Monday
page('6 &middot; First contacts', 'Hear something first, then talk', f'''
<table class="grid fc">
  <thead><tr><th style="width:23%">Try</th><th style="width:18%">Zone</th><th style="width:30%">Channel</th><th>Frequency</th></tr></thead>
  <tbody>
  <tr class="fmrow"><td class="nm">NOAA weather<br><span class="small">receive only</span></td><td><b class="big">5</b> NOAA</td>
    <td><b>WX4</b><br><span class="small">shows NOAA CH 4</span></td><td class="mono">162.425</td></tr>
  <tr class="dmrrow gold"><td class="nm">DMR parrot<br><span class="small">echo test</span></td><td><b class="big">11</b> Seattle/West</td>
    <td><b class="big">15</b> <b>Parrot 1 SWE</b><br><span class="ts ts1">TS1</span> <span class="mono small">TG 9998</span></td>
    <td class="mono">440.975 +5</td></tr>
  <tr class="fmrow gold"><td class="nm">Monday net<br><span class="small">analog, 70 cm</span></td><td><b class="big">1</b> ACS UHF</td>
    <td><b class="big">11</b> <b>U11 West Sea</b></td><td class="mono">441.800 +5<br>tone 141.3</td></tr>
  <tr class="fmrow gold"><td class="nm">Monday net<br><span class="small">analog, 2 m</span></td><td><b class="big">3</b> ACS VHF</td>
    <td><b class="big">5</b> <b>V04 WEST SEA</b></td><td class="mono">145.130 &minus;0.6<br>tone 103.5</td></tr>
  <tr class="dmrrow gold"><td class="nm">DMR Gathering</td><td><b class="big">11</b> Seattle/West</td>
    <td><b class="big">17</b> <b>Seattle 1 SWE</b><br><span class="ts ts1">TS1</span> <span class="mono small">TG 803153</span></td>
    <td class="mono">440.975 +5</td></tr>
  </tbody>
</table>

<div class="two">
<div>
  <h2 class="fmh">NOAA weather: practice zones and channels</h2>
  <ol class="steps">
    <li>Press {key('P1')} or {key('P2')} until the zone reads <b>NOAA</b>.</li>
    <li>Turn the channel knob until the screen shows <b class="mono">162.42500</b> / <b>NOAA CH 4</b>.</li>
    <li>No signal? Try the other WX channels in the zone.</li>
  </ol>
</div>
<div>
  <h2 class="dmrh">DMR parrot: your first transmission</h2>
  <ol class="steps">
    <li>Zone 11, channel 15 <b>Parrot 1 SWE</b>.</li>
    <li>Press PTT, <b>pause about 1 second</b>, give your call, release.</li>
    <li>You hear yourself played back. No keys to press.</li>
  </ol>
</div>
</div>
''', accent='navy', key='fc')

page('6 (cont.) &middot; Every Monday', 'The club net, then the DMR Gathering', f'''
  <div class="box gold"><div class="bh">W7AW net: 6:30 pm</div>
  Early check-in 6:15. Analog, on U11 West Sea or V04 WEST SEA (the linked club repeaters). The DMR repeater is
  <b>not</b> linked to the net.</div>
<div class="box dmr"><div class="bh">DMR Gathering: about 7 pm</div>
  Right after the net, on <b>Seattle 1 SWE</b> (zone 11, channel 17). Check the club calendar.</div>
<div class="box warn"><div class="bh">Before you talk on DMR</div>
  Your radio must show your own DMR ID (page {ref("basics")}).</div>

<p class="small">Codes below: the club repeater page, the calendar and the club website.</p>
{qr_strip('Club repeaters', 'Club calendar', 'W7AW club home')}
''', accent='navy', key='monday')

# ---------------------------------------------------------------- page 7: troubleshooting
TROUBLE = [
    ('A bare frequency shows (maybe with VFO) and the channel name is gone',
     f'The radio is in frequency mode. Press {key("SK1")} briefly, or hold the red {key("&#8962;", "home")} key about a second, to get channel names back.'),
    ('DMR: you can&rsquo;t get into the repeater',
     f'Set the power to H ({key("SK2")}). Pick a zone for a repeater you can hear. Check that your own DMR ID is in the radio, not 1234567.'),
    ('DMR: you hear nothing',
     'The radio usually plays only the talkgroup on the channel you chose. Try the parrot: zone 11, channel 15.'),
    ('Your first words are cut off', 'Press PTT and pause about 1 second before you talk.'),
    ('No sound from the speaker', 'Unplug the programming cable. Check the volume.'),
    ('Blank screen when you turn it on', 'The programming cable was plugged in. Unplug it, turn the radio on, then plug the cable back in.'),
    ('An analog channel is silent',
     f'The channel may need the repeater&rsquo;s tone to open. Hold {key("SK1")} about a second (Monitor) to hear whether anything is there.'),
    ('Keys do nothing',
     f'The keypad is locked: press {key("Menu")}, then {key("*")}. For a press-and-hold, hold about a second.'),
]
rows = ''.join(f'<tr><td class="chn">{i}</td><td class="nm">{p}</td><td>{f}</td></tr>' for i, (p, f) in enumerate(TROUBLE, 1))
page('7 &middot; Troubleshooting', 'Common first-week problems', f'''
<table class="grid trouble">
  <thead><tr><th style="width:6%"></th><th style="width:34%">Problem</th><th>Try this</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<p class="small">Still stuck? Ask at the Monday net, the Elmers&rsquo; Breakfast or the club meeting (page {ref("help")}).</p>
''', accent='navy', key='trouble')

# ---------------------------------------------------------------- pages 8-9: screen
SCREEN_SVG = '''
<svg class="scr" viewBox="0 -56 560 616" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica Neue, Helvetica, Arial, sans-serif">
  <rect x="90" y="10" width="380" height="530" rx="16" fill="#121a26" stroke="#5b6470" stroke-width="4"/>
  <!-- status bar -->
  <g fill="#e8edf3" font-size="20" font-weight="700">
    <path d="M128 30 a9 9 0 1 1 0.1 0 Z M128 48 l-8 -12 h16 Z" fill="none" stroke="#e8edf3" stroke-width="3"/>
    <text x="262" y="45">DW</text>
    <rect x="400" y="28" width="42" height="20" rx="3" fill="none" stroke="#e8edf3" stroke-width="3"/>
    <rect x="442" y="33" width="5" height="10" fill="#e8edf3"/>
    <rect x="404" y="32" width="30" height="12" fill="#7bd389"/>
  </g>
  <line x1="100" y1="60" x2="460" y2="60" stroke="#3a4656" stroke-width="2"/>
  <!-- top half -->
  <path d="M106 74 l16 10 l-16 10 Z" fill="#e53935"/>
  <g fill="#e8edf3" font-size="22" font-weight="700">
    <text x="132" y="92">L</text><text x="162" y="92">N</text>
    <text x="196" y="92" font-family="Menlo, monospace">|+|</text>
  </g>
  <rect x="385" y="72" width="62" height="26" rx="5" fill="#1e6fe0"/><text x="393" y="92" fill="#fff" font-size="19" font-weight="800">DIG</text>
  <text x="280" y="132" fill="#fff" font-size="30" font-weight="800" text-anchor="middle">Seattle 1 SWE</text>
  <text x="280" y="166" fill="#e8edf3" font-size="26" text-anchor="middle" font-family="Menlo, monospace">440.97500</text>
  <text x="110" y="198" fill="#c9d1db" font-size="22">Seattle/West</text><text x="450" y="198" fill="#c9d1db" font-size="22" text-anchor="end">CH 17</text>
  <text x="108" y="230" fill="#e8edf3" font-size="20" font-weight="800">A</text>
  <g stroke="#7f8b99" stroke-width="2" fill="none">
    <rect x="132" y="214" width="316" height="18" rx="3"/>
  </g>
  <rect x="134" y="216" width="140" height="14" fill="#4f8fe6"/>
  <line x1="100" y1="248" x2="460" y2="248" stroke="#3a4656" stroke-width="2"/>
  <!-- bottom half -->
  <g fill="#e8edf3" font-size="22" font-weight="700">
    <text x="132" y="280">L</text><text x="160" y="280">CTC</text>
    <text x="216" y="280" font-family="Menlo, monospace">|+|</text>
  </g>
  <rect x="385" y="260" width="62" height="26" rx="5" fill="#e53935"/><text x="391" y="280" fill="#fff" font-size="19" font-weight="800">ANA</text>
  <text x="280" y="320" fill="#fff" font-size="30" font-weight="800" text-anchor="middle">U11 West Sea</text>
  <text x="280" y="354" fill="#e8edf3" font-size="26" text-anchor="middle" font-family="Menlo, monospace">441.80000</text>
  <text x="110" y="386" fill="#c9d1db" font-size="22">ACS UHF</text><text x="450" y="386" fill="#c9d1db" font-size="22" text-anchor="end">CH 11</text>
  <text x="108" y="418" fill="#e8edf3" font-size="20" font-weight="800">B</text>
  <rect x="132" y="402" width="316" height="18" rx="3" stroke="#7f8b99" stroke-width="2" fill="none"/>
  <line x1="100" y1="440" x2="460" y2="440" stroke="#3a4656" stroke-width="2"/>
  <text x="280" y="474" fill="#c9d1db" font-size="20" text-anchor="middle" font-family="Menlo, monospace">2026/11/26  07:07</text>
  <text x="110" y="520" fill="#fff" font-size="21" font-weight="800">Menu</text>
  <text x="450" y="520" fill="#fff" font-size="21" font-weight="800" text-anchor="end">A/B</text>
  <!-- callouts -->
  <g font-size="20" font-weight="800" text-anchor="middle">
    <g stroke="#d9a400" stroke-width="2.5">
      <line x1="62" y1="84" x2="104" y2="84"/><line x1="62" y1="150" x2="132" y2="88"/>
      <line x1="498" y1="84" x2="449" y2="84"/><line x1="62" y1="230" x2="102" y2="226"/>
      <line x1="498" y1="270" x2="449" y2="273"/><line x1="62" y1="300" x2="160" y2="282"/>
      <line x1="290" y1="-22" x2="283" y2="26"/><line x1="62" y1="38" x2="116" y2="38"/>
      <line x1="62" y1="514" x2="106" y2="514"/><line x1="212" y1="-22" x2="212" y2="70"/>
    </g>
    <g fill="#f6d77a" stroke="#8a6a00" stroke-width="2">
      <circle cx="44" cy="84" r="17"/><circle cx="44" cy="150" r="17"/><circle cx="212" cy="-36" r="17"/>
      <circle cx="44" cy="300" r="17"/><circle cx="516" cy="84" r="17"/><circle cx="516" cy="270" r="17"/>
      <circle cx="44" cy="230" r="17"/><circle cx="290" cy="-36" r="17"/><circle cx="44" cy="38" r="17"/>
      <circle cx="44" cy="514" r="17"/>
    </g>
    <g fill="#1b1f24">
      <text x="44" y="91">1</text><text x="44" y="157">2</text><text x="212" y="-29">3</text>
      <text x="44" y="307">4</text><text x="516" y="91">5</text><text x="516" y="277">5</text>
      <text x="44" y="237">6</text><text x="290" y="-29">7</text><text x="44" y="45">8</text>
      <text x="44" y="521">9</text>
    </g>
  </g>
</svg>'''

SCREEN_ROWS = [
    ('1', 'red <span class="tri">&#9654;</span>', 'The channel you talk on. There is only one.'),
    ('2', 'L / M / H', 'Transmit power: low, medium, high. SK2 changes it.'),
    ('3', '|+| or |&minus;|', 'Repeater channel: you transmit above (+) or below (&minus;) the receive frequency. None on simplex.'),
    ('4', 'CTC', 'Probably: this channel listens for a tone before it opens (not confirmed). It shows on U11, not on V04.'),
    ('5', 'DIG / ANA', 'DMR or analog channel. Red = idle, <b>blue = receiving now</b> (as in the top half of the drawing).'),
    ('6', 'bar after A / B', 'A rough signal meter. It fills in blue when a signal comes in.'),
    ('7', 'DW', 'Dual Watch is on: the radio listens to both channels.'),
    ('8', 'pin', 'GPS: one pin when it has a position, a similar one while it is still looking.'),
    ('9', 'Menu &middot; A/B', 'Labels for the keys at each end of the row below the screen. A/B is the red &#8962; key, which switches channels if your screen shows two.'),
]
srows = ''.join(f'<tr><td class="chn"><span class="cn">{n}</span></td><td class="nm">{i}</td><td>{m}</td></tr>' for n, i, m in SCREEN_ROWS)
page('8 &middot; Reading the screen', 'A drawing of the screen with two channels shown (Dual Watch on)', f'''
<div class="scrwrap">{SCREEN_SVG}</div>
<div class="box plain"><div class="bh">One channel or two</div>
  This drawing shows two channels. If your radio shows one channel at a time, the screen looks different.
  <b>N</b> on the top channel means narrowband.</div>
''', accent='navy', key='screen')

page('8 (cont.) &middot; What the screen shows', 'The numbers match the drawing on the page before', f'''
<table class="grid scrt">
  <thead><tr><th style="width:7%"></th><th style="width:20%">You see</th><th>What it means</th></tr></thead>
  <tbody>{srows}</tbody>
</table>
''', accent='navy')

# ---------------------------------------------------------------- page 10: radio drawing
RADIO_SVG = '''
<svg class="rad" viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica Neue, Helvetica, Arial, sans-serif">
  <!-- antenna -->
  <rect x="236" y="8" width="18" height="140" rx="9" fill="#d5dbe3" stroke="#1b1f24" stroke-width="3"/>
  <rect x="228" y="130" width="34" height="34" rx="5" fill="#9aa7b6" stroke="#1b1f24" stroke-width="3"/>
  <!-- knobs -->
  <rect x="322" y="112" width="38" height="52" rx="6" fill="#c9d1db" stroke="#1b1f24" stroke-width="3"/>
  <g stroke="#1b1f24" stroke-width="2"><line x1="331" y1="118" x2="331" y2="158"/><line x1="341" y1="118" x2="341" y2="158"/><line x1="351" y1="118" x2="351" y2="158"/></g>
  <rect x="400" y="122" width="46" height="42" rx="8" fill="#c9d1db" stroke="#1b1f24" stroke-width="3"/>
  <g stroke="#1b1f24" stroke-width="2"><line x1="410" y1="128" x2="410" y2="158"/><line x1="423" y1="128" x2="423" y2="158"/><line x1="436" y1="128" x2="436" y2="158"/></g>
  <!-- body -->
  <rect x="210" y="160" width="260" height="520" rx="26" fill="#f4f6f9" stroke="#1b1f24" stroke-width="4"/>
  <!-- side keys (left edge) -->
  <rect x="190" y="250" width="22" height="86" rx="6" fill="#9aa7b6" stroke="#1b1f24" stroke-width="3"/>
  <rect x="194" y="352" width="18" height="30" rx="5" fill="#c9d1db" stroke="#1b1f24" stroke-width="3"/>
  <line x1="198" y1="367" x2="210" y2="367" stroke="#1b1f24" stroke-width="2.5"/>
  <rect x="194" y="392" width="18" height="30" rx="5" fill="#c9d1db" stroke="#1b1f24" stroke-width="3"/>
  <line x1="198" y1="402" x2="210" y2="402" stroke="#1b1f24" stroke-width="2.5"/><line x1="198" y1="412" x2="210" y2="412" stroke="#1b1f24" stroke-width="2.5"/>
  <!-- screen -->
  <rect x="236" y="186" width="208" height="166" rx="10" fill="#121a26" stroke="#1b1f24" stroke-width="3"/>
  <text x="340" y="262" fill="#e8edf3" font-size="21" font-weight="800" text-anchor="middle">Seattle 1 SWE</text>
  <text x="340" y="294" fill="#c9d1db" font-size="20" text-anchor="middle" font-family="Menlo, monospace">440.97500</text>
  <!-- key row under the screen -->
  <rect x="236" y="368" width="36" height="34" rx="7" fill="#1e5aa8" stroke="#1b1f24" stroke-width="2.5"/>
  <g stroke="#fff" stroke-width="3"><line x1="246" y1="378" x2="262" y2="378"/><line x1="246" y1="385" x2="262" y2="385"/><line x1="246" y1="392" x2="262" y2="392"/></g>
  <rect x="278" y="368" width="36" height="34" rx="7" fill="#e3e9f1" stroke="#1b1f24" stroke-width="2.5"/>
  <text x="296" y="393" font-size="20" font-weight="800" text-anchor="middle">P1</text>
  <rect x="320" y="364" width="40" height="42" rx="7" fill="#e3e9f1" stroke="#1b1f24" stroke-width="2.5"/>
  <path d="M340 370 l8 10 h-16 Z M340 400 l8 -10 h-16 Z" fill="#1b1f24"/>
  <rect x="366" y="368" width="36" height="34" rx="7" fill="#e3e9f1" stroke="#1b1f24" stroke-width="2.5"/>
  <text x="384" y="393" font-size="20" font-weight="800" text-anchor="middle">P2</text>
  <rect x="408" y="368" width="36" height="34" rx="7" fill="#e53935" stroke="#1b1f24" stroke-width="2.5"/>
  <path d="M426 375 l11 10 h-4 v10 h-14 v-10 h-4 Z" fill="#fff"/>
  <!-- keypad -->
  <g fill="#e3e9f1" stroke="#1b1f24" stroke-width="2.5" font-size="18" font-weight="700">
    <rect x="244" y="420" width="56" height="34" rx="7"/><rect x="312" y="420" width="56" height="34" rx="7"/><rect x="380" y="420" width="56" height="34" rx="7"/>
    <rect x="244" y="462" width="56" height="34" rx="7"/><rect x="312" y="462" width="56" height="34" rx="7"/><rect x="380" y="462" width="56" height="34" rx="7"/>
    <rect x="244" y="504" width="56" height="34" rx="7"/><rect x="312" y="504" width="56" height="34" rx="7"/><rect x="380" y="504" width="56" height="34" rx="7"/>
    <rect x="244" y="546" width="56" height="34" rx="7"/><rect x="312" y="546" width="56" height="34" rx="7"/><rect x="380" y="546" width="56" height="34" rx="7"/>
  </g>
  <g font-size="21" font-weight="700" text-anchor="middle" fill="#1b1f24">
    <text x="272" y="443">1</text><text x="340" y="443">2</text><text x="408" y="443">3</text>
    <text x="272" y="485">4</text><text x="340" y="485">5</text><text x="408" y="485">6</text>
    <text x="272" y="527">7</text><text x="340" y="527">8</text><text x="408" y="527">9</text>
    <text x="272" y="569">*</text><text x="340" y="569">0</text><text x="408" y="569">#</text>
  </g>
  <circle cx="340" cy="606" r="6" fill="#1b1f24"/>
  <!-- labels -->
  <g font-size="22" font-weight="700" fill="#1b1f24">
    <g stroke="#5b6470" stroke-width="2">
      <line x1="150" y1="60" x2="234" y2="60"/>
      <line x1="150" y1="292" x2="188" y2="292"/>
      <line x1="150" y1="367" x2="192" y2="367"/>
      <line x1="150" y1="407" x2="192" y2="407"/>
      <line x1="520" y1="100" x2="341" y2="112"/>
      <line x1="520" y1="150" x2="448" y2="143"/>
      <line x1="520" y1="250" x2="446" y2="250"/>
      <line x1="520" y1="560" x2="438" y2="540"/>
    </g>
    <text x="146" y="67" text-anchor="end">Antenna</text>
    <text x="146" y="299" text-anchor="end">PTT</text>
    <text x="146" y="363" text-anchor="end">SK1</text><text x="146" y="386" text-anchor="end" font-size="20" font-weight="400">one ridge</text>
    <text x="146" y="414" text-anchor="end">SK2</text><text x="146" y="436" text-anchor="end" font-size="20" font-weight="400">two ridges</text>
    <text x="526" y="90">Channel knob</text><text x="526" y="112" font-size="20" font-weight="400">also scrolls menus</text>
    <text x="526" y="157">Power / volume</text>
    <text x="526" y="257">Screen</text>
    <text x="526" y="567">Keypad</text>
  </g>
</svg>'''

page('9 &middot; The radio, front view', 'The keys and knobs this guide talks about (simplified drawing)', f'''
<div class="radwrap">{RADIO_SVG}</div>
<div class="box plain"><div class="bh">The row of keys under the screen, left to right</div>
  <span class="krow">{key('&#9776;', 'menu')} blue Menu &nbsp; {key('P1')} &nbsp; {key('&#9650;')}{key('&#9660;')} &nbsp; {key('P2')} &nbsp; {key('&#8962;', 'home')} red A/B key</span>
  <br>The red key switches channels if your screen shows two.</div>
<div class="box plain"><div class="bh">Light on top</div>
  <b class="red">Red</b> = transmitting, <b class="grn">green</b> = receiving, slow orange = scanning.</div>
<div class="two">
  <div class="box plain"><div class="bh">Right side: speaker-mic jack</div>
    For a speaker-mic, and for the <b>programming cable</b>.</div>
  <div class="box plain"><div class="bh">Back: USB-C on the battery</div>
    <b>Charging only.</b> It can&rsquo;t program the radio.</div>
</div>
''', accent='navy', key='radio')

# ---------------------------------------------------------------- page 11: keys + firmware
KEYS = [
    ('SK1', 'Channel &harr; frequency mode', 'Monitor (open squelch)'),
    ('SK2', 'Power L &rarr; M &rarr; H', 'GPS information'),
    ('P1', 'Next zone', 'Scan &sup1;'),
    ('P2', 'Previous zone', 'Nothing (beeps)'),
    ('&#8962;', 'In menus: back / exit.<br>Otherwise A/B: switch channels (if two show)', 'Channel &harr; frequency mode'),
]
krows = ''.join(f'<tr><td>{key(k, "home" if k == "&#8962;" else "")}</td><td>{s}</td><td>{l}</td></tr>' for k, s, l in KEYS)
page('9 (cont.) &amp; 10 &middot; What the keys do, and firmware', 'Key functions with the W7AW club codeplug', f'''
<table class="grid keyt">
  <thead><tr><th style="width:14%">Key</th><th>Short press</th><th>Press and hold<br><span class="h2n">about a second</span></th></tr></thead>
  <tbody>{krows}
  <tr><td>{key('&#9650;')}{key('&#9660;')}</td><td colspan="2">Channel up / down (or turn the channel knob)</td></tr>
  </tbody>
</table>
<p class="small">&sup1; Scan starts only after a scan list is chosen in the radio menu.</p>

<h2>10. Firmware: get the radio working first</h2>
<div class="box warn big"><div class="bh">Don&rsquo;t update the firmware until the radio works with the club codeplug</div>
  More than one kind of DM-32UV exists. They look alike, and firmware meant for the other kind
  can &ldquo;soft-brick&rdquo; the radio. It can usually be recovered, but you need a computer and the right file.
  <p>If you do decide to update later, <b>make sure you know exactly which firmware your radio needs</b> before you start.
  Ask at an Elmers&rsquo; Breakfast if you&rsquo;re unsure.</p></div>
<div class="box plain"><div class="bh">See your firmware version</div>
  Blue {key('Menu')} key &rarr; <b>Settings &rarr; Device Info &rarr; Versions</b> (the radio spells it &ldquo;VerSions&rdquo;).</div>
''', accent='navy', key='fw')

# ---------------------------------------------------------------- pages 12-13: help, all links
page('11 &middot; Where to get help', 'Ask the club', f'''
<div class="box gold"><div class="bh">On the air</div>
  The <b>W7AW net</b>, every Monday at <b>6:30 pm</b> (early check-in 6:15), on U11 West Sea or V04 WEST SEA.</div>
<div class="box gold"><div class="bh">In person</div>
  The <b>Elmers&rsquo; Breakfast</b> (1st Saturday, Taste &amp; Best restaurant) and the <b>club meeting</b>
  (3rd Saturday, Salvation Army White Center). <b>Check the club calendar</b> for times and places, and the
  <b>club website</b> for news.</div>
<div class="box plain"><div class="bh">On paper</div>
  The <b>Reference Sheet</b> (linked as the &ldquo;Reference Guide&rdquo; on the club codeplug page): club repeaters,
  Seattle DMR channels, zones 1 and 3, and all 102 zones. Where it differs from this guide, follow this guide.</div>

{qr_strip('Club calendar', 'W7AW club home', 'Club codeplug page')}
''', accent='navy', key='help')

page('12 &middot; All the links', 'Point your phone&rsquo;s camera at a code to open the site', f'''
<div class="qrs">{"".join(qr_card(t) for t, _ in QR)}</div>
''', accent='navy', key='links')


CSS = '''
@page { size: letter; margin: 0; }
:root { --navy:#1f3a5f; --blue:#1e5aa8; --green:#2e7d4f; --gold:#f6d77a; --goldbg:#fff4cc;
        --ink:#1b1f24; --muted:#4f5763; --line:#c9d1db; --stripe:#f2f5f9; --ts1:#1e5aa8; --ts2:#c25e00; }
* { box-sizing:border-box; }
html,body { margin:0; padding:0; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color:var(--ink); font-size:14pt; line-height:1.35; }
.mono { font-family: Menlo, "SF Mono", Consolas, monospace; }
.page { width:8.5in; height:11in; padding:0.4in 0.45in 0.55in; position:relative; page-break-after:always; overflow:hidden; }
.page:last-child { page-break-after:auto; }
.band { color:#fff; border-radius:10px; padding:11px 18px 10px; margin-bottom:14px; }
.band.navy { background:var(--navy); } .band.blue { background:var(--blue); } .band.green { background:var(--green); }
.ttl { font-size:23pt; font-weight:800; letter-spacing:.2px; }
.sub { font-size:13pt; opacity:.95; margin-top:2px; }
h2 { font-size:16pt; margin:14px 0 6px; color:var(--navy); border-bottom:2px solid var(--line); padding-bottom:3px; }
h2.dmrh { color:var(--blue); } h2.fmh { color:var(--green); }
footer { position:absolute; left:0.45in; right:0.45in; bottom:0.22in; font-size:9.5pt; color:var(--muted);
         display:flex; justify-content:space-between; gap:12px; border-top:1px solid var(--line); padding-top:4px; }
footer .pg { white-space:nowrap; font-weight:700; }
.small { font-size:13pt; color:var(--muted); margin:6px 0; }
td .small { font-size:11pt; }
.lead { font-size:15pt; margin:2px 0 10px; }
b.red { color:#c62828; } b.grn { color:var(--green); }
/* page 1 road map */
ol.road { list-style:none; padding:0; margin:0 0 12px; display:grid; grid-template-columns:1fr 1fr; gap:8px 14px; }
ol.road li { display:flex; align-items:center; gap:10px; border:2px solid var(--line); border-radius:10px; padding:8px 10px;
             background:var(--stripe); font-size:14pt; line-height:1.25; }
.rn { flex:none; width:38px; height:38px; border-radius:50%; background:var(--navy); color:#fff; font-weight:800; font-size:17pt;
      display:flex; align-items:center; justify-content:center; }
.pref { display:block; color:var(--muted); font-size:12pt; font-weight:400; }
/* boxes */
.box { margin:9px 0; border-left:7px solid var(--navy); background:var(--stripe); border-radius:8px; padding:8px 12px; font-size:14pt; }
.box .bh { font-weight:800; font-size:15pt; margin-bottom:2px; }
.box p { margin:6px 0 0; }
.box.dmr { border-left-color:var(--blue); background:#eef4fc; } .box.dmr .bh { color:var(--blue); }
.box.fm { border-left-color:var(--green); background:#eef7f1; }
.box.gold { border-left-color:#d9a400; background:var(--goldbg); }
.box.warn { border-left-color:#c62828; background:#fdecea; } .box.warn .bh { color:#b71c1c; }
.box.plain { border-left-color:#6b7785; background:#f6f7f9; }
.box.tbdbox { border:2px dashed #7a4fb3; border-left:7px solid #7a4fb3; background:#f4effb; }
.tbd { display:inline-block; font-size:11pt; font-weight:800; color:#fff; background:#7a4fb3; border-radius:4px; padding:0 6px; }
/* lists */
ul.pts, ol.steps { margin:4px 0 0; padding-left:24px; } ul.pts li, ol.steps li { margin-bottom:6px; }
ol.steps.tight li { margin-bottom:3px; }
/* tables */
table.grid { border-collapse:separate; border-spacing:0; width:100%; border:1.5px solid #9aa7b6; border-radius:8px; overflow:hidden; }
table.grid th { background:#e3e9f1; color:var(--navy); text-align:left; font-size:12.5pt; padding:6px 9px; border-bottom:1.5px solid #9aa7b6; }
table.grid td { padding:6px 9px; border-bottom:1px solid #dde3ea; vertical-align:middle; font-size:13pt; }
table.grid tbody tr:nth-child(even) td { background:var(--stripe); }
table.grid tbody tr:last-child td { border-bottom:none; }
td.chn { font-weight:800; text-align:center; color:var(--navy); }
td.nm { font-weight:700; }
.fc td { font-size:13pt; } .fc .big, .big { font-size:16pt; }
.fc tr.dmrrow td:first-child { border-left:6px solid var(--blue); } .fc tr.fmrow td:first-child { border-left:6px solid var(--green); }
.fc tr.gold td { background:var(--goldbg) !important; }
.ts { display:inline-block; font-family:Menlo,monospace; font-weight:800; font-size:11pt; color:#fff; border-radius:5px; padding:0 6px; }
.ts1 { background:var(--ts1); } .ts2 { background:var(--ts2); }
.two { display:grid; grid-template-columns:1fr 1fr; gap:18px; } .two > * { min-width:0; }
.key { display:inline-block; font-family:Menlo,monospace; font-weight:800; font-size:12pt; border:1.5px solid #6b7785;
       border-bottom-width:3px; border-radius:5px; padding:0 6px; background:#fafbfc; line-height:1.3; }
.key.home { background:#e53935; color:#fff; border-color:#8e1b1b; }
.key.menu { background:var(--blue); color:#fff; border-color:#123a70; }
.krow { white-space:nowrap; }
.tri { color:#e53935; }
.h2n { font-size:13pt; font-weight:400; color:var(--muted); }
.cn { display:inline-block; width:28px; height:28px; line-height:28px; border-radius:50%; background:var(--gold); border:2px solid #8a6a00; font-size:13pt; }
.scrwrap { text-align:center; } svg.scr { width:5.0in; height:auto; }
.scrt td { font-size:14pt; padding:8px 10px; line-height:1.3; }
.radwrap { text-align:center; } svg.rad { width:5.6in; height:auto; }
.keyt td { font-size:13pt; }
/* QR */
.qrs { display:flex; flex-wrap:wrap; justify-content:center; gap:22px 18px; margin-top:10px; }
.qrs .qr { width:2.3in; }
.qrstrip { display:flex; justify-content:center; gap:28px; margin:14px 0 4px; }
.qrstrip .qr { width:2.4in; }
.qrstrip svg.qrsvg { width:1.25in; height:1.25in; }
.qr { display:block; text-align:center; break-inside:avoid; color:inherit; text-decoration:none; }
.nw { white-space:nowrap; }
svg.qrsvg { width:1.4in; height:1.4in; display:block; margin:0 auto; }
.ql { font-weight:800; font-size:13pt; margin-top:3px; line-height:1.2; }
.qu { font-size:11pt; color:var(--muted); line-height:1.2; }
'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>W7AW DM-32UV Starter Guide</title>
<style>{CSS}</style></head><body>
{render()}
</body></html>'''
open(DST, 'w').write(html)
print(f'wrote {DST} ({len(PAGES)} pages)')
