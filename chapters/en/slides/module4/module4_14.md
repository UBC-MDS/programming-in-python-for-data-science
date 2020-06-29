---
type: slides
---

# Dataframes, series and column dtypes

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is a Dataframe … again

Since the beginning of this module, we have explored basic Python Data
types and structures. We’ve covered how they can be transformed into a
dataframe but that didn’t answer the lingering question ***“What is and
makes up a Pandas dataframe?”***

Let’s greet our cereal data back with a warm welcome.

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

On first instinct is to see what `type()` returns.

``` python
type(cereal)
```

```out
<class 'pandas.core.frame.DataFrame'>
```

It appears that dataframes have their own data type called a
`pandas.core.frame.DataFrame` or let’s just call it a `pd.DataFrame`
type for short.

Looking into this further the documentation states a dataframe as a:

*" Two-dimensional tabular data structure with columns and axis
labels."*

More directly, we can describe a dataframe as a collection of columns
but that brings us to the new question:

**“What is a dataframe column?”**

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s think back to Module 1 when we were selecting a single column from
a dataframe.  
There are two ways of doing so; with single brackets, and with double
brackets. What is the difference?

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

That’s no surprise, what about single brackets?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pandas Series

A pandas Series is a one-dimensional array of values with an axis label.
This is the base data type that makes up a pandas dataframe. In fact,
the \<a
href=“<https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe>”
target="\_blank“Pandas documentation”</a> explain it as “a dict of
Series objects”.

let’s look back at the series output again:

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

We can see additional information at the bottom. The axis labelled
`mfr`, the length equal to 77 and the `dtype`: object.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is a dtype?

So far we know a dataframe is made up of a collection of series and a
series contains values, a label as well as some additional information
regarding a **dtype**.

Just like how values have the data types ( `str`, `int`, `float`, etc.),
Columns in a Pandas dataframe have types called **dtypes**.

In this course we are going to concentrate on the following dtypes but
there others:

<center>

<img src='/module4/branch2.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module4/branch3num.png' width="80%">

</center>

Just like with Python data types, Pandas has numeric and non-numeric
data types.

#### Numeric dtypes

  - `float64` dtype is a column that contains only `float` type values
    in the cells of the dataframe, whereas,
  - `int64` columns only contains values of type `int` in the cells.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can use the noun `.dtypes` to find the dtype of a column:

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

Let’s see the `calories` column dtype:

``` python
cereal['calories'].dtypes
```

```out
dtype('int64')
```

What is the data type of one of the values in the the column?

``` python
all_bran_fiber =  cereal.loc[2, 'calories']
type(all_bran_fiber)
```

```out
<class 'numpy.int64'>
```

We are going to ignore the `numpy` portion for now but we clearly see it
says `int`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

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

Let’s check out the `fiber` column dtype now:

``` python
cereal['fiber'].dtypes
```

```out
dtype('float64')
```

Ah yes float64. What about the data type of one of the values in the the
column now?

``` python
all_bran_fiber =  cereal.loc[2, 'fiber']
type(all_bran_fiber)
```

```out
<class 'numpy.float64'>
```

of type `float`\! (Again, let’s not worry about the numpy portion of
this) Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module4/full.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Non-Numeric dtypes

<center>

<img src='/module4/full.png' width="80%">

</center>

These can be a bit more complicated but let’s concentrate on the dtypes
`object` and `bool`. We will be exploring `datetime64` in Module 7.

  - `object` is a dtype that contains `str` type values in the cells of
    the dataframe or that had a mixture of different types to begin
    with. This is the “default” dtype when pandas is not quite sure what
    is the cell type values are or when there is a mixture of numeric
    and non-numeric value types.

  - `bool` dtypes, just like it’s dtype name, contains `bool` type
    values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

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

Let’s take a look at the `name` column:

``` python
cereal['name'].dtypes
```

```out
dtype('O')
```

Here, “O” stands for object. What about a value within the column
series:

``` python
type(cereal.loc[2, 'name'])
```

```out
<class 'str'>
```

The “All-Bran” is a `str` value type that resides in a column of dtype
`object`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

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

What about the `hot` column:

``` python
cereal['hot'].dtypes
```

```out
dtype('bool')
```

And the column value within the series:

``` python
type(cereal.loc[2, 'hot'])
```

```out
<class 'numpy.bool_'>
```

Also a `bool`. We can ignore the numpy part as we did before, we will
discuss this later.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

An easy way to check all dtypes of the columns in our dataframe is to
use `.dtypes` on the dataframe object.

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

Knowing what dtype the values are, helps us understand how we can
transform them and how they respond to different operations and
operators.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
