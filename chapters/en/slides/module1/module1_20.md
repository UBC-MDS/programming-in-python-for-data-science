---
type: slides
---

# Slicing and selecting using .iloc\[\]

Notes: <br>

---

## Slicing Dataframe

``` python
cereal = pd.read_csv('cereal.csv')
cereal.head(10)
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3    1.00  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3    1.00  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3    1.00  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3    1.00  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3    1.00  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6                Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                    Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                  Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9                Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813

[10 rows x 16 columns]
```

Notes:

Up to this point, we have been manipulating our dataframe with column
and row ***labels*** using `.loc[]`.

Slicing can also be done by the location position of each row with
`.iloc[]`.

`.iloc[]` is very similar, however, the “i” in `iloc` refers to the
index ***integer*** position.

We are going to return to our cereal dataset and take a look at the
first 10 rows.

Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` but
we want to slice based on their position.

Using Python’s counting method of starting at zero, we conclude
`All-Bran` to be at position to 2.

We get `Apple Cinnamon Cheerios` position to be 5 in the same way.

We are lucky with this dataframe because our index labels match the
position of the rows.

---

``` python
cereal.loc[2:5]
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1     1.0  0.75  29.509541

[4 rows x 16 columns]
```

``` python
cereal.iloc[2:5]
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[3 rows x 16 columns]
```

Notes:

We can use the same coding structure we learned with `.loc[]` but this
time using row positions instead of labels with `.iloc[]`.

But wait\! Something is missing here\!

Why doesn’t `Apple Cinnamon Cheerios` appear in the dataframe?

---

``` python
cereal.iloc[2:6]
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1     1.0  0.75  29.509541

[4 rows x 16 columns]
```

Notes:

That’s because when we use slicing by index position, it will take all
the indices including the lower bound but *EXCLUDING* the upper bound.

If we wanted to include `Apple Cinnamon Cheerios` we would have to go 1
index position further.

If we think about this a bit it actually make some sense. Think about
the calculation `6 - 2 = 4` . We get 4 items remaining which is the
amount of cereals we want in our in new dataframe.

---

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[5 rows x 16 columns]
```

``` python
cereal.iloc[:, 0:6]
```

```out
                         name mfr  type  calories  protein  fat
0                   100% Bran   N  Cold        70        4    1
1           100% Natural Bran   Q  Cold       120        3    5
2                    All-Bran   K  Cold        70        4    1
3   All-Bran with Extra Fiber   K  Cold        50        4    0
4              Almond Delight   R  Cold       110        2    2
..                        ...  ..   ...       ...      ...  ...
72                    Triples   G  Cold       110        2    1
73                       Trix   G  Cold       110        1    1
74                 Wheat Chex   R  Cold       100        3    1
75                   Wheaties   G  Cold       100        3    1
76        Wheaties Honey Gold   G  Cold       110        2    1

[77 rows x 6 columns]
```

Notes:

The same concept can be applied to the columns of the dataframe.

Let’s say we want all the rows but we only want the columns starting at
`name` and ending (and including) at column `fat`.  
Using the logic we learned in the last set of slides, we would use the
following code:

We would need to specify all rows using `:` as we did when we used
`.loc[]`.

The column `name` is at index position 0 (we do not include the index
label as a column) and `fat` is at index position 5.

Since we want to include the 5th column we need to use the 6th position
to make sure we get all the columns *BEFORE* the upper bound.

---

Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` and
`protein` to `fat`.

#### Rows

**Lower Bound**: `All-Bran` located at position 2.  
**Upper Bound**:`Apple Cinnamon Cheerios` is located at position 5.

#### Columns

**Lower Bound**: `protein` is located at position 4.  
**Upper Bound**:`fat` is located at position 5.

``` python
cereal.iloc[2:6, 0:6]
```

```out
                        name mfr  type  calories  protein  fat
2                   All-Bran   K  Cold        70        4    1
3  All-Bran with Extra Fiber   K  Cold        50        4    0
4             Almond Delight   R  Cold       110        2    2
5    Apple Cinnamon Cheerios   G  Cold       110        2    2
```

Notes:

Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` and
`protein` to `fat`.

For rows, the lower bound `All-Bran` is located at position 2 and the
upper bound `Apple Cinnamon Cheerios` is located at position 5.

