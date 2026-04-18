---
name: wiki-compilation
description: Use this skill when the user asks to compile the wiki, update the wiki, or process new documents into the wiki. It refreshes wiki/_pending.md from raw/ when needed, processes pending files, creates or updates concept notes, updates wiki/_index.md, and records processed files.
---

# Wiki Compilation Skill

Use this skill when the user asks to:
- compile the wiki
- update the wiki
- process new documents into the wiki
- integrate new raw files into the wiki

Do not use this skill for:
- one-off summaries that should not modify the wiki
- unrelated repository refactors
- taxonomy redesign unless the user explicitly asks for it

## Expected repository structure

This skill expects:

- `raw/`
- `raw/digests/` when source digestion is used
- `wiki/_pending.md`
- `wiki/_index.md`
- `wiki/_sources.md`
- section folders under `wiki/`

Preferred sections:
- `wiki/llm-fundamentals/`
- `wiki/reasoning/`
- `wiki/fairness-bias/`
- `wiki/ai-ethics/`

Skill resources:
- `references/wiki-standards.md`
- `scripts/refresh_pending.py`

If `raw/` is missing, stop and report the issue.

If `raw/digests/` exists, prefer processing digest Markdown files from `raw/digests/` rather than original long-form sources from `raw/originals/`.

Read `references/wiki-standards.md` before creating or updating concept notes.

## Workflow

### Step 1 — Refresh or initialize the pending queue

1. Check whether `wiki/_pending.md` exists.
2. If it is missing, run:

```bash
python scripts/refresh_pending.py
```

3. If it exists but appears outdated relative to the contents of `raw/`, run:

```bash
python scripts/refresh_pending.py
```

4. After refreshing, read `wiki/_pending.md`.
5. Only process files listed under `## Pending`.
6. When both originals and digests exist for the same source, process the digest and preserve the original only as traceability.
7. If `## Pending` is empty, stop and report that there is nothing to process.

### Step 2 — Read pending files

For each file under `## Pending`:
1. Open the source file in `raw/`.
2. If the file is a digest, treat it as the compilation input and follow its original-source link for provenance only when needed.
3. Extract the main reusable concepts.
4. Ignore boilerplate and non-conceptual noise.

### Step 3 — Create or update concepts

For each extracted concept:
1. Assign it to exactly one wiki section.
2. Search for an existing overlapping concept in that section.
3. If a similar note already exists:
   - update it instead of creating a new one
4. If no similar note exists:
   - create a new note using the reference standards

Prefer merging over creating.

### Step 4 — Update wiki index

Update `wiki/_index.md` for every created or updated concept.

For each entry:
- include the concept path
- include a one-sentence summary
- include the current date

Preserve the existing index structure when possible.

### Step 5 - Update source map

Update `wiki/_sources.md` for every processed source and every created or updated concept.

For each processed source:
- include a heading linking to the source, such as `## [[raw/source-file]]`
- list every concept note that uses that source
- use the same concept paths used in `wiki/_index.md`
- preserve existing source mappings that remain valid
- remove mappings only when the corresponding concept no longer cites that source

If `wiki/_sources.md` is missing, create it.

### Step 6 — Update pending status after processing

After a file is successfully processed:
1. Remove it from `## Pending`
2. Add it to `## Processed` with the current date

Do not mark a file as processed unless its content was actually integrated.

### Step 7 — Final report

Always output a final report in this format:

## Wiki compilation report
- Processed files: [number]
- Created concepts: [number]
- Updated concepts: [number]
- Ambiguous classifications: [list or "none"]
- Detected gaps: [list or "none"]

## Execution rules

- Prefer fewer, richer concept notes
- Avoid duplicate or near-duplicate notes
- Keep filenames stable
- Preserve existing useful content
- Avoid destructive overwrites
- Make the wiki more maintainable after each run
