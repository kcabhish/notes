# Conditional Expressions and Procedures

## CASE

General CASE Statement Syntax
There are two main ways to use a CASE statement: the general CASE statement and the CASE expression. In many situations, both methods can retrieve the same results. The general CASE statement uses the following syntax:

- Start with the CASE keyword.
- Use WHEN to specify a condition, followed by THEN to specify the result.
- You can list multiple WHEN ... THEN ... pairs.
- Use ELSE for a default result if none of the conditions are met.
- End with END.

```SQL
SELECT a,
CASE
  WHEN a = 1 THEN 1
  WHEN a = 2 THEN 2
  ELSE 'other'
END AS label
FROM test;
```

## COALESCE

The COALESCE function accespts an unlimited number of arguements and returns the first argument that is not null.
```
SELECT COALESCE(1, 2); // returns 1
SELECT COALESCE(NULL, 2, 3); // returns 2
```

Using COALESCE to Handle Null Discounts
You can use COALESCE to fill in values for nulls without affecting the original table. Instead of just subtracting the discount column, use:

```SQL
SELECT item, price - COALESCE(discount, 0) AS final_price FROM table;
```
SQL first checks if the discount is a non-null value. If it is, it returns that number. If the discount is null, it continues to the next value, which is zero. It is common to use these two values in a COALESCE function to substitute a default value when a column is null.

## NULLIF

The NULLIF function takes two inputs and returns null if both inputs are equal; otherwise, it returns the first argument passed.

The syntax is NULLIF(arg1, arg2). For example, if you pass in 10 and 10 to NULLIF, since both are equal, it returns null. However, if you pass in 10 and 12, since they are not equal, it returns 10.

This function is very useful in cases where a null value would prevent errors or unwanted results.