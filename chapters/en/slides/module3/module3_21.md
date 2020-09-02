---
type: slides
---

# Joining dataframes using merge

Notes: <br>

---

<center>

<img src='/module3/mergex.gif' width="800">

</center>

Notes:

We discussed concatenation in the last section and it how it glues
dataframes together, but what if we needed to combine dataframes of
different sizes where rows need to be matched up?

<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html" target="_blank">`.merge()`</a>
if a verb that give more precision and options when we join dataframes.

We compared `.merge()` in the last section to stitching fabric together,
where we line up the patterns of each piece of cloth.

Unlike `pd.concat()`, `.merge()` can only combined dataframes
horizontally but it can do so in many different ways.

---

## Introducing the Data

Let’s use a subset of the candy bars dataset to explain this concept
further.

``` python
candy = pd.read_csv('candybars.csv', nrows=5, usecols=['name', 'weight', 'chocolate', 'peanuts'])
candy.head()
```

```out
           name  weight  chocolate  peanuts
0  Coffee Crisp      50          1        0
1  Butterfinger     184          1        1
2          Skor      39          1        0
3      Smarties      45          1        0
4          Twix      58          1        0
```

`candy` has a column labeled `name` which has unique candy bar names.

Notes:

With `.merge()`, we need to identify a column in each dataframe that
acts as a connection between them.

It’s a column where the values in Dataframe A are the same values to
those in Dataframe B.

In the easiest situations both columns are named the same thing, but
that doesn’t have to be the case.

---

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

Let’s load in the next dataset:

``` python
candy2m = pd.read_csv('candybars_merge.csv')
candy2m
```

```out
   id_number  calories  fat  sugar chocolate_bar
0      45623       798   30   72.0  Butterfinger
1      34534       262    8   40.0  3 Musketeers
2      32686       220   12   25.0          Aero
3      12482       260   13   25.0  Coffee Crisp
4      85254       244   16   41.2  Kinder Bueno
```

Notes:

This dataframe has new columns and rows not in the `candy` dataframe (`3
Musketeers`, `Aero`, and `Kinder Bueno`). We can see that a column named
`chocolate_bar` is the same variable as the `name` column in the `candy`
dataframe.

---

First, we decide which dataframe will be our left dataframe by
implementing the merge verb on the selected dataframe. We are going to
choose `candy` as our left dataframe.

``` python
candy.merge(...)
```

Next, we specify the right dataframe as the first argument in
`.merge()`. In our case, that’s `candy2m`.

``` python
candy.merge(candy2m, ...)
```

The last step, which is the bulk of the work, is specifying the
arguments.

We need to make sure we indicate which columns are the identifying key
columns for each dataframe and what type of joining we want in our
resulting dataframe.

Notes:

When we combine dataframes using `.merge()`, it’s quite different than
`pd.concat()`.

---

## Key Columns

`.merge()` needs arguments that identify a common **key** column. This
is a column present in both dataframes which contain common values.

To choose our key columns in each dataframe, we use the following
arguments:

  - `left_on` - The left dataframe identifying key column label.
  - `right_on` - The right dataframe identifying key column label.

Notes:

Key columns do not need to be named identically.

For example:  
Dataframe A can have a column labelled `cereal` and Dataframe B could
have a column labelled `product_name` that both share cereal names.

---

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
candy2m
```

```out
   id_number  calories  fat  sugar chocolate_bar
0      45623       798   30   72.0  Butterfinger
1      34534       262    8   40.0  3 Musketeers
2      32686       220   12   25.0          Aero
3      12482       260   13   25.0  Coffee Crisp
4      85254       244   16   41.2  Kinder Bueno
```

Notes:

Our `candy` dataframe which we said was our left dataframe, would use
the argument `left_on='name'`.

our `candy2m` dataframe is our right dataframe and would use the
argument `right_on='chocolate_bar'`.

---

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar')
```

```out
           name  weight  chocolate  peanuts  id_number  calories  fat  sugar chocolate_bar
0  Coffee Crisp      50          1        0      12482       260   13   25.0  Coffee Crisp
1  Butterfinger     184          1        1      45623       798   30   72.0  Butterfinger
```

Notes:

We combine that with the earlier code to get the following dataframe.

Great, we’ve combined the 2 dataframes horizontally. In the future, we
may want to drop the columns named `chocolate_bar` or rename it before
we merge.

If our identifying columns are named the same in both dataframes,
`.merge()` only keeps one of them.

Ok so what happened? We now only have 2 rows\! We seemed to have lost
all the rows that are not in both columns.

This is because `.merge()` uses a default joining method called `inner`
join, which returns only the rows present in both dataframes. We can
change that with the argument `how`.

---

## how

This argument specifies ***“how”*** our dataframes are joined.

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar', how='inner')
```

```out
           name  weight  chocolate  peanuts  id_number  calories  fat  sugar chocolate_bar
