# Explanation

On the survey page, users can vote for individuals, assigning points from 1 to 10. The vulnerability is in the dropdown selection for voting:

```html
<select name="valeur" onchange="javascript:this.form.submit();">
	<option value="1">1</option>
	...
	<option value="10">10</option>
</select>
```

An attacker can modify the `value` attribute of the `option` tags to an arbitrary number, manipulating the total points.

# How to Prevent This

To prevent this exploit, the backend should validate the submitted vote values, ensuring they are strictly within 1 to 10. This check avoids the submission of inflated vote counts.