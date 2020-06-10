---
type: slides
---

# Slicing and selecting using .iloc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Slicing Dataframe

Up to this point, we have been manipulating our dataframe with column
and row ***labels*** using `.loc[]`.  
Slicing can also be done by the location position of each row with
`.iloc[]`. `.iloc[]` is very similar, however, the “i” in `iloc` refers
to the index ***integer*** position.

We are going to return to our cereal dataset and take a look at the
first 15 rows.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
df = pd.read_csv('cereal.csv')
df.head(15)
```

```out
                         name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3    1.00  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3    1.00  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3    1.00  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3    1.00  0.75  34.384843
5     Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6                 Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                     Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                   Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9                 Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813
10               Cap'n'Crunch   Q  Cold       120        1    2     220  ...      12      35        25      2    1.00  0.75  18.042851
11                   Cheerios   G  Cold       110        6    2     290  ...       1     105        25      1    1.00  1.25  50.764999
12      Cinnamon Toast Crunch   G  Cold       120        1    3     210  ...       9      45        25      2    1.00  0.75  19.823573
13                   Clusters   G  Cold       110        3    2     140  ...       7     105        25      3    1.00  0.50  40.400208
14                Cocoa Puffs   G  Cold       110        1    1     180  ...      13      55        25      2    1.00  1.00  22.736446

[15 rows x 16 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` but
we want to slice based on their position.  
Using Python’s counting method of starting at zero, we conclude
`All-Bran` to be at position to 2.

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1     1.0  0.75  29.509541
6                Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2     1.0  1.00  33.174094

[7 rows x 16 columns]
```

We get `Apple Cinnamon Cheerios` position to be 5 in the same way.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can use the same coding structure we learned with `.loc[]`, but this
time using row positions instead of labels with `.iloc[]`

``` python
df.iloc[2:5]
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[3 rows x 16 columns]
```

But wait\! Something is missing here\!

Why doesn’t `Apple Cinnamon Cheerios` appear in the dataframe?

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

That’s because when we use slicing by index position, it will take all
the indices including the lower bound but *EXCLUDING* the upper bound.
If we wanted to include `Apple Cinnamon Cheerios` we would have to go 1
index position further.

``` python
df.iloc[2:6]
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1     1.0  0.75  29.509541

[4 rows x 16 columns]
```

If we think about this a bit it actually make some sense. Think about
the calculation `6 - 2 = 4` . We get 4 items remaining which is the
amount of cereals we want in our in new dataframe.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The same concept can be appled to the columns of the dataframe. Let’s
say we want all the rows but we only want the columns starting at `name`
and ending (including) at column `sugars`.  
Using the logic we learned in the last set of slides, we would use the
following code:

``` python
df.iloc[:, 0:10]
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...
72                    Triples   G  Cold       110        2    1     250    0.0   21.0       3
73                       Trix   G  Cold       110        1    1     140    0.0   13.0      12
74                 Wheat Chex   R  Cold       100        3    1     230    3.0   17.0       3
75                   Wheaties   G  Cold       100        3    1     200    3.0   17.0       3
76        Wheaties Honey Gold   G  Cold       110        2    1     200    1.0   16.0       8

[77 rows x 10 columns]
```

We would need to specify all rows using `:` as we did when we used
`.loc[]`. The column `name` is at index position 0 (we do not include
the index label as a column) and `sugars` is at index position 9. Since
we want to include the 9th column we need to use the 10th position to
make sure we get all the columns *BEFORE* the upper bound.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The same would apply if we only wanted certain rows with certain
columns. Let’s say we want the rows `All-Bran` to `Apple Cinnamon
Cheerios` and `protein` to `sugars`.  
**Rows**  
`All-Bran` located at position 2.  
`Apple Cinnamon Cheerios` is located at position 5.  
**Columns**  
`protein` is located at position 4.  
`sugar` is located at position 9.

``` python
df.iloc[2:6, 0:10]
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10
```

Both of our upper bound have been compensated with + 1 to make sure they
are included in the new dataframe.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There are multiple different syntaxes you may want to use when you are
selecting items from the begining or end of your data. Perhaps you only
want the first 3 rows of your data. We can use `.head(3)` or we can use
`.iloc()`. Normally you would this syntax if using the latter:

``` python
df.iloc[0:3]
```

```out
                name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2           All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505

[3 rows x 16 columns]
```

However, if we are indicating the begining of the dataframe we can omit
the `0` just like we learned using `.loc[]`

``` python
df.iloc[:3]
```

```out
                name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2           All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505

[3 rows x 16 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can do something similar for end of a dataframe. This time we want
the last 3 rows.

Instead of writing this:

``` python
df.iloc[74:77]
```

```out
                   name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
74           Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75             Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76  Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[3 rows x 16 columns]
```

We can specify a negative number which indicates that we are counting
from the other end of the data. Since we are collecting data to the end
of the dataframe, we do not need to include the ending row index number.

``` python
df.iloc[-3:]
```

```out
                   name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
74           Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75             Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76  Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[3 rows x 16 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Selecting with .iloc\[\]

Selecting using `iloc` is done identically to `loc`, however, the items
within each set of square brackets **MUST** be integers, and not in
quotation marks.

Let’s say we want the rows `Cheerios`, `Basic 4` and `Apple Jacks` with
the columns `name`, `rating`, `fat` and `type` *in that order*.

**Rows**  
`Cheerios` is located at position 11.  
`Basic 4` is located at position 7.  
`Apple Jacks` is located at position 6.

**Columns**  
`name` is located at position 0 `rating` is located at position 15.  
`fat` is located at position 5.  
`type` is located at position 2.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Now let’s put those position into square backing within `df.iloc[]`

Recap the locations: Rows: `Cheerios` = 11, `Basic 4` = 7 and `Apple
Jacks` = 6 Columns: `name` = 0, `rating` = 15, `fat` = 5 and `type` = 2.

``` python
df.iloc[[11, 7, 6], [0, 15, 5, 2]]
```

```out
           name     rating  fat  type
11     Cheerios  50.764999    2  Cold
7       Basic 4  37.038562    2  Cold
6   Apple Jacks  33.174094    0  Cold
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Nice work\! Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
