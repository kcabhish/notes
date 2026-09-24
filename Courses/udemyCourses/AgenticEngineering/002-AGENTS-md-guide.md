# AGENTS.md: What It Is and How to Use It

## Overview

`AGENTS.md` is a Markdown instruction file designed for AI coding agents.

Think of it as a combination of:

- A README for AI coding agents
- Coding standards
- Project architecture guidance
- Development workflow instructions
- Testing requirements
- Security and safety guardrails

The purpose is to tell an AI agent **how it should work inside your repository** without requiring you to repeat the same project instructions in every prompt.

---

## Basic Example

A repository might look like:

```text
my-project/
├── AGENTS.md
├── package.json
├── src/
│   ├── components/
│   └── services/
├── tests/
└── README.md
```

A simple `AGENTS.md` could contain:

```md
# Project Instructions

## Project Overview

This is a React + TypeScript application.

## Package Manager

Use pnpm.

Do not use npm or yarn.

## Development

Install dependencies:

    pnpm install

Start development:

    pnpm dev

## Testing

Before completing a task, run:

    pnpm test

    pnpm lint

## Code Style

- Use TypeScript strict mode.
- Prefer functional components.
- Use named exports.
- Avoid `any`.
- Use existing shared components before creating new ones.

## Architecture

- UI components belong in `src/components`.
- API clients belong in `src/services`.
- Business logic should not live inside React components.
- Keep components accessible according to WCAG guidelines.

## Do Not

- Do not modify generated files.
- Do not introduce a new dependency without checking whether an existing dependency can solve the problem.
- Do not change public APIs without updating tests.

## Definition of Done

Before finishing:

1. Run tests.
2. Run lint.
3. Verify TypeScript compilation.
4. Summarize changed files.
5. Mention any remaining issues.
```

Now a prompt such as:

> Add a user profile page.

can be interpreted using the project's existing development rules.

---

# How AGENTS.md Works

Conceptually, an AI coding agent works something like this:

```text
Your request
     ↓
┌─────────────────────┐
│   AI Coding Agent   │
├─────────────────────┤
│ System instructions │
│ AGENTS.md           │ ← project instructions
│ Repository context  │
│ Your prompt         │
│ Tools               │
└──────────┬──────────┘
           ↓
      LLM reasoning
           ↓
   Read / Edit / Test
           ↓
      Final result
```

The important distinction is:

> `AGENTS.md` is not an LLM feature by itself. It is an agent/harness convention.

The underlying LLM does not inherently know that `AGENTS.md` exists.

The **coding agent or development tool** must discover the file and provide its contents to the model as context.

---

# Does AGENTS.md Work With All LLMs?

Not automatically.

A better way to state it is:

> `AGENTS.md` is model-independent, but it is not automatically tool-independent.

The same Markdown file can be used with GPT, Claude, Gemini, and other models **if the coding agent using those models supports `AGENTS.md`**.

The model itself is not what determines whether the file is loaded. The agent/harness does.

## Examples

| Tool / Agent | Common Instruction Mechanism |
|---|---|
| OpenAI Codex | `AGENTS.md` |
| Cursor | `AGENTS.md` and/or `.cursor/rules/` |
| Claude Code | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Aider | Configured instruction/convention files |
| Windsurf | `.windsurf/rules/` |
| Other agents | Depends on the tool |

Therefore, do not assume that putting an `AGENTS.md` in a repository guarantees that every AI coding tool will automatically read it.

Always check the specific tool's instruction-file convention.

---

# AGENT.md vs AGENTS.md

You may encounter both:

```text
AGENT.md
AGENTS.md
```

These are not necessarily equivalent.

The widely adopted cross-tool convention is:

```text
AGENTS.md
```

Some projects or tools use `AGENT.md` for their own schemas or workflows.

For a new general-purpose AI coding project, use:

```text
AGENTS.md
```

unless the specific AI coding tool you're using explicitly requires another filename.

---

# Hierarchical AGENTS.md Files

One of the most useful patterns is having multiple `AGENTS.md` files at different levels of the repository.

For example:

```text
my-app/
│
├── AGENTS.md
│
├── frontend/
│   ├── AGENTS.md
│   └── src/
│
├── backend/
│   ├── AGENTS.md
│   └── src/
│
└── infrastructure/
    ├── AGENTS.md
    └── terraform/
```

## Root Instructions

The root `AGENTS.md` can contain rules that apply broadly:

```md
# Global Project Rules

- Use pnpm.
- Run tests before completing work.
- Do not introduce unnecessary dependencies.
- Never commit credentials.
```

## Frontend Instructions

`frontend/AGENTS.md` can contain frontend-specific rules:

```md
# Frontend Instructions

- Use React + TypeScript.
- Use Storybook for reusable components.
- Follow WCAG accessibility requirements.
- Use Vitest.
```

