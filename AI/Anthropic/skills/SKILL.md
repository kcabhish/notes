---
name: react-code-review
description: Reviews React components and pull requests for hook mistakes, prop/type issues, unnecessary re-renders, accessibility gaps, and missing tests. Use this whenever the user asks to review a component, check a PR, look over a diff, or says things like "review my changes", "lgtm check", "does this look right", or "check my hooks" in a React/TypeScript codebase, even if they don't say the word "skill" or "review" explicitly.
---

# React Code Review

A structured checklist-driven review for React (and React + TypeScript) code changes. The goal is a consistent, prioritized review every time, not a freeform read-through.

## Step 1: Find what changed

- If in a git repo, run `git diff` (or `git diff main...HEAD` for a branch) to scope the review to actual changes rather than the whole file.
- If the user pasted or pointed to specific files instead, review exactly those.
- Don't review generated files, lockfiles, or `node_modules`.

## Step 2: Run the checklist

Go through each changed component/file against these categories. Only report what's actually present — don't pad the review with categories that don't apply.

### Hooks
- `useEffect`/`useMemo`/`useCallback` dependency arrays are complete and accurate (no stale closures, no missing deps silently suppressed with eslint-disable).
- No hooks called conditionally, in loops, or after an early return.
- Custom hooks follow the `useXyz` naming convention and don't break the rules of hooks internally.
- Cleanup functions exist for subscriptions, timers, and event listeners.

### Props & typing
- Props are typed (TypeScript interface/type, or PropTypes if it's a JS codebase) — flag `any`.
- Required vs. optional props make sense given how the component is used.
- Default values are set sensibly rather than defaulted deep inside the component body.

### Rendering & performance
- Lists render with a stable, unique `key` (not array index unless the list is static).
- No obviously expensive work (filtering, sorting, formatting) running unmemoized on every render when it doesn't need to.
- No inline object/array/function literals passed as props to memoized children in a way that defeats the memoization.
- State lives at the right level — not lifted higher than necessary, not duplicated across components.

### Accessibility
- Images have meaningful `alt` text (or `alt=""` if decorative).
- Interactive elements are actual buttons/links, not `div`/`span` with `onClick`.
- Form inputs have associated labels.
- Color/visual state isn't the only way information is conveyed.

### Structure & readability
- Component does one thing; flag components that are clearly doing too much and could be split.
- Naming is consistent with the rest of the codebase.
- No dead code, commented-out blocks, or leftover `console.log`s.

### Tests
- New logic (especially conditionals, hooks with dependencies, edge cases) has a corresponding test.
- Existing tests weren't modified in a way that just makes them pass rather than actually testing the change.

For anything project-specific — naming conventions, folder structure, state management library rules — check `references/style-guide.md` if present in this skill's folder before flagging a style issue, so you don't contradict the team's own conventions.

## Step 3: Format the output

Report findings grouped by file, then by severity within each file:

```
## ComponentName.tsx

**Blocking**
- [Hooks] `useEffect` on line 42 is missing `userId` in its dependency array — will use a stale value after the prop changes.

**Should fix**
- [Accessibility] Icon-only button on line 18 has no `aria-label`.

**Nit**
- [Readability] `handleClick` and `handleSubmit` could be combined — minor, up to you.
```

- Use "Blocking" only for things that are actually bugs or will break at runtime/build — not style preferences.
- If a file has no issues, say so briefly rather than omitting it silently.
- End with a one-line summary: how many blocking issues, how many should-fix, how many nits.

## Notes

- Prefer pointing at the specific line/snippet over describing the issue abstractly.
- If the codebase uses a specific state library (Redux, Zustand, Jotai, etc.) or a specific styling approach (CSS Modules, Tailwind, styled-components), review against that convention rather than a generic React opinion.
- If test coverage tooling is available (e.g. `npm test -- --coverage`), it's fine to run it to check whether new code is covered, but don't block a review on flaky or unrelated failing tests — call those out separately from the review itself.
