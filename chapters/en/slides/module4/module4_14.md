---
type: slides
---

# Dataframes, series and column dtypes

Notes:

<br>

---

## What is a Dataframe … again

``` python
cereal
```

```out
                         name mfr  calories  protein  fiber  fat  carbo     rating    hot
0                   100% Bran   N        70        4   10.0    1    5.0  68.402973  False
1           100% Natural Bran   Q       120        3    2.0    5    8.0  33.983679  False
2                    All-Bran   K        70        4    9.0    1    7.0  59.425505  False
3   All-Bran with Extra Fiber   K        50        4   14.0    0    8.0  93.704912  False
4              Almond Delight   R       110        2    1.0    2   14.0  34.384843  False
..                        ...  ..       ...      ...    ...  ...    ...        ...    ...
72                    Triples   G       110        2    0.0    1   21.0  39.106174  False
73                       Trix   G       110        1    0.0    1   13.0  27.753301  False
74                 Wheat Chex   R       100        3    3.0    1   17.0  49.787445  False
75                   Wheaties   G       100        3    3.0    1   17.0  51.592193  False
76        Wheaties Honey Gold   G       110        2    1.0    1   16.0  36.187559  False

[77 rows x 9 columns]
```

Notes:

Since the beginning of this module, we have explored basic Python Data
types and structures. We’ve covered how they can be transformed into a
dataframe, but that didn’t answer the lingering question:

***“What is and makes up a Pandas dataframe?”***

Let’s greet our cereal data back with a warm welcome.

---

``` python
type(cereal)
```

```out
<class 'pandas.core.frame.DataFrame'>
```

Notes:

Our first instinct is to see what `type()` returns.

It appears that dataframes have their own data type called a
`pandas.core.frame.DataFrame` or let’s just call it a `pd.DataFrame`
type for short.

Looking into this further, the documentation states a dataframe as a:

*“Two-dimensional tabular data structure with columns and axis labels.”*

More directly, we can describe a dataframe as a collection of columns,
but that brings us to the new question:

**“What is a dataframe column?”**

---

``` python
cereal[['mfr']]
```

```out
   mfr
0    N
1    Q
2    K
3    K
4    R
..  ..
72   G
73   G
74   R
75   G
76   G

[77 rows x 1 columns]
```

``` python
type(cereal[['mfr']])
```

```out
<class 'pandas.core.frame.DataFrame'>
```

Notes:

Let’s think back to Module 1 when we were selecting a single column from
a dataframe.

There are two ways of doing so; with single square brackets and with
double square brackets.

When indexing with double square brackets, we get back another object of
type `pd.DataFrame`.

What about single brackets?

---

``` python
cereal['mfr']
```

```out
0     N
1     Q
2     K
3     K
4     R
     ..
72    G
73    G
74    R
75    G
76    G
Name: mfr, Length: 77, dtype: object
```

``` python
type(cereal['mfr'])
```

```out
<class 'pandas.core.series.Series'>
```

Notes:

`pandas.core.series.Series` Well, that’s something new.

What are panda series?

---

## Pandas Series

``` python
cereal['mfr']
```

```out
0     N
1     Q
2     K
3     K
4     R
     ..
72    G
73    G
74    R
75    G
76    G
Name: mfr, Length: 77, dtype: object
```

Notes:

A pandas Series is a one-dimensional array of values with an axis label,
sort of like a list with a name attached to it.

This is the base data type that makes up a pandas dataframe.

In fact, the
<a href="https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe" target="_blank">Pandas
documentation“</a> explains a dataframe as”a dict of Series objects".

Let’s look back at the series output again.

We can see additional information at the bottom.

The series contains the name of the column series, which is `mfr` , the
length of the series, which is equal to 77, and a `dtype` equal to
object.

Ok, we know what `type` is, but what is a `dtype`?

---

## What is a dtype?

<br> <br> <br>

<center>

<img src='/module4/branch2.png' width="100%">

</center>

Notes:

So far, we know a dataframe is made up of a collection of series, and a
series contains values, a label as well as some additional information
regarding a **dtype**.

Just like how objects have data types ( `str`, `int`, `float`, etc.),
columns in a Pandas dataframe have types called **dtypes**.

In this course we are going to concentrate on the following dtypes.

---

<center>

<img src='/module4/branch3num.png' width="100%">

</center>

#### Numeric dtypes

  - `float64`: contains `float` type values
  - `int64`: contains `int` type values.

Notes:

Just like with Python data types, Pandas has numeric and non-numeric
data types.

Let’s look at the numeric ones first.

  - `float64` dtype is a column that contains only `float` type values
    in the cells of the dataframe, whereas,
  - `int64` columns only contains integers.

---

``` python
cereal.head()
```

