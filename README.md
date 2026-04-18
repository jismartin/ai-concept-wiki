# Personal AI Knowledge Wiki

This repository is a Codex-managed personal knowledge wiki for AI-related research. It is designed to turn long source materials into structured Markdown digests, then compile those digests into an Obsidian-friendly network of concept notes.

The system is inspired by Andrej Karpathy's idea of an LLM-managed wiki: the model does not only answer questions, but helps maintain a small, navigable knowledge base over time. See: https://x.com/karpathy/status/2039805659525644595

## Current Design

The repository separates four workflows:

1. **Source digestion**: long sources such as PDFs, papers, articles, reports, or transcripts are preserved under `raw/originals/` and converted into structured Markdown digests under `raw/digests/`.
2. **Wiki compilation**: Codex processes pending digests and creates or updates concept notes under `wiki/`.
3. **Wiki query**: Codex answers questions by reading the wiki index, searching the wiki with `rg`, reading the best candidate notes, and clearly separating wiki-grounded claims from supplemental context.
4. **Wiki maintenance**: Codex audits consistency, broken links, source traceability, duplicate concepts, and missing connections.

## Repository Structure

```text
<project-root>/
|-- raw/
|   |-- originals/             # Preserved original source files
|   |-- digests/               # Structured Markdown digests for compilation
|   `-- _source_registry.md     # Source-to-digest status registry
|-- wiki/                      # Obsidian vault root for compiled knowledge
|   |-- _index.md              # Concept index
|   |-- _pending.md            # Pending compilation queue
|   |-- _sources.md            # Source-to-concept map
|   |-- llm-fundamentals/
|   |-- reasoning/
|   |-- fairness-bias/
|   `-- ai-ethics/
`-- .agents/
    `-- skills/
        |-- source-digestion/
        |-- wiki-compilation/
        |-- wiki-query/
        `-- wiki-maintenance/
```

## Typical Workflow

1. Add an original source to `raw/originals/`.
2. Ask Codex to digest it, for example:

```text
Digest this source for wiki compilation.
```

3. Review the generated digest in `raw/digests/`.
4. Ask Codex to compile or update the wiki:

```text
Compile the wiki from pending digests.
```

5. Query the wiki conversationally:

```text
According to the wiki, how does mechanistic interpretability relate to hallucination?
```

6. Periodically ask for maintenance:

```text
Audit the wiki for broken links, duplicate concepts, and source-map inconsistencies.
```

## Key Files To Read

- `AGENTS.md` defines the repository-level operating rules and trigger conditions.
- `.agents/skills/source-digestion/SKILL.md` defines how long sources become structured digests.
- `.agents/skills/wiki-compilation/SKILL.md` defines how digests become concept notes.
- `.agents/skills/wiki-query/SKILL.md` defines how Codex answers questions from the compiled wiki.
- `.agents/skills/wiki-maintenance/SKILL.md` defines audit and cleanup behavior.

Detailed standards live in each skill's `references/` directory.

## Principles

- Preserve original sources.
- Compile from structured digests when possible.
- Keep wiki notes concept-oriented, concise, and interconnected.
- Avoid duplicate or near-duplicate concepts.
- Keep all wiki content and filenames in English.
- Use Obsidian-compatible links.
- Prefer small, precise updates over broad rewrites.

## Status

The wiki has been reset for the current design. Add new materials under `raw/originals/`, digest them into `raw/digests/`, and then compile the wiki incrementally.
