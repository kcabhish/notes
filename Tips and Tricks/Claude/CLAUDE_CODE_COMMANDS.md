# Claude Code Commands Reference

A practical cheat sheet for commonly useful **Claude Code CLI** commands, workflows, and prompts.

> **Note:** Claude Code evolves frequently. Some commands or flags may vary by version. Run `claude --help` or `/help` inside Claude Code to see the commands available in your installed version.

---

## 1. Starting Claude Code

### Start Claude in the current directory

```bash
claude
```

### Start Claude with a prompt

```bash
claude "Explain this project and identify the main architecture"
```

### Start Claude in a specific directory

```bash
cd my-project
claude
```

### Continue a previous conversation

```bash
claude --continue
```

### Resume a previous session

```bash
claude --resume
```

### Show version

```bash
claude --version
```

### Show CLI help

```bash
claude --help
```

---

## 2. Useful Slash Commands

Slash commands are entered **inside Claude Code**.

| Command | Purpose |
|---|---|
| `/help` | Show available commands |
| `/clear` | Clear the current conversation |
| `/compact` | Compress the current conversation/context |
| `/cost` | Display usage/cost information |
| `/status` | Show current session/status information |
| `/model` | View or change the current model |
| `/config` | Configure Claude Code |
| `/permissions` | Review/configure permissions |
| `/memory` | Work with Claude Code memory/instructions |
| `/init` | Initialize project instructions |
| `/doctor` | Diagnose common problems |
| `/mcp` | Manage/inspect MCP servers |
| `/hooks` | Manage Claude Code hooks |
| `/agents` | Manage/inspect agents |
| `/tasks` | Inspect background/delegated tasks when supported |

---

## 3. CLI Options

### Non-interactive mode

```bash
claude -p "Explain this codebase"
```

Useful for scripting and automation.

### Pipe input into Claude

```bash
cat README.md | claude -p "Summarize this README"
```

Review a Git diff:

```bash
git diff | claude -p "Review this diff for bugs"
```

Specify a model when supported by your installed version:

```bash
claude --model <model>
```

Check available options:

```bash
claude --help
```

---

# 4. Exploring a Codebase

Start Claude from the repository root:

```bash
cd my-project
claude
```

Then ask:

```text
Explain the architecture of this repository.

Identify:
1. Application entry points
2. Major modules
3. API layer
4. Database access
5. Authentication
6. Testing strategy
7. Build/deployment configuration

Do not modify anything.
```

---

# 5. Explore Before Coding

A useful workflow is to make Claude inspect the code first:

```text
First inspect the relevant files and understand the existing implementation.

Do not modify anything yet.

Explain:
- how the current implementation works
- relevant files
- dependencies
- potential risks
- recommended implementation approach
```

Then, after reviewing the plan:

```text
Implement the proposed changes.
```

---

# 6. Create an Implementation Plan

```text
Create an implementation plan for this feature.

Do not modify any files.

Include:
- files that need to change
- files that need to be created
- architectural considerations
- testing strategy
- migration considerations
- potential risks
```

For larger tasks:

```text
Break this feature into small implementation steps.

For each step provide:
- objective
- files involved
- implementation details
- tests
- dependencies
```

---

# 7. Code Review

Review current changes:

```text
Review my current changes for:

- bugs
- security issues
- performance problems
- accessibility problems
- error handling
- maintainability
- test coverage
```

Review Git changes:

```bash
git diff | claude -p "Perform a detailed code review."
```

Review staged changes:

```bash
git diff --cached | claude -p "Review these staged changes."
```

---

# 8. Git Workflows

### Explain current changes

```bash
git diff | claude -p "Explain these changes."
```

### Generate a commit message

```bash
git diff --cached | claude -p "Generate a concise conventional commit message."
```

### Review a commit

```bash
git show <commit> | claude -p "Review this commit for potential issues."
```

### Review a branch

```bash
git diff main...HEAD | claude -p "Review this branch against main."
```

---

# 9. Debugging

Start with investigation:

```text
Investigate this bug.

First:
1. Reproduce the problem if possible.
2. Trace the relevant code.
3. Identify the root cause.
4. Explain why it happens.

Do not modify anything yet.
```

Then:

```text
Implement the smallest safe fix.

Add or update tests that reproduce the original bug.
```

