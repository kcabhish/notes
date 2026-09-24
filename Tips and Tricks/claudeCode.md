# Useful claude commands/skills

| skills | Description |
|---|---|
|/init|initializes the claude.md for the project|
|/context| provides details on the available context window|
|/compact| compresses and frees up context window,may loose some context during compression|
|/status| gives details of the claude version and session info |
|/help | shows available commands |
|/cost | Displays information about token usage/cost for the crrent session|
|/model | view or change the current model|
|/mcp | Manage or inspect MCP servers |
|/hooks | Manage claude code hooks |
|/agents | Manage or inspect agents/subagents when supported by your claude code version |


## MCP Servers

| MCP | Description |
| --- | --- |
| Perplexity MCP | Lets claude search the internet from terminal |
| Playwright MCP | Open pages, clicks buttons and fill out forms and test apps |
| Firecrawl  MCP | pull context from website |
| higgsfield MCP | this connects claude to over 30 image and vidoe generation models at once |
| Chrome Devtools MCP | This connects to what ever tool you have open in chrome, debug, test and automate tasks |

## Essential CLI Options

Print response without interactive mode
claude -p "Explain this codebase"

-p is useful for scripting and automation.

*Example:*

claude -p "Find all TODO comments in this repository"
Pipe input into Claude
cat README.md | claude -p "Summarize this README"

*Another example:*

git diff | claude -p "Review this diff for bugs"

This is extremely useful in development workflows.

## Specify a model

Depending on your installed Claude Code version:

claude --model <model>

Example:

claude --model sonnet

Check available models with:

claude --help
## Working With a Codebase


Start Claude from the repository root:

cd my-project
claude

Then ask:

Explain the architecture of this repository.

A better approach for a large project:

Analyze this repository.

1. Identify the application entry points.
2. Identify the major modules.
3. Identify the API layer.
4. Identify database access.
5. Identify authentication.
6. Identify testing strategy.
7. Identify build/deployment configuration.

Do not modify anything.

## Ask Claude to Explore Before Coding

A useful workflow is:

First inspect the relevant files and understand the existing implementation.

Do not modify anything yet.

Explain:
- how the current implementation works
- relevant files
- dependencies
- potential risks
- recommended implementation approach

Then, after reviewing the plan:

Implement the proposed changes.

This helps prevent unnecessary modifications.

## Ask Claude to Create a Plan
Create an implementation plan for this feature.

Do not modify any files.

Include:
- files that need to change
- files that need to be created
- architectural considerations
- testing strategy
- migration considerations
- potential risks

For a larger task:

Break this feature into small implementation steps.

For each step provide:
- objective
- files involved
- implementation details
- tests
- dependencies

## Code Review

Review the current changes:

Review my current changes for:
- bugs
- security issues
- performance problems
- accessibility problems
- error handling
- maintainability
- test coverage

Review Git changes:

git diff | claude -p "Perform a detailed code review."

Review staged changes:

git diff --cached | claude -p "Review these staged changes."
## Git Workflows
Explain current changes
```
git diff | claude -p "Explain these changes."
```
Generate a commit message
```
git diff --cached | claude -p "Generate a concise conventional commit message."
```
Review a commit
```
git show <commit> | claude -p "Review this commit for potential issues."
```

Review a branch
```
git diff main...HEAD | claude -p "Review this branch against main."
```