
# 🏷️ Git Tags – Beginner-Friendly Guide

Tags in Git help you mark important points in your project, like releases (`v1.0.0`, `v2.0.0`, etc.).

---

##  Step 1: Make Sure You're in Your Git Project

```bash
cd path/to/your/project
```

---

## 🔍 Step 2: View Your Commit History

To tag an older commit, you'll need its hash:

```bash
git log --oneline
```

Example output:

```
a1b2c3d Fix login bug
9f8e7d6 Add homepage
3c4b5a6 Initial commit
```

Copy the hash of the commit you want to tag.

---

## 🏷️ Step 3: Create a Tag

### Option A: Annotated Tag (recommended for releases)

```bash
git tag -a v1.0.0 -m "First release"
```

You can also tag an older commit:

```bash
git tag -a v1.0.0 <commit-hash> -m "Tagging first release"
```

### Option B: Lightweight Tag (quick and simple)

```bash
git tag v1.0.0
```

To tag an older commit:

```bash
git tag v1.0.0 <commit-hash>
```

---

## 📤 Step 4: Push the Tag to Remote (e.g., GitHub)

Push a specific tag:

```bash
git push origin v1.0.0
```

Push all tags:

```bash
git push origin --tags
```

---

## 🔍 View Tags

List all tags:

```bash
git tag
```

See the commit a tag points to:

```bash
git show v1.0.0
```

---

## ❌ Delete a Tag

### Delete Locally:

```bash
git tag -d v1.0.0
```

### Delete from Remote:

```bash
git push origin --delete tag v1.0.0
```

---

## 🚨 Does Deleting a Tag Delete the Commit?

**No!** Deleting a tag does **not** delete the commit. It only removes the label (bookmark).

### Example:

Before:
```
[Commit A] → [Commit B] → [Commit C] ← v1.0.0 → [Commit D]
```

After:
```
[Commit A] → [Commit B] → [Commit C]       → [Commit D]
                         (still exists)
```

The commit stays in the history, accessible by its hash or if other tags/branches point to it.

---

##  Summary

- Tags mark specific commits.
- You can create tags for current or past commits.
- Tags can be pushed, viewed, or deleted.
- **Deleting a tag doesn’t delete the commit**.

Happy tagging! 🎉