---

# 10. Testing

Ask Claude to run relevant tests:

```text
Run the relevant tests for the changes we made.
```

Or:

```text
Run the test suite and fix failures related to our changes.

Do not change unrelated functionality.
```

For a specific module:

```text
Run the tests for the authentication module.
```

---

# 11. Test Generation

```text
Analyze this component and generate comprehensive tests.

Cover:
- happy paths
- edge cases
- invalid input
- error states
- loading states
- accessibility behavior
```

For React:

```text
Generate tests for this React component using the testing framework already used by this repository.

Do not introduce a new testing framework unless necessary.
```

---

# 12. Refactoring

Safe refactoring prompt:

```text
Refactor this code while preserving existing behavior.

Requirements:
- no API changes
- preserve existing functionality
- maintain backward compatibility
- improve readability
- avoid unnecessary abstractions
- update tests if necessary
```

For a larger refactor:

```text
First analyze the existing architecture.

Identify:
- duplicated logic
- unnecessary dependencies
- coupling
- problematic abstractions
- opportunities for reuse

Do not modify anything yet.
```

---

# 13. Dependency Management

Analyze dependencies:

```text
Analyze the project's dependencies.

Identify:
- unused dependencies
- duplicate dependencies
- outdated dependencies
- security concerns
- packages that can be removed
```

Before upgrading:

```text
Determine what could break if we upgrade <package>.

Inspect the codebase and relevant documentation if available.

Do not upgrade anything yet.
```

---

# 14. Security Review

```text
Perform a security review of this application.

Look for:
- authentication problems
- authorization issues
- injection vulnerabilities
- XSS
- CSRF
- secrets
- insecure dependencies
- unsafe file handling
- sensitive data exposure
- logging of sensitive information
```

For APIs:

```text
Review this API for common security vulnerabilities.

Pay particular attention to:
- authentication
- authorization
- input validation
- injection
- rate limiting
- error responses
- sensitive data exposure
```

---

# 15. Accessibility Review

For frontend projects:

```text
Review this UI for WCAG accessibility issues.

Check:
- keyboard navigation
- focus management
- semantic HTML
- ARIA usage
- color contrast
- form labels
- screen reader behavior
- error messaging
- interactive elements
```

---

# 16. Performance Analysis

```text
Analyze this application for frontend performance issues.

Look for:
- unnecessary renders
- expensive computations
- large bundles
- unnecessary dependencies
- inefficient network requests
- image optimization
- lazy loading opportunities
- caching
- Core Web Vitals
```

For React:

```text
Analyze this React application for unnecessary renders and state-management problems.
```

---

# 17. Documentation

Generate/update a README:

```text
Analyze this project and update the README with:

- prerequisites
- installation
- development setup
- environment variables
- available scripts
- architecture overview
- testing
- build instructions
- deployment
```

Generate API documentation:

```text
Analyze the API implementation and generate API documentation based on the actual code.

Do not invent endpoints.
```

---

# 18. CLAUDE.md

A `CLAUDE.md` file provides project-specific instructions to Claude Code.

Example:

```markdown
# Project Instructions

## Architecture

This is a React + TypeScript application.

## Package Manager

Use pnpm.

Do not use npm or yarn.

## Development

Run:

pnpm install
pnpm dev

## Testing

Run:

pnpm test

## Coding Standards

- Use TypeScript.
- Prefer functional React components.
- Avoid `any`.
- Follow existing project patterns.
- Do not introduce new dependencies without approval.

## Before Making Changes

- Inspect existing implementation.
- Reuse existing components.
- Do not rewrite unrelated code.

## Testing Requirements

Every feature should include appropriate tests.
```

---

# 19. AGENTS.md + CLAUDE.md

If you use multiple AI coding tools, you can maintain common project instructions in:

```text
AGENTS.md
```

and Claude-specific instructions in:

```text
CLAUDE.md
```

A useful structure:

```text
project/
├── AGENTS.md
├── CLAUDE.md
├── package.json
├── src/
└── tests/
```

Use `AGENTS.md` for general engineering rules and `CLAUDE.md` for Claude-specific behavior.

---

# 20. MCP

Inspect MCP configuration:

```text
/mcp
```

MCP can connect Claude Code to tools such as:

