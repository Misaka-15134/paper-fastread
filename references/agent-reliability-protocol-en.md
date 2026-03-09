# Agent Reliability Protocol (No Missing Images / Sections)

Use this protocol when `paper-fastread` is invoked by other agents.

## Objectives

1. Never miss required sections (fixed 9-section structure)
2. Never miss required figure blocks
3. Never ship empty figure image slots

## Mandatory execution flow

### Step 1: copy template first, then fill

- Chinese: `templates/lecture-template.html`
- English: `templates/lecture-template-en.html`

Do not free-generate from blank files.

### Step 2: image resolution with fallback

Each `figure-section` must include `<img ...>`.

Resolve in order:

1. PMC main figures (`gr`)
2. Elsevier main figures (`gr`)
3. Publisher full-text figure URLs

If all fail, keep the image tag with traceable placeholder:

```html
<img src="https://placehold.co/1200x700?text=Figure+Unavailable" class="fig-img" alt="Figure unavailable" />
```

Also record attempted sources in `caption-box`.

### Step 3: run structural checker (mandatory)

Chinese:

```bash
bash tools/check_template_consistency.sh <output.html> lecture
```

English:

```bash
bash tools/check_template_consistency.sh <output.html> lecture-en
```

### Step 4: self-repair loop (max 3 rounds)

- If check fails, patch only missing blocks and empty content.
- Re-run checker after every patch.
- If still failing after 3 rounds, deliver partial output + explicit missing-items list + next-step plan.

## Forbidden shortcuts

- Do not delete failed figure sections
- Do not replace Results quotes with abstract paraphrase
- Do not skip checker before delivery
