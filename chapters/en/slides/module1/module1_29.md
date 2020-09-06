---
type: slides
---

# Frequency Tables and Writing CSVs

Notes: <br>

---

## What is Frequency?

*_Frequency_*: The number of times a value occurs within the data.

``` python
cereal_mini
```

```out
                        name  weight available_canada_america
0               Coffee Crisp      50                   Canada
1               Butterfinger     184                  America
2                       Skor      39                     Both
3                   Smarties      45                   Canada
4                       Twix      58                     Both
5  Reeses Peanutbutter Cups       43                     Both
6               3 Musketeers      54                  America
```

## What is a Frequency Table?

```out
Both       3
America    2
Canada     2
Name: available_canada_america, dtype: int64
```

Notes:

Before we explain what a frequency table is, you must know what
frequency means first.

*_Frequency_* is simply put, the number of times a value occurs within
the data. For example, let’s say we have a sample of our candybars data.
For example, let’s say we have a sample of our candybars data.

If we count the number of times the value `Both` appears in the
`available_canada_america` column, we get 3 times. This is the frequency
of the value `both`.

A frequency table is a manner of displaying all the possible values of a
column in our data and the number of occurrences (frequencies) of each
value.

For our sample data, a frequency table for the
`available_canada_america` column would look like this:

---

``` python
mfr_column = cereal['mfr']
mfr_column
```

```out
0     N
1     Q
2     K
3     K
     ..
73    G
74    R
75    G
76    G
Name: mfr, Length: 77, dtype: object
```

``` python
mfr_freq = mfr_column.value_counts()
mfr_freq
```

```out
K    23
G    22
P     9
Q     8
R     8
N     6
A     1
Name: mfr, dtype: int64
```

Notes:

If we want to get a frequency table of a categorical column, there are a
few steps that need to be followed.

Up until now, we discussed getting a single column from a dataframe
using double brackets - `df[['column name']]`.

For frequency tables, however, we only use single brackets to obtain the
column values.

We saved the object in a variable called `manufacturer_column` in the
same way we have saved objects before.

Next we can use `.value_counts()` referencing that the column we saved
as `manufacturer_column`.

This let’s us see the frequency of each categorical value.

---

``` python
mfr_col_wrong = cereal[['mfr']]
mfr_col_wrong
```

```out
   mfr
0    N
1    Q
2    K
3    K
..  ..
73   G
74   R
75   G
76   G

[77 rows x 1 columns]
```

``` python
mfr_col_wrong.value_counts()
```

``` out
AttributeError: 'DataFrame' object has no attribute 'value_counts'

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.7/site-packages/pandas/core/generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
```

Notes:

If we used double square brackets with `pd.value_counts()` we would get
an error that looks like this so it’s important to take care with using
the correct number of square brackets.

---

## Saving a dataframe

``` python
mfr_freq.to_csv('mfr_frequency.csv', index=False)
```

Notes:

Sometimes it’s useful to save a new dataframe as a `csv` file for future
use or to use in another application.

We can save dataframes using the method `.to_csv()`.

Simply put our desired `csv` file name in quotations within the
parentheses.

We include the argument `index=False` so we don’t export our index
column which is just a column of numbers.

---

# Let’s apply what we learned\!

Notes:

<br>
