# ⚙️ Error Handling in React with TypeScript

## 🧩 Overview

Error handling in React (with TypeScript) involves managing both **UI-level rendering errors** and **runtime/async errors** gracefully and safely. TypeScript’s static typing helps make error management predictable and robust.

---

## 🧱 1. Error Boundaries (for Class Components)

Error Boundaries catch **render-time errors** in child components.

```tsx
import React from "react";

interface ErrorBoundaryState {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends React.Component<
  React.PropsWithChildren,
  ErrorBoundaryState
> {
  constructor(props: React.PropsWithChildren) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error("Error caught by boundary:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return <div>Something went wrong. Please refresh.</div>;
    }
    return this.props.children;
  }
}
```

**Usage:**
```tsx
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

✅ **Best Practice:**
- Use multiple small boundaries (not one global one).
- Display fallback UI instead of crashing.

---

## ⚙️ 2. Handling Async / API Errors

Use a structured approach when dealing with API calls.

```tsx
type ApiResponse<T> = { data: T } | { error: string };

async function fetchUser(): Promise<ApiResponse<User>> {
  try {
    const res = await fetch("/api/user");
    if (!res.ok) throw new Error("Failed to fetch user");
    const data: User = await res.json();
    return { data };
  } catch (error) {
    return { error: (error as Error).message };
  }
}
```

✅ **Best Practice:**
- Return predictable objects (`Result` pattern).
- Avoid throwing raw exceptions.
- Use `try/catch` for async functions.

---

## 🧠 3. Type Narrowing for Unknown Errors

```tsx
try {
  // ...
} catch (err: unknown) {
  if (err instanceof Error) {
    console.error(err.message);
  } else {
    console.error("Unknown error", err);
  }
}
```

✅ **Best Practice:**
Always narrow `unknown` errors with `instanceof` before using them.

---

## 🔐 4. Custom Error Classes

```tsx
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = "ValidationError";
  }
}
```

✅ **Best Practice:**
Use subclasses of `Error` to categorize (validation, network, etc.).

---

## 🌐 5. Global Error Handlers

```tsx
useEffect(() => {
  const onError = (event: ErrorEvent) => {
    console.error("Global error:", event.error);
  };
  const onRejection = (event: PromiseRejectionEvent) => {
    console.error("Unhandled promise:", event.reason);
  };

  window.addEventListener("error", onError);
  window.addEventListener("unhandledrejection", onRejection);

  return () => {
    window.removeEventListener("error", onError);
    window.removeEventListener("unhandledrejection", onRejection);
  };
}, []);
```

✅ **Best Practice:**
Combine with logging tools (e.g., Sentry, Datadog).

---

## 🪄 6. Error Handling in Functional Components (Custom Hook)

A reusable and type-safe **custom hook** for async operations.

### `useAsync` Hook

```tsx
import { useState, useCallback } from "react";

export function useAsync<T>(
  asyncFunction: () => Promise<T>,
  immediate = true
) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const execute = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await asyncFunction();
      setData(result);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("An unknown error occurred");
      }
    } finally {
      setLoading(false);
    }
  }, [asyncFunction]);

  React.useEffect(() => {
    if (immediate) execute();
  }, [execute, immediate]);

  return { data, error, loading, execute };
}
```

### Example API Function

```tsx
export interface User {
  id: number;
  name: string;
  email: string;
}

export async function fetchUser(): Promise<User> {
  const res = await fetch("https://jsonplaceholder.typicode.com/users/1");
  if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
  return res.json();
}
```

### Usage in a Functional Component

```tsx
import React from "react";
import { useAsync } from "./useAsync";
import { fetchUser, User } from "./api";

export function UserProfile() {
  const { data: user, error, loading, execute } = useAsync<User>(fetchUser);

  if (loading) return <p>Loading user info...</p>;
  if (error)
    return (
      <div>
        <p style={{ color: "red" }}>Error: {error}</p>
        <button onClick={execute}>Retry</button>
      </div>
    );
  if (!user) return <p>No user data found.</p>;

  return (
    <div>
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
    </div>
  );
}
```

✅ **Best Practice:**
- Handle all 3 states (`loading`, `error`, `data`).
- Use retry logic for resiliency.
- Keep hooks pure (no side effects outside React lifecycle).

---

## ✅ Summary Table

| Layer | Best Practice |
|-------|----------------|
| UI errors | Use Error Boundaries |
| Async/API | Use `useAsync` or `Result` patterns |
| Type safety | Narrow `unknown` errors |
| Business logic | Custom `Error` classes |
| Global errors | Catch `window.error` & `unhandledrejection` |
| UX fallback | Show retry + fallback UIs |

---

## 🚀 Bonus: AbortController for Fetch Cleanup

```tsx
useEffect(() => {
  const controller = new AbortController();
  const fetchData = async () => {
    try {
      const res = await fetch("...", { signal: controller.signal });
    } catch (err: unknown) {
      if ((err as Error).name === "AbortError") return;
    }
  };
  fetchData();
  return () => controller.abort();
}, []);
```

✅ Prevents memory leaks when components unmount during async calls.

---

## 🧭 Key Takeaways
- **Centralize** async handling with reusable hooks.  
- **Type safely** narrow and categorize errors.  
- **Design resilient UI** with fallbacks and retry options.  
- **Integrate monitoring** for full visibility.  
