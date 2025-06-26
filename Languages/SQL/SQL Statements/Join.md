# SQL JOIN

[join SQL wiki](https://en.wikipedia.org/wiki/Join_(SQL))

[sql joins with venn diagrams](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)

A join operation allows us to combine multiple tables together. The main reason for different join types is to decide how to handle information present only in one of the joined tables.

## INNER JOIN | JOIN

- An inner join results in the set of records that match in both tables.
- An inner join will join these tables together for records that are a match in both tables.
```SQL
SELECT * FROM tableA INNER JOIN tableB ON tableA.column = tableB.column
SELECT * FROM tableA JOIN tableB ON tableA.column = tableB.column
```
The above two querry are the same, if `JOIN` is used it defaults to `INNER JOIN`.

## FULL OUTER JOIN

Outer joins allow us to specify how to handle values present in only one of the tables being joined. These joins are more complex than the simpler inner join, which only grabs rows present in both tables. It is important to take your time understanding these outer joins, especially when discussing left and right outer joins.
```
- Full outer joins return all rows from both tables, filling in NULLs where there is no match.
- The order of tables in a full outer join does not matter due to its symmetrical nature.
- Adding a WHERE clause with NULL checks after a full outer join allows you to find rows unique to either table.
- Full outer joins are useful for data validation, such as ensuring all payments are linked to customers and vice versa.
```

Example for full outer join:

```SQL
SELECT * FROM tableA FULL OUTER JOIN tableB ON tableA.column = tableB.column
```

Example for Unique rows to the tables:

```SQL
SELECT * FROM registrations FULL OUTER JOIN logins ON registrations.name = logins.name WHERE registrations.reg_id IS NULL OR logins.login_id IS NULL
```

## LEFT OUTER JOIN

 A left outer join results in the set of records that are in the left table. If there is no match with the right table, then those results are filled with NULL values.

```SQL
SELECT * FROM tableA LEFT OUTER JOIN tableB ON tableA.col_match = tableB.col_match
```

## UNION

- The union operator combines the results of two or more select statements by concatenating them vertically.
- Union requires the select statements to have compatible columns so their results can be stacked.
- Unlike joins, union simply pastes the results of queries on top of each other without merging rows.
- Multiple union calls can be chained, and the combined results can be ordered using an ORDER BY clause.