# Subverting application logic

- If a user submits the username and password as 'username' and 'password' respectively, the application will check the credentials by performing the following SQL query:

```sql
SELECT * FROM users WHERE username = 'username' AND password = 'password'
```

- In this case, attacker can bypass the login mechanism by submitting the following input:

```sql
username: ' OR 1=1 --
```
for eg: submitting the username `administrator'--` will bypass the login mechanism and log in as the administrator.

-------

# Lab: SQL injection vulnerability allowing login bypass

### SQL injection -> Login function

### To solve: perform a SQL injection attack that logs in to the application as the `administrator` user.

## Analysis:
******************
- When `'` was used in the username and any password, the login directed to the `internal server error` page. This indicates that the username input is vulnerable to SQL injection as it does something in the backend that broke the application.

```sql
SELECT firstname FROM users WHERE username = ''' AND password = 'admin'
```
as internal server error is because of the extra `'` in the query.


- Taking above into consideration, the sql query might be something like this:
```sql
SELECT firstname FROM users WHERE username = 'admin' AND password = 'admin'
```
- The backend code might check like this and password are not stored in text there might be some kind of the encoding technique used to store the password.

- Now, what we try to do is bypass the login using sql injection in username field and ignore the password field.

-let's modify the query to bypass the login mechanism.
```sql
SELECT firstname FROM users WHERE username = 'administrator'--' AND password = 'can be anything here'
```

- The above query will bypass the login mechanism by using the payload `administrator'--` in the username field.

- Now, let's try to login with the username `administrator'--` and any password. We bypass the login system.



