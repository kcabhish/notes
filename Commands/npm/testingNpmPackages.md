# Testing npm Packages Locally Before Publishing

There are several ways to **test npm packages locally** before publishing to the npm registry. This guide covers the most common and reliable methods.

---

## 1️⃣ Use `npm link` (or `pnpm link`)

This is the classic way to test a local package in another project.

### Steps:

1. In your library folder:

```bash
npm link
```

2. In your consuming project:

```bash
npm link your-package-name
```

3. Import it normally:

```ts
import { usePerfMonitor } from "react-use-perf-monitor";
```

4. Rebuild your library whenever you make changes:

```bash
npm run build
```

5. Cleanup when done:

```bash
npm unlink your-package-name
npm unlink      # optional, in library folder
```

> For `pnpm`, use `pnpm link --global` in the library and `pnpm link your-package-name` in the consumer.

---

## 2️⃣ Local file install

You can install your library directly from a local path:

```bash
cd your-consumer-project
npm install /path/to/react-use-perf-monitor
```

- Copies the package into `node_modules`.  
- Any changes in the library require reinstalling unless you use `npm pack` or watch mode.

---

## 3️⃣ Using `npm pack`

`npm pack` creates a **tarball (.tgz) of your package**, simulating the published version:

```bash
cd react-use-perf-monitor
npm pack
```

- Creates a file like `react-use-perf-monitor-1.0.0.tgz`  
- In your consuming project, install it:

```bash
npm install ../react-use-perf-monitor/react-use-perf-monitor-1.0.0.tgz
```

- Tests exactly what would be published.  
- Great for catching missing files in `files` or `dist`.

---

## 4️⃣ Test in a sandbox project

- Create a minimal React project (CRA, Vite, or Next.js).  
- Use either `npm link`, local install, or `.tgz` install.  
- Import and test all hooks/components.  
- Helps catch **runtime issues**, **build issues**, and **TypeScript typings**.

---

## 5️⃣ Watch mode for live testing

For packages using TypeScript + Rollup:

```json
"scripts": {
  "build": "tsc && rollup -c",
  "build:watch": "tsc -w & rollup -c -w"
}
```

Run:

```bash
npm run build:watch
```

- Automatically rebuilds your library while testing in the consumer project.  
- Great for rapid development and iterative testing.

---

✅ **Summary**

- **`npm link`** → fast iterative testing.  
- **Local install** → simple copy for testing.  
- **`npm pack`** → test exactly what will be published.  
- Combine with **watch mode** for live updates.