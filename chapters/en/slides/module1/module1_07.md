---
type: slides
---

# Slicing with Pandas Using .loc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Congratulations on writing your first code\! This is great\! We have
read in our data and know the dimensions. What now? Let’s go over how we
would **index**, **slice** and **select** certain columns or rows of our
data.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Cereal Data

Let’s import pandas and bring in a dataset named `cereal.csv`.

Attribution:  
*“[80 Cereals](https://www.kaggle.com/crawford/80-cereals/)” (c) by
[Chris Crawford](https://www.linkedin.com/in/crawforc3/) is licensed
under [Creative Commons Attribution-ShareAlike 3.0
Unported](http://creativecommons.org/licenses/by-sa/3.0/)*

``` python
import pandas as pd
  
df = pd.read_csv('cereal.csv')
df.head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[5 rows x 16 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## The Index

We can see all the columns and the first 5 rows of the dataframe. Let’s
say we only want certain rows of the whole dataframe or certain columns.

We talked about how `.head()` will generate the first few rows (5 as
default) of a dataframe but what if we wanted rows 5-10?

The first column of this dataframe is called the `index`. Each row has a
label (the index) as well as a position. In this case, the index label
of an observation is the same as it’s position. This doesn’t always have
to be the case. We can assign columns as the index, but we will discuss
this in the next section.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here are the first 10 rows of the dataframe:

``` python
df.head(10)
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

Let’s talk about observation 4 named `Almond Delight`. Its index label
is `4` as well as it’s index position.  
If you just went and counted those again and started screaming “5\! It’s
the fifth position”, that’s ok. In the Python language, we start
counting at position 0 (then 1, 2, 3, and 4 for Almond Delight).

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

So now let’s say we want the 5 rows past `Almond Delight`. That means we
want rows `Apple Cinnamon Cheerios` to `Cap'n'Crunch`.  
The following code cuts the dataframe from “Apple Cinnamon Cheerios” to
“Cap’n’Crunch” keeping all the columns:

``` python
df.loc[5:10]
```

```out
                       name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
5   Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6               Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                   Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                 Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9               Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813
10             Cap'n'Crunch   Q  Cold       120        1    2     220  ...      12      35        25      2    1.00  0.75  18.042851

[6 rows x 16 columns]
```

``` python
df.loc[5:10]
```

This essentially means to *“Obtain the values in the dataframe located
from `5` to `10`.”*

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3"/>

</audio>

</html>

---

What if we only wanted certain columns now?

Perhaps we were only interested in the `calories` to `fiber` columns of
the “Apple Cinnamon Cheerios” to “Cap’n’Crunch” rows? We put our desired
rows first, then columns and separate them with a comma.

``` python
df.loc[5:10, 'calories':'fiber']
```

```out
    calories  protein  fat  sodium  fiber
5        110        2    2     180    1.5
6        110        2    0     125    1.0
7        130        3    2     210    2.0
8         90        2    1     200    4.0
9         90        3    0     210    5.0
10       120        1    2     220    0.0
```

`loc` is used to slice columns and rows by **label** and within an
interval.

The general format to slice both rows and columns together looks like
this:

``` python
`df.loc['row name start':'row name end', 'column name start':'column name end']`
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There is a handy shortcut for slices where you want the begining of a
dataframe to a specified row or column label or a specified row or
column label to the end of a dataframe.

For example if we want all the rows up to “Apple Jacks” which has a
label equal to 6, we could omit the first label in the code all
together:

``` python
df.loc[:6]
```

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

We can do something similar for the end of a dataframe. Let’s say now we
want the first 6 rows and only the columns from ‘sugars’ onwards. we
would omit the ending label this time:

``` python
df.loc[:6, 'sugars':]
```

```out
   sugars  potass  vitamins  shelf  weight  cups     rating
0       6     280        25      3     1.0  0.33  68.402973
1       8     135         0      3     1.0  1.00  33.983679
2       5     320        25      3     1.0  0.33  59.425505
3       0     330        25      3     1.0  0.50  93.704912
4       8       1        25      3     1.0  0.75  34.384843
5      10      70        25      1     1.0  0.75  29.509541
6      14      30        25      2     1.0  1.00  33.174094
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s try it out\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
