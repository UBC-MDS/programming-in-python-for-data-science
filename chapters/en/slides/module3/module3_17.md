---
type: slides
---

# Concatenation

Notes: <br>

---

There are 2 different verbs we will use for joining dataframes together:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html" target="_blank">`pd.concat()`</a>

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html" target="_blank">`.merge()`</a>

Notes: Up until this moment, we have been working with a single
dataframe.

Many organizations split their data into multiple tables and join them
together depending on what columns they need for their analysis.

There are 2 different verbs we will use for joining dataframes together:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html" target="_blank">`pd.concat()`</a>;
    A forceful way of joining dataframes across rows or columns. A
    useful analogy is the gluing or taping of 2 pieces of paper together
    so the shapes match up.

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html" target="_blank">`.merge()`</a>
    A more precision based approach for combining data on common columns
    or indices. This can be compared to stitching fabric together so
    that the pattern/print lines up.

---

## Concatenation

<center>

<img src='/module3/concatx.gif' width="630">

</center>

Notes:

Concatenation works extremely well when you have similar dataframes
which both share identical column or row index labels.

`pd.concat()` can glue the 2 dataframes together either horizontally or
vertically.

In this animation you can see that the peices are joined in the order
that was presented and the pattern does not necessarily match up.

---

``` python
candy = pd.read_csv('candybars.csv').loc[:4, 'name': 'peanuts']
candy
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
```

Notes:

For the next couple of examples, we are going to look at concatenating a
subset of our original candy bars dataframe.

This dataframe has 5 rows and 4 columns.

---

## Horizontal Concatenation

``` python
candy
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
```

``` python
candy2 = pd.read_csv('candy_bars2.csv')
candy2
```

```out
           name  calories  fat  sugar
0  Coffee Crisp       260   13     25
1  Butterfinger       798   30     72
2          Skor       209   12     23
3      Smarties       210    6     33
4          Twix       250   12     25
```

Notes:

`candy_bars2.csv` is a new dataframe that has additional nutritional
information about each candy bar like the columns `calories` `fat` and
`sugar`. You’ll notice that this dataframe has the same number and order
of candy bars.

We want to combine `candy2` with `candy` horizontally.

---

``` python
candy_nutrition = pd.concat([candy, candy2], axis=1)
candy_nutrition
```

```out
           name  weight  chocolate  peanuts          name  calories  fat  sugar
0  Coffee Crisp      50          1        0  Coffee Crisp       260   13     25
1  Butterfinger     184          1        1  Butterfinger       798   30     72
2          Skor      39          1        0          Skor       209   12     23
3      Smarties      45          1        0      Smarties       210    6     33
4          Twix      58          1        0          Twix       250   12     25
```

This results in the same 4 rows but now we have 8 columns.

Notes:

We can combine these two dataframes using `pd.concat()` but we need to
clarify on which axis to combine.

We use square brackets around the dataframes we wish to glue together.
In the context of dataframes, it’s normal to refer to `axis=1` as the
columns of the dataframe and `axis=0` as the rows.

Since we are performing a horizontal concatenation, we need to use the
argument `axis=1` to glue them along the column axis.

---

``` python
candy_nutrition
```

```out
           name  weight  chocolate  peanuts          name  calories  fat  sugar
0  Coffee Crisp      50          1        0  Coffee Crisp       260   13     25
1  Butterfinger     184          1        1  Butterfinger       798   30     72
2          Skor      39          1        0          Skor       209   12     23
3      Smarties      45          1        0      Smarties       210    6     33
4          Twix      58          1        0          Twix       250   12     25
```

``` python
candy_nutrition.loc[:,~candy_nutrition.columns.duplicated()]
```

```out
           name  weight  chocolate  peanuts  calories  fat  sugar
0  Coffee Crisp      50          1        0       260   13     25
1  Butterfinger     184          1        1       798   30     72
2          Skor      39          1        0       209   12     23
3      Smarties      45          1        0       210    6     33
4          Twix      58          1        0       250   12     25
```

Notes: After inspection, we can see that there are 2 `name` columns,
which isn’t necessary.

Is there a convenient way to remove duplicated columns? Fortunately
there is\!

We can remove any duplicate columns by using both `.duplicated()`,
`.loc[]` and the *Tilde* operator we discussed in Module 2.

This removed one of the `name` columns. But let’s inspect this code a
bit more carefully.

---

