# SQL injection UNION attack
- When an application is vulnerable to an SQL injection, and the result of the query are returned within the application's responses, attacker use the `UNION` keyword to retrieve data from other tables in the database
```sql
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```
- The SQL query returns a single result set with two columns, `a` and `b`, from `table1` and `c` and `d` from `table2`

- For `UNION` query to work, two key requirements must be met:
  1. The number of columns in the two `SELECT` statements must be the same
  2. The data types in each column must be compatible between the two `SELECT` statements

- To carry out an SQL injection `UNION` attack, make sure these two requirements.
    - How mny columns are being returned by the original query
    - Which columns returned from the original query are of a suitable data type to hold the results from the injected query

