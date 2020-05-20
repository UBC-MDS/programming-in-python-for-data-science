---
type: slides
---

# Reshaping using pivot

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`pandas` provides 2 functions for reshaping data:

  - <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
    to make a wide dataframe long (convert columns to row)
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
    to make a long dataframe wide (convert rows to columns)

<center>

<img src='/module3/pivot_melt.gif' width="400">

</center>

“Source: Garrick Aden-Buie,
<https://github.com/gadenbuie/tidyexplain#spread-and-gather> and Tomas
Beuzen, DSCI 523 Data Wrangling”

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot

`.pivot()` can be used in situations where our data may not meet
criterion \#2: \_ Each variable is a single column\_.

It can be used to elongate the dataframe: it convert variables to their
own columns that were previously being stored in a single column.

The code for this verb takes quite a few arguments that can be a bit
tricky so we are going to go through it.

``` python
df.pivot(index=['index-label'], columns='column-name', values='new_colum-name')
```

  - `df` to express with dataframe we want to pivot
  - `index` is going to be use to make the new dataframe’s index.
  - `columns` is the column that currently exists but that we want to
    create new columns labels from. Each unique value in this column
    will become a new column label.
  - `values` is the name of the column that currently exists but that
    contains the cell values we want. These values will be display in
    the respective newly created columns.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We must take care with the `index` argument when transforming
dataframes. This argument will only accept column labels and not column
index labels. Before we do any type of transformation, it’s a good idea
to reset and remove and labels an an index.  
This can be done with `.reset_index()` This converts the index to a
regular column. On our trusty cereal dataset, we see the name column as
our index and we can reset it by calling `.reset_index()`

``` python
cereal.head()
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

``` python
cereal.reset_index().head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The process of pivoting and it’s argument can be explained well using
the animation made by
<a href="https://github.com/apreshill/teachthat" target="_blank"> Alison
Presmanes Hill</a>

<center>

<img src='/module3/pivot_py.gif' width="600">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Or if we wanted to use our cereal dataframe as an example, the diagram
below shows the spreading of column `nutrition` into 2 columns named
`calories` and `protein` which were the 2 values contained in the
`nutrition` column.

<center>

<img src='/module3/pivot_cereal.png' width="600">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s try an example. Our cereal dataframe has information on 77
different cereals,

``` python
cereal
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Triples                     G  Cold       110        2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
Trix                        G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
Wheat Chex                  R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
Wheaties                    G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
Wheaties Honey Gold         G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 15 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Our dataframe that we want to tidy looks like this:

``` python
cereal_long
```

```out
                    mfr  type  fat  sodium  fiber  carbo  potass  vitamins  shelf  weight  cups     rating nutrition  measure
name                                                                                                                         
100% Bran             N  Cold    1     130   10.0    5.0     280        25      3     1.0  0.33  68.402973   protein        4
100% Bran             N  Cold    1     130   10.0    5.0     280        25      3     1.0  0.33  68.402973  calories       70
100% Bran             N  Cold    1     130   10.0    5.0     280        25      3     1.0  0.33  68.402973    sugars        6
100% Natural Bran     Q  Cold    5      15    2.0    8.0     135         0      3     1.0  1.00  33.983679   protein        3
100% Natural Bran     Q  Cold    5      15    2.0    8.0     135         0      3     1.0  1.00  33.983679  calories      120
...                  ..   ...  ...     ...    ...    ...     ...       ...    ...     ...   ...        ...       ...      ...
Wheaties              G  Cold    1     200    3.0   17.0     110        25      1     1.0  1.00  51.592193   protein        3
Wheaties              G  Cold    1     200    3.0   17.0     110        25      1     1.0  1.00  51.592193  calories      100
Wheaties Honey Gold   G  Cold    1     200    1.0   16.0      60        25      1     1.0  0.75  36.187559  calories      110
Wheaties Honey Gold   G  Cold    1     200    1.0   16.0      60        25      1     1.0  0.75  36.187559   protein        2
Wheaties Honey Gold   G  Cold    1     200    1.0   16.0      60        25      1     1.0  0.75  36.187559    sugars        8

