# Wiki Maintenance Standards

This document defines checks and safe maintenance actions for the compiled wiki.

## 1. Control files

The maintenance workflow uses three control files:

- `wiki/_index.md` - concept catalog
- `wiki/_pending.md` - source processing state
- `wiki/_sources.md` - inverse map from sources to concepts

These files should agree with each other and with the concept notes.

## 2. Link checks

Check Obsidian links of these forms:

- `[[section/concept-note]]`
- `[[raw/source-file]]`

Rules:
- concept links should resolve to Markdown files under `wiki/`
- raw source links should resolve to files under `raw/`
- links should use full paths from the wiki link convention already used in the repository
- do not create placeholder target files just to satisfy links

## 3. Index consistency

Every concept note under the main topic folders should appear in `wiki/_index.md`.

Every index entry should point to an existing note.

Each index entry should include:
- concept name
- concept link
- one-sentence summary
- updated date

Avoid rewriting summaries unless they are inaccurate, duplicated, or stale.

## 4. Source map consistency

`wiki/_sources.md` should list only source-to-concept relationships that are backed by a concept note's `Sources` section.

For each `[[raw/source-file]]` cited in a concept note:
- the source should appear as a heading in `wiki/_sources.md`
- the concept should appear under that source

For each concept listed under a source in `wiki/_sources.md`:
- the concept note should exist
- the concept note should cite that same source

Do not add explanatory summaries to `wiki/_sources.md`; keep summaries in concept notes.

## 5. Duplicate and overlap checks

Potential duplicates may share:
- similar filenames
- overlapping aliases
- near-identical definitions
- the same source claims
- the same related-concept neighborhood

When duplicates are suspected:
- report them with evidence
- prefer merge recommendations over immediate merges
- do not delete or rename notes without explicit user approval

## 6. Missing link checks

Suggest related-concept links when two existing notes:
- cite the same source for closely related ideas
- refer to each other's topic without linking
- occupy adjacent roles in the same explanation
- connect a mechanism, benchmark, risk, or conceptual tension

Avoid link explosion. Suggest only links that improve navigation or reasoning.

## 7. Missing concept checks

Suggest a missing concept note when:
- several notes repeatedly mention the same absent idea
- a source map cluster points to an important unrepresented concept
- a broad note contains a distinct reusable sub-concept
- a recurring tension has no dedicated page

Do not create the missing concept unless the user asks for it.

## 8. Safe fixes

Safe fixes include:
- correcting clearly broken links
- adding missing source map entries backed by note citations
- adding missing index entries for existing concept notes
- normalizing table formatting
- fixing frontmatter placement
- fixing obvious typo-level inconsistencies

Unsafe structural changes require approval:
- merging notes
- splitting notes
- renaming files
- moving notes between sections
- deleting notes
- changing the taxonomy

## 9. Report style

Report concrete findings over broad advice.

Include file paths and, when useful, line numbers.

Separate:
- fixed issues
- unfixed issues
- optional improvements
- changes needing approval
