# Explanation

The image search page of the website was vulnerable to SQL injection, a common security flaw in web applications. The exploit was executed by injecting the SQL statement `1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns` into the search input. This injection revealed the structure of the database by listing all tables and their columns.

Further exploration was done using `1 OR 1=1 UNION SELECT title, comment FROM list_images`, which extracted data from the 'list_images' table, specifically the 'title' and 'comment' columns. This led to finding a critical comment: "If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46". Decoding this MD5 hash revealed the word "albatroz", which, when processed through SHA256, provided the final flag.

## How to Prevent This

Prevent such SQL injections by sanitizing and validating user inputs on the server side. Use functions provided by frameworks for robust protection against such vulnerabilities. This defense ensures user inputs cannot alter the intended SQL query structure.