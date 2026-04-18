# Source Digest Standards

This document defines the structure and quality rules for source digests.

## 1. Purpose

A source digest is an extended, structured Markdown summary of a long source. It reduces compilation cost while preserving enough evidence and context for later wiki integration.

The original source remains the source of truth. The digest is an intermediate artifact optimized for concept extraction.

## 2. Recommended folder layout

Use:

```text
raw/
├── originals/
│   └── source-file.pdf
├── digests/
│   └── source-file.md
└── _source_registry.md
```

`raw/originals/` stores original files.

`raw/digests/` stores Markdown digests.

`raw/_source_registry.md` maps originals to digests and status.

## 3. Digest filename rules

Digest filenames must be:
- English
- kebab-case
- stable
- based on the original source title or filename

Preferred pattern:

```text
raw/originals/paper-name.pdf
raw/digests/paper-name.md
```

Avoid vague names such as:
- `summary.md`
- `paper.md`
- `notes.md`

## 4. Digest template

Use this structure for new digests.

```markdown
---
digest_type: source-digest
original_source: raw/originals/source-file.pdf
status: ready-for-wiki-compilation
---

# Source Digest: [Source Title]

## Bibliographic metadata

- Title:
- Authors:
- Year:
- Venue or source:
- Original source: [[raw/originals/source-file.pdf]]

## Research problem or central question

[What problem, question, or gap the source addresses.]

## Context and motivation

[Background needed to understand why the source matters.]

## Methodology or approach

[Methods, data, argument structure, experimental setup, or analytical approach.]

## Evidence and results

[Main findings, observations, evidence, or results.]

## Main claims

- [Claim 1]
- [Claim 2]

## Conclusions

[What the source concludes.]

## Limitations and caveats

[Limitations stated by the source and limitations detected during digestion.]

## Concepts likely relevant to the wiki

- [Concept candidate] - [why it may matter]

## Notable passages

- [Short passage or paraphrase] - [why it matters]

## Open questions

- [Question]

## Suggested wiki integration

- Potential new concepts:
- Existing concepts likely to update:
- Related sections:
```

## 5. Quality rules

The digest must be:
- faithful to the source
- structured
- sufficiently detailed for later concept extraction
- explicit about uncertainty
- clear about what comes from the source versus interpretation

Avoid:
- replacing evidence with vague summary
- overstating the source's claims
- omitting limitations
- inventing methodology or results
- copying long copyrighted passages

## 6. Length guidance

For short articles, a digest may be 800 to 1500 words.

For long papers, reports, or transcripts, a digest may be 1500 to 4000 words.

Prefer enough detail for concept extraction over extreme compression.

## 7. Source registry format

Use `raw/_source_registry.md` to track digestion status.

Recommended structure:

```markdown
# Source Registry

## [[raw/originals/source-file.pdf]]

- Digest: [[raw/digests/source-file]]
- Status: ready-for-wiki-compilation
- Date digested: YYYY-MM-DD
- Extraction limitations: none
```

Valid statuses:
- `not-digested`
- `digestion-in-progress`
- `ready-for-wiki-compilation`
- `needs-better-source-text`
- `do-not-compile`

## 8. Boundary with wiki compilation

Source digestion creates or updates digests only.

Wiki compilation creates or updates concept notes under `wiki/`.

Do not perform both workflows in one step unless the user explicitly asks for a full pipeline run.
