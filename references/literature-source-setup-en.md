# Literature Source Setup (OpenAlex-first)

## Required checks at session start

Before generating any lecture output, verify:

1. OpenAlex is available (default primary source)
2. PubMed is available for biomedical cross-check (recommended)
3. `paper-distill` MCP is connected

## Environment variables

Minimum recommended:

```bash
OPENALEX_EMAIL=your-email@example.com
```

Biomedical enhancement (optional):

```bash
NCBI_EMAIL=your-email@example.com
NCBI_API_KEY=your-ncbi-api-key
```

MCP runtime data directory (example):

```bash
PAPER_DISTILL_DATA_DIR=C:/Users/Lenovo/.paper-distill
```

## Quick MCP check (OpenCode example)

```bash
opencode mcp list
```

Expected status: `paper-distill` is `connected`.

## Source priority policy

Default retrieval order:

1. OpenAlex (primary)
2. PubMed (biomedical cross-check)
3. Other sources (supplementary)

Use DOI/PMID/PMCID as canonical identifiers to avoid title-only mismatch.
