# Explanation

The exploit involves injecting a script through a Data URI in a `src` parameter. First, write your script, like `<script>alert('toto')</script>`. Then, encode this script into Base64. You can use [Base64 Encode](https://www.base64encode.org) for encoding. The encoded script is placed in a Data URI: `data:text/html;base64,[Encoded Script]`. Finally, inject this Data URI into the `src` parameter of the vulnerable webpage.

# How to Prevent This

Validate and sanitize input parameters to prevent the inclusion of external or encoded scripts. Use backend verification to ensure only intended content is processed.