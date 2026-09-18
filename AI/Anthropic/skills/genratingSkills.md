# Claude Skills

Claude Code works differently — skills go in ~/.claude/skills/<name>/skill.md for everything, or .claude/skills/<name>/skill.md inside a project.

## Scope what the review actually checks

List the concrete things you want flagged in a React PR — hook rules (missing deps, conditional hooks), prop typing, unnecessary re-renders, key props in lists, accessibility (alt text, aria labels, semantic elements), state management patterns, and test coverage. Write these down first; this list becomes the checklist inside the skill body.

## Decide where the skill should live

For a single repo, put it at .claude/skills/react-code-review/ so it's checked into the project and shared with your team. For a personal habit you want across every React project, use ~/.claude/skills/react-code-review/ instead. Claude Code loads project skills from the current directory up through the repo root, so it also works from subfolders.

## Write the YAML frontmatter

Every SKILL.md needs --- name: react-code-review --- and a description field. The description is what Claude reads to decide when to trigger the skill, so make it specific and slightly 'pushy': mention React, PRs, component reviews, hooks, and phrases like 'review this component' or 'check my PR' so it fires even when the user doesn't say the word 'skill'.

## Write the review instructions in the body
Below the frontmatter, write Markdown instructions Claude follows step by step: how to find changed files (e.g. git diff), what to check per category from Step 1, what severity levels to use (blocking vs. nit), and what the output should look like — a structured comment per file, or a summary table. Be explicit about format so every review looks consistent.

## Add reference files for anything long or team-specific
If you have a full ESLint config, a component style guide, or naming conventions, don't paste them into SKILL.md — put them in a references/ subfolder (e.g. references/style-guide.md) and just point to them from the main file ('see references/style-guide.md for naming rules'). This keeps the main file short and loads the details only when needed.

## Test it against a real PR or diff
Open a branch with some real or intentionally flawed React code, run Claude Code, and ask something like 'review my changes.' Check whether the skill actually triggers and whether the output matches the format and checklist you wrote. If it misses cases or gives inconsistent output, that's a sign the instructions need to be more explicit, not that Claude needs a longer prompt each time.