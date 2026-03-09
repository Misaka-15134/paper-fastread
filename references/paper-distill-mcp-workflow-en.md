# paper-distill-mcp Workflow for paper-fastread (EN)

## Goal

Use `paper-distill-mcp` to:

1. Search and shortlist papers (OpenAlex-first)
2. Retrieve figure assets suitable for lecture output

## Step 1: search papers

- Query by title, keywords, or authors.
- Lock DOI first, then enrich with PMID/PMCID when available.
- For biomedical papers, run PubMed cross-check (title/year/authors).

Keep these fields:

- title
- journal
- year
- doi
- pmid / pmcid
- abstract

## Step 2: choose canonical source

Priority:

1. DOI landing page
2. PMC full text (if open access)
3. Publisher full text page

Avoid relying on secondary aggregators only.

## Step 3: get figure URLs

### If PMCID exists

- Prefer PMC `gr` main figure assets.

### If Elsevier paper

- Prefer main figure pattern:

`https://ars.els-cdn.com/content/image/1-s2.0-{PII}-gr1.jpg`

- Avoid `fx` unless supplemental figures are explicitly needed.

## Step 4: map figures to lecture blocks

For each figure include:

- `logic-box`: why this figure follows previous evidence
- `caption-box`: original caption + translated caption with quantitative details
- `quote-box`: 3–5 consecutive Results sentences
- `steps-box`: sample, condition, readout
- `results-box`: panel-level outcomes + local conclusion

## Step 5: quality gate

Before delivery ensure:

- DOI/PMID/PMCID consistency
- figure URL accessibility and correct figure index
- quantitative fidelity in caption translation (`n`, `P`, `fold`, `scale bar`)
- Results quote source is main text, not abstract-only paraphrase
