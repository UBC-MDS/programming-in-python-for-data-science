---
type: slides
---

# Splitting a column

Notes:

<br>

---

## String Split

``` python
cereal_amended
```

```out
                         name mfr_type calories  protein  fiber  fat  carbo     rating    hot
0                   100% Bran   N-Cold       70        4   10.0    1    5.0  68.402973  False
1           100% Natural Bran   Q-Cold      120        3    2.0    5    8.0  33.983679  False
2                    All-Bran   K-Cold       70        4    9.0    1    7.0  59.425505  False
3   All-Bran with Extra Fiber   K-Cold       50        4   14.0    0    8.0  93.704912  False
..                        ...      ...      ...      ...    ...  ...    ...        ...    ...
73                       Trix   G-Cold      110        1    0.0    1   13.0  27.753301  False
74                 Wheat Chex   R-Cold      100        3    3.0    1   17.0  49.787445  False
75                   Wheaties   G-Cold      100        3    3.0    1   17.0  51.592193  False
76        Wheaties Honey Gold   G-Cold      110        2    1.0    1   16.0  36.187559  False

[77 rows x 9 columns]
```

Notes:

Here is a new cereal dataframe.

You’ll notice that our column `mfr_type` contains two variables.

It is displaying both the manufacturer (N, Q, etc.) of the cereal and
the cereal type (Cold, Hot).

To convert this into tidier data, we will need to split up this column
into two separate columns, but how?

---

``` python
cereal_amended.head(5)
```

```out
                        name mfr_type calories  protein  fiber  fat  carbo     rating    hot
0                  100% Bran   N-Cold       70        4   10.0    1    5.0  68.402973  False
1          100% Natural Bran   Q-Cold      120        3    2.0    5    8.0  33.983679  False
2                   All-Bran   K-Cold       70        4    9.0    1    7.0  59.425505  False
3  All-Bran with Extra Fiber   K-Cold       50        4   14.0    0    8.0  93.704912  False
4             Almond Delight   R-Cold      110        2    1.0    2   14.0  34.384843  False
```

``` python
new = cereal_amended['mfr_type'].str.split('-', expand=True)
new 
```

```out
    0     1
0   N  Cold
1   Q  Cold
2   K  Cold
3   K  Cold
.. ..   ...
73  G  Cold
74  R  Cold
75  G  Cold
76  G  Cold

[77 rows x 2 columns]
```

Notes:

At the beginning of this Module, we were introduced to the verb
`.split()` which split up a string into separate substrings.

Pandas has a verb that similarly splits a column into separate ones.
It’s called `.str.split()`.

Let’s test it out.

First, we need to grab the column and make sure we are splitting on the
correct separator.

In this case, the column is `mfr_type`, and the separator is `-`.

It’s important that we set `expand=True` to indicate that we want to
split the substrings into separate columns.

As you can see from the result, we now have two new columns.

---

``` python
new.head()
```

```out
   0     1
0  N  Cold
1  Q  Cold
2  K  Cold
3  K  Cold
4  R  Cold
```

``` python
new = new.rename(columns = {0:'mfr', 1: 'type'})
new.head()
```

```out
  mfr  type
0   N  Cold
1   Q  Cold
2   K  Cold
3   K  Cold
4   R  Cold
```

Notes:

We will need to rename them before we add them back to our original
dataframe.

---

``` python
cereal = cereal_amended.assign(mfr=new['mfr'],
                       type=new['type'])
cereal
```

```out
                         name mfr_type calories  protein  fiber  fat  carbo     rating    hot mfr  type
0                   100% Bran   N-Cold       70        4   10.0    1    5.0  68.402973  False   N  Cold
1           100% Natural Bran   Q-Cold      120        3    2.0    5    8.0  33.983679  False   Q  Cold
2                    All-Bran   K-Cold       70        4    9.0    1    7.0  59.425505  False   K  Cold
3   All-Bran with Extra Fiber   K-Cold       50        4   14.0    0    8.0  93.704912  False   K  Cold
..                        ...      ...      ...      ...    ...  ...    ...        ...    ...  ..   ...
73                       Trix   G-Cold      110        1    0.0    1   13.0  27.753301  False   G  Cold
74                 Wheat Chex   R-Cold      100        3    3.0    1   17.0  49.787445  False   R  Cold
75                   Wheaties   G-Cold      100        3    3.0    1   17.0  51.592193  False   G  Cold
76        Wheaties Honey Gold   G-Cold      110        2    1.0    1   16.0  36.187559  False   G  Cold

[77 rows x 11 columns]
```

Notes:

We can then use `.assign()` to add the columns from the `new` dataframe
into the original `cereal` one.

Now we can see our new columns at the end of our cereal dataframe.

---

``` python
new = cereal_amended['mfr_type'].str.split('-', expand=False)
new 
```

```out
0     [N, Cold]
1     [Q, Cold]
2     [K, Cold]
3     [K, Cold]
        ...    
73    [G, Cold]
74    [R, Cold]
75    [G, Cold]
76    [G, Cold]
Name: mfr_type, Length: 77, dtype: object
```

``` python
type(new)
```

```out
<class 'pandas.core.series.Series'>
```

Notes:

You may be wondering **What happens if we use `expand=False` instead of
`expand=True`**?

Well, let’s take a look\!

Our output is now a Pandas Series data type with a list containing both
column values as the Series values.

This makes it a little harder to add to the dataframe as separate
columns.

This not ideal for splitting up values in a column.

---

# Let’s apply what we learned\!

Notes:

<br>
