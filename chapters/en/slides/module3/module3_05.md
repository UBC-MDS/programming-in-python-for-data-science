---
type: slides
---

# Reshaping with Pivot

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In this section we will explore two useful pandas functions for
reshaping our data that can be handy to convert it into tidy data.

  - <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
    to make a wide dataframe long (convert columns to row)
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
    to make a long dataframe wide (convert rows to columns)

Before going forward we should understand the difference between
***wide*** data and ***long*** data.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Wide and long dataframes

#### Wide

We are used to seeing the data presented in a wide format, where there
is a column for each measurement. We know that with a wide format, the
data may not be tidy.

<center>

<img src='/module3/wide.png' width="30%">

</center>

### Long

A long dataframe would consist of the same information as contained in a
wide dataframe, however in this case, for each datapoint there is a row
for each measurement.

<center>

<img src='/module3/long.png' width="30%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot

`.pivot()` can be used in situations where our data may not meet
criterion \#2: *Each variable is a single column*.

It can be used to widen the dataframe by converting the variables to
their own columns that were previously being stored in a single column.

Before we go into detail, let’s introduce the code that converts this
cereal dataset

``` python
cereal_long_sample
```

```out
                  mfr  type  cups nutrition  measure
name                                                
100% Bran           N  Cold  0.33   protein        4
100% Bran           N  Cold  0.33  calories       70
100% Bran           N  Cold  0.33    sugars        6
100% Natural Bran   Q  Cold  1.00   protein        3
100% Natural Bran   Q  Cold  1.00  calories      120
100% Natural Bran   Q  Cold  1.00    sugars        8
All-Bran            K  Cold  0.33   protein        4
All-Bran            K  Cold  0.33  calories       70
```

into a wide dataset

``` python
tidy_pivot = (cereal_long_sample.reset_index()
            .pivot(index='name', columns='nutrition', values='measure')
             )
tidy_pivot
```

```out
nutrition          calories  protein  sugars
name                                        
100% Bran              70.0      4.0     6.0
100% Natural Bran     120.0      3.0     8.0
All-Bran               70.0      4.0     NaN
```

---

The code for this verb takes quite a few arguments that can be a bit
tricky to remember so we are going to explain each argument.

``` python
df.pivot(index=['index label'], columns='column name', values='new column name')
```

  - `df`: The dataframe we want to pivot.
  - `index`: Used to make the new dataframe’s index.
  - `columns`: The column that currently exists but that we want to
    create new columns labels from. Each unique value in this column
    will become a new column label.
  - `values`: The name of the column that currently exists but that
    contains the cell values we want to relocate to new columns. These
    values will be displayed in the respective newly created columns.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Resetting the Index

We must take extra precautions with the `index` argument when
transforming dataframes. This argument will only accept column labels
and not column index labels.

Before we do any type of transformation, it’s a good idea to reset and
remove and labels an index. This can be done with `.reset_index()` which
converts the index to a regular column.

On our example dataset, we see `name` as the index and we can reset it
by calling `.reset_index()`.

``` python
cereal_long_sample.head()
```

```out
                  mfr  type  cups nutrition  measure
name                                                
100% Bran           N  Cold  0.33   protein        4
100% Bran           N  Cold  0.33  calories       70
100% Bran           N  Cold  0.33    sugars        6
100% Natural Bran   Q  Cold  1.00   protein        3
100% Natural Bran   Q  Cold  1.00  calories      120
```

``` python
cereal_long_sample.reset_index().head()
```

```out
                name mfr  type  cups nutrition  measure
0          100% Bran   N  Cold  0.33   protein        4
1          100% Bran   N  Cold  0.33  calories       70
2          100% Bran   N  Cold  0.33    sugars        6
3  100% Natural Bran   Q  Cold  1.00   protein        3
4  100% Natural Bran   Q  Cold  1.00  calories      120
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The process of pivoting can be explained using the animation made by
<a href="https://github.com/apreshill/teachthat" target="_blank"> Alison
Presmanes Hill</a>. It shows exactly the relocation of values, when a
dataframe undergoes a pivot transformation.

<center>

<img src='/module3/pivot_py.gif' width="850">

</center>

We see the `var_name` values becoming new columns labels and the
`var_value` being relocated to it’s respective new column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can do the same thing for our cereal dataframe as an example. The
diagram below shows the column `nutrition` being spread into 2 columns
named `calories` and `protein` which are the two unique values contained
in that column.

<center>

<img src='/module3/pivot_cereal.png' width="850">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s attempt this with code.

Our dataframe that we want to tidy looks like this:

``` python
cereal_long
```

```out
                    mfr  type  weight  cups     rating nutrition  measure
