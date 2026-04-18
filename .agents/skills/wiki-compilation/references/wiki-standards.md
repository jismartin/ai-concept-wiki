# Wiki Standards Reference

This document defines the quality rules for concept extraction, naming, note structure, linking, deduplication, and indexing.

## 1. Concept extraction rules

When `raw/digests/` exists, treat digest Markdown files as the preferred compilation inputs.
Use original files under `raw/originals/` for traceability only, unless the user explicitly asks to compile directly from an original source.

For each pending file, extract between 2 and 10 concepts.

A concept must be:
- reusable
- distinct
- non-overlapping
- meaningful outside the source file
- suitable for a standalone wiki note

Avoid:
- concepts that are too broad
- concepts that are too granular
- restating the same idea as multiple notes
- splitting synonyms into separate concepts

Prefer fewer, richer concepts over many shallow ones.

## 2. Section assignment

Each concept must go into exactly one section.

Preferred section folders:
- `wiki/llm-fundamentals/`
- `wiki/reasoning/`
- `wiki/fairness-bias/`
- `wiki/ai-ethics/`

Choose the most specific section.

If a concept could fit more than one section:
- choose the best primary location
- connect related areas using links
- mention ambiguity in the final report if it matters

Do not duplicate the same note in multiple folders.

## 3. Deduplication rules

Before creating a note, search the corresponding section folder for related concepts.

Check overlap using:
- filename
- aliases
- definition
- conceptual scope
- major claims or ideas

If a similar note exists:
- update it instead of creating a new one

If two existing notes partially overlap:
- prefer the most precise existing note
- avoid creating a third overlapping note

Core rule:
> Prefer merging over creating.

When uncertain, choose the option that reduces duplication and preserves conceptual clarity.

## 4. File naming rules

Filenames must be:
- English only
- kebab-case
- globally unique within the wiki
- semantically precise
- stable over time

Good examples:
- `attention-mechanism.md`
- `chain-of-thought.md`
- `reward-model-overoptimization.md`

Avoid:
- `attention.md`
- `reasoning.md`
- `bias.md`

Prefer stable naming over frequent renaming.
Use aliases to handle naming variants.

## 5. Note template

Use this structure for new notes.

```markdown
---
aliases:
  - [alternative name]
  - [common variation]
---

# [Concept Name]

## Definition

[2–3 precise sentences]

## Core ideas

[Structured explanation of the concept]

## Key tensions or open questions

[Debates, trade-offs, unresolved issues]
[Omit this section if there is no meaningful content]

## Related concepts

- [[llm-fundamentals/example-note]] — [relation]
- [[reasoning/example-note]] — [relation]

## Sources

- [[raw/digests/source-file]] - [how this digest contributed]
- [[raw/originals/source-file.pdf]] - [original source, when useful for traceability]
```

## 6. Content quality rules

Every concept note must be:
- self-contained
- precise
- readable independently
- non-redundant
- useful as a long-term knowledge asset

Avoid:
- fluff
- repetition
- vague language
- empty filler
- unsupported speculation presented as fact

Use concise, information-dense prose.

## 7. Update rules for existing notes

When updating an existing note:
- preserve useful content
- integrate new material cleanly
- remove duplication where needed
- keep the note coherent as one concept page
- append source-specific contributions without rewriting stable definitions unless the new source materially changes the concept

Do not overwrite good content unnecessarily.
Do not create near-duplicate notes because wording differs.

## 8. Cross-linking rules

Use Obsidian-compatible forward links.

Rules:
- use only forward links
- do not manually create backlink sections
- use full paths from `wiki/`
- prefer precise links over generic ones
- avoid excessive linking
- only link to notes that already exist or are being created in the same run

Correct:
```markdown
[[llm-fundamentals/attention-mechanism]]
```

Incorrect:
```markdown
[[attention-mechanism]]
```

Maintain a clean conceptual graph.
Avoid link explosion.

## 9. Index update rules

Update `wiki/_index.md` for every created or updated concept.

Each index entry should include:
- concept path
- one-sentence summary
- current date

Constraints:
- summary must be one sentence
- summary should be 20 words or fewer

Preserve existing index structure when practical.

## 10. Source map update rules

Maintain `wiki/_sources.md` as an inverse map from processed sources to concept notes.

Each processed source should have one section:

```markdown
## [[raw/source-file]]

- [[section/concept-note]]
```

Rules:
- update `wiki/_sources.md` whenever a concept note's `Sources` section changes
- list only concept notes that explicitly cite the source
- use one bullet per concept note
- keep concept bullets sorted by section path when practical
- keep source sections sorted by source path when practical
- do not include summaries in the source map; detailed source contributions belong in concept notes

## 11. Pending queue update rules

After successful integration of a source file:
- remove it from `## Pending`
- add it under `## Processed` with the current date

Do not mark a file as processed if integration was incomplete or failed.

## 12. Final report rules

Always end with:

## Wiki compilation report
- Processed files: [number]
- Created concepts: [number]
- Updated concepts: [number]
- Ambiguous classifications: [list or "none"]
- Detected gaps: [list or "none"]

Detected gaps may include:
- underspecified concepts
- taxonomy weaknesses
- repeated ambiguity patterns
- missing section categories

## 13. Long-term maintenance heuristics

Optimize for long-term maintainability.

Principles:
- prefer fewer, richer notes
- merge overlapping knowledge
- avoid duplicate concepts
- keep filenames stable
- use aliases for naming variation
- keep the graph clean and navigable

When uncertain, choose the option that makes the wiki easier to maintain in future runs.