Now the column’s lower Bound `protein` is located at position 4 and the
upper bound `fat` is located at position 5.

The same would apply if we only wanted certain rows with certain
columns.

Both of our upper bound have been compensated with + 1 to make sure they
are included in the new dataframe.

---

``` python
cereal.head(3)
```

```out
                name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2           All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505

[3 rows x 16 columns]
```

``` python
cereal.iloc[0:3]
```

```out
                name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2           All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505

[3 rows x 16 columns]
```

``` python
cereal.iloc[:3]
```

```out
                name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2           All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505

[3 rows x 16 columns]
```

Notes:

There are multiple different way of writing code when you are selecting
items from the beginning or end of your data.

Perhaps you only want the first 3 rows of your data.

We can use `.head(3)` or we can use `.iloc()`.

Since we are indicating the beginning of the dataframe, we can omit the
upper bound `0` just like we did we we learned slicing with `.loc[]`.

---

``` python
cereal.iloc[74:77]
```

```out
                   name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
74           Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75             Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76  Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[3 rows x 16 columns]
```

``` python
cereal.iloc[-3:]
```

```out
                   name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
74           Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75             Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76  Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[3 rows x 16 columns]
```

Notes:

The same logic can be applied for end of a dataframe. This time we want
the last 3 rows.

Since this dataframe has 76 rows we could use our lower bound as 74 and
upper bound as 77 (76 +1).

A better and easier way to write this, where you don’t even need to know
the number of rows in the dataframe would be to specify you are counting
your rows from the bottom with a negative in front of the number of rows
you want.

This example takes the first 3 rows of the **bottom** of the dataframe.
since we are collecting data to the end of the dataframe, we do not need
to include the ending row index number.

---

## Selecting with .iloc\[\]

``` python
cereal.head(10)
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3    1.00  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3    1.00  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3    1.00  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3    1.00  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3    1.00  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6                Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                    Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                  Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9                Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813

[10 rows x 16 columns]
```

<div>

<table id="**Rows**" style="width:50%; float:left">

<tr>

<td>

| **Row**          | **Row Position** |
| ---------------- | ---------------- |
| `Almond Delight` | Position 4       |
| `Basic 4`        | Position 7       |
| `Apple Jacks`    | Position 6       |

</td>

</tr>

</table>

<table id="**Columns**" style="width:50%; float:left">

<tr>

<td>

| **Columns** | **Column Position** |
| ----------- | ------------------- |
| `name`      | Position 0          |
| `calories`  | Position 3          |
| `fat`       | Position 5          |
| `type`      | Position 2          |

</td>

</tr>

</table>

</div>

Notes:

Selecting using `iloc` is done identically to `loc`, however, the items
within each set of square brackets **MUST** be integers, and not in
quotation marks.

Let’s say we want the rows `Almond Delight`, `Basic 4` and `Apple Jacks`
with the columns `name`, `calories`, `fat` and `type` *in that order*.

---

<table id="**Rows**" style="width:50%; float:left">

<tr>

<td>

| **Row**          | **Row Position** |
| ---------------- | ---------------- |
| `Almond Delight` | Position 4       |
| `Basic 4`        | Position 7       |
| `Apple Jacks`    | Position 6       |

</td>

</tr>

</table>

<table id="**Columns**" style="width:50%; float:left">

<tr>

<td>

| **Columns** | **Column Position** |
| ----------- | ------------------- |
| `name`      | Position 0          |
| `calories`  | Position 3          |
| `fat`       | Position 5          |
| `type`      | Position 2          |

</td>

</tr>

</table>

<br> <br> <br> <br> <br> <br> <br> <br> <br>

``` python
cereal.iloc[[4, 7, 6], [0, 3, 5, 2]]
```

```out
             name  calories  fat  type
4  Almond Delight       110    2  Cold
7         Basic 4       130    2  Cold
6     Apple Jacks       110    0  Cold
```

Notes:

`Almond Delight` takes row position 4, `Basic 4` takes row position 7
and `Apple Jacks` is located at position 6. The desired columns `name`,
`calories`, `fat`, and `type` take column index positions 0,5,3, and 2
respectively.

Now let’s put those position into square backing within `df.iloc[]`.

---

# Nice work\! Let’s apply what we learned\!

Notes:

<br>
