---
name: paper-fastread
description: 将单篇科研论文重构为9章节讲义并输出可投屏HTML（支持中文/英文）。用于“逐图精读”“Results原文提取+推导”“方法学深挖”“讲课版论文导读”等场景；要求严格保留n值、P值、fold change、scale bar，并按Figure逻辑链条组织内容。
---

# Paper FastRead (Single Paper → Lecture, ZH)

## Language mode (ZH / EN)

- If user requests Chinese output, follow Chinese chapter titles and references under `*-zh.md`.
- If user requests English output, follow English chapter titles and references under `*-en.md`.
- Keep the same evidence rigor for both languages:
  - Results quotes must be verbatim
  - figure logic chain must be explicit
  - quantitative details must be preserved (`n=`, `P<`, `fold`, `scale bar`)

## Session start (must prompt first)

Before any paper processing, always ask the user to confirm literature source configuration:

1. OpenAlex source (default): confirm `OPENALEX_EMAIL` is configured.
2. PubMed source (optional but recommended for biomedical papers): confirm `NCBI_EMAIL` / `NCBI_API_KEY` if available.
3. MCP availability: confirm `paper-distill` MCP is connected.

If not configured, stop generation and provide setup guidance from:
- Chinese workflow: `references/literature-source-setup.md`
- English workflow: `references/literature-source-setup-en.md`

Use this fixed startup prompt template (Chinese):

```text
在开始前请先确认文献源配置：
1) OpenAlex（默认主源）：请确认 OPENALEX_EMAIL 已配置；
2) PubMed（医学论文推荐）：如可用请配置 NCBI_EMAIL / NCBI_API_KEY；
3) MCP 连通性：请先运行 `opencode mcp list`，确认 paper-distill 为 connected。

若未配置，我会先引导你完成配置，再开始论文检索与讲义生成。
```

Use this fixed startup prompt template (English):

```text
Before we start, please confirm your literature source setup:
1) OpenAlex (default primary source): confirm OPENALEX_EMAIL is configured.
2) PubMed (recommended for biomedical papers): configure NCBI_EMAIL / NCBI_API_KEY if available.
3) MCP connectivity: run `opencode mcp list` (or your client equivalent) and confirm paper-distill is connected.

If not configured, I will guide setup first, then proceed to paper retrieval and lecture generation.
```

## Literature source policy

- Default source priority: **OpenAlex → PubMed → other sources**.
- For biomedical/clinical papers, run PubMed cross-check after OpenAlex retrieval.
- Keep metadata canonical: Title, Journal, DOI, PMID/PMCID (if present).

## Core workflow (must follow)

1. Parse paper metadata and full-text sections: Introduction, Abstract, Results, Methods, Discussion, and figure captions.
2. Produce the fixed 9-chapter lecture structure in the exact required order.
3. Build each Figure module with required HTML blocks and labels.
4. Run quality-gate checklist before delivering final HTML.
5. If user needs shareable handout, convert final HTML to PDF.
6. Enforce agent reliability protocol to prevent missing sections/images.

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
  - `references/single-paper-lecture-template-en.md`
- Delivery quality checklist:
  - `references/checklists/release-checklist.md`
- Literature source setup and MCP workflow:
  - `references/literature-source-setup.md`
  - `references/paper-distill-mcp-workflow.md`
  - `references/literature-source-setup-en.md`
  - `references/paper-distill-mcp-workflow-en.md`
 - Reliability protocol:
  - `references/agent-reliability-protocol.md`
  - `references/agent-reliability-protocol-en.md`
- HTML to PDF export:
  - `references/html-to-pdf.md`
 - Prompt packs:
  - `references/quick-prompts.md`
  - `references/quick-prompts-en.md`

## Template and validation tools

- Canonical lecture template: `templates/lecture-template.html`
- English lecture template: `templates/lecture-template-en.html`
- Optional checks:
  - `tools/check_template_consistency.py`
  - `tools/check_template_consistency.sh`
  - `tools/html_to_pdf.sh`

## Execution rules

- Prioritize evidence-rich interpretation over summary-style paraphrase.
- Keep story continuity explicit: explain why Figure B follows Figure A.
- Do not fabricate unavailable evidence; clearly mark missing full-text dependencies.
- Keep output reusable for teaching: structured, traceable, and citation-grounded.

## Reliability rules for cross-agent usage (mandatory)

1. Start from template file, never from blank output.
2. Every figure-section must contain an image tag (`<img ...>`).
3. If no valid source image can be resolved, use a placeholder image and log attempted sources in caption-box.
4. Always run template checker before delivery.
5. If checker fails, run self-repair loop up to 3 rounds; then deliver partial output with explicit missing list.
