---
type: slides
---

# Sorting dataframes

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Sorting

When we load in our data, it is generally ordered in the same way it is
stored. We can easily sort the rows of a dataframe based on its column
values. The verb for that? `.sort_values()`.

As an example, if we wanted to order the cereals based on rating, we
could do the following:

``` python
df.sort_values(by='rating')
```

```out
                         name mfr  calories  shelf  weight  cups     rating
10               Cap'n'Crunch   Q       120      2    1.00  0.75  18.042851
12      Cinnamon Toast Crunch   G       120      2    1.00  0.75  19.823573
35           Honey Graham Ohs   Q       120      2    1.00  1.00  21.871292
18              Count Chocula   G       110      2    1.00  1.00  22.396513
14                Cocoa Puffs   G       110      2    1.00  1.00  22.736446
..                        ...  ..       ...    ...     ...   ...        ...
63             Shredded Wheat   N        80      1    0.83  1.00  68.235885
0                   100% Bran   N        70      3    1.00  0.33  68.402973
65  Shredded Wheat spoon size   N        90      1    1.00  0.67  72.801787
64     Shredded Wheat 'n'Bran   N        90      1    1.00  0.67  74.472949
3   All-Bran with Extra Fiber   K        50      3    1.00  0.50  93.704912

[77 rows x 7 columns]
```

This allows us to see the cereals with lower ratings on the top.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What if we wanted the cereals with a higher rating on the top? Then we
would order them in `descending` order by setting the parameter
`ascending=False`:

``` python
sorted_ratings = df.sort_values(by='rating', ascending=False)
sorted_ratings
```

```out
                         name mfr  calories  shelf  weight  cups     rating
3   All-Bran with Extra Fiber   K        50      3    1.00  0.50  93.704912
64     Shredded Wheat 'n'Bran   N        90      1    1.00  0.67  74.472949
65  Shredded Wheat spoon size   N        90      1    1.00  0.67  72.801787
0                   100% Bran   N        70      3    1.00  0.33  68.402973
63             Shredded Wheat   N        80      1    0.83  1.00  68.235885
..                        ...  ..       ...    ...     ...   ...        ...
14                Cocoa Puffs   G       110      2    1.00  1.00  22.736446
18              Count Chocula   G       110      2    1.00  1.00  22.396513
35           Honey Graham Ohs   Q       120      2    1.00  1.00  21.871292
12      Cinnamon Toast Crunch   G       120      2    1.00  0.75  19.823573
10               Cap'n'Crunch   Q       120      2    1.00  0.75  18.042851

[77 rows x 7 columns]
```

Perfect, now we have the highest rated cereals at the top of the
dataframe.

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
