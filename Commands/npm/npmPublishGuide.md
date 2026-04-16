# NPM Publish Guide

## 1. Ensure You Have an npm Account

If you don’t have an npm account yet, create one:

```bash
npm adduser
```

You’ll be prompted for:
- **Username**
- **Password**
- **Email**


## 2. Prepare Your Package

Make sure your project has a `package.json` file. You can create it if it doesn’t exist:

```bash
npm init
```

Key fields to check:
- `"name"` – must be unique on npm.
- `"version"` – follows semantic versioning (e.g., `1.0.0`).
- `"main"` – entry point file (like `index.js`).
- `"files"` – optional, files to include in the package.


## 3. Build Your Package (if needed)

If your project uses TypeScript, JSX, or modern ESNext syntax, you need to compile it before publishing.

1. Add a build script in `package.json`:

```json
"scripts": {
  "build": "tsc"
}
```

2. Make sure the output directory (e.g., `dist/`) is included in `"files"`:

```json
"files": ["dist"]
```

3. Run the build:

```bash
npm run build
```

For pure JavaScript packages, this step can be skipped.


## 4. Login to npm (if not already)

```bash
npm login
```


## 5. Test Your Package Locally (Optional)

```bash
npm pack
```

This creates a `.tgz` file. Inspect it to ensure only the intended files are included.


## 6. Publish the Package

```bash
npm publish
```

### Optional Flags
- **Public scope (for scoped packages):**

```bash
npm publish --access public
```

- **Tagging a release:**

```bash
npm publish --tag beta
```


## 7. Update Your Package

When making changes, update the `version` in `package.json` using semantic versioning:

```bash
npm version patch   # 1.0.0 -> 1.0.1
npm version minor   # 1.0.1 -> 1.1.0
npm version major   # 1.1.0 -> 2.0.0
```

Then publish again:

```bash
npm publish
```


## 8. Verify Your Package

After publishing, check it on npm:

```bash
npm view <package-name>
```

