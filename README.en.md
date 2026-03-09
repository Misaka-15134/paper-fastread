# paper-fastread

[中文说明](./README.md) | [English README](./README.en.md)

`paper-fastread` is a skill-oriented repository for turning daily paper feeds into **deep, teachable outputs**.

Instead of stopping at “paper links”, it extends your literature workflow into:

- A structured 9-section lecture-style HTML brief
- Figure-by-figure evidence walkthrough (logic chain + Results quotes + parameter fidelity)
- Methodology deep-dive and critical discussion prompts
- One-click HTML → PDF export for sharing

It integrates the `paper-distill-mcp` workflow (search + metadata + figure retrieval), then adds translation, extraction, synthesis, and critical framing for fast comprehension.

---

## Why this skill

Compared with plain link push systems, `paper-fastread` helps you move from:

1. **Discovering papers → understanding papers**
2. **Abstract summary → evidence-driven Results interpretation**
3. **Viewing figures → teaching figures**
4. **Personal reading → team-ready deliverables (HTML/PDF)**

---

## Core capabilities

- Fixed 9-section output structure
- Mandatory figure block order:
  `logic-box → image → caption-box → quote-box → steps-box → results-box`
- Default source policy: **OpenAlex first**, PubMed cross-check for biomedical papers
- Integrated `paper-distill-mcp` workflow
- HTML to PDF export via `tools/html_to_pdf.sh`

---

## Quick start (multi-client)

### A) Common setup

```bash
uv tool install paper-distill-mcp
```

Recommended environment variables:

```bash
OPENALEX_EMAIL=your-email@example.com
NCBI_EMAIL=your-email@example.com
NCBI_API_KEY=your-ncbi-api-key
```

Clone this repo:

```bash
git clone https://github.com/Misaka-15134/paper-fastread.git
cd paper-fastread
```

### B) Client integration

#### OpenCode

Add to `opencode.json`:

```json
{
  "mcp": {
    "paper-distill": {
      "type": "local",
      "command": ["uvx", "paper-distill-mcp"]
    }
  }
}
```

Check:

```bash
opencode mcp list
```

#### Claude Code

```bash
claude mcp add paper-distill -- uvx paper-distill-mcp
```

or `.mcp.json`:

```json
{
  "mcpServers": {
    "paper-distill": {
      "command": "uvx",
      "args": ["paper-distill-mcp"]
    }
  }
}
```

#### OpenClaw

```bash
mcporter config add paper-distill --command uvx --scope home -- paper-distill-mcp
mcporter list
```

#### Qoder (and other MCP-capable clients)

Use the same `mcpServers.paper-distill` JSON template as above and place it in your client’s MCP config file.

---

## Prompt for other agents (self-install + self-run)

```text
Install paper-fastread into the current client skill directory and connect paper-distill-mcp.

Requirements:
1) Install MCP tool: uv tool install paper-distill-mcp
2) Register MCP server: command=uvx, args=[paper-distill-mcp]
3) Verify connection status in the current client
4) Read SKILL.md and references/literature-source-setup-en.md
5) Ask user to confirm OPENALEX_EMAIL and optional PubMed config
6) Generate a 9-section lecture HTML and export PDF
```

---

## Usage example (prompt + outputs)

### Example prompt

```text
Use paper-fastread for this paper:
Blood metabolites mediate causal inference studies on the effect of gut microbiota on the risk of vascular calcification

Requirements:
1) Run source config check (OpenAlex default + PubMed cross-check)
2) Output a 9-section lecture HTML
3) Enforce figure blocks: logic/caption/quote/steps/results
4) Export same-name PDF
5) Generate 2 screenshots: overview + figure deep-read module
```

### Example outputs in this repo

- HTML: `examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html`
- PDF: `examples/Blood_metabolites_VC_PMID40139524_lecture_demo.pdf`
- Screenshots:
  - `assets/screenshots/demo-overview.png`
  - `assets/screenshots/demo-figure-module.png`

---

## HTML → PDF

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html
```

Custom output path:

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html outputs/demo.pdf
```

See: `references/html-to-pdf-en.md`

---

## Key docs

- Skill entry: `SKILL.md`
- English setup: `references/literature-source-setup-en.md`
- MCP workflow: `references/paper-distill-mcp-workflow-en.md`
- English lecture spec: `references/single-paper-lecture-template-en.md`
- English prompts: `references/quick-prompts-en.md`
- English PDF guide: `references/html-to-pdf-en.md`
