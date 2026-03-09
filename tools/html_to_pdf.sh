#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: bash tools/html_to_pdf.sh <input.html> [output.pdf]"
  exit 1
fi

INPUT="$1"
if [ ! -f "$INPUT" ]; then
  echo "[ERROR] Input HTML not found: $INPUT"
  exit 1
fi

if [ "$#" -eq 2 ]; then
  OUTPUT="$2"
else
  OUTPUT="${INPUT%.html}.pdf"
fi

ABS_INPUT="$(realpath "$INPUT")"
ABS_OUTPUT="$(realpath -m "$OUTPUT")"
FILE_URL="file:///$ABS_INPUT"

CHROME=""
for CANDIDATE in \
  "C:/Program Files/Google/Chrome/Application/chrome.exe" \
  "C:/Program Files/Microsoft/Edge/Application/msedge.exe" \
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"; do
  if [ -f "$CANDIDATE" ]; then
    CHROME="$CANDIDATE"
    break
  fi
done

if [ -z "$CHROME" ]; then
  echo "[ERROR] No Chromium browser found (Chrome/Edge)."
  exit 1
fi

mkdir -p "$(dirname "$ABS_OUTPUT")"

"$CHROME" \
  --headless \
  --disable-gpu \
  --print-to-pdf="$ABS_OUTPUT" \
  --no-pdf-header-footer \
  "$FILE_URL"

echo "[OK] PDF generated: $ABS_OUTPUT"
