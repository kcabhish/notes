# Removing Global NPM Packages from Old Node Versions

This guide explains how to clean up global npm packages from old Node versions managed via **nvm** (Linux/macOS) or **nvm-windows** (Windows).

---

## **For Linux / macOS (`nvm`)**

1. **List all installed Node versions:**

```bash
nvm ls
```

2. **Switch to the old Node version you want to clean:**

```bash
nvm use <version>
# Example:
nvm use 18.0.0
```

3. **List globally installed npm packages:**

```bash
npm list -g --depth=0
```

4. **Remove all global packages:**

```bash
npm ls -gp --depth=0 | awk -F/ '/node_modules/ {print $NF}' | xargs npm -g rm
```

5. **Repeat for each old Node version.**

---

## **For Windows (`nvm-windows`)**

1. **List installed Node versions:**

```cmd
nvm list
```

2. **Switch to the old Node version:**

```cmd
nvm use <version>
# Example:
nvm use 18.0.0
```

3. **List global packages:**

```cmd
npm list -g --depth=0
```

4. **Remove each package manually:**

```cmd
npm uninstall -g <package-name>
```

5. **Optional PowerShell one-liner to remove all global packages:**

```powershell
npm ls -g --parseable --depth=0 | Select-String "node_modules" | ForEach-Object { npm uninstall -g (Split-Path $_ -Leaf) }
```

💡 **Tip:** For `nvm-windows`, open a **new terminal** after switching Node versions to ensure changes take effect.

---

This ensures that your global npm packages are cleaned from old Node versions, keeping your environment tidy and avoiding conflicts.