- Figma
- GitHub
- databases
- internal enterprise systems
- custom local MCP servers
- APIs

Example prompt:

```text
Analyze the selected Figma design and identify:

- components
- design tokens
- typography
- spacing
- responsive behavior

Map these to the existing React component architecture.
```

---

# 21. Figma → React Workflow

A useful workflow:

```text
1. Inspect the Figma design.
2. Identify reusable components.
3. Identify design tokens.
4. Identify responsive breakpoints.
5. Map components to the existing design system.
6. Create a component plan.
7. Implement the components.
8. Add Storybook stories.
9. Add tests.
10. Compare implementation against the design.
```

---

# 22. Frontend Development Prompt

For React/TypeScript:

```text
Implement this feature using the existing architecture.

Requirements:
- TypeScript
- reuse existing components
- follow existing state-management patterns
- follow existing styling conventions
- maintain accessibility
- add tests
- do not introduce unnecessary dependencies

Before coding, inspect the relevant implementation.
```

---

# 23. Storybook

```text
Create a Storybook story for this component.

Include:
- default state
- loading state
- error state
- empty state
- populated state
- relevant interaction states

Follow the existing Storybook conventions in this repository.
```

---

# 24. Database Work

Before modifying a database:

```text
Analyze the current database schema and data-access layer.

Explain:
- relevant tables
- relationships
- indexes
- constraints
- query patterns

Do not make changes yet.
```

Migration:

```text
Create a database migration for this change.

Requirements:
- safe migration
- backward compatibility where possible
- appropriate indexes
- rollback strategy
- migration tests if supported
```

---

# 25. API Development

```text
Implement this API endpoint.

Requirements:
- follow existing API patterns
- validate input
- handle errors consistently
- enforce authorization
- add tests
- update API documentation
```

---

# 26. Environment Variables

```text
Identify all environment variables used by this project.

Create a table containing:
- variable name
- purpose
- required/optional
- where it is used

Do not expose secret values.
```

---

# 27. Finding Code

```text
Find all places where this function/component is used.
```

```text
Find all API calls related to authentication.
```

```text
Find all references to this environment variable.
```

```text
Find duplicate implementations of this functionality.
```

---

# 28. Understanding Unknown Code

```text
Explain this code to me as if I am joining the project for the first time.

Start with the high-level purpose, then explain:

1. inputs
2. processing
3. state
4. external dependencies
5. outputs
6. error handling
7. tests
```

---

# 29. Avoid Overengineering

```text
Implement the simplest solution that satisfies the requirements.

Do not:
- introduce unnecessary abstractions
- create unnecessary files
- add dependencies without justification
- refactor unrelated code
- over-engineer the solution
```

---

# 30. Limit Scope of Changes

```text
Only modify files necessary to implement this feature.

Do not:
- reformat unrelated files
- upgrade dependencies
- change unrelated components
- rename existing APIs
- perform opportunistic refactoring
```

---

# 31. Verify Claude's Work

After implementation:

```text
Review the changes you just made.

Verify:
- requirements are satisfied
- tests pass
- types compile
- lint passes
- no unrelated files were modified
- no security issues were introduced

Fix any issues you find.
```

---

# 32. Dry Run

Before making changes:

```text
Show me what files you would modify and what changes you would make.

Do not modify anything yet.
```

Then:

```text
Proceed with the changes.
```

---

# 33. Large Feature Workflow

For a complex feature:

```text
Understand
   ↓
Plan
   ↓
Implement
   ↓
Test
   ↓
Review
   ↓
Verify
   ↓
Commit
```

Example:

### Step 1 — Understand

```text
Analyze the feature requirements and existing architecture.

Do not modify anything.
```

### Step 2 — Plan

```text
Create a detailed implementation plan.

Do not modify anything.
```

### Step 3 — Implement

```text
Implement the plan.
```

### Step 4 — Test

```text
Run the relevant tests and fix failures.
```

### Step 5 — Review

```text
Review the implementation for:

- correctness
- security
- performance
- accessibility
- maintainability
```

### Step 6 — Verify

```text
Show me:

1. files changed
2. what changed
3. tests run
4. remaining risks
```

---

# 34. Ralph Loop / Iterative Development

For iterative autonomous work:

