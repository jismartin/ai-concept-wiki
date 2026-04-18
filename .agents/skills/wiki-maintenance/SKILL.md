---
name: wiki-maintenance
description: Use this skill when the user asks to maintain, audit, validate, clean up, or improve the compiled wiki without processing new raw documents. It checks index consistency, source mappings, broken links, duplicate concepts, missing connections, taxonomy gaps, and maintenance recommendations for the Codex-managed AI wiki.
---

# Wiki Maintenance Skill

Use this skill when the user asks to:
- maintain the wiki
- audit the wiki
- validate the wiki
- clean up wiki inconsistencies
- find duplicate concepts
- find broken links
- suggest missing connections
- suggest missing concept notes
- check source traceability

Do not use this skill for:
- processing new raw files into concept notes
- answering conceptual questions from the wiki
- broad taxonomy redesign unless explicitly requested

## Expected repository structure

This skill expects:

- `raw/`
- `wiki/_index.md`
- `wiki/_pending.md`
- `wiki/_sources.md`
- concept notes under `wiki/`

Typical section folders:
- `wiki/llm-fundamentals/`
- `wiki/reasoning/`
- `wiki/fairness-bias/`
- `wiki/ai-ethics/`

Skill resources:
- `references/maintenance-standards.md`

Read `references/maintenance-standards.md` before making maintenance edits or recommendations.

## Workflow

### Step 1 - Establish scope

Identify whether the user wants:
- a read-only audit
- direct fixes
- a maintenance report with suggested changes
- a narrow check, such as links, sources, duplicates, or index consistency

If the user does not specify, default to a read-only audit and ask before making large structural changes.

### Step 2 - Read control files

Read:
1. `wiki/_index.md`
2. `wiki/_pending.md`
3. `wiki/_sources.md`

Use these files as the control plane for the wiki.

### Step 3 - Inspect concept notes

Inspect relevant concept notes under `wiki/`.

Check:
- frontmatter presence and placement
- required sections
- source citations
- related concept links
- concept overlap
- filename consistency
- index coverage
- source map coverage

### Step 4 - Detect maintenance issues

Look for:
- broken concept links
- broken raw source links
- notes missing from `wiki/_index.md`
- index entries pointing to missing notes
- source citations missing from `wiki/_sources.md`
- source map entries not backed by concept note citations
- duplicate or near-duplicate concepts
- overly broad or overly granular notes
- missing related-concept links
- missing concept notes suggested by repeated gaps
- taxonomy placement ambiguities

### Step 5 - Apply safe fixes when requested

If the user asked for direct fixes, apply only low-risk maintenance edits:
- repair broken links when the intended target is clear
- add missing index entries for existing notes
- add missing source map entries backed by note citations
- normalize formatting that is already defined by the wiki standards
- add obvious related-concept links between existing notes

Do not merge, rename, delete, or split notes unless the user explicitly approves that structural change.

### Step 6 - Report results

Always end with:

## Wiki maintenance report
- Files inspected: [number]
- Issues fixed: [number]
- Issues found but not fixed: [number]
- Broken links: [list or "none"]
- Source map inconsistencies: [list or "none"]
- Index inconsistencies: [list or "none"]
- Duplicate or overlapping concepts: [list or "none"]
- Suggested missing links: [list or "none"]
- Suggested missing concepts: [list or "none"]
- Structural changes needing approval: [list or "none"]

## Execution rules

- Treat `raw/` as read-only.
- Keep all wiki edits inside `wiki/`.
- Preserve existing knowledge.
- Prefer precise, minimal fixes.
- Do not create new concept notes during maintenance unless explicitly requested.
- Do not mark pending files as processed.
- Distinguish detected problems from optional improvements.
