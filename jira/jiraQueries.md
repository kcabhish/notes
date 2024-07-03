# JQL Cheat Sheet

A simple query in JQL consists of a filed, followed by an operator, followed by one or more values or functions.

```
field operator value
project = TEST
```

Clauses can be linked together with keywords.

```
field operator value keyword field operator function
project = TEST AND assignee in (currentuser())
```


# Jira Queries

Finding issues assigned to users
```
assignee = <username> ORDER BY created DEC

assignee = akc ORDER BY created DEC
```