---
type: slides
---

# Selecting using .loc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Unordered Indexing

We have our trusty `cereal.csv` data once again.

```out
                         name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
..                        ...  ..   ...       ...      ...  ...     ...  ...     ...     ...       ...    ...     ...   ...        ...
72                    Triples   G  Cold       110        2    1     250  ...       3      60        25      3     1.0  0.75  39.106174
73                       Trix   G  Cold       110        1    1     140  ...      12      25        25      2     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75                   Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[77 rows x 16 columns]
```

What would we do if we want to select columns and rows that don’t fall
consecutively or if we want to rearrange them?

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s say we wanted only the rows labeled `Clusters` (13), `Trix` (73)
and `Wheaties` (75) and the columns `name`, `type`, `sugars` and
`rating`. How would we obtain them now?

We need to specify each column and row label that we want between square
brackets `[]`, separated with commas:

``` python
df.loc[[13,73,75], ['name', 'type', 'sugars', 'rating']]
```

```out
        name  type  sugars     rating
13  Clusters  Cold       7  40.400208
73      Trix  Cold      12  27.753301
75  Wheaties  Cold       3  51.592193
```

We can also reorder the entries to change the column and row order.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What if we wanted the rows to be in the order `Wheaties`, `Trix` and
`Clusters` and columns in the order `name`, `type`, `rating` and
`sugars` How would we obtain that?  
It’s as simple as rearranging the order you target your rows and
columns:

``` python
df.loc[[75, 73, 13], ['name', 'type', 'rating', 'sugars']]
```

```out
        name  type     rating  sugars
75  Wheaties  Cold  51.592193       3
73      Trix  Cold  27.753301      12
13  Clusters  Cold  40.400208       7
```

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
