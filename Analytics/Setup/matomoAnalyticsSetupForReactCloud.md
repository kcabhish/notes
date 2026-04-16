# Matomo Analytics Setup Guide for React

This guide walks through setting up **Matomo Analytics** in a **React (SPA) application**, focusing on:

- User interaction tracking
- Time spent on pages
- Core Web Vitals
- Page navigation (SPA-aware)
- Session lifecycle (open → exit)

The guide is written from a **production-ready, senior front-end engineering perspective**.

---

## 1. Prerequisites

Before you start, make sure you have:

- A Matomo account (Cloud or Self-Hosted)
- A Matomo **Site ID**
- A Matomo base URL (e.g. `https://your-org.matomo.cloud`)
- A React app (Vite, CRA, Next.js SPA mode, etc.)
- `pnpm` as your package manager

---

## 2. Install Dependencies

```bash
pnpm add @datapunt/matomo-tracker-react web-vitals
```

---

## 3. Initialize Matomo

Create a Matomo instance configuration.

```ts
// src/matomo.ts
import { createInstance } from "@datapunt/matomo-tracker-react";

export const matomo = createInstance({
  urlBase: "https://YOUR_MATOMO_URL",
  siteId: 1,
  trackerUrl: "https://YOUR_MATOMO_URL/matomo.php",
  srcUrl: "https://YOUR_MATOMO_URL/matomo.js",
});
```

---

## 4. Wrap Your Application

```tsx
// src/main.tsx
import React from "react";
import ReactDOM from "react-dom/client";
import { MatomoProvider } from "@datapunt/matomo-tracker-react";
import { matomo } from "./matomo";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <MatomoProvider value={matomo}>
    <App />
  </MatomoProvider>
);
```

---

## 5. Track Page Navigation (SPA)

Matomo does not automatically track SPA route changes. You must track them manually.

```ts
// src/hooks/useMatomoPageView.ts
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { useMatomo } from "@datapunt/matomo-tracker-react";

export function useMatomoPageView() {
  const location = useLocation();
  const { trackPageView } = useMatomo();

  useEffect(() => {
    trackPageView({
      documentTitle: document.title,
      href: window.location.href,
    });
  }, [location.pathname]);
}
```

Use it once at the root of your app.

```tsx
useMatomoPageView();
```

---

## 6. Track User Interactions (Events)

Example: button click tracking.

```tsx
import { useMatomo } from "@datapunt/matomo-tracker-react";

function SaveButton() {
  const { trackEvent } = useMatomo();

  return (
    <button
      onClick={() =>
        trackEvent({
          category: "User Interaction",
          action: "Click",
          name: "Save Button",
        })
      }
    >
      Save
    </button>
  );
}
```

### Recommended Event Taxonomy

```
Category: User Interaction
Action: Click | Hover | Submit
Name: Component or Feature Name
```

---

## 7. Track Session Lifecycle

Matomo automatically manages sessions, but you can enrich them.

### App Open

```ts
trackEvent({
  category: "Session",
  action: "App Opened",
});
```

### App Exit (Best Effort)

```ts
useEffect(() => {
  const onUnload = () => {
    navigator.sendBeacon(
      "https://YOUR_MATOMO_URL/matomo.php",
      JSON.stringify({
        idsite: 1,
        rec: 1,
        e_c: "Session",
        e_a: "App Closed",
      })
    );
  };

  window.addEventListener("beforeunload", onUnload);
  return () => window.removeEventListener("beforeunload", onUnload);
}, []);
```

---

## 8. Track Time on Page (Heartbeat)

Enable Matomo's heartbeat timer for accurate engagement tracking.

```ts
window._paq = window._paq || [];
window._paq.push(["enableHeartBeatTimer", 15]);
```

This sends activity pings every 15 seconds only when the page is active.

---

## 9. Track Core Web Vitals

Create a Web Vitals reporter.

```ts
// src/reportWebVitals.ts
import { onCLS, onFID, onLCP, onINP, onTTFB } from "web-vitals";
import { matomo } from "./matomo";

function sendToMatomo(metric: any) {
  matomo.trackEvent({
    category: "Web Vitals",
    action: metric.name,
    value: Math.round(metric.value),
  });
}

onCLS(sendToMatomo);
onFID(sendToMatomo);
onLCP(sendToMatomo);
onINP(sendToMatomo);
onTTFB(sendToMatomo);
```

Import it once in your app entry.

```ts
import "./reportWebVitals";
```

---

## 10. Verify Tracking

In the Matomo dashboard, verify data in:

- Visitors → Real-Time
- Behavior → Pages
- Behavior → Events
- Behavior → Engagement

Use browser DevTools to confirm network calls to `matomo.php`.

---

## 11. Production Best Practices

- Disable analytics in local development
- Respect Do-Not-Track headers
- Enable IP anonymization in Matomo
- Centralize analytics helpers
- Avoid sending PII

Example helper:

```ts
export const trackClick = (name: string) =>
  trackEvent({
    category: "User Interaction",
    action: "Click",
    name,
  });
```

---

## 12. Outcome

With this setup, you now have:

- Element-level interaction tracking
- Accurate time-on-page metrics
- SPA-safe page navigation analytics
- Core Web Vitals visibility
- Session lifecycle insights
- Privacy-friendly analytics without third-party data brokers

---

