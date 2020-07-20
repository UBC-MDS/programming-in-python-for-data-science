---
type: slides
---

# Splitting a column

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## String Split

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

You may have noticed that one of our columns contains 2 variables.
`mfr_type` is displaying both the manufacturer (N, Q, etc.) and the
cereal type (Cold, Hot). To convert this into tidier data we will need
to split up this column into 2 separate ones, but how?

At the beginning of this Module, we were introduced to the verb
`.split()` which split up a string into separate substrings. Pandas has
a verb that similarly splits a column into separate ones. It’s called
`.str.split()`. Let’s test it out.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal.head(2)
```

```out
                name mfr_type calories  protein  fiber  fat  carbo     rating    hot
0          100% Bran   N-Cold       70        4   10.0    1    5.0  68.402973  False
1  100% Natural Bran   Q-Cold      120        3    2.0    5    8.0  33.983679  False
```

We need to isolate the column and make sure we are splitting on the
correct separator. In this case, the column is `mfr_type` and the
separator is `-`.  
It’s important that we set `expand=True` to indicate that we want to
split the sub strings into separate columns.

``` python
new = cereal['mfr_type'].str.split('-', expand=True)
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Great\! We have 2 new columns. We will need to rename them and add them
back to our original dataframe.

``` python
new = new.rename(columns = {0:'mfr', 1: 'type'})
new
```

```out
   mfr  type
0    N  Cold
1    Q  Cold
2    K  Cold
3    K  Cold
..  ..   ...
73   G  Cold
74   R  Cold
75   G  Cold
76   G  Cold

[77 rows x 2 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can then use assign to add the columns from the `new` dataframe into
the original `cereal` one:

``` python
cereal = cereal.assign(mfr=new['mfr'],
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

You may be wondering **What happens if we don’t use `expand=False`**?
Well, let’s take a look\!

``` python
new = cereal['mfr_type'].str.split('-', expand=False)
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

Our output is now a Pandas Series data type with a list containing both
column values as the Series values.

``` python
type(new)
```

```out
<class 'pandas.core.series.Series'>
```

This not ideal for splitting up values in a column.

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
