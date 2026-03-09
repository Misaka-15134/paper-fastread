# HTML → PDF Export

## Purpose

将最终讲义 HTML 导出为便于打印与分享的 PDF。

## Command

```bash
bash tools/html_to_pdf.sh <input.html> [output.pdf]
```

示例：

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html outputs/demo.pdf
```

## Browser requirements

脚本会自动检测以下浏览器（按顺序）：

1. `C:/Program Files/Google/Chrome/Application/chrome.exe`
2. `C:/Program Files/Microsoft/Edge/Application/msedge.exe`
3. `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`

若未检测到浏览器会报错并终止。

## Quality tips

- 导出前先检查 HTML 的 Figure 图片是否可访问。
- 建议用 `tools/check_template_consistency.sh` 先做结构校验。
- PDF 为浏览器打印渲染，若需更强排版控制可后续补充专用模板。
