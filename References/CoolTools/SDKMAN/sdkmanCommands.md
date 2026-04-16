# 📦 SDKMAN! Command Cheat Sheet

A curated list of **SDKMAN!** commands, ranked by usefulness and frequency of use.

---

## 🚀 Most Useful Commands

### 1. Install a version of a tool/SDK

```
sdk install <candidate> <version>
```

Installs a specific version of a candidate (e.g., Java, Maven, Gradle).

Example:

```
sdk install java 17.0.9-tem
```

---

### 2. List all available versions of a candidate

```
sdk list <candidate>
```

Shows all available versions and highlights installed/default ones.

Example:

```
sdk list java
```

---

### 3. Use a version temporarily (for current terminal session only)

```
sdk use <candidate> <version>
```

Example:

```
sdk use java 21.0.1-tem
```

---

### 4. Set a version as default (globally)

```
sdk default <candidate> <version>
```

Example:

```
sdk default java 17.0.9-tem
```

---

### 5. Show currently active versions

```
sdk current
```

Lists the active version of each installed candidate.

---

### 6. Show current version of a specific candidate

```
sdk current <candidate>
```

Example:

```
sdk current java
```

---

### 7. Uninstall a specific version

```
sdk uninstall <candidate> <version>
```

Example:

```
sdk uninstall java 8.0.392-tem
```

---

## 🛠️ Advanced / Less Common Commands

### 8. Update SDKMAN! itself

```
sdk selfupdate
```

---

### 9. Upgrade all installed candidates

```
sdk upgrade
```

---

### 10. Initialize `.sdkmanrc` for project-local SDK versioning

```
sdk env init
```

Creates a `.sdkmanrc` file with the current versions of all active SDKs in that directory.

To activate:

```
sdk env
```

---

### 11. Broadcast latest SDKMAN! news

```
sdk broadcast
```

---

### 12. Show all available SDKMAN! commands

```
sdk help
```

---

## 💡 Tips

- Run `sdk list` (with no candidate) to see all supported tools (e.g., java, gradle, maven, kotlin, etc.).
- Use `.sdkmanrc` in a project folder to auto-switch SDKs when `cd` into it.
- Versions are labeled like `17.0.9-tem` (Temurin), `21.0.1-zulu`, etc.

---

## 🔗 Resources

- [SDKMAN! Official Site](https://sdkman.io/)
- [GitHub Repository](https://github.com/sdkman/sdkman-cli)
