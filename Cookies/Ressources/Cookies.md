# Explanation

Examine the browser cookies, specifically the "I_am_admin" field with its MD5 value. Decrypt this value using [md5decrypt.net](https://md5decrypt.net). The MD5 hash "68934a3e9455fa72420237eb05902327" translates to "false". Exploit this by encrypting "true" into MD5 ("b326b5062b2f0e69046810717534cb09") and updating the cookie. Reload the website to access admin privileges and obtain the flag.

# Patch

Do not trust cookie contents for sensitive operations. Avoid MD5 for encryption; instead, use stronger algorithms like bcrypt for better security.