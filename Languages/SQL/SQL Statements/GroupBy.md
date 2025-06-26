# GROUP BY STATEMENTS

## Aggregation Functions In SQL

SQL provides a variety of aggregate functions, and PostgreSQL is no exception. All the functions discussed here are available in any major SQL engine. The main idea behind an aggregate function is to take multiple inputs and return a single output.

PostgreSQL provides many different types of aggregate functions. You can check out the official documentation page for more details. In this lecture, we will discuss the most common aggregation functions.

### Common Aggregate Functions
The most common aggregate functions are:
```
AVG: Returns the average or mean value.
COUNT: Returns the number of values or rows returned.
MAX: Returns the maximum value.
MIN: Returns the minimum value.
SUM: Returns the sum of all the values in a column.
```

#### Example

```SQL
SELECT AVG(replacement_cost) FROM film;
SELECT ROUND(AVG(replacement_cost), 2) FROM film;
SELECT COUNT(*) FROM film;
SELECT MIN (column) FROM table_name;
SELECT MAX (column) FROM table_name;
SELECT SUM(replacement_cost) FROM film;
```

## GROUP BY

GROUP BY allows aggregation of columns per some category.

```SQL
SELECT category_column, AG(data_column)
FROM table
GROUP BY category_column
```

### Example

```SQL
SELECT customer_id, SUM(amount) as total FROM payment GROUP BY customer_id ORDER BY total DESC;
```

## HAVING

The HAVING clause allows us to filter after an aggregation has already taken place. It comes after a GROUP BY call.

```SQL
SELECT company, SUM(sales)
FROM financial_table
GROUP BY company
HAVING SUM(sales) > 1000;
```