0  Coffee Crisp      50          1        0      12482       260   13   25.0  Coffee Crisp
1  Butterfinger     184          1        1      45623       798   30   72.0  Butterfinger
```

<br>

<img src='/module3/inner.png' width="900">

Notes:

We mentioned that the default argument value`inner` which will only keep
the rows with identifying column values that are present in both
dataframes.

---

But there are 4 types of joins we could choose from for the `how`
argument:

  - `inner`
  - `outer`
  - `left`
  - `right`

Notes: <br>

---

  - `outer`: Will return not only the rows with identifying column
    values that are present in both tables but all the rows in both
    tables. If there are any rows where any of the column values are
    missing, it will be filled with a `NaN` value.

<!-- end list -->

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar', how='outer')
```

```out
           name  weight  chocolate  peanuts  id_number  calories   fat  sugar chocolate_bar
0  Coffee Crisp    50.0        1.0      0.0    12482.0     260.0  13.0   25.0  Coffee Crisp
1  Butterfinger   184.0        1.0      1.0    45623.0     798.0  30.0   72.0  Butterfinger
2          Skor    39.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN
3      Smarties    45.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN
4          Twix    58.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN
5           NaN     NaN        NaN      NaN    34534.0     262.0   8.0   40.0  3 Musketeers
6           NaN     NaN        NaN      NaN    32686.0     220.0  12.0   25.0          Aero
7           NaN     NaN        NaN      NaN    85254.0     244.0  16.0   41.2  Kinder Bueno
```

Notes: Let’s colour coordinate this table and explore it on the next
slide.

---

<br> <br> <br>

<img src='/module3/outer.png' width="900">

Notes:

Here we see that `Coffee Crisp` and `Butterfinger` have complete rows.
Rows from the left dataframe that were not present in the right
dataframe are `Skor`, `Smarties` and `Twix` and therefore have `NaN`
values for columns from the right table. The opposite occurs for the
values `3 Musketeers`, `Aero` and `Kinder Bueno` which are present in
the right dataframe and not the left one. This results in `NaN` for
values in the left dataframe columns.

---

  - `left`: This will only output the rows that are in the left
    dataframe and if they are missing from the right dataframe, `NaN`
    values will occur. No candy bars that are only present in the right
    dataframe will be present.

<!-- end list -->

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar', how='left')
```

```out
           name  weight  chocolate  peanuts  id_number  calories   fat  sugar chocolate_bar
0  Coffee Crisp      50          1        0    12482.0     260.0  13.0   25.0  Coffee Crisp
1  Butterfinger     184          1        1    45623.0     798.0  30.0   72.0  Butterfinger
2          Skor      39          1        0        NaN       NaN   NaN    NaN           NaN
3      Smarties      45          1        0        NaN       NaN   NaN    NaN           NaN
4          Twix      58          1        0        NaN       NaN   NaN    NaN           NaN
```

<img src='/module3/left.png' width="750">

Notes:

Here we can see the values `3 Musketeers`, `Aero` and `Kinder Bueno` are
not present in the resulting dataframe as they are only present in the
right one.

---

  - `right`: Will only output the rows that are in the right dataframe
    and if they are missing from the left dataframe, `NaN` values will
    occur. No candy bars that are only present in the left dataframe
    will be present.

<!-- end list -->

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar', how='right')
```

```out
           name  weight  chocolate  peanuts  id_number  calories  fat  sugar chocolate_bar
0  Coffee Crisp    50.0        1.0      0.0      12482       260   13   25.0  Coffee Crisp
1  Butterfinger   184.0        1.0      1.0      45623       798   30   72.0  Butterfinger
2           NaN     NaN        NaN      NaN      34534       262    8   40.0  3 Musketeers
3           NaN     NaN        NaN      NaN      32686       220   12   25.0          Aero
4           NaN     NaN        NaN      NaN      85254       244   16   41.2  Kinder Bueno
```

<img src='/module3/right.png' width="750">

Notes:

We can see that the rows `Skor`, `Smarties` and `Twix` that were only
present in the left dataframe, have been dropped.

One thing that all 4 joins have in common, is they all will have the
same columns labels that came from both dataframes.

---

## indicator

`indicator` makes a new column name `_merge` and informs us from which
dataframe the row originated from.

``` python
candy.merge(candy2m, left_on='name', right_on='chocolate_bar', how='outer', indicator=True)
```

```out
           name  weight  chocolate  peanuts  id_number  calories   fat  sugar chocolate_bar      _merge
0  Coffee Crisp    50.0        1.0      0.0    12482.0     260.0  13.0   25.0  Coffee Crisp        both
1  Butterfinger   184.0        1.0      1.0    45623.0     798.0  30.0   72.0  Butterfinger        both
2          Skor    39.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN   left_only
3      Smarties    45.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN   left_only
4          Twix    58.0        1.0      0.0        NaN       NaN   NaN    NaN           NaN   left_only
5           NaN     NaN        NaN      NaN    34534.0     262.0   8.0   40.0  3 Musketeers  right_only
6           NaN     NaN        NaN      NaN    32686.0     220.0  12.0   25.0          Aero  right_only
7           NaN     NaN        NaN      NaN    85254.0     244.0  16.0   41.2  Kinder Bueno  right_only
```

Notes:

If we want to do an outer join and show all the possible rows from both
dataframes there is a useful argument called `indicator`.

Here we can see three possible values `left_only`, `right_only` or
`both` which informs us if the row came from the left dataframe, the
right dataframe or if the row index label is shared between both
dataframes.

---

# Let’s practice what we learned\!

Notes: <br>
