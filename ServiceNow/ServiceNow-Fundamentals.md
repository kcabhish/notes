# ServiceNow Fundamentals for Experienced Engineers

## 1. Tables and Records
ServiceNow stores data in tables.

- Table = Database table
- Record = Row
- Field = Column

Examples:
- `incident`
- `task`
- `change_request`
- `problem`
- `sys_user`

---

## 2. sys_id (Primary Key)

Every record has a unique `sys_id`.

Example:

```text
46d44f8adb1230101234567890abcd12
```

Key points:
- 32-character unique identifier
- Used internally throughout ServiceNow
- Similar to a primary key in SQL

---

## 3. Reference Fields (Foreign Keys)

Reference fields connect records across tables.

Example:

```text
incident.caller_id -> sys_user
```

Instead of storing a user's name, ServiceNow stores the user's `sys_id`.

Common reference fields:

| Field | References |
|---------|---------|
| caller_id | sys_user |
| assigned_to | sys_user |
| assignment_group | sys_user_group |
| manager | sys_user |

---

## 4. Dot Walking

Dot walking is ServiceNow's equivalent of traversing relationships.

Example:

```javascript
current.assigned_to.email
current.assigned_to.manager.phone
```

Instead of writing joins, developers navigate references using dot notation.

---

## 5. GlideRecord

GlideRecord is the primary API for querying and manipulating data.

### Query Example

```javascript
var gr = new GlideRecord('incident');
gr.addQuery('active', true);
gr.query();

while (gr.next()) {
    gs.info(gr.number);
}
```

### Insert Example

```javascript
var incident = new GlideRecord('incident');
incident.initialize();
incident.short_description = 'Test Incident';
incident.insert();
```

---

## 6. Table Inheritance

Many tables extend parent tables.

```text
task
├── incident
├── problem
├── change_request
└── sc_task
```

Benefits:
- Shared fields
- Shared behaviors
- Reduced duplication

Understanding the Task hierarchy is critical.

---

## 7. Business Rules

Business Rules execute server-side logic when records change.

Execution points:
- Before
- After
- Async
- Display

Example use cases:
- Validation
- Auto-assignment
- Notifications
- Data synchronization

---

## 8. Client Scripts

Client Scripts run in the browser.

Common types:
- onLoad
- onChange
- onSubmit

Typical use cases:
- Field validation
- Dynamic UI behavior
- Conditional field visibility

---

## 9. Script Includes

Reusable server-side JavaScript classes.

Benefits:
- Code reuse
- Better architecture
- Easier testing and maintenance

Comparable to utility or service classes in traditional applications.

---

## 10. Access Controls (ACLs)

ACLs determine who can:

- Read records
- Create records
- Update records
- Delete records

Security is heavily ACL-driven in ServiceNow.

---

## 11. Service Catalog

The Service Catalog provides request workflows.

Common tables:

- sc_request
- sc_req_item
- sc_task

Hierarchy:

```text
Request
 └── Requested Item (RITM)
      └── Catalog Task (SCTASK)
```

---

## 12. Flow Designer

Modern low-code automation platform.

Used for:
- Approvals
- Notifications
- Integrations
- Process automation

Often preferred over legacy Workflow Editor.

---

## 13. CMDB (Configuration Management Database)

Stores infrastructure and application assets.

Examples:
- Servers
- Databases
- Applications
- Network devices

Core table:

```text
cmdb_ci
```

A key concept for ITSM and ITOM implementations.

---

## 14. Update Sets

Used to migrate changes between instances.

Typical flow:

```text
Development
    ↓
Test
    ↓
Production
```

Always understand:
- Captured changes
- Missing changes
- Merge conflicts

---

## 15. REST Integrations

ServiceNow can both expose and consume APIs.

Common APIs:
- Table API
- Import Set API
- Attachment API

Server-side example:

```javascript
var rm = new sn_ws.RESTMessageV2();
```

---

# Recommended Learning Order

1. Tables & Records
2. sys_id
3. Reference Fields
4. Dot Walking
5. GlideRecord
6. Task Table Hierarchy
7. Business Rules
8. Client Scripts
9. Script Includes
10. ACLs
11. Service Catalog
12. Flow Designer
13. CMDB
14. Update Sets
15. REST APIs

Mastering the first six topics will provide the foundation needed for most day-to-day ServiceNow development work.
