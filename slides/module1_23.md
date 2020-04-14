---
type: slides
---

# Sorting Dataframes

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Sorting

When we load in our data, it is generally ordered in the same way it is
stored. We can easily sort the rows of a dataframe based on its column
values. The verb for that? `df.sort_values()`.

As an example, if we wanted to order the cereals based on rating, we
could do the
    following:

``` python
df.sort_values(by='rating')
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
Cap'n'Crunch                Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
Cinnamon Toast Crunch       G  Cold       120        1    3     210    0.0   13.0       9      45        25      2    1.00  0.75  19.823573
Honey Graham Ohs            Q  Cold       120        1    2     220    1.0   12.0      11      45        25      2    1.00  1.00  21.871292
Count Chocula               G  Cold       110        1    1     180    0.0   12.0      13      65        25      2    1.00  1.00  22.396513
Cocoa Puffs                 G  Cold       110        1    1     180    0.0   12.0      13      55        25      2    1.00  1.00  22.736446
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Shredded Wheat              N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83  1.00  68.235885
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3    1.00  0.33  68.402973
Shredded Wheat spoon size   N  Cold        90        3    0       0    3.0   20.0       0     120         0      1    1.00  0.67  72.801787
Shredded Wheat 'n'Bran      N  Cold        90        3    0       0    4.0   19.0       0     140         0      1    1.00  0.67  74.472949
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912

[77 rows x 15 columns]
```

This allows us to see the cereals with lower ratings on the top.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

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
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
Shredded Wheat 'n'Bran      N  Cold        90        3    0       0    4.0   19.0       0     140         0      1    1.00  0.67  74.472949
Shredded Wheat spoon size   N  Cold        90        3    0       0    3.0   20.0       0     120         0      1    1.00  0.67  72.801787
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3    1.00  0.33  68.402973
Shredded Wheat              N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83  1.00  68.235885
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Cocoa Puffs                 G  Cold       110        1    1     180    0.0   12.0      13      55        25      2    1.00  1.00  22.736446
Count Chocula               G  Cold       110        1    1     180    0.0   12.0      13      65        25      2    1.00  1.00  22.396513
Honey Graham Ohs            Q  Cold       120        1    2     220    1.0   12.0      11      45        25      2    1.00  1.00  21.871292
Cinnamon Toast Crunch       G  Cold       120        1    3     210    0.0   13.0       9      45        25      2    1.00  0.75  19.823573
Cap'n'Crunch                Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851

[77 rows x 15 columns]
```

Perfect, now we have the highest rated cereals at the top of the
dataframe.

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