``` python
candy_nutrition.columns.duplicated()
```

```out
array([False, False, False, False,  True, False, False, False])
```

``` python
~candy_nutrition.columns.duplicated()
```

```out
array([ True,  True,  True,  True, False,  True,  True,  True])
```

Notes:

`.columns.duplicated()` shows us whether a column is duplicated by
assigning the column position with either a `True` or `False` value.

Since we need to instead keep all `False` columns and not the `True`
values, we can easily use the *Tilde* operator to convert all the
`False` values to `True` and vice versa.

---

``` python
candy_nutrition_cleaned = candy_nutrition.loc[:,~candy_nutrition.columns.duplicated()]
candy_nutrition_cleaned
```

```out
           name  weight  chocolate  peanuts  calories  fat  sugar
0  Coffee Crisp      50          1        0       260   13     25
1  Butterfinger     184          1        1       798   30     72
2          Skor      39          1        0       209   12     23
3      Smarties      45          1        0       210    6     33
4          Twix      58          1        0       250   12     25
```

Notes:

When we combine this with `.loc[]` to select which columns to display,
Python will only select columns that were not identified as duplicates.

---

## Vertical Concatenation

``` python
candy
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
```

``` python
candy_more = pd.read_csv('candybars_more.csv')
candy_more
```

```out
           name  weight  chocolate  peanuts
0  Kinder Bueno      43          1        0
1    5th Avenue      56          1        1
2        Crunch      44          1        0
```

Notes:

The new dataset `candybars_more.csv` has 3 additional candy bars that we
wish to add to the original `candy` dataframe. The columns in this
dataframe have the same order as in the `candy` dataframe.

---

``` python
large_candybars = pd.concat([candy, candy_more], axis=0)
large_candybars
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
0  Kinder Bueno      43          1        0
1    5th Avenue      56          1        1
2        Crunch      44          1        0
```

Notes:

When we want to vertically combine dataframes (add rows), we use the
argument `axis=0` with `pd.concat()`.

After combining them, there are now 8 rows and the same 4 columns. But
wait\! The index column has non-unique values.

---

``` python
large_candybars
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
0  Kinder Bueno      43          1        0
1    5th Avenue      56          1        1
2        Crunch      44          1        0
```

``` python
large_candybars_cleaned = large_candybars.reset_index(drop=True)
large_candybars_cleaned
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
5  Kinder Bueno      43          1        0
6    5th Avenue      56          1        1
7        Crunch      44          1        0
```

Notes:

We can reset the index with `reset_index()` and the argument `drop=True`
to remove the original index:

---

## Be careful of order\!

``` python
candy
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
```

``` python
snacksize_candybars = pd.read_csv('snacksize_candybars.csv')
snacksize_candybars
```

```out
           name  calories  fat  sugar
0  Butterfinger       798   30     72
1          Skor       209   12     23
2          Twix       250   12     25
3  Coffee Crisp       260   13     25
4      Smarties       210    6     33
```

Notes:

`pd.concat()` is great when our dataframes have the same order for each
observation. What happens if our dataframes have different orders for
the candy bars?

Let’s use an horizontal concatenation example with the
dataframe`snacksize_candybars.csv`. This data contains the candy bars
from `candy` in a shuffled order.

---

``` python
pd.concat([candy, snacksize_candybars], axis=1)
```

```out
           name  weight  chocolate  peanuts          name  calories  fat  sugar
0  Coffee Crisp      50          1        0  Butterfinger       798   30     72
1  Butterfinger     184          1        1          Skor       209   12     23
2          Skor      39          1        0          Twix       250   12     25
3      Smarties      45          1        0  Coffee Crisp       260   13     25
4          Twix      58          1        0      Smarties       210    6     33
```

Notes:

What happens when we concatenate `candy` and `snacksize_candybars` now
that it has shuffled mix-matched rows?

Oh no. This does not look good. You can see that the 2 `name` columns
have different values in each row which means this concatenation would
produce incorrect results\!

---

### Remember…

<center>

<img src='/module3/concatx.gif' width="600">

</center>

Notes:

The biggest takeaway remark with concatenation is that it works well
when we are trying to glue two dataframes together horizontally or
vertically where the rows and columns are in the same order.

If your dataframes don’t have the same row values, your data will be
displayed incorrectly and therefore your results will also have no
meaning.

---

# Let’s apply what we learned\!

Notes: <br>
