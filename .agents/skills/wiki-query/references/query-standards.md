# Wiki Query Reference

This document defines retrieval, reading, synthesis, attribution, and coverage rules for answering questions from the compiled wiki.

## 1. Retrieval principle

The wiki is the primary source for this skill.

Default behavior:
1. read `wiki/_index.md` as a general map
2. use `rg` over `wiki/` with terms from the question to find candidate notes
3. read the 2 to 5 best candidate notes
4. read `wiki/_sources.md` only for provenance, source coverage, or raw-file integration questions
5. answer from retrieved wiki notes when possible
6. add supplemental general knowledge only when it helps clarify the answer
7. clearly separate wiki-grounded content from supplemental context

Do not skip the wiki and answer from memory unless the question is obviously outside the skill scope.

## 2. Start from the index

Always begin by reading `wiki/_index.md`.

Use it to:
- identify candidate concept notes
- understand section placement
- estimate whether coverage is likely strong or weak
- avoid random or incomplete file selection
- derive likely search terms and aliases for `rg`

If the index is missing or severely inconsistent with the wiki contents, report that limitation clearly.

Do not rely on the index alone when the wiki is large enough that names and summaries may miss relevant material.

## 3. Search with rg

After reading the index, use `rg` over `wiki/` with a small set of terms from the user's question.

Good search targets:
- exact concept names from the index
- aliases or near-synonyms suggested by the question
- distinctive technical terms
- source names when the question names a raw file

Search rules:
- search concept notes as evidence
- treat `_index.md` as a map
- treat `_sources.md` as provenance metadata
- ignore `_pending.md` for substantive answers
- broaden terms once if no useful candidates appear
- narrow terms if too many loose hits appear

Use `wiki/_sources.md` when the question involves:
- source provenance
- which concepts came from a raw file
- whether a source has been integrated
- tracing a concept back to source material

Treat `wiki/_sources.md` as a navigation aid, not as a substitute for reading the concept notes.

## 4. Note selection rules

Select the smallest set of notes that gives good conceptual coverage.

Typical range:
- 2 to 5 notes for a focused question
- more only when the question genuinely spans several concepts or sections

Prioritize notes that are:
- most directly relevant
- more central than peripheral
- likely to contain definitions and core explanations
- likely to resolve ambiguity in the user’s wording
- found by both the index and `rg`, when applicable

Avoid reading many loosely related notes when a smaller set is sufficient.

## 5. Reading rules

When reading a concept note, pay attention to:
- `Definition`
- `Core ideas`
- `Key tensions or open questions`
- `Related concepts`
- `Sources`

Treat `Related concepts` as optional expansion paths, not mandatory traversal.

Follow a related note only if it materially improves the answer.
Do not recursively traverse the graph without need.

Resolve wiki links as follows:
- `[[llm-fundamentals/attention-mechanism]]` → `wiki/llm-fundamentals/attention-mechanism.md`
- `[[reasoning/chain-of-thought]]` → `wiki/reasoning/chain-of-thought.md`
- `[[raw/source-file]]` -> `raw/source-file.md`

## 6. Synthesis rules

The answer should be conceptually synthesized, not pasted from note fragments.

Preferred answer structure:
1. direct answer to the user’s question
2. short elaboration using the most relevant wiki concepts
3. optional clarification or contrast where helpful
4. final wiki coverage note

Prefer:
- explanation
- comparison
- integration across notes
- careful distinction of central vs secondary points

Avoid:
- note-by-note dumping
- excessive quoting
- fragmentary snippet retrieval
- repeating the same idea from multiple notes without adding synthesis

## 7. Attribution discipline

You must distinguish clearly between:
- claims grounded in the wiki
- supplemental general knowledge

Good pattern:
- “According to the wiki, ...”
- “The wiki emphasizes ...”
- “As additional context beyond the wiki, ...”

Do not blur the boundary between retrieved content and outside knowledge.
Do not imply that the wiki states something it does not state.

## 8. Handling weak coverage

If the wiki only partly covers the question:
- answer the covered part from the wiki
- identify what is missing
- optionally add clearly labeled supplemental context

If the wiki does not meaningfully cover the question:
- say so directly
- do not force an answer as if the wiki had sufficient material

Lack of coverage is a valid outcome.

## 9. Coverage note format

Always end with:

**Wiki coverage note:**
- Strong coverage: [what the wiki covers well]
- Partial coverage: [what the wiki touches but does not fully develop]
- Not in wiki: [what appears absent]

Guidelines:
- keep it brief
- be concrete
- do not use vague filler
- mention missing dimensions when relevant

## 10. Quality rules for answers

Answers should be:
- precise
- structured
- faithful to the wiki
- concise unless the user asks for depth
- explicit about uncertainty or missing coverage

Avoid:
- unsupported generalizations
- overclaiming from sparse wiki content
- pretending conceptual consensus where the notes show tension
- mixing wiki claims and outside knowledge without labels

## 11. Multi-note comparison rules

When the answer draws from several notes:
- integrate them around the user’s question
- surface agreements and tensions when relevant
- avoid listing notes mechanically

Good uses:
- comparing two related concepts
- connecting a mechanism with its ethical implications
- combining foundational and reasoning-related notes

## 12. When not to use this skill

Do not use this skill when the task is actually to:
- compile or update the wiki
- edit the taxonomy
- process new raw files
- answer a question clearly outside the wiki domain

In those cases, use a different skill or report the mismatch.
