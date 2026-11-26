#!/bin/zsh
# Build the Starter Guide: HTML -> PDF (+ PNG previews). Doesn't touch the Reference Sheet.
# Usage: ./make-starter.sh
set -euo pipefail
cd "${0:A:h}"

PDF="output/W7AW-DM32UV-Starter-Guide.pdf"

# The Starter Guide needs segno (QR codes) from the project's virtual environment.
PY=".venv/bin/python"
if [[ ! -x "$PY" ]] || ! "$PY" -c 'import segno' 2>/dev/null; then
  echo "ERROR: $PY is missing or can't import segno." >&2
  echo "Set it up once per checkout: see \"Python setup\" in AGENTS.md." >&2
  exit 1
fi

mkdir -p build output build/starter-preview
"$PY" tools/build_starter.py build/starter.html

# Same browser as make.sh: Playwright's headless Chromium, the Chrome app only as a fallback.
CHROME=$(find ~/Library/Caches/ms-playwright -name chrome-headless-shell -type f -perm +111 2>/dev/null | sort | tail -1 || true)
[[ -z "$CHROME" ]] && CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "ERROR: no headless Chromium found (see AGENTS.md)." >&2; exit 1; }

rm -f "$PDF"           # so a failed run can't leave last run's PDF looking new
PROFILE="$(mktemp -d)"
trap 'rm -rf "$PROFILE"' EXIT

# Run the browser in a process group of its own and wait for it (at most 3 minutes).
# The group is signalled only while its leader is still running and not yet reaped, so the
# group id can't have been reused. After the leader exits, the group is only checked, never signalled.
"$PY" - "$CHROME" --headless --no-sandbox --disable-gpu --user-data-dir="$PROFILE" \
  --no-pdf-header-footer --print-to-pdf="$PWD/$PDF" "file://$PWD/build/starter.html" <<'PYEOF'
import os, signal, subprocess, sys
p = subprocess.Popen(sys.argv[1:], start_new_session=True, stderr=subprocess.DEVNULL)
pgid = p.pid
print(f"browser pid {p.pid}, process group {pgid}")
stopped = False
try:
    rc = p.wait(timeout=180)
except (subprocess.TimeoutExpired, KeyboardInterrupt) as why:
    stopped = True
    print(f"browser stopped ({type(why).__name__}): signalling its group {pgid}")
    os.killpg(pgid, signal.SIGTERM)      # leader not reaped yet, so the group id is still ours
    try:
        p.wait(timeout=10)
    except subprocess.TimeoutExpired:
        print(f"browser group {pgid} ignored TERM: sending KILL")
        os.killpg(pgid, signal.SIGKILL)
        p.wait()
try:
    os.killpg(pgid, 0)
    print(f"WARNING: processes from browser group {pgid} are still running (left alone)")
except ProcessLookupError:
    print(f"browser group {pgid} has exited")
if stopped:
    print("browser was stopped: build failed")
    sys.exit(124)
print(f"browser exit status {rc}")
sys.exit(128 - rc if rc < 0 else rc)
PYEOF

pdfinfo "$PDF" | grep -E 'Pages|Page size'
rm -f build/starter-preview/*.png(N)
pdftoppm -r 90 -png "$PDF" build/starter-preview/page
echo "PDF: $PDF   previews: build/starter-preview/"
