# Explanation

If you're on the home page, click on 'Sign in,' and then select 'I forgot my password.'

You'll be taken to the password recovery page (/?page=recover).

By looking at the page's code, you'll find a form connected to the 'SUBMIT' button:
```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```
Inside this form, there's a hidden field containing the email address for password recovery.

This means you can change the email address by modifying the input value. Afterward, simply click the 'SUBMIT' button to reveal the flag.

# How to prevent this?

The best way to avoid such issues is to handle sensitive information on the backend of the system, rather than in the front-end code.