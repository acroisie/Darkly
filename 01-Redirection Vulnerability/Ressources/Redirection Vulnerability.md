# Explanation

On the homepage, find the link to social media redirects, such as `index.php?page=redirect&site=facebook`. By altering the URL parameter (`site=`), you can redirect to any chosen site. For example, change it to `index.php?page=redirect&site=[malicious-site]`. Sharing this URL can mislead others into visiting a harmful site instead of the intended social media page.

# How to Prevent This

To prevent such vulnerabilities, validate and restrict external URL inputs on the server side. Ensure only legitimate sites like Facebook or Twitter are allowed as redirection targets. This approach prevents attackers from using the website's functionality to redirect users to malicious sites.