## Backend Instructions

`backend/AGENTS.md` can contain backend-specific rules:

```md
# Backend Instructions

- Use Python 3.13.
- Use FastAPI.
- Use uv.
- Use pytest.
- Follow the repository service/repository architecture.
```

This lets the agent receive instructions that are relevant to the part of the repository it is working on.

When supported by the agent, more specific instructions can take precedence over broader project instructions.

---

# What Should Go Into AGENTS.md?

Good candidates include:

## 1. Project Overview

Explain what the project is and its major technologies.

```md
## Project

This is a React + TypeScript frontend with a Python FastAPI backend.

## Main Technologies

- React
- TypeScript
- Vite
- Python
- FastAPI
- PostgreSQL
```

## 2. Development Commands

Document the commands an agent should use.

```md
## Commands

Install dependencies:

    pnpm install

Run frontend:

    pnpm dev

Run tests:

    pnpm test

Run lint:

    pnpm lint
```

## 3. Architecture

Tell the agent where different types of code belong.

```md
## Architecture

- UI components belong in `src/components`.
- API clients belong in `src/services`.
- Business logic belongs in `src/domain`.
- Shared utilities belong in `src/lib`.
- Tests should be colocated with the code they test.
```

## 4. Coding Conventions

```md
## Coding Standards

- Use TypeScript strict mode.
- Prefer functional React components.
- Avoid `any`.
- Prefer existing abstractions.
- Keep functions focused.
- Avoid unnecessary dependencies.
```

## 5. Testing

```md
## Testing

Before completing a task:

1. Run unit tests.
2. Run linting.
3. Run type checking.
4. Run relevant integration tests.
```

## 6. Security

This is especially important for AI agents.

```md
## Security

- Never commit secrets.
- Never hardcode credentials.
- Do not log sensitive information.
- Validate external input.
- Follow least-privilege principles.
```

## 7. Definition of Done

Tell the agent what "finished" means.

```md
## Definition of Done

Before declaring a task complete:

1. Run relevant tests.
2. Run linting.
3. Check for type errors.
4. Review the diff.
5. Confirm no unrelated files were modified.
6. Summarize the changes.
7. Report any remaining issues.
```

---

# AGENTS.md vs README.md

A useful distinction is:

| File | Primary Audience | Purpose |
|---|---|---|
| `README.md` | Humans | Explain the project |
| `AGENTS.md` | AI coding agents | Explain how agents should work on the project |
| `CLAUDE.md` | Claude Code | Claude-specific instructions |
| `.cursor/rules/` | Cursor | Cursor-specific rules |
| `GEMINI.md` | Gemini CLI | Gemini-specific instructions |
| User prompt | Agent | Task-specific instructions |
| System prompt | Model/agent | Highest-level behavior |

Think about it this way:

```text
README.md
    ↓
"What is this project?"

AGENTS.md
    ↓
"How should an AI work on this project?"

Your prompt
    ↓
"What do I want you to do right now?"
```

---

# AGENTS.md Does Not Make the LLM Smarter

`AGENTS.md` does not increase the underlying intelligence of the model.

Instead, it improves the **context available to the agent**.

Without project instructions, the agent may have to infer:

- Framework
- Architecture
- Naming conventions
- Testing strategy
- Package manager
- Security rules
- File organization
- Development workflow

With `AGENTS.md`, those rules are explicitly provided.

For example:

Without project instructions:

> Add a new API endpoint.

The agent has to discover or infer where the endpoint belongs and how it should be implemented.

With `AGENTS.md`:

> Add a new API endpoint.

The agent already knows:

```text
Framework: FastAPI
Package manager: uv
API location: backend/app/api
Testing: pytest
Style: service/repository architecture
Validation: Pydantic
```

This reduces ambiguity and makes agent behavior more consistent.

---

# AGENTS.md and Context Engineering

`AGENTS.md` is closely related to **context engineering**.

Context engineering is about intentionally controlling:

- What information the model receives
- When it receives that information
- Which instructions apply
- Which project artifacts are relevant
- What tools the agent can use
- What constraints the agent must follow

A useful mental model is:

```text
                 Agent Context
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
  System Rules    AGENTS.md    User Request
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                    LLM
                      ↓
               Agent Actions
                      ↓
              Code / Tests / Tools
```

`AGENTS.md` is therefore one practical mechanism for **encoding project context and constraints for coding agents**.

---

# Recommended Structure for an AI Project

For a modern full-stack AI application, a structure like this works well:

```text
project/
│
├── AGENTS.md
│
├── frontend/
│   ├── AGENTS.md
│   └── src/
│
├── backend/
│   ├── AGENTS.md
│   └── app/
│
├── agents/
│   ├── AGENTS.md
│   └── ...
│
├── infrastructure/
│   └── AGENTS.md
│
└── docs/
```

The root file contains general project rules.

More specific directories contain specialized instructions.

---

# Example: AI Investigation Platform

For an application involving React, Python, RAG, MCP, and sensitive investigation data, a root `AGENTS.md` could look like:

```md
# AGENTS.md

## Mission

Build a secure, maintainable investigation platform.

## Technology

### Frontend

- React
- TypeScript
- Vite
- Storybook

### Backend

- Python
- FastAPI
- PostgreSQL

### AI

- LLM accessed through LiteLLM
- RAG
- Embeddings
- MCP

## General Rules

- Prefer existing abstractions.
- Do not introduce dependencies unnecessarily.
- Keep changes focused.
- Do not modify unrelated code.
- Never hardcode secrets.
- Never commit credentials.
- Write tests for new functionality.

## Security

- Treat investigation data as sensitive.
- Never expose PII in logs.
- Never place credentials in source code.
- Validate external input.
- Apply least-privilege principles.

## Testing

### Frontend

    pnpm test
    pnpm lint

### Backend

    uv run pytest
    uv run ruff check .

## Git

- Do not commit directly to main.
- Use descriptive commit messages.
- Keep commits focused.

## Completion Requirements

Before declaring a task complete:

1. Run relevant tests.
2. Run linting.
3. Check for type errors.
4. Review the diff.
5. Report what changed.
6. Report tests that were executed.
7. Report any remaining issues.
```

Then specialized files can provide more detailed rules:

```text
frontend/AGENTS.md
backend/AGENTS.md
agents/AGENTS.md
infrastructure/AGENTS.md
```

---

# Recommended Strategy for Multi-LLM Development

If you use multiple AI coding tools, keep a **single canonical set of project rules** whenever possible.

For example:

```text
AGENTS.md
    │
    ├── Codex
    ├── Cursor
    └── Other compatible agents

CLAUDE.md
    │
    └── Claude-specific instructions

GEMINI.md
    │
    └── Gemini-specific instructions
```

Avoid copying the same large set of rules into every tool-specific file.

Otherwise, the files can drift:

```text
AGENTS.md
    ↓
Rule A

CLAUDE.md
    ↓
Rule A + different Rule B

GEMINI.md
    ↓
Rule A + outdated Rule C
```

That can create inconsistent behavior between agents.

A better strategy is:

```text
             Shared Project Rules
                    │
                    ↓
                AGENTS.md
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      Codex       Cursor      Other
        │
        └──── Tool-specific rules ────┐
                                     ↓
                              CLAUDE.md / etc.
```

Keep tool-specific files limited to instructions that genuinely need to be different for that tool.

---

# Practical Guidelines

## Keep Instructions Specific

Prefer:

```md
Use `pnpm` for dependency management.
```

over:

```md
Use modern package management practices.
```

Specific instructions are easier for agents to follow.

## Explain Why When It Matters

Instead of:

```md
Do not modify generated files.
```

consider:

```md
Do not modify generated files because they are regenerated by the build pipeline.
```

The reason can help an agent make better decisions when encountering an unusual situation.

## Avoid Excessive Rules

Do not turn `AGENTS.md` into a giant instruction dump.

Too many instructions can:

- Increase context size
- Make important rules harder to notice
- Create contradictions
- Make maintenance difficult

Prefer concise, high-value instructions.

## Keep It Current

Treat `AGENTS.md` like code.

When the project architecture changes:

```text
Update architecture
       ↓
Update AGENTS.md
       ↓
AI receives current instructions
```

Outdated instructions can be worse than no instructions because they actively steer the agent toward incorrect behavior.

---

# Key Takeaways

1. **`AGENTS.md` is an instruction file for AI coding agents.**
2. It is written in ordinary Markdown.
3. It provides project-specific context, conventions, workflows, and guardrails.
4. It is **not an LLM capability**.
5. The AI coding tool must support and load the file.
6. It can be used with different LLMs when the agent/harness supports it.
7. `AGENTS.md` is the broadly adopted filename; `AGENT.md` may be tool/project-specific.
8. Multiple `AGENTS.md` files can provide hierarchical instructions.
9. Keep general project rules in the root file.
10. Use nested files for frontend, backend, infrastructure, AI agents, etc.
11. Keep tool-specific files such as `CLAUDE.md` focused on tool-specific behavior.
12. Treat `AGENTS.md` as part of your project's **context-engineering strategy**.

---

# References

- AGENTS.md community specification and ecosystem: https://agents.md/
- Claude Code documentation: https://docs.anthropic.com/
- GitHub Copilot documentation: https://docs.github.com/en/copilot
- Gemini CLI documentation: https://github.com/google-gemini/gemini-cli
