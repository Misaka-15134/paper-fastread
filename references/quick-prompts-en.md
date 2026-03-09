# Quick Prompt Pack (EN)

## Prompt 0: source configuration check (mandatory)

```text
Before starting, verify literature source setup:
- Primary source: OpenAlex (confirm OPENALEX_EMAIL)
- Biomedical cross-check: PubMed (confirm NCBI_EMAIL / NCBI_API_KEY if available)
- MCP: confirm paper-distill is connected (e.g., `opencode mcp list`)

If not configured, provide setup steps first, then proceed.
```

## Prompt 1: single-paper lecture generation

```text
Generate a full lecture HTML from templates/lecture-template-en.html with this paper:
- Keep fixed 9-section structure
- For each figure, include logic/caption/quote/steps/results blocks
- Preserve quantitative details in caption translation: n, P, fold change, scale bar
- Use OpenAlex metadata first, then PubMed cross-check for biomedical papers

Input: {PDF/HTML/URL/PMID/DOI}
Output filename: lecture_<topic>_<PMID>.html
```

## Prompt 2: improve an existing lecture file

```text
Enhance the existing lecture HTML without changing visual style:
- deepen figure interpretation
- fill missing quantitative details in caption translation
- keep template block structure intact
```

## Prompt 3: caption completeness repair

```text
Check each figure caption translation against original caption and repair missing details:
- panel labels (a)(b)(c)...
- n values / P values / scale bars / dose / time points
Do not modify original caption text and image URLs.
```

## Prompt 4: bibliometric dashboard generation

```text
Generate bibliometric HTML using templates/bibliometric-network-template.html:
- input CSV: {path_to_csv}
- keep layout and chart set
- keep yearly mode as year-specific (not cumulative)
- output: {name}_network.html + nodes/edges/centrality.csv
```

## Prompt 5: access-failure fallback

```text
Check paper accessibility first:
- if accessible: generate full lecture
- if inaccessible: ask user to place PDF under ./inputs/papers/
- if full text unavailable: output partial lecture skeleton with explicit missing-evidence marks
```

## Prompt 6: batch lecture generation

```text
Generate lectures in batch:
- use templates/lecture-template-en.html
- one HTML per paper
- generate index page
- mark status for each item (full/partial)

Input list: {pmid_or_doi_list}
```
