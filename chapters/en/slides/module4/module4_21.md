---
type: slides
---

# Operations with Columns

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We’ve just learned what Python values work with certain operations but
what about dataframes?  
Let’s take a look at our cereal dataframe once more:

``` python
cereal
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

It’s always a good idea to see what column types we have before
operating on them, since they may not be of the type we expect.

``` python
cereal.dtypes
```

```out
name         object
mfr_type     object
calories     object
protein       int64
             ...   
fat           int64
carbo       float64
rating      float64
hot            bool
Length: 9, dtype: object
```

In this case, we discover that the `calories` column is of dtype
`object` which isn’t the `int64` category expected.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Since it is not a numerical value, it will not show up in our summary
statistics if we do `describe()`:

``` python
cereal.describe()
```

```out
         protein      fiber        fat      carbo     rating
count  77.000000  77.000000  77.000000  77.000000  77.000000
mean    2.545455   2.151948   1.012987  14.623377  42.665705
std     1.094790   2.383364   1.006473   4.188138  14.047289
min     1.000000   0.000000   0.000000   1.000000  18.042851
25%     2.000000   1.000000   0.000000  12.000000  33.174094
50%     3.000000   2.000000   1.000000  14.000000  40.400208
75%     3.000000   3.000000   2.000000  17.000000  50.828392
max     6.000000  14.000000   5.000000  23.000000  93.704912
```

If we attempt to sum the column, we get a concatenation of the column:

``` python
cereal['calories'].sum()
```

```out
'70120705011011011013090901201101201101101101001101101101001101001001101101001201201101001101001101201201101101101401101001101001501501601001201409013012010050501001001201009011011080909011011090110140100110110100100110'
```

We saw earlier that when we add strings, they concatenate together.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To go forward with any analysis, we are going to have to convert it to a
numeric value. Luckily, there is an easy way to do it using verb
`astype()`:

``` python
cereal = cereal.assign(calories=cereal['calories'].astype('int'))
cereal.head(3)
```

```out
                name mfr_type  calories  protein  fiber  fat  carbo     rating    hot
0          100% Bran   N-Cold        70        4   10.0    1    5.0  68.402973  False
1  100% Natural Bran   Q-Cold       120        3    2.0    5    8.0  33.983679  False
2           All-Bran   K-Cold        70        4    9.0    1    7.0  59.425505  False
```

We simply assign the column back to the same name but as dtype `int`.

``` python
cereal.dtypes
```

```out
name         object
mfr_type     object
calories      int64
protein       int64
             ...   
fat           int64
carbo       float64
rating      float64
hot            bool
Length: 9, dtype: object
```

Great, it looks like we are back on track.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal.head(3)
```

```out
                name mfr_type  calories  protein  fiber  fat  carbo     rating    hot
0          100% Bran   N-Cold        70        4   10.0    1    5.0  68.402973  False
1  100% Natural Bran   Q-Cold       120        3    2.0    5    8.0  33.983679  False
2           All-Bran   K-Cold        70        4    9.0    1    7.0  59.425505  False
```

If we take the sum of the column now we get the actual sum:

``` python
cereal['calories'].sum()
```

```out
8230
```

And the mean caloric value make much more sense now:

``` python
cereal['calories'].mean()
```

```out
106.88311688311688
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## object columns

What happens if we try to take summary statistics of some of the other
columns?

``` python
cereal['mfr_type'].mean()
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: Could not convert N-ColdQ-ColdK-ColdK-ColdR-ColdG-ColdK-ColdG-ColdR-ColdP-ColdQ-ColdG-ColdG-ColdG-ColdG-ColdR-ColdK-ColdK-ColdG-ColdK-ColdN-HotK-ColdG-ColdR-ColdK-ColdK-ColdK-ColdP-ColdK-ColdP-ColdP-ColdG-ColdP-ColdP-ColdP-ColdQ-ColdG-ColdP-ColdK-ColdK-ColdG-ColdQ-ColdG-ColdA-HotR-ColdR-ColdK-ColdG-ColdK-ColdK-ColdK-ColdG-ColdP-ColdK-ColdQ-ColdQ-ColdQ-ColdQ-HotK-ColdG-ColdK-ColdR-ColdK-ColdN-ColdN-ColdN-ColdK-ColdK-ColdN-ColdG-ColdG-ColdG-ColdG-ColdG-ColdR-ColdG-ColdG-Cold to numeric

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 11217, in stat_func
    f, name, axis=axis, skipna=skipna, numeric_only=numeric_only
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/series.py", line 3891, in _reduce
    return op(delegate, skipna=skipna, **kwds)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 69, in _f
    return f(*args, **kwargs)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 125, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 542, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/nanops.py", line 1310, in _ensure_numeric
    raise TypeError(f"Could not convert {x} to numeric")
