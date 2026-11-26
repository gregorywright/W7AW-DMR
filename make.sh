#!/bin/zsh
# Rebuild the cheat sheet: codeplug (.data) -> JSON -> HTML -> PDF (+ PNG previews).
# Usage: ./make.sh [codeplug.data]
set -euo pipefail
cd "${0:A:h}"

CODEPLUG="${1:-codeplug/Gregs-BaofengDM32UV_NWDMR.data}"
PDF="output/W7AW-DM32UV-Cheat-Sheet.pdf"
mkdir -p build output build/preview

python3 tools/decode.py "$CODEPLUG" build/sheet.json
python3 tools/build.py build/sheet.json build/cheatsheet.html

# Headless Chromium from Playwright's cache. The Google Chrome app crashes in
# headless print mode under the Kiro Crew sandbox, so it is only a fallback.
CHROME=$(find ~/Library/Caches/ms-playwright -name chrome-headless-shell -type f -perm +111 2>/dev/null | sort | tail -1)
[[ -z "$CHROME" ]] && CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

"$CHROME" --headless --no-sandbox --disable-gpu --user-data-dir="$(mktemp -d)" \
  --no-pdf-header-footer --print-to-pdf="$PWD/$PDF" "file://$PWD/build/cheatsheet.html" 2>/dev/null

pdfinfo "$PDF" | grep -E 'Pages|Page size'
# Page images for checking layout (needs poppler: brew install poppler)
rm -f build/preview/*.png(N)
pdftoppm -r 90 -png "$PDF" build/preview/page
echo "PDF: $PDF   previews: build/preview/"