[231 rows x 14 columns]
```

We can see there are 231 rows and the `nutrition` column is made up of 3
variables; `protein`, `calories` and `sugar`. That means there are 3
rows for each of the 77 cereals. This explains why this untidy dataframe
contains 231 rows (77 cereals \* 3 variables = 231 rows).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To transform this into tidy data we would specify the following
arguments.  
\- Indicate `index` as the `name` column.  
\- Target the column `nutrition` with the values contained as new
columns labels.  
\- Specify `measure` as the values associated with each of the new
columns.

Also we can’t forget to reset the index\!  
(Just like any other dataframe, if we want to keep the changes, makes
sure to assign it to an object)

``` python
tidy_pivot = (cereal_long.reset_index()
            .pivot(index='name', columns='nutrition', values='measure')
             )
tidy_pivot
```

```out
nutrition                  calories  protein  sugars
name                                                
100% Bran                        70        4       6
100% Natural Bran               120        3       8
All-Bran                         70        4       5
All-Bran with Extra Fiber        50        4       0
Almond Delight                  110        2       8
...                             ...      ...     ...
Triples                         110        2       3
Trix                            110        1      12
Wheat Chex                      100        3       3
Wheaties                        100        3       3
Wheaties Honey Gold             110        2       8

[77 rows x 3 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

```out
nutrition                  calories  protein  sugars
name                                                
100% Bran                        70        4       6
100% Natural Bran               120        3       8
All-Bran                         70        4       5
All-Bran with Extra Fiber        50        4       0
Almond Delight                  110        2       8
...                             ...      ...     ...
Triples                         110        2       3
Trix                            110        1      12
Wheat Chex                      100        3       3
Wheaties                        100        3       3
Wheaties Honey Gold             110        2       8

[77 rows x 3 columns]
```

We are now back to 77 rows and it looks like we’ve tidied our data up\!
There appears to be a problem though. `pivot` works well when we are
only concerned with the columns we are pivoting but as we can see we
lost all our other columns in the dataset. There is a solution for this
and it’s called `.pivot_table()`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot\_table

`.pivot_table()` works with multiple indexes and duplicate values. That
just means we can keep all the columns that we are not pivoting. Let’s
attempt at fixing our untidy data again but keeping all our columns. The
only problem is after we pivot we want to reset our index to avoid any
indexing confusion.

``` python
tidy_pivot = (cereal_long.reset_index()
            .pivot_table(index=['name','mfr', 'type','fat',
                                'sodium', 'fiber', 'carbo', 
                                'potass', 'vitamins', 'shelf',
                                'weight', 'cups', 'rating'],
                         columns='nutrition', 
                         values='measure').reset_index()
             )
tidy_pivot.head()
```

```out
nutrition                       name mfr  type  fat  sodium  fiber  carbo  potass  vitamins  shelf  weight  cups     rating  calories  protein  sugars
0                          100% Bran   N  Cold    1     130   10.0    5.0     280        25      3     1.0  0.33  68.402973        70        4       6
1                  100% Natural Bran   Q  Cold    5      15    2.0    8.0     135         0      3     1.0  1.00  33.983679       120        3       8
2                           All-Bran   K  Cold    1     260    9.0    7.0     320        25      3     1.0  0.33  59.425505        70        4       5
3          All-Bran with Extra Fiber   K  Cold    0     140   14.0    8.0     330        25      3     1.0  0.50  93.704912        50        4       0
4                     Almond Delight   R  Cold    2     200    1.0   14.0       1        25      3     1.0  0.75  34.384843       110        2       8
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Look’s like we are back to fully tidied data with all the columns. We
just need to reassign our index back the cereal name using
`.set_index('name')`

``` python
tidy_pivot = tidy_pivot.set_index('name')
tidy_pivot.head()
```

```out
nutrition                 mfr  type  fat  sodium  fiber  carbo  potass  vitamins  shelf  weight  cups     rating  calories  protein  sugars
name                                                                                                                                       
100% Bran                   N  Cold    1     130   10.0    5.0     280        25      3     1.0  0.33  68.402973        70        4       6
100% Natural Bran           Q  Cold    5      15    2.0    8.0     135         0      3     1.0  1.00  33.983679       120        3       8
All-Bran                    K  Cold    1     260    9.0    7.0     320        25      3     1.0  0.33  59.425505        70        4       5
All-Bran with Extra Fiber   K  Cold    0     140   14.0    8.0     330        25      3     1.0  0.50  93.704912        50        4       0
Almond Delight              R  Cold    2     200    1.0   14.0       1        25      3     1.0  0.75  34.384843       110        2       8
```

Perfect\!

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