```

Yikes\! let’s not take the mean of columns of dtype `object`.

As we saw before, taking a `.sum()` of a column concatenates the values
together:

``` python
cereal['mfr_type'].sum()
```

```out
'N-ColdQ-ColdK-ColdK-ColdR-ColdG-ColdK-ColdG-ColdR-ColdP-ColdQ-ColdG-ColdG-ColdG-ColdG-ColdR-ColdK-ColdK-ColdG-ColdK-ColdN-HotK-ColdG-ColdR-ColdK-ColdK-ColdK-ColdP-ColdK-ColdP-ColdP-ColdG-ColdP-ColdP-ColdP-ColdQ-ColdG-ColdP-ColdK-ColdK-ColdG-ColdQ-ColdG-ColdA-HotR-ColdR-ColdK-ColdG-ColdK-ColdK-ColdK-ColdG-ColdP-ColdK-ColdQ-ColdQ-ColdQ-ColdQ-HotK-ColdG-ColdK-ColdR-ColdK-ColdN-ColdN-ColdN-ColdK-ColdK-ColdN-ColdG-ColdG-ColdG-ColdG-ColdG-ColdR-ColdG-ColdG-Cold'
```

What about the column of type `bool`?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Bool

Since booleans adopt the values of 0 and 1 for True and False values
respectively, we can take the sum of a column to obtain the total number
of `True` values:

``` python
cereal['hot'].sum()
```

```out
3
```

`.mean()` works by suming up all the values and divides them by the
total number of rows.

In the case where the column is of dtype `bool`, since `True` has a
value of 1 and `False` has a value of 0, the mean is calculated as the
total number of `True` values divided by the total number of `True` and
`False` values. This gives the proportion of `True` values over the
total number of rows.

``` python
cereal['hot'].mean()
```

```out
0.03896103896103896
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Axis Operations

We are quite familiar with taking the mean and sum of entire columns but
there are times where we want the mean or sum of the values in a row.

``` python
cereal.head(2)
```

```out
                name mfr_type  calories  protein  fiber  fat  carbo     rating    hot
0          100% Bran   N-Cold        70        4   10.0    1    5.0  68.402973  False
1  100% Natural Bran   Q-Cold       120        3    2.0    5    8.0  33.983679  False
```

Perhaps we wanted the total grams of `protein`,`fiber`,`fat` and `carbo`
for each cereal? Remember when we discussed the argument `axis` in
Module 3? We can use it in our operations as well. `axis=1` refers to
the calculation being done for a row, across multiple columns, whereas
`axis=0` (which is the default for aggregation verbs) refers to the
calculation for a column, across multiple rows.

``` python
cereal.loc[:, 'protein': 'carbo'].sum(axis=1)
```

```out
0     20.0
1     18.0
2     21.0
3     26.0
      ... 
73    15.0
74    24.0
75    24.0
76    20.0
Length: 77, dtype: float64
```

Although this produces the totals, we want it as an additional column in
the dataframe. That means we will have to combine it with `.assign()`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal.loc[:, 'protein': 'carbo'].sum(axis=1)
```

```out
0     20.0
1     18.0
2     21.0
3     26.0
      ... 
73    15.0
74    24.0
75    24.0
76    20.0
Length: 77, dtype: float64
```

Although this produces the totals for each row, we want it as an
additional column in the dataframe. We will have to combine it with the
`.assign()` verb.

``` python
cereal = cereal.assign(total_pffc=cereal.loc[:, 'protein': 'carbo'].sum(axis=1))
cereal.head()
```

```out
                        name mfr_type  calories  protein  fiber  fat  carbo     rating    hot  total_pffc
0                  100% Bran   N-Cold        70        4   10.0    1    5.0  68.402973  False        20.0
1          100% Natural Bran   Q-Cold       120        3    2.0    5    8.0  33.983679  False        18.0
2                   All-Bran   K-Cold        70        4    9.0    1    7.0  59.425505  False        21.0
3  All-Bran with Extra Fiber   K-Cold        50        4   14.0    0    8.0  93.704912  False        26.0
4             Almond Delight   R-Cold       110        2    1.0    2   14.0  34.384843  False        19.0
```

We can do the same syntax for calculating the mean over multiple columns
too.

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
