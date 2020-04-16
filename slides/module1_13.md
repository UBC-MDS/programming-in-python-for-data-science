---
type: slides
---

# Selecting using df.loc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Unordered Indexing

We have our trusty `cereal.csv` data again with the cereal names as the
index
    labels.

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Triples                     G  Cold       110        2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
Trix                        G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
Wheat Chex                  R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
Wheaties                    G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
Wheaties Honey Gold         G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 15 columns]
```

What would we do if we want to select columns and rows that don’t fall
consecutively or if we want to rearrange them?

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Let’s say we wanted only the rows labeled `Clusters`, `Trix` and
`Wheaties` and the columns `type`, `sugars` and `rating` How would we
obtain them now?

We need to specify each column and row label that we want between square
brackets `[]`, separated with
commas.

``` python
df.loc[ ['Clusters', 'Trix', 'Wheaties'] , ['type', 'sugars', 'rating'] ]
```

```out
          type  sugars     rating
name                             
Clusters  Cold       7  40.400208
Trix      Cold      12  27.753301
Wheaties  Cold       3  51.592193
```

We can also reorder it to change the column and row order.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

What if we wanted the rows to be in the order `Wheaties`, `Trix` and
`Clusters` and columns in the order `type`, `rating` and `sugars` How
would we obtain that?  
It’s as simple as rearranging the order you target your rows and
columns\!

``` python
df.loc[ ['Wheaties', 'Trix', 'Clusters'] , ['type', 'rating', 'sugars'] ]
```

```out
          type     rating  sugars
name                             
Wheaties  Cold  51.592193       3
Trix      Cold  27.753301      12
Clusters  Cold  40.400208       7
```

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
