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

Since the begining of this module, we have explored basic Python Data
types and structures. We’ve covered how they can be transformed into a
dataframe but that didn’t answer the lingering question ***“What is and
makes up a Pandas Dataframe?”***

Let’s greet our cereal data back with a warm welcome.

``` python
cereal
```

```out
   mfr  type  calories  protein  fiber  fat  carbo     rating
0    N  Cold        70        4   10.0    1    5.0  68.402973
1    Q  Cold       120        3    2.0    5    8.0  33.983679
2    K  Cold        70        4    9.0    1    7.0  59.425505
3    K  Cold        50        4   14.0    0    8.0  93.704912
4    R  Cold       110        2    1.0    2   14.0  34.384843
..  ..   ...       ...      ...    ...  ...    ...        ...
72   G  Cold       110        2    0.0    1   21.0  39.106174
73   G  Cold       110        1    0.0    1   13.0  27.753301
74   R  Cold       100        3    3.0    1   17.0  49.787445
75   G  Cold       100        3    3.0    1   17.0  51.592193
76   G  Cold       110        2    1.0    1   16.0  36.187559

[77 rows x 8 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

On first instinct why don’t we try to see what `type()` returns.

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

> " Two-dimensional tabular data structure with columns and axis
> labels."

More directly we can describe a dataframe of multiple columns. That
brings us to the new question:

**“What is a Dataframe column?”**

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

A pandas Series is a one dimension array of values with an axis label.
This is the base datatype that make up a pandas dataframe. In fact the
\<a
href=“<https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe>”
target="\_blank“Pandas documentation</a> explain it as a”a dict of
Series objects".

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

We can see additional information at the bottom. The axis labeled `mfr`,
the length equal to 77 and the `dtype`: object.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is a dtype?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

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
