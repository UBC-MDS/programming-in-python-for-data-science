---
type: slides
---

# Hierarchical indexing

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

***Hierarchy*** is defined by
<a href="https://dictionary.cambridge.org/dictionary/english/hierarchy" target="_blank">
as \> “a system in which people or things are put at various levels or
ranks according to their importance”.

This helps explain the concept of ***hierarchical indexing*** which is
the capability of a dataframe posessing multiple levels of index labels.

<center>

<img src='module3/hierarchy.png' width="400">

</center>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Multi level indexing allows the possibility of some much more advanced
data analysis, however, that also can open the door to more complex
issues and bugs.

We are going keep this as simple and elegant as possible by introducing
you to the concept and how to transform dataframe with hierarchical
indexing.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Believe it or not but you have already seen this concepts when we
explained the concept of grouping and aggregating.

``` python
cereal.groupby('mfr').agg(['max', 'min'])
```

```out
     type       calories      protein     fat     sodium      fiber      carbo       sugars     potass     vitamins     shelf     weight        cups           rating           
      max   min      max  min     max min max min    max  min   max  min   max   min    max min    max min      max min   max min    max   min   max   min        max        min
mfr                                                                                                                                                                             
A     Hot   Hot      100  100       4   4   1   1      0    0   0.0  0.0  16.0  16.0      3   3     95  95       25  25     2   2   1.00  1.00  1.00  1.00  54.850917  54.850917
G    Cold  Cold      140  100       6   1   3   1    290  140   4.0  0.0  21.0  10.5     14   1    230  25      100  25     3   1   1.50  1.00  1.50  0.50  51.592193  19.823573
K    Cold  Cold      160   50       6   1   3   0    320    0  14.0  0.0  22.0   7.0     15   0    330  20      100  25     3   1   1.50  1.00  1.00  0.33  93.704912  29.924285
N     Hot  Cold      100   70       4   2   1   0    130    0  10.0  1.0  21.0   5.0      6   0    280   1       25   0     3   1   1.00  0.83  1.00  0.33  74.472949  59.363993
P    Cold  Cold      120   90       3   1   3   0    210   45   6.0  0.0  17.0  11.0     15   3    260  25       25  25     3   1   1.33  1.00  1.33  0.25  53.371007  28.025765
Q     Hot  Cold      120   50       5   1   5   0    220    0   2.7  0.0  14.0   1.0     12   0    135  15       25   0     3   1   1.00  0.50  1.00  0.50  63.005645  18.042851
R    Cold  Cold      150   90       4   1   3   0    280   95   4.0  0.0  23.0  14.0     11   2    170   1       25  25     3   1   1.00  1.00  1.13  0.67  49.787445  34.139765
```

Here you can see that each of the original cereal dataframe columns have
subcolumns `max` and `min` and that there a hierarchy of index labels.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Setting indexes

In the last section you learned how to set a single index using
`.set_index()`. Here we are going use the same verb but set `caramel`
AND `name` as the indexes from the candy dataframe. Remember in the last
section where we explained that `pandas` doesn’t recognize indexes as
columns and we needed to `.reset_index()` to makes sure we has all the
columns in our dataframe? The same applies here, we are going to avoid
resetting by reading the data without assigning any index with the
`index_col` argument.

``` python
df = pd.read_csv('candybars.csv')
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Next we can assign multiple indexes using square brackets within the
`.set_index()` verb and sort the dataframe according to the index using
verb `sort_index()`. (`.sort_index()` is similar to `.sort_values()`
however now we can sort by the index\!)

``` python
df2 = df.set_index(['caramel', 'name']).sort_index()
df2
```

```out
                           weight  chocolate  peanuts  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
caramel name                                                                                                                              
0       3 Musketeers           54          1        0       1                  0        0                0      0                  America
        Aero                   42          1        0       0                  0        0                0      0                   Canada
        Almond Joy             46          1        0       0                  0        1                0      0                  America
        Coffee Crisp           50          1        0       0                  1        0                0      0                   Canada
        Cookies and Cream      43          0        0       0                  1        0                1      0                     Both
...                           ...        ...      ...     ...                ...      ...              ...    ...                      ...
1       Skor                   39          1        0       0                  0        0                0      0                     Both
        Snickers               48          1        1       1                  0        0                0      0                     Both
        Take 5                 43          1        1       0                  1        0                0      0                  America
        Twix                   58          1        0       0                  1        0                0      1                     Both
        Wonderbar              58          1        1       0                  0        0                0      0                   Canada

