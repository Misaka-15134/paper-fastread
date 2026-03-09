# Single Paper -> Lecture Template (EN)

Goal: Convert one paper into a reusable, evidence-rich 9-section lecture handout.

## Fixed section order (mandatory)

1. Paper overview card (title/journal/PMID/DOI/authors/core claim)
2. Research logic and storyline (question-hypothesis-stepwise validation-conclusion)
3. Introduction guide (2-3 original English paragraphs + interpretation)
4. Abstract deep dive (sentence-by-sentence)
5. Figure-by-figure analysis and logic chaining
6. Core methods deep dive
7. Methods critique
8. Discussion guide
9. Discussion questions (3-5)

## Figure module structure (mandatory)

```html
<div class="figure-section">
  <h3>Figure X: [Main message]</h3>

  <div class="logic-box">
    <h4>🔗 Research logic chain:</h4>
    <p><strong>Bridge:</strong>[What was concluded before, what remains unresolved, why this figure is designed next]</p>
  </div>

  <img src="[Correct URL]" class="fig-img" onclick="openModal(this.src)" alt="Figure X" />

  <div class="caption-box">
    <p><strong>Original caption:</strong>[verbatim English caption]</p>
    <p><strong>Translated caption:</strong>[preserve all quantitative details]</p>
  </div>

  <div class="quote-box">
    <h4>📝 Results text analysis:</h4>
    <p><strong>Quoted Results text:</strong><em>"[3-5 consecutive Results sentences]"</em></p>
    <p><strong>Data interpretation:</strong>[how figure-level data support the local claim]</p>
  </div>

  <div class="steps-box">
    <h4>🔬 Experimental details:</h4>
    <ol>
      <li><strong>Sample & grouping:</strong>[materials, n, groups]</li>
      <li><strong>Conditions:</strong>[dose, timing, medium]</li>
      <li><strong>Readouts:</strong>[assays, antibodies/probes]</li>
    </ol>
  </div>

  <div class="results-box">
    <h4>📊 Result summary:</h4>
    <div class="panel-details">
      <p>Panel A-B: [observations + significance]</p>
      <p>Panel C-D: [observations + fold changes]</p>
    </div>
    <p><strong>Local conclusion:</strong>[1-2 sentences leading to next figure]</p>
  </div>
</div>
```

## Methods deep dive standard

In Section 6, select 1-2 key methods and include:

1. Original Methods paragraph (verbatim)
2. Rationale behind parameter/model choices
3. Rigor analysis (blinding, multi-center, cutoffs, QC)
4. Advantages and limitations

## Quantitative fidelity baseline

- Do not paraphrase away numeric detail.
- Preserve: `n=`, `P<`, fold changes, scale bars, doses, time points.
- Results interpretation must be grounded in main text quotes.