```text
Implement the feature.

Continue iterating until:

- all requirements are implemented
- tests pass
- lint passes
- type checking passes
- no known errors remain
- implementation matches existing architecture

After each iteration:

1. inspect the result
2. run relevant tests
3. fix failures
4. repeat

Do not stop simply because the code compiles.
```

---

# 35. Useful Shell + Claude Combinations

### Analyze TODOs

```bash
grep -R "TODO" src | claude -p "Organize these TODOs by priority and area."
```

### Analyze package.json

```bash
cat package.json | claude -p "Explain this project's dependencies and scripts."
```

### Analyze TypeScript errors

```bash
pnpm tsc --noEmit 2>&1 | claude -p "Analyze these TypeScript errors and propose fixes."
```

### Analyze test failures

```bash
pnpm test 2>&1 | claude -p "Analyze these test failures and identify root causes."
```

---

# 36. Useful Development Prompts

## Before coding

```text
Do not code yet.

Understand the existing implementation and explain
the smallest change required to implement this feature.
```

## During coding

```text
Follow existing project patterns instead of introducing
new architectural patterns unless necessary.
```

## After coding

```text
Critically review your implementation.

Look for things you may have missed.
```

## Before committing

```text
Review the final diff against the original requirements.

Identify:
- missing requirements
- unnecessary changes
- bugs
- security concerns
- test gaps
```

---

# 37. Commands Worth Memorizing

| Command | Purpose |
|---|---|
| `claude` | Start Claude Code |
| `claude --help` | Show CLI help |
| `claude --version` | Show version |
| `claude -p "..."` | Run a prompt non-interactively |
| `claude --continue` | Continue previous conversation |
| `claude --resume` | Resume a session |
| `/help` | Show Claude Code commands |
| `/clear` | Clear conversation |
| `/compact` | Compress context |
| `/cost` | View usage/cost |
| `/status` | View session status |
| `/model` | View/change model |
| `/config` | Configure Claude Code |
| `/permissions` | Manage permissions |
| `/memory` | Manage memory/instructions |
| `/init` | Initialize project instructions |
| `/doctor` | Diagnose problems |
| `/mcp` | Manage/inspect MCP |
| `/hooks` | Manage hooks |
| `/agents` | Manage agents |
| `/tasks` | Manage/inspect tasks |

---

# 38. Recommended Daily Workflow

Start:

```bash
cd my-project
claude
```

Understand:

```text
Understand the project structure and the relevant code for my task.

Do not modify anything.
```

Plan:

```text
Create an implementation plan.
```

Implement:

```text
Implement the plan.
```

Test:

```text
Run the relevant tests.
Fix any failures.
```

Review:

```text
Review your changes for:

- bugs
- security issues
- performance problems
- accessibility issues
- unnecessary changes
```

Verify:

```text
Show me:

1. files changed
2. what changed
3. tests run
4. remaining risks
```

---

# 39. Golden Rules for Claude Code

### 1. Understand before modifying

```text
Inspect first. Modify second.
```

### 2. Give Claude constraints

Specify:

- files it can modify
- technologies to use
- technologies not to use
- testing requirements
- architectural constraints

### 3. Prefer existing patterns

```text
Follow existing project conventions unless there is
a documented reason to change them.
```

### 4. Keep changes small

```text
Implement the smallest change that satisfies the requirement.
```

### 5. Verify everything

```text
Code → Test → Review → Diff → Commit
```

### 6. Document project rules

Use:

```text
CLAUDE.md
AGENTS.md
```

to capture rules that Claude should consistently follow.

### 7. Don't blindly trust generated code

Always review:

```bash
git diff
```

and run:

```text
tests
lint
type checking
security checks
```

before merging.

---

# Quick Cheat Sheet

```bash
# Start
claude

# Start with prompt
claude "Explain this repository"

# Non-interactive
claude -p "Review this code"

# Version
claude --version

# Help
claude --help

# Continue
claude --continue

# Resume
claude --resume
```

Inside Claude:

```text
/help
/clear
/compact
/cost
/status
/model
/config
/permissions
/memory
/init
/doctor
/mcp
/hooks
/agents
/tasks
```

Recommended development loop:

```text
Understand
   ↓
Plan
   ↓
Implement
   ↓
Test
   ↓
Review
   ↓
Verify
   ↓
Commit
```
