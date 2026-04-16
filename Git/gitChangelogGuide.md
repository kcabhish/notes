# Git Changelog Generation Guide

This document lists common Git commands used to generate changelogs from diffs, commits, and tags. These commands are useful for release notes, audits, and deployment summaries.

---

## Generate Changelog Between Two Commits (One Line Summary)

```sh
git log --oneline <old_commit>..<new_commit>
```

Example:
```sh
git log --oneline abc123..HEAD
```

---

## Generate Detailed Changelog Between Two Commits

```sh
git log <old_commit>..<new_commit>
```

---

## Generate Changelog Showing File Change Summary

```sh
git diff --stat <old_commit>..<new_commit>
```

---

## Generate Full Diff Output

```sh
git diff <old_commit>..<new_commit>
```

---

## Generate Changelog From Last Git Tag to HEAD

```sh
git log --oneline $(git describe --tags --abbrev=0)..HEAD
```

---

## Generate Pretty-Formatted Changelog (Release Notes Friendly)

```sh
git log <old_commit>..<new_commit> \
  --pretty=format:"- %s (%an)"
```

---

## Generate Changelog Listing Only Modified Files

```sh
git diff --name-only <old_commit>..<new_commit>
```

---

## Optional: Save Changelog to a File

```sh
git log --oneline <old_commit>..<new_commit> > CHANGELOG.md
```

---

## Recommended Usage

- Use `--oneline` for high-level summaries
- Use `--stat` for deployment validation
- Use pretty formatting for release notes
- Use tags to track production releases
