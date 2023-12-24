# SQL Injection (Advanced).md

This README explains an advanced SQL injection on a member search page. Like basic SQL injection, this exploit reveals database structure and data through crafted inputs. The process starts with `1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns` to identify table fields. Then, it targets the `users` table to extract the `Commentaire` and `countersign` columns using `1 OR 1=1 UNION SELECT Commentaire, countersign from users`.

The found comment instructs to decrypt a password ("FortyTwo"), convert it to lowercase, and hash it using SHA256 to reveal the flag. 

## How to Prevent This

Prevent such SQL injections by sanitizing and validating user inputs on the server side. Use functions provided by frameworks for robust protection against such vulnerabilities. This defense ensures user inputs cannot alter the intended SQL query structure.