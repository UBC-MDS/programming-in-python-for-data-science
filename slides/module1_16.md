---
type: slides
---

# Obtaining dataframe Values

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Now we know how to get a subset of an existing dataframe but what if we
just want to get a single value from it? For example, what if I wanted
to save the calorie content of `Shredded Wheat` without typing in the
number?  
We specify the row we are targeting, followed by the column.

``` python
df.loc['Shredded Wheat', 'calories']
```

```out
80
```

This displays the value.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

What about if we wanted the rating of `Smacks`?

``` python
df.loc['Smacks', 'rating']
```

```out
31.230054
```

You will be using this often so let’s make sure we practice this one
right away\!

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
