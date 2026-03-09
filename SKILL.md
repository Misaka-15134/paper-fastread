---
name: paper-fastread
description: 将单篇科研论文重构为9章节中文讲义并输出可投屏HTML。用于“逐图精读”“Results原文提取+中文推导”“方法学深挖”“讲课版论文导读”等场景；要求严格保留n值、P值、fold change、scale bar，并按Figure逻辑链条组织内容。
---

# Paper FastRead (Single Paper → Lecture, ZH)

## Core workflow (must follow)

1. Parse paper metadata and full-text sections: Introduction, Abstract, Results, Methods, Discussion, and figure captions.
2. Produce the fixed 9-chapter lecture structure in the exact required order.
3. Build each Figure module with required HTML blocks and labels.
4. Run quality-gate checklist before delivering final HTML.

## Output contract (strict)

- Always output exactly **9 chapters** in this order:
  1) 论文概览卡片
  2) 研究逻辑与故事主线
  3) 引言导读
  4) 摘要精读
  5) Figure逐图精读与逻辑串联
  6) 核心方法学精读
  7) 方法学批判
  8) 讨论导读
  9) 课堂讨论题
- For each Figure, enforce block order:
  `logic-box → image → caption-box → quote-box → steps-box → results-box`.
- In caption translation, preserve all quantitative information:
  `n=`, `P<`, fold change, scale bar, dose, and timepoint.
- For Elsevier images, use `gr` IDs for primary figures; avoid `fx` IDs unless supplemental figures are explicitly required.

## Required references (progressive disclosure)

- Primary specification and figure HTML template:
  - `references/single-paper-lecture-template-zh.md`
- Delivery quality checklist:
  - `references/checklists/release-checklist.md`

## Template and validation tools

- Canonical lecture template: `templates/lecture-template.html`
- Optional checks:
  - `tools/check_template_consistency.py`
  - `tools/check_template_consistency.sh`

## Execution rules

- Prioritize evidence-rich interpretation over summary-style paraphrase.
- Keep story continuity explicit: explain why Figure B follows Figure A.
- Do not fabricate unavailable evidence; clearly mark missing full-text dependencies.
- Keep output reusable for teaching: structured, traceable, and citation-grounded.
