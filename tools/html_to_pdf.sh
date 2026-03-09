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

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_HTML="$TMP_DIR/input.html"
cp "$ABS_INPUT" "$TMP_HTML"

if command -v cygpath >/dev/null 2>&1; then
  INPUT_PATH="$(cygpath -am "$TMP_HTML")"
  OUTPUT_PATH="$(cygpath -am "$ABS_OUTPUT")"
  FILE_URL="file:///$INPUT_PATH"
else
  INPUT_PATH="$TMP_HTML"
  OUTPUT_PATH="$ABS_OUTPUT"
  FILE_URL="file://$INPUT_PATH"
fi

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
  --headless=old \
  --disable-gpu \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=10000 \
  --print-to-pdf="$OUTPUT_PATH" \
  --no-pdf-header-footer \
  "$FILE_URL"

echo "[OK] PDF generated: $OUTPUT_PATH"
