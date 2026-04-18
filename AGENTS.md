## Purpose

This repository implements a Codex-driven personal knowledge wiki.
Your role is to incrementally transform source documents into structured,
interconnected concept entries optimized for Obsidian navigation, and to answer
wiki-grounded questions using the compiled knowledge base.

------------------------------------------------------------------------

## Core Principles

- Incremental processing only
- No duplication of concepts
- Preservation of existing knowledge
- Preservation of original sources
- High precision, low verbosity
- English wiki structure and filenames
- Obsidian-compatible structure and linking

------------------------------------------------------------------------

## Scope of Work

- You MAY read and modify files in this repository.
- You MUST preserve original source files under `raw/originals/`.
- You MAY write structured digests under `raw/digests/` only when using the source-digestion workflow.
- You MAY update `raw/_source_registry.md` only when using the source-digestion workflow.
- You MUST write all wiki outputs inside `wiki/`.
- You MAY read skill resources under `.agents/skills/`.

------------------------------------------------------------------------

## Folder Structure

```text
<project-root>/
├── raw/
│   ├── originals/             # Original source documents, preserved
│   ├── digests/               # Structured source digests for compilation
│   └── _source_registry.md     # Optional source-to-digest registry
├── .agents/
│   └── skills/
│       ├── source-digestion/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── digest-standards.md
│       ├── wiki-compilation/
│       │   ├── SKILL.md
│       │   ├── references/
│       │   │   └── wiki-standards.md
│       │   └── scripts/
│       │       └── refresh_pending.py
│       ├── wiki-query/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── query-standards.md
│       └── wiki-maintenance/
│           ├── SKILL.md
│           └── references/
│               └── maintenance-standards.md
└── wiki/                      # Obsidian vault root
    ├── _index.md
    ├── _pending.md
    ├── _sources.md
    ├── llm-fundamentals/
    ├── reasoning/
    ├── fairness-bias/
    └── ai-ethics/
```

IMPORTANT:
- The `wiki/` folder is the Obsidian vault root for compiled knowledge.
- All internal wiki concept links must be relative to this root.
- Original sources are preserved; digests are intermediate compilation inputs.

------------------------------------------------------------------------

## Execution Triggers

When the user requests any of the following:
- "digest this source"
- "preprocess this source"
- "summarize this paper for the wiki"
- "prepare this PDF for wiki compilation"
- "create a source digest"

-> Read `.agents/skills/source-digestion/SKILL.md` and follow that workflow.

When the user requests any of the following:
- "compile the wiki"
- "update the wiki"
- "process new documents"

-> Read `.agents/skills/wiki-compilation/SKILL.md` and follow that workflow.

When the user asks questions about topics that may be covered by the wiki:
- AI
- LLMs
- reasoning
- fairness or bias
- AI ethics
- concept notes already compiled in `wiki/`

-> Read `.agents/skills/wiki-query/SKILL.md` and follow that workflow.

When the user requests wiki maintenance, auditing, validation, cleanup, consistency checks,
duplicate detection, broken-link checks, source traceability checks, or missing-connection suggestions:

-> Read `.agents/skills/wiki-maintenance/SKILL.md` and follow that workflow.

------------------------------------------------------------------------

## Hard Constraints

- NEVER modify original source files under `raw/originals/`.
- NEVER write to `raw/` except for `raw/digests/` and `raw/_source_registry.md` during source digestion.
- NEVER write wiki content outside `wiki/`.
- ALWAYS use English for wiki filenames, section names, and concept note structure.
- ALWAYS use kebab-case for concept and digest filenames.
- NEVER duplicate concepts.
- ALWAYS use full relative links from `wiki/` for wiki concept links.
- ALWAYS keep Obsidian compatibility.

------------------------------------------------------------------------

## Source Digestion Behavior

When preparing sources for wiki compilation:
- preserve the original source under `raw/originals/`
- create a structured Markdown digest under `raw/digests/`
- link each digest back to its original source
- update `raw/_source_registry.md` when maintaining the source pipeline
- do not update concept notes during source digestion unless the user explicitly asks for a full pipeline run

------------------------------------------------------------------------

## Querying Behavior

When answering questions from the wiki:
- prefer the wiki as the primary knowledge source
- read `wiki/_index.md` as a general map, not as the only retrieval mechanism
- use `rg` over `wiki/` with terms from the question to identify candidate notes
- read the 2 to 5 best candidate notes before answering
- read `wiki/_sources.md` only when the question asks about provenance, source coverage, or raw-file integration
- clearly distinguish wiki-grounded claims from supplemental general knowledge
- if coverage is partial, say so explicitly
- do not imply the wiki contains material that was not retrieved

------------------------------------------------------------------------

## Output Behavior

- Make minimal necessary changes
- Preserve existing structure
- Do not introduce inconsistencies