```out
                        name mfr  calories  protein  fiber  fat  carbo     rating    hot
0                  100% Bran   N        70        4   10.0    1    5.0  68.402973  False
1          100% Natural Bran   Q       120        3    2.0    5    8.0  33.983679  False
2                   All-Bran   K        70        4    9.0    1    7.0  59.425505  False
3  All-Bran with Extra Fiber   K        50        4   14.0    0    8.0  93.704912  False
4             Almond Delight   R       110        2    1.0    2   14.0  34.384843  False
```

``` python
cereal['calories'].dtypes
```

```out
dtype('int64')
```

``` python
all_bran_fiber =  cereal.loc[2, 'calories']
type(all_bran_fiber)
```

```out
<class 'numpy.int64'>
```

Notes:

We can use the noun `.dtypes` to find the dtype of a column.

Let’s see what the dtype is of the `calories` column.

What is the data type of one of the values in this column?

We are going to ignore the `numpy` portion for now (You’ll see this in
Module 8), but for now, we can clearly see it says `int`.

---

``` python
cereal.head()
```

```out
                        name mfr  calories  protein  fiber  fat  carbo     rating    hot
0                  100% Bran   N        70        4   10.0    1    5.0  68.402973  False
1          100% Natural Bran   Q       120        3    2.0    5    8.0  33.983679  False
2                   All-Bran   K        70        4    9.0    1    7.0  59.425505  False
3  All-Bran with Extra Fiber   K        50        4   14.0    0    8.0  93.704912  False
4             Almond Delight   R       110        2    1.0    2   14.0  34.384843  False
```

``` python
cereal['fiber'].dtypes
```

```out
dtype('float64')
```

``` python
all_bran_fiber =  cereal.loc[2, 'fiber']
type(all_bran_fiber)
```

```out
<class 'numpy.float64'>
```

Notes:

Let’s check out the `fiber` column dtype now.

Ah yes, `float64` as expected.

What about the data type of one of the values in the column now?

It’s of type `float`, just what we suspected\! (Again, let’s not worry
about the `numpy` portion of this)

---

## Non-Numeric dtypes

<br> <br>

<center>

<img src='/module4/full.png' width="100%">

</center>

Notes:

Non-numeric types can be a bit more complicated but let’s concentrate on
the dtypes `object` and `bool`. We will be exploring `datetime64` and
`timedelta[ns]` in Module 8.

  - `object` is a dtype that contains `str` type values in the cells of
    the dataframe or that had a mixture of different types, to begin
    with. This is the “default” dtype when pandas is not quite sure what
    is the cell type values are or when there is a mixture of numeric
    and non-numeric value types.

  - `bool` dtypes, just like its dtype name, contains Boolean values.

---

``` python
cereal.head()
```

```out
                        name mfr  calories  protein  fiber  fat  carbo     rating    hot
0                  100% Bran   N        70        4   10.0    1    5.0  68.402973  False
1          100% Natural Bran   Q       120        3    2.0    5    8.0  33.983679  False
2                   All-Bran   K        70        4    9.0    1    7.0  59.425505  False
3  All-Bran with Extra Fiber   K        50        4   14.0    0    8.0  93.704912  False
4             Almond Delight   R       110        2    1.0    2   14.0  34.384843  False
```

``` python
cereal['name'].dtypes
```

```out
dtype('O')
```

``` python
type(cereal.loc[2, 'name'])
```

```out
<class 'str'>
```

Notes:

Let’s take a look at the `name` column.

Here, “O” stands for object.

What about a value within the column series?

The “All-Bran” is a `str` value type that resides in a column of dtype
`object`.

---

``` python
cereal.head()
```

```out
                        name mfr  calories  protein  fiber  fat  carbo     rating    hot
0                  100% Bran   N        70        4   10.0    1    5.0  68.402973  False
1          100% Natural Bran   Q       120        3    2.0    5    8.0  33.983679  False
2                   All-Bran   K        70        4    9.0    1    7.0  59.425505  False
3  All-Bran with Extra Fiber   K        50        4   14.0    0    8.0  93.704912  False
4             Almond Delight   R       110        2    1.0    2   14.0  34.384843  False
```

``` python
cereal['hot'].dtypes
```

```out
dtype('bool')
```

``` python
type(cereal.loc[2, 'hot'])
```

```out
<class 'numpy.bool_'>
```

Notes:

Let’s look at the `hot` column now.

This outputs a dtype of `bool`.

What are column value types within the series?

Also a `bool`. We can ignore the numpy part as we did before since we
will discuss this later on.

---

``` python
cereal.dtypes
```

```out
name         object
mfr          object
calories      int64
protein       int64
fiber       float64
fat           int64
carbo       float64
rating      float64
hot            bool
dtype: object
```

Notes:

An easy way to check all dtypes of the columns in our dataframe is to
use `.dtypes` on the dataframe object.

Knowing what dtype the values are, helps us understand how we can
transform them and how they respond to different operations and
operators.

---

# Let’s apply what we learned\!

Notes:

<br>
