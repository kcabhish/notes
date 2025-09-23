# Testing Your Local npm Package Using `npm link`

`npm link` allows you to test your local npm package in another project **without publishing it**. Here’s a step-by-step guide for `react-use-perf-monitor`.

---

## Create a global link in your library

Navigate to your library project root:

```bash
cd react-use-perf-monitor
npm link
```

- This creates a **global symlink** for your package.
- Example message:

```
/usr/local/lib/node_modules/react-use-perf-monitor -> /your/path/react-use-perf-monitor
```

---

## Link the package in your consuming project

Navigate to the project where you want to test your library:

```bash
npm link react-use-perf-monitor
```

- This links your local package into the project’s `node_modules`.
- You can now import it like a normal npm package:

```ts
import { usePerfMonitor } from "react-use-perf-monitor";
```

---

## Build your library first

Since your library uses TypeScript + Rollup, make sure it’s built before testing:

```bash
cd react-use-perf-monitor
npm run build
```

- Generates the `dist/` folder with CJS, ESM, and `.d.ts` files.
- Any changes in `src/` require **rebuilding** for them to appear in the consuming project.

---

## Optional: Watch mode for development

Add a watch script in your library's `package.json`:

```json
"scripts": {
  "build": "tsc && rollup -c",
  "build:watch": "tsc -w & rollup -c -w"
}
```

Run the watch mode:

```bash
npm run build:watch
```

- Changes are automatically rebuilt while testing via `npm link`.

---

## Cleanup after testing

When done testing:

```bash
# In the consuming project
npm unlink react-use-perf-monitor

# In your library (optional)
npm unlink
```

---

This allows user to **develop your library locally**, test it in a real project, and **iterate quickly** without publishing to npm.

