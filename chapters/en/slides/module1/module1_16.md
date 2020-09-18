---
type: slides
---

# Obtaining dataframe values

Notes: <br>

---

``` python
cereal.loc[[63]]
```

```out
              name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
63  Shredded Wheat   N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83   1.0  68.235885
```

``` python
cereal.loc[63, 'calories']
```

```out
80
```

Notes:

At this point of the module, we now know how to get a subset of an
existing dataframe but what if we just want to get a single value from
it?

For example, what if I wanted to save the calorie content of `Shredded
Wheat` by extracting it from the dataframe and not manually typing in
the number?

To do this we use again our `.loc` notation and we specify the row we
are targeting which is 63, followed by the column, here `calories`. This
goes in the square brackets.

When we do this, it displays the the value contained in the cell, which
in this case, is 80.

---

``` python
cereal.loc[[66]]
```

```out
      name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
66  Smacks   K  Cold       110        2    1      70    1.0    9.0      15      40        25      2     1.0  0.75  31.230054
```

``` python
cereal.loc[66, 'rating']
```

```out
31.230054
```

Notes:

What about if we want the rating of `Smacks` which is located at index
66?

Again we use `.loc[]`, specify the row and the column location separated
by a comma.

So here we write `cereal.loc` and the inside the brackets we write `[66,
'rating']`.

---

# Let’s apply what we learned\!

Notes: <br>
