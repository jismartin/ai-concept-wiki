---
name: source-digestion
description: Use this skill when the user asks to digest, preprocess, summarize, or prepare long source documents such as PDFs, papers, articles, transcripts, reports, datasets, or repositories before wiki compilation. It creates structured extended Markdown digests in raw/digests/ from originals in raw/originals/ while preserving source traceability for the Codex-managed AI wiki.
---

# Source Digestion Skill

Use this skill when the user asks to:
- digest a source
- preprocess a source for the wiki
- summarize an article, paper, PDF, transcript, dataset, or repository for later compilation
- create an extended source summary
- prepare a raw document before updating the wiki
- turn a long source into a structured digest

Do not use this skill for:
- creating or updating concept notes under `wiki/`
- answering conceptual questions from the compiled wiki
- auditing the compiled wiki
- replacing the original source with a summary

## Expected repository structure

This skill expects or creates:

- `raw/originals/` - original source files, preserved as source-of-truth inputs
- `raw/digests/` - structured Markdown digests used by wiki compilation

Optional control file:
- `raw/_source_registry.md` - maps originals to digests and digestion status

Skill resources:
- `references/digest-standards.md`

Read `references/digest-standards.md` before creating or updating digests.

## Workflow

### Step 1 - Identify the source

Identify the source to digest.

Preferred source location:
- `raw/originals/source-file`

If the source is elsewhere in the repository, use it as input only when the user clearly requested it.

If the source is outside the repository or not available locally, ask the user to provide it or paste the source text.

### Step 2 - Extract usable content

For Markdown or text sources, read the file directly.

For PDFs or other binary sources, extract text with available local tools when possible. If extraction is incomplete or unreliable, state the limitation and ask for a better text source if needed.

Do not modify the original source.

### Step 3 - Create or update the digest

Create a structured Markdown digest in:

```text
raw/digests/source-name.md
```

Use a stable kebab-case filename based on the original source title or filename.

If a digest already exists:
- preserve useful content
- update it only with material supported by the original source
- do not silently overwrite analyst notes, caveats, or prior extraction limitations

### Step 4 - Preserve traceability

Every digest must link back to the original source.

Use Obsidian-style links where possible, for example:

```markdown
- Original source: [[raw/originals/paper-name.pdf]]
```

If `raw/_source_registry.md` exists, update it. If it does not exist and the user is building the digestion pipeline, create it.

### Step 5 - Prepare for wiki compilation

The digest should be optimized for later concept extraction by `wiki-compilation`.

Include likely wiki concepts, but do not create concept notes under `wiki/` during source digestion.

### Step 6 - Final report

Always output:

## Source digestion report
- Original source: [path]
- Digest file: [path]
- Registry updated: [yes/no]
- Extraction limitations: [list or "none"]
- Suggested wiki concepts: [list or "none"]
- Ready for wiki compilation: [yes/no]

## Execution rules

- Preserve originals.
- Write digests only under `raw/digests/`.
- Keep digest filenames English and kebab-case.
- Keep the digest faithful to the source.
- Distinguish source claims from your interpretive synthesis.
- Avoid unsupported claims.
- Do not update `wiki/` concept notes.
- Do not mark files as processed in `wiki/_pending.md`.
