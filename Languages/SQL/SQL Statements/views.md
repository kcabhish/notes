# VIEWS

A view is a database object that is essentially a stored query. In PostgreSQL, a view can be accessed as a virtual table. It is called a virtual table because the view does not store data physically in another location. Instead, it stores the query in a way that allows you to execute it as if selecting from an existing table. Essentially, it transforms a complex query that you use repeatedly into a simple call to the view.

- Views allow you to save complex queries as virtual tables for easy reuse.
- Creating a view in PostgreSQL uses the syntax: CREATE VIEW view_name AS <query>.
- Views do not store data physically; they store the query and execute it on demand.
- You can update views using CREATE OR REPLACE VIEW and rename or drop them with ALTER VIEW and DROP VIEW commands.

```SQL
CREATE OR REPLACE VIEW view_name AS SELECT first_name, last_name, address FROM customer INNER JOIN address ON customer.address_id = address.address_id;

ALTER VIEW view_name RENAME to v_info;

DROP VIEW IF EXISTS view_name;
```