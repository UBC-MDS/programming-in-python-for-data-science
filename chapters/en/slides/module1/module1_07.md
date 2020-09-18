---
type: slides
---

# Slicing Rows using .loc\[\]

Notes:

<br>

---

## Cereal Data

``` python
import pandas as pd
  
cereal = pd.read_csv('cereal.csv')
cereal.head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

Attribution:  
*“[80 Cereals](https://www.kaggle.com/crawford/80-cereals/)” (c) by
[Chris Crawford](https://www.linkedin.com/in/crawforc3/) is licensed
under [Creative Commons Attribution-ShareAlike 3.0
Unported](http://creativecommons.org/licenses/by-sa/3.0/)*

Notes:

Congratulations on writing your first code\!

We have read in our data and we know the dimensions. Well now what now?

Let’s go over how we would **index**, **slice** and **select** certain
columns or rows of our data.

Let’s start by importing pandas and loading in a dataset named
`cereal.csv` and we’ll save it as `cereal`.

We can see all the columns and the first 5 rows of the dataframe using
`.head()`

Let’s say we only want certain rows of the whole dataframe or certain
columns.

We talked about how `.head()` will generate the first few rows of a
dataframe (5 as default) but what if we wanted rows 5-10?

The first column of this dataframe is called the `index`.

Each row has a label (the index) as well as a position. In this case,
the index label of an observation is the same as it’s position.

This doesn’t always have to be the case. We can assign another columns
as the index, but we will discuss this in the next module.

---

``` python
cereal.head(15)
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3    1.00  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3    1.00  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3    1.00  0.75  34.384843
5     Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
6                 Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
7                     Basic 4   G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
8                   Bran Chex   R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
9                 Bran Flakes   P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
10               Cap'n'Crunch   Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
11                   Cheerios   G  Cold       110        6    2     290    2.0   17.0       1     105        25      1    1.00  1.25  50.764999
12      Cinnamon Toast Crunch   G  Cold       120        1    3     210    0.0   13.0       9      45        25      2    1.00  0.75  19.823573
13                   Clusters   G  Cold       110        3    2     140    2.0   13.0       7     105        25      3    1.00  0.50  40.400208
14                Cocoa Puffs   G  Cold       110        1    1     180    0.0   12.0      13      55        25      2    1.00  1.00  22.736446
```

Notes:

Here are the first 15 rows of the dataframe.

Let’s talk about observation 4 named `Almond Delight`. Its index label
is `4` as well as it’s index position.

If you just went and counted those again and started screaming “5\! It’s
the fifth position”, that’s OK. In the Python language, we start
counting at position 0 (then 1, 2, 3, and 4 for Almond Delight).

---

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3    1.00  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3    1.00  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3    1.00  0.75  34.384843
5     Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
6                 Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
7                     Basic 4   G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
8                   Bran Chex   R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
9                 Bran Flakes   P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
10               Cap'n'Crunch   Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
11                   Cheerios   G  Cold       110        6    2     290    2.0   17.0       1     105        25      1    1.00  1.25  50.764999
```

``` python
cereal.loc[5:10]
```

```out
                       name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
5   Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
6               Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
7                   Basic 4   G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
8                 Bran Chex   R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
9               Bran Flakes   P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
10             Cap'n'Crunch   Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
```

Notes:

Now let’s say we want all 5 rows past `Almond Delight`. That means we
want rows `Apple Cinnamon Cheerios` to `Cap'n'Crunch`.

We use `.loc[]` with square brackets to cuts the dataframe from “Apple
Cinnamon Cheerios” to “Cap’n’Crunch” keeping the columns and everything
between.

This code can be interpreted as *“Obtain the rows in the dataframe
located from `5` to `10`.”*

---

```out
                       name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
5   Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
6               Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
7                   Basic 4   G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
8                 Bran Chex   R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
9               Bran Flakes   P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
10             Cap'n'Crunch   Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
```

``` python
cereal.loc[5:10, 'calories':'fiber']
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

The general format to slice both rows and columns together looks like
this:

``` python
`cereal.loc['row name start':'row name end', 'column name start':'column name end']`
```

Notes:

What if we only wanted certain columns now?

Perhaps we were only interested in the `calories` to `fiber` columns of
the “Apple Cinnamon Cheerios” to “Cap’n’Crunch” rows?

We put in desired rows first, and then the interval of the columns we
are interested in and separate them with a comma.

`.loc[]` is used to slice columns and rows by **label** and within an
interval.

The general format to slice both rows and columns together looks like
this:

``` python
`df.loc['row name start':'row name end', 'column name start':'column name end']`
```

---

``` python
cereal.loc[:6]
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
5    Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1     1.0  0.75  29.509541
6                Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2     1.0  1.00  33.174094
```

``` python
cereal.loc[:6, 'sugars':]
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

Notes:

There is a handy shortcut for slices that include the beginning of a
dataframe to a specified row or column label or a specified row or
column label to the end of a dataframe.

For example if we want all the rows up to “Apple Jacks” which has a
label equal to 6, we could omit the first label in the code all
together.

Or we can do something similar for the end of a dataframe. Let’s say now
we want all the rows up to `Apple Jacks` and only the columns from
`sugars` onward.

We would omit the ending label this time after the `:` (colon) .

---

# Let’s try it out\!

Notes:

<br>