name                                                                     
100% Bran             N  Cold     1.0  0.33  68.402973   protein        4
100% Bran             N  Cold     1.0  0.33  68.402973  calories       70
100% Bran             N  Cold     1.0  0.33  68.402973    sugars        6
100% Natural Bran     Q  Cold     1.0  1.00  33.983679   protein        3
100% Natural Bran     Q  Cold     1.0  1.00  33.983679  calories      120
...                  ..   ...     ...   ...        ...       ...      ...
Wheaties              G  Cold     1.0  1.00  51.592193   protein        3
Wheaties              G  Cold     1.0  1.00  51.592193  calories      100
Wheaties Honey Gold   G  Cold     1.0  0.75  36.187559  calories      110
Wheaties Honey Gold   G  Cold     1.0  0.75  36.187559   protein        2
Wheaties Honey Gold   G  Cold     1.0  0.75  36.187559    sugars        8

[231 rows x 7 columns]
```

We can see there are 231 rows and the `nutrition` column is made up of 3
variables; `protein`, `calories` and `sugar`. That means there are 3
rows for each of the 77 kinds of cereal which explains the 231 rows (77
kinds of cereal \* 3 variables = 231 rows).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To transform this into tidy data we would specify the following
arguments.  
\- Set `index` as the `name` column.  
\- Target the column `nutrition` with the values contained as new
columns labels.  
\- Specify `measure` as the values associated with each of the new
columns.

Also, we can’t forget to reset the index\!  
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

Can you see the difference?

``` python
cereal_long.head()
```

```out
                  mfr  type  weight  cups     rating nutrition  measure
name                                                                   
100% Bran           N  Cold     1.0  0.33  68.402973   protein        4
100% Bran           N  Cold     1.0  0.33  68.402973  calories       70
100% Bran           N  Cold     1.0  0.33  68.402973    sugars        6
100% Natural Bran   Q  Cold     1.0  1.00  33.983679   protein        3
100% Natural Bran   Q  Cold     1.0  1.00  33.983679  calories      120
```

``` python
tidy_pivot.head()
```

```out
nutrition                  calories  protein  sugars
name                                                
100% Bran                        70        4       6
100% Natural Bran               120        3       8
All-Bran                         70        4       5
All-Bran with Extra Fiber        50        4       0
Almond Delight                  110        2       8
```

We are now back to 77 rows and it looks like we’ve tidied our data up\!
There appears to be a problem though. `.pivot()` works well when we are
only concerned with the columns we are pivoting but as we can see, we
lost all our other columns in the dataset like `type`, `weight` and
`cups`.  
There is a solution for this and it’s called `.pivot_table()`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot\_table()

`.pivot_table()` works with multiple indexes (we will take about this
shortly). That just means we can keep all the columns that we are not
pivoting. Let’s attempt fixing our untidy data again but this time,
keeping all our columns.

``` python
tidy_pivot = (cereal_long.reset_index()
            .pivot_table(index=['name','mfr', 'type',
                                'weight', 'cups', 'rating'],
                         columns='nutrition', 
                         values='measure').reset_index()
             )
tidy_pivot.head()
```

```out
nutrition                       name mfr  type  weight  cups     rating  calories  protein  sugars
0                          100% Bran   N  Cold     1.0  0.33  68.402973        70        4       6
1                  100% Natural Bran   Q  Cold     1.0  1.00  33.983679       120        3       8
2                           All-Bran   K  Cold     1.0  0.33  59.425505        70        4       5
3          All-Bran with Extra Fiber   K  Cold     1.0  0.50  93.704912        50        4       0
4                     Almond Delight   R  Cold     1.0  0.75  34.384843       110        2       8
```

After we pivot, we have multiple column indexes which we should reset to
avoid any confusion. Don’t worry, we wil talk about multiple indexes in
this module.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To get our dataframe back to a structure we are used to, we have to
`.reset_index()` and then reassign a single index such as `name` using
`.set_index()`.

``` python
tidy_pivot = tidy_pivot.reset_index().set_index('name')
tidy_pivot.head()
```

```out
nutrition                  index mfr  type  weight  cups     rating  calories  protein  sugars
name                                                                                          
100% Bran                      0   N  Cold     1.0  0.33  68.402973        70        4       6
100% Natural Bran              1   Q  Cold     1.0  1.00  33.983679       120        3       8
All-Bran                       2   K  Cold     1.0  0.33  59.425505        70        4       5
All-Bran with Extra Fiber      3   K  Cold     1.0  0.50  93.704912        50        4       0
Almond Delight                 4   R  Cold     1.0  0.75  34.384843       110        2       8
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
