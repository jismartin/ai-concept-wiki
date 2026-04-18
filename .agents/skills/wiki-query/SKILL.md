---
name: wiki-query
description: Use this skill when the user asks a question about topics that may be covered by the compiled wiki in this project, especially AI, LLMs, reasoning, fairness, bias, or AI ethics. Prefer the wiki as the primary source before using general knowledge.
---

# Wiki Query Skill

Use this skill when the user asks questions that may be answered from the compiled wiki.

Typical cases:
- conceptual questions about AI, LLMs, reasoning, fairness, bias, or AI ethics
- requests to explain, compare, or synthesize wiki topics
- questions that likely map to concept notes already compiled in `wiki/`

Do not use this skill for:
- questions unrelated to the wiki domain
- tasks that should update or compile the wiki instead of querying it
- broad open-ended research where the wiki is clearly insufficient as a primary source

## Expected repository structure

This skill expects:
- `wiki/_index.md`
- `wiki/_sources.md`
- concept notes under `wiki/`

Typical section folders:
- `wiki/llm-fundamentals/`
- `wiki/reasoning/`
- `wiki/fairness-bias/`
- `wiki/ai-ethics/`

Skill resources:
- `references/query-standards.md`

If `wiki/_index.md` is missing, stop and report that the wiki index is unavailable.

Read `references/query-standards.md` before answering.

## Workflow

### Step 1 - Read the index as a map

1. Read `wiki/_index.md` in full.
2. Use it to identify which concept files exist and where they are located.
3. Treat the index as a general map, not as the only retrieval mechanism.
4. Use the index to infer likely sections, concept names, and synonyms for the user's question.

### Step 2 - Search the wiki with rg

1. Build a small set of search terms from the user's question, including likely aliases from `wiki/_index.md`.
2. Use `rg` over `wiki/` to find candidate concept notes.
3. Search concept notes first; avoid treating `_index.md`, `_pending.md`, and `_sources.md` as substantive evidence.
4. If the first search is too narrow, broaden terms once before concluding that coverage is weak.
5. If the first search is too broad, prefer exact concept names, aliases, and section-specific terms.

### Step 3 - Select relevant concept files

1. Identify the most relevant concept notes for the user’s question.
2. Usually read 2 to 5 notes.
3. If the question spans multiple domains, retrieve notes from multiple sections.
4. If the wiki appears to have weak or incomplete coverage, note that explicitly.
5. Rank candidate notes by direct relevance to the question, centrality in the index, and whether the search hits occur in definitions, core ideas, related concepts, or sources.

### Step 4 - Read concept notes

1. Read the selected notes in full.
2. Pay attention to:
   - Definition
   - Core ideas
   - Key tensions or open questions
   - Related concepts
   - Sources
3. Follow related concept links only when they are directly relevant.
4. Resolve links of the form `[[section/concept]]` as `wiki/section/concept.md`.
5. If the question asks about source coverage, provenance, or what came from a particular raw file, read `wiki/_sources.md`.
6. Use `wiki/_sources.md` only as a provenance map; read the concept notes themselves before making substantive claims.

### Step 5 - Synthesize the answer

1. Answer the user’s question directly first.
2. Then elaborate using the wiki material.
3. Distinguish clearly between:
   - claims grounded in the wiki
   - supplemental general knowledge added for context
4. Prefer conceptual synthesis over snippet extraction.

### Step 6 - Add a coverage note

Always end with:

**Wiki coverage note:**
- Strong coverage:
- Partial coverage:
- Not in wiki:

## Execution rules

- Prefer the wiki as the primary source.
- Do not present general knowledge as if it came from the wiki.
- Keep the answer precise, structured, and faithful to the retrieved notes.
- If the wiki is incomplete, say so clearly.
- Do not pretend the wiki contains material that was not retrieved.