[25 rows x 9 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

To get the entire picture, the image belows shows the complete dataset.
It almost looks like there are 2 separate dataframes on top of one
another. The top dataframe containing non-caramel chocolate bars and the
second dataframe containing caramel filled chocolate bars.

<center>

<img src='module3/candy_index.png' width="400">

</center>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Some of you may now be asking “How do we select and slice now?”. The
answer is just like before but now we specify 2 indexes\! To specify 2
indexes, we wrap them in parenthesis. Perhaps I wanted the non-caramel
filled “3 Musketeers” bar. I would use `0` to represent the first index
of “non-caramel filled” and `3 Musketeers` for the bar name.

``` python
df2.loc[(0, '3 Musketeers')]
```

```out
weight                           54
chocolate                         1
peanuts                           0
nougat                            1
cookie_wafer_rice                 0
coconut                           0
white_chocolate                   0
multi                             0
available_canada_america    America
Name: (0, 3 Musketeers), dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

This works if I want a specific cell value too. Let’s say I wanted the
non-caramel filled “3 Musketeers” bar weight.

``` python
df2.loc[(0,'3 Musketeers'), 'weight']
```

```out
54
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Stacking

If this organization is no ideal for your analysis you may want to
*transpose* your data (swap columns to rows or rows to columns). This
can be done with something called **Stacking**. Stacking is exactly what
it sounds like, we *stack* values.

``` python
stacked = df2.stack()
stacked
```

```out
caramel  name                                  
0        3 Musketeers  weight                          54
                       chocolate                        1
                       peanuts                          0
                       nougat                           1
                       cookie_wafer_rice                0
                                                    ...  
1        Wonderbar     cookie_wafer_rice                0
                       coconut                          0
                       white_chocolate                  0
                       multi                            0
                       available_canada_america    Canada
Length: 225, dtype: object
```

This dataframe now all the columns available in a single column and our
dataframe has elongated from 25 rows to 225 rows.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

Just for fun, let’s bring back the example we used of hierarchical
indexing involving our groupby cereal aggregated dataframe.

``` python
cereal.groupby('mfr').agg(['max', 'min'])
```

```out
     type       calories      protein     fat     sodium      fiber      carbo       sugars     potass     vitamins     shelf     weight        cups           rating           
      max   min      max  min     max min max min    max  min   max  min   max   min    max min    max min      max min   max min    max   min   max   min        max        min
mfr                                                                                                                                                                             
A     Hot   Hot      100  100       4   4   1   1      0    0   0.0  0.0  16.0  16.0      3   3     95  95       25  25     2   2   1.00  1.00  1.00  1.00  54.850917  54.850917
G    Cold  Cold      140  100       6   1   3   1    290  140   4.0  0.0  21.0  10.5     14   1    230  25      100  25     3   1   1.50  1.00  1.50  0.50  51.592193  19.823573
K    Cold  Cold      160   50       6   1   3   0    320    0  14.0  0.0  22.0   7.0     15   0    330  20      100  25     3   1   1.50  1.00  1.00  0.33  93.704912  29.924285
N     Hot  Cold      100   70       4   2   1   0    130    0  10.0  1.0  21.0   5.0      6   0    280   1       25   0     3   1   1.00  0.83  1.00  0.33  74.472949  59.363993
P    Cold  Cold      120   90       3   1   3   0    210   45   6.0  0.0  17.0  11.0     15   3    260  25       25  25     3   1   1.33  1.00  1.33  0.25  53.371007  28.025765
Q     Hot  Cold      120   50       5   1   5   0    220    0   2.7  0.0  14.0   1.0     12   0    135  15       25   0     3   1   1.00  0.50  1.00  0.50  63.005645  18.042851
R    Cold  Cold      150   90       4   1   3   0    280   95   4.0  0.0  23.0  14.0     11   2    170   1       25  25     3   1   1.00  1.00  1.13  0.67  49.787445  34.139765
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

The dataframe is currently unstacked but we can stack the `max` and
`min` values, to elongate the dataframe.

``` python
cereal.groupby('mfr').agg(['max', 'min']).stack()
```

```out
         type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
mfr                                                                                                                  
A   max   Hot       100        4    1       0    0.0   16.0       3      95        25      2    1.00  1.00  54.850917
    min   Hot       100        4    1       0    0.0   16.0       3      95        25      2    1.00  1.00  54.850917
G   max  Cold       140        6    3     290    4.0   21.0      14     230       100      3    1.50  1.50  51.592193
    min  Cold       100        1    1     140    0.0   10.5       1      25        25      1    1.00  0.50  19.823573
K   max  Cold       160        6    3     320   14.0   22.0      15     330       100      3    1.50  1.00  93.704912
    min  Cold        50        1    0       0    0.0    7.0       0      20        25      1    1.00  0.33  29.924285
N   max   Hot       100        4    1     130   10.0   21.0       6     280        25      3    1.00  1.00  74.472949
    min  Cold        70        2    0       0    1.0    5.0       0       1         0      1    0.83  0.33  59.363993
P   max  Cold       120        3    3     210    6.0   17.0      15     260        25      3    1.33  1.33  53.371007
    min  Cold        90        1    0      45    0.0   11.0       3      25        25      1    1.00  0.25  28.025765
Q   max   Hot       120        5    5     220    2.7   14.0      12     135        25      3    1.00  1.00  63.005645
    min  Cold        50        1    0       0    0.0    1.0       0      15         0      1    0.50  0.50  18.042851
R   max  Cold       150        4    3     280    4.0   23.0      11     170        25      3    1.00  1.13  49.787445
    min  Cold        90        1    0      95    0.0   14.0       2       1        25      1    1.00  0.67  34.139765
```

This now shows the `max` and `min` values for each manufacturer on top
of each other instead of side by side.  
Which way do you prefer?

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />
