# Explanation

The image search page of the website was vulnerable to SQL injection, a common security flaw in web applications. The exploit was executed by injecting the SQL statement `1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns` into the search input. This injection revealed the structure of the database by listing all tables and their columns.

Further exploration was done using `1 OR 1=1 UNION SELECT title, comment FROM list_images`, which extracted data from the 'list_images' table, specifically the 'title' and 'comment' columns. This led to finding a critical comment: "If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46". Decoding this MD5 hash revealed the word "albatroz", which, when processed through SHA256, provided the final flag.

# How to Prevent This

Preventing SQL injections involves securing the backend user input processing. Key practices include:

- **Input Sanitization**: Ensure inputs are properly sanitized to prevent the insertion of malicious SQL code.
- **Use of Prepared Statements**: Implement prepared statements to separate SQL logic from user data.
- **Leverage Framework Security Features**: Many modern frameworks have built-in functions to protect against SQL injections.

By incorporating these security measures, SQL injection vulnerabilities can be significantly reduced.