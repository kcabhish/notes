# ADVANCEED SQL

## TIME

PostgreSQL can hold date and time information:
- TIME - contains only time
- DATE - contains only date
- TIMESTAMP - contains date and time
- TIMESTAMPTZ - contains date, time and timezone

### Functions and Operations related to specific data types:

- TIMEZONE
- NOW
- TIMEOFDAY
- CURRENT_TIME
- CURRNT_DATE

### Show Command

In PostgreSQL, the SHOW command is used to display the current value of a runtime parameter (i.e., a server configuration setting).
Some examples:

```SQL
SHOW ALL;
SHOW TIMEZONE;
SHOW search_path;
SHOW client_encoding;
```

### SQL Functions

```SQL
SELECT NOW();
SELECT TIMEOFDAY();
```

#### Extract()

Allows user to "extract" or obtaing a sub-component of a date value. The following information can be extracted from the date column.

- YEAR
- MONTH
- DAY
- WEEK
- QUARTER

- Extract (YEAR FROM date_col)

#### [TO_CHAR()](https://www.postgresql.org/docs/current/functions-formatting.html#FUNCTIONS-FORMATTING)

```
SELECT TO_CHAR(payment_date, 'mm-dd-yyyy') FROM payment;
```

#### String Concatination

```SQL
SELECT LEFT(first_name,1) || ' ' || last_name as full_name from customer;
```

### SUB QUERY

- A sub query allows you to construct complex queries, essentially performing a query on the results of another query.
- The syntax is staraightforward and involves two SELECT statements.

```SQL
SELECT student, grade FROM test_scores WHERE grade > (SELECT AVG(grade) FROM test_scores);
```

If the sub query returns more than on result, the following example can be used:

```SQL
SELECT student, grade FROM test_scores WHERE student IN (SELECT student_name FROM honor_roll);
```

#### Key Takeaways
- Subqueries allow for more complex SQL queries by enabling queries within queries.
- The IN operator is used with subqueries that return multiple results, while comparison operators are used when a subquery returns a single value.
- The EXISTS operator checks for the existence of rows returned by a subquery and is useful for filtering results based on related data.
- Subqueries can be used in conjunction with joins and other SQL operations to dynamically filter and retrieve data.

## SELF-JOIN

A self join can be viewed as a join of two copies of the same table. The table is not actually copied internally, but SQL performs the command as though it were. There is no special keyword for a self join; it uses the same syntax as a standard join, with the same table appearing in both parts. When using a self join, it is necessary to use an alias for the table to avoid ambiguity.

```SQL
SELECT tableA.column, tableB.column FROM table AS tableA JOIN table AS tableB ON tableA.some_column = tableB.some_other_column
```