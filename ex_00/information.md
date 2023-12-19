# Explanation

From the home page, click on 'Sign in,' then 'I forgot my password.'

You will then be taken to the password recovery page (/?page=recover).

By inspecting the page's source code, you can see the form related to the 'SUBMIT' button:
```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```
It contains a hidden field with the email address for password recovery.

This allows us to redirect the email by changing the input value, and then simply clicking the 'SUBMIT' button to display the flag.

# How to prevent this?

Simply manage this kind of information on the backend.
