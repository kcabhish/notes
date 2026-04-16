# Matomo On-Premise Analytics Setup Guide for React

This guide explains how to set up **Matomo On-Premise (Self-Hosted)** analytics in a **React Single Page Application**, with a strong focus on **privacy, control, and production readiness**.

It covers tracking:

- User interactions on UI elements
- Time spent on pages (accurate engagement)
- Core Web Vitals
- SPA page navigation
- Session lifecycle (app open → exit)

---

## 1. Why Matomo On-Premise?

Matomo On-Premise is ideal when you need:

- Full data ownership
- No third-party data sharing
- GDPR / HIPAA / internal compliance
- Custom plugins & extensions
- First-party analytics for internal platforms

Typical use cases:
- Enterprise dashboards
- Internal tools
- Regulated industries
- In-house analytics platforms

---

## 2. Infrastructure Prerequisites

### Server Requirements

- Linux server (Ubuntu recommended)
- PHP 8.1+
- MySQL / MariaDB
- Nginx or Apache
- SSL (HTTPS required)

### Minimum Sizing (Small–Medium Traffic)

| Component | Recommendation |
|--------|---------------|
| CPU | 2 vCPU |
| Memory | 4 GB RAM |
| Storage | SSD |
| Database | MySQL 8+ |

---

## 3. Install Matomo On-Premise

### Download & Extract

```bash
wget https://builds.matomo.org/matomo.zip
unzip matomo.zip
sudo mv matomo /var/www/matomo
```

### Set Permissions

```bash
sudo chown -R www-data:www-data /var/www/matomo
sudo chmod -R 755 /var/www/matomo
```

### Configure Web Server (Nginx Example)

```nginx
server {
  listen 443 ssl;
  server_name analytics.yourdomain.com;

  root /var/www/matomo;
  index index.php;

  location / {
    try_files $uri $uri/ =404;
  }

  location ~ \.php$ {
    include snippets/fastcgi-php.conf;
    fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
  }
}
```

Visit:

```
https://analytics.yourdomain.com
```

Follow the Matomo UI installer to:
- Create DB
- Create admin user
- Create first site → note **Site ID**

---

## 4. Security & Privacy Hardening (Critical)

### Enable HTTPS Only

- Redirect HTTP → HTTPS

### IP Anonymization

Admin → Privacy → Anonymize IP addresses

### Respect Do-Not-Track

Admin → Privacy → Users opt-out

### Disable Cookies (Optional)

Admin → Privacy → Tracking without cookies

---

## 5. Install React Dependencies

```bash
pnpm add @datapunt/matomo-tracker-react web-vitals
```

---

## 6. Configure Matomo in React

```ts
// src/matomo.ts
import { createInstance } from "@datapunt/matomo-tracker-react";

export const matomo = createInstance({
  urlBase: "https://analytics.yourdomain.com",
  siteId: 1,
  trackerUrl: "https://analytics.yourdomain.com/matomo.php",
  srcUrl: "https://analytics.yourdomain.com/matomo.js",
});
```

---

## 7. Wrap the Application

```tsx
// src/main.tsx
import { MatomoProvider } from "@datapunt/matomo-tracker-react";
import { matomo } from "./matomo";

<MatomoProvider value={matomo}>
  <App />
</MatomoProvider>
```

---

## 8. Track SPA Page Navigation

Matomo does not auto-track SPA routing.

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

Call once in app root.

---

## 9. Track User Interactions

```tsx
trackEvent({
  category: "User Interaction",
  action: "Click",
  name: "Create Order Button",
});
```

### Event Taxonomy (Recommended)

```
Category: User Interaction | Navigation | Session | Performance
Action: Click | Submit | View | Start | End
Name: Component / Feature
```

---

## 10. Track Session Lifecycle

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
      "https://analytics.yourdomain.com/matomo.php",
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

## 11. Track Accurate Time on Page (Heartbeat)

```ts
window._paq = window._paq || [];
window._paq.push(["enableHeartBeatTimer", 15]);
```

This ensures:
- Idle tabs are excluded
- Engagement is accurate

---

## 12. Track Core Web Vitals

```ts
// src/reportWebVitals.ts
import { onCLS, onFID, onLCP, onINP, onTTFB } from "web-vitals";
import { matomo } from "./matomo";

function send(metric: any) {
  matomo.trackEvent({
    category: "Web Vitals",
    action: metric.name,
    value: Math.round(metric.value),
  });
}

onCLS(send);
onFID(send);
onLCP(send);
onINP(send);
onTTFB(send);
```

---

## 13. Verify Data

Check:

- Visitors → Real-Time
- Behavior → Pages
- Behavior → Events
- Engagement → Time on Page

Debug using browser DevTools → Network → `matomo.php`.

---

## 14. Production Best Practices

- Disable tracking in local dev
- Use environment-based configs
- Avoid PII
- Enable log rotation
- Backup database
- Monitor MySQL size growth

---

## 15. Scaling Considerations

| Traffic | Recommendation |
|------|---------------|
| < 100k/day | Single server |
| 100k–1M/day | Separate DB |
| 1M+/day | Queue + Archiving cron |

Use:

```bash
./console core:archive
```

via cron for performance.

---

## 16. Outcome

You now have:

- Fully self-hosted analytics
- SPA-safe tracking
- Web Vitals observability
- Session lifecycle visibility
- Compliance-ready analytics
- No external data leakage

---

## 17. Optional Enhancements

- Custom Matomo plugins
- Feature-level funnels
- Typed analytics SDK
- Internal analytics dashboard
- Data export to warehouse

---

**This setup is suitable for enterprise-grade, privacy-first React applications.**

