# SELECT Statements

## SELECT

```SQL
SELECT column_name FROM table_name
SELECT column_name1, column_name2 FROM table_name
SELECT * FROM table_name
```

In general it is not a good practise to use an asterisk(*) in the SELECT statement if you don't really need all columns. It will automatically query everyting, which increases traffic between the  database server and the application, which can slow down the retrieval of results.

## SELECT DISTINCT

```SQL
SELECT DISTINCT column_name FROM table_name
SELECT DISTINCT (column_name) FROM table_name
```

## COUNT

- The COUNT function returns the number of input rows that match a specific condition of a query.
- We can apply COUNT on a specific column or just pass COUNT(*).

```SQL
SELECT COUNT (column_name) FROM table_name
SELECT COUNT (DISTINCT (column_name)) FROM table_name
```

## WHERE

- The WHERE clause appears immediately after the FROM clause of the SELECT statement.
- The conditions are used to filter the rows returned from the SELECT statement.

```SQL
SELECT * FROM table_name WHERE conditions
```

### Comparison Operators

```
=   -- Equal to
>   -- Greater than
<   -- Less than
>=  -- Greater than or equal to
<=  -- Less than or equal to
<>  -- Not equal to (alternative)
!=  -- Not equal to (common)
```

### Logical Operators

```
AND   -- Both conditions must be true
OR    -- At least one condition must be true
NOT   -- The condition must not be true
```

### example

The example query below will return all the rows where with all the male who are above the age of 30.

```SQL
SELECT * FROM customers_table WHERE gender = 'M' AND age > 30;
```

## ORDER BY

- Use ORDER BY to sort rows based on a column value, in either ascending or descending order.
- Order of preferance for the columns for the `ORDER BY` caluse is left to right.

```SQL
SELECT column1, column2 FROM table_name ORDER BY column2 ASC;
SELECT column1, column2 FROM table_name ORDER BY column2 DESC;
SELECT column1, column2 FROM table_name ORDER BY column1, column2 DESC;
```

## LIMIT

- The LIMIT command allows us to limit the number of rows returned for a query.
- LIMIT also becomes extremely useful in combination with the ORDER BY statement. LIMIT goes at the very bottom end of a query request and is the last command to be executed. After filtering with the WHERE statement, ordering with ORDER BY, and applying any other conditions, LIMIT specifies how many rows you want at the end.

```SQL
SELECT * FROM customers_table WHERE gender = 'M' AND age > 30 LIMIT 5;
```

## BETWEEN

The BETWEEN operator can be used to match a value against a range of values. For example, we can ask where a value is between a low and a high. This essentially acts as a condition you can attach to a WHERE statement.

```SQL
SELECT * FROM payment WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-15';
```
## IN
Instead of writing several OR statements such as Name = 'David' OR Name = 'Claire' OR Name = 'Zach', the IN operator allows the creation of a condition that quickly checks if a value is included in a list of multiple options.

```SQL
SELECT * FROM customers WHERE name IN ('David', 'Claire','Zach')
```

## LIKE and ILIKE

```SQL
SELECT title from movies WHERE title LIKE 'ROCKY _';
SELECT title from movies WHERE title LIKE 'R%';
```

### WILD CARDS
`%` can be placed in string to match any 1 or more characters.
`_` can be placed in string to match any single characters.