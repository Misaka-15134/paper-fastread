# HTML → PDF Export (EN)

## Purpose

Convert final lecture HTML into a shareable PDF for distribution and archiving.

## Command

```bash
bash tools/html_to_pdf.sh <input.html> [output.pdf]
```

Examples:

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html outputs/demo.pdf
```

## Browser requirements

The script auto-detects Chromium browsers in this order:

1. `C:/Program Files/Google/Chrome/Application/chrome.exe`
2. `C:/Program Files/Microsoft/Edge/Application/msedge.exe`
3. `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`

If none are found, it exits with an error.

## Quality tips

- Validate lecture structure before export:
  - Chinese: `bash tools/check_template_consistency.sh <file> lecture`
  - English: `bash tools/check_template_consistency.sh <file> lecture-en`
- Ensure figure URLs are accessible before printing.
- If source HTML is in a Unicode path, the script automatically stages to a temp ASCII path for stable rendering.
