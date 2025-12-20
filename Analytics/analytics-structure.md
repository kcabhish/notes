# JSON Structure for Custom Analytics (Matomo-Style)

## 1. Basic Event Schema

``` json
{
  "event": "button_click",
  "timestamp": "2025-12-11T16:20:00Z",
  "session_id": "abc123xyz",
  "user_id": "optional-user-123",
  "page": {
    "url": "https://example.com/dashboard",
    "title": "Dashboard",
    "referrer": "https://example.com/login"
  },
  "device": {
    "type": "desktop",
    "os": "Windows 11",
    "browser": "Chrome 142",
    "screen": "1920x1080"
  },
  "context": {
    "app_version": "1.3.5",
    "environment": "production"
  },
  "properties": {
    "button_id": "save-btn",
    "button_text": "Save Changes"
  }
}
```

------------------------------------------------------------------------

## 2. Page View Event

``` json
{
  "event": "page_view",
  "timestamp": "2025-12-11T16:20:00Z",
  "session_id": "abc123xyz",
  "user_id": "optional-user-123",
  "page": {
    "url": "https://example.com/home",
    "title": "Home Page",
    "load_time_ms": 423
  },
  "device": {
    "browser": "Chrome",
    "os": "Windows",
    "language": "en-US"
  }
}
```

------------------------------------------------------------------------

## 3. Performance Metrics Event

``` json
{
  "event": "performance_metric",
  "timestamp": "2025-12-11T16:25:00Z",
  "session_id": "abc123xyz",
  "page": {
    "url": "https://example.com/home"
  },
  "metrics": {
    "fcp": 1123,
    "lcp": 1840,
    "cls": 0.03,
    "fid": 22
  }
}
```

------------------------------------------------------------------------

## 4. Custom User Interaction Event

``` json
{
  "event": "scroll_depth",
  "timestamp": "2025-12-11T16:22:00Z",
  "session_id": "abc123xyz",
  "page": {
    "url": "https://example.com/blog/post-1"
  },
  "properties": {
    "percentage": 75,
    "scroll_y": 1400
  }
}
```

------------------------------------------------------------------------

## 5. E-commerce Event

``` json
{
  "event": "purchase",
  "timestamp": "2025-12-11T16:30:00Z",
  "user_id": "user-456",
  "order": {
    "order_id": "ORD-1234",
    "total": 128.50,
    "currency": "USD",
    "items": [
      {
        "sku": "SKU-001",
        "name": "Blue T-Shirt",
        "price": 25,
        "qty": 2
      }
    ]
  }
}
```

------------------------------------------------------------------------

## Design Principles

-   Event-based model.
-   Consistent required fields.
-   Modular and extensible context objects.
-   Clean JSON structure compatible with Matomo-like analytics.

------------------------------------------------------------------------

## Recommended SDK Folder Structure

    analytics/
     ├── core/
     │    ├── tracker.ts
     │    ├── session.ts
     │    ├── sender.ts
     ├── events/
     │    ├── pageview.ts
     │    ├── click.ts
     │    ├── performance.ts
     ├── utils/
     │    ├── uuid.ts
     │    ├── device.ts
     └── index.ts
