---
type: slides
---

# Obtaining Dataframe Values

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now we know how to get a subset of an existing dataframe but what if we
just want to get a single value from it? For example, what if I wanted
to save the calorie content of `Shredded Wheat` without typing in the
number?

```out
              name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
63  Shredded Wheat   N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83   1.0  68.235885
```

We specify the row we are targeting (63), followed by the column:

``` python
df.loc[63, 'calories']
```

```out
80
```

This displays the value.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What about if we wanted the rating of `Smacks`?

```out
      name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
66  Smacks   K  Cold       110        2    1      70    1.0    9.0      15      40        25      2     1.0  0.75  31.230054
```

``` python
df.loc[66, 'rating']
```

```out
31.230054
```

You will be using this often so let’s make sure we practice this one
right away\!

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
