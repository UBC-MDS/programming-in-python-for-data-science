---
type: slides
---

# Reshaping with pivot

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In this section, we will explore two useful pandas functions for
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
wide dataframe, however in this case, for each data point there is a row
for each measurement.

<center>

<img src='/module3/long.png' width="25%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot

`.pivot()` can be used in situations where our data may not meet our
tidy data criteria.  
Consider the dataframe below:

<center>

<img src='/module3/cereal_long2.png' width="60%">

</center>

Here we can see that *Criterion \#1: Each row is a single observation*
does not hold. Each cereal has 2 rows for different measurements. How do
we convert it to tidy data?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is the same dataframe that we have named `cereal_long`:

``` python
cereal_long
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1    Special K   K   protein      6
2  Apple Jacks   K  calories    110
3  Apple Jacks   K   protein      2
4  Raisin Bran   K  calories    120
5  Raisin Bran   K   protein      3
6     Cheerios   G  calories    110
7     Cheerios   G   protein      6
8     Wheaties   G  calories    100
9     Wheaties   G   protein      3
```

We can see there are 14 rows and the `nutrition` column is made up of 2
variables; `calories` and `protein`. That means there are 2 rows for
each of the 7 kinds of cereal. This explains the 14 rows (7 kinds of
cereal \* 2 variables = 14 rows).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We use `pivot` in the following way to transform it into a wide
dataframe.

We:

  - Set `index` as the `name` column.
  - Target the column `nutrition` with the values contained as new
    columns labels.  
  - Specify `value` as the `values` argument.

<!-- end list -->

``` python
tidy_pivot = cereal_long.pivot(index='name', columns='nutrition', values='value')
tidy_pivot
```

```out
nutrition    calories  protein
name                          
Apple Jacks       110        2
Cheerios          110        6
Raisin Bran       120        3
Special K         110        6
Wheaties          100        3
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
cereal_long
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1    Special K   K   protein      6
2  Apple Jacks   K  calories    110
3  Apple Jacks   K   protein      2
4  Raisin Bran   K  calories    120
5  Raisin Bran   K   protein      3
6     Cheerios   G  calories    110
7     Cheerios   G   protein      6
8     Wheaties   G  calories    100
9     Wheaties   G   protein      3
```

``` python
tidy_pivot
```

```out
nutrition    calories  protein
name                          
Apple Jacks       110        2
Cheerios          110        6
Raisin Bran       120        3
Special K         110        6
Wheaties          100        3
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The following diagram explains what is happening in the transformation.

<center>

<img src='/module3/piv_cereal3.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module3/piv_cereal3.png' width="80%">

</center>

``` python
tidy_pivot = cereal_long.pivot(index='name', columns='nutrition', values='value')
```

Here are a few important things to notice:

  - Our index is reassigned to the `name` column which we assigned to
    the `index` argument. This also acts as the identifier for which
    rows in the original dataframe get compiled to a single one in the
    new dataframe.  
  - The unique values in the `nutrition` column depict what will be the
    new columns after the transformation. We assigned this in the
    `columns` argument.  
  - The values in the `value` column are transformed into the values in
    the newly created `protein` and `calories` columns. This was defined
    in the `values` argument of the code.
  - We lost the `mfr` column\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Resetting the Index

When we pivot our dataframe, we need to specify which rows are being
combined to create a single elongated row. This is determined by the
`index` argument. While pivoting we transformed the `name` column as our
index. This may not be the most ideal structure for our data and we can
adjust this and return to the original index of a column of number by
using the verb `.reset_index()`.

On our example dataset `tidy_pivot`:

``` python
tidy_pivot.head(2)
```

```out
nutrition    calories  protein
name                          
Apple Jacks       110        2
Cheerios          110        6
```

We can remove the `name` index by doing the following:

``` python
tidy_pivot_messy = tidy_pivot.reset_index()
tidy_pivot_messy.head(2)
```

```out
nutrition         name  calories  protein
0          Apple Jacks       110        2
1             Cheerios       110        6
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to remove the `nutrition` label that is in the top left of
the dataframe, we can rename the “axis” using `.rename_axis()`. We
simple add in quotations what we want to rename the index label as the
first argument (we are going to rename it tosomething blank hence empty
quotations) and specify that in the `axis` argument that we are renaming
the “columns” index.

``` python
tidy_pivot_cleaned = tidy_pivot_messy.rename_axis("", axis="columns")
tidy_pivot_cleaned.head()
```

```out
          name  calories  protein
0  Apple Jacks       110        2
1     Cheerios       110        6
2  Raisin Bran       120        3
3    Special K       110        6
4     Wheaties       100        3
```

That looks all cleaned up\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot Table

We discussed that one of the effects of using `.pivot()` on our
`cereal_long` dataframe was that the new dataframe was missing the
column `mfr`.

<center>

<img src='/module3/piv_cereal3.png' width="90%">

</center>

That’s because `.pivot()` discards any columns that are not being
directly affected by the pivot. Only the column that is specified as the
index and the columns that need to be transformed are present in the new
dataframe.

That’s where `pivot_table` steps in\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`.pivot_table()` has the same arguments as `.pivot()` but the biggest
difference is that it allows us to include multiple columns under the
`index` argument. That just means we can keep any of the columns that
are not directly affected by the pivot.

<center>

<img src='/module3/piv_table_cereal.png' width="90%">

</center>

Let’s try to convert our dataframe again but this time keeping the `mfr`
column with `.pivot_table()`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is our long dataframe:

``` python
cereal_long
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1    Special K   K   protein      6
2  Apple Jacks   K  calories    110
3  Apple Jacks   K   protein      2
4  Raisin Bran   K  calories    120
5  Raisin Bran   K   protein      3
6     Cheerios   G  calories    110
7     Cheerios   G   protein      6
8     Wheaties   G  calories    100
9     Wheaties   G   protein      3
```

We include any columns that we wish to keep under the `index` argument
contained in square brackets.

``` python
tidy_pivot2 = cereal_long.pivot_table(index=['name', 'mfr'], columns='nutrition', values='value')
tidy_pivot2
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
tidy_pivot2 = cereal_long.pivot_table(index=['name','mfr'], columns='nutrition', values='value')
```

``` python
tidy_pivot2
```

```out
nutrition        calories  protein
name        mfr                   
Apple Jacks K         110        2
Cheerios    G         110        6
Raisin Bran K         120        3
Special K   K         110        6
Wheaties    G         100        3
```

And just like before, if we want to return to our original dataframe
with a column of numbers for our index, we use `.reset_index()` and
`rename_axis()` to clean up the index label.

``` python
tidy_pivot2.reset_index().rename_axis('', axis='columns')
```

```out
          name mfr  calories  protein
0  Apple Jacks   K       110        2
1     Cheerios   G       110        6
2  Raisin Bran   K       120        3
3    Special K   K       110        6
4     Wheaties   G       100        3
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module3/piv_table_cereal.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Why use pivot at all then?

When we use `.pivot_table()` we have to proceed with caution.

We talked about how `.pivot()` and `.pivot_table()` take the arguments
`index` and `columns`. What happens if we have multiple rows with the
same `index` and `column` values?

Take the following example where we see that Special K has 2 rows with
differing values for `calories`.

<center>

<img src='/module3/problem_table.png' width="60%">

</center>

What happens when we try to pivot this?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is our dataframe:

``` python
cereal_problem
```

```out
          name mfr nutrition  value
0    Special K   K  calories    100
1    Special K   K  calories    130
2    Special K   K   protein      6
3  Apple Jacks   K  calories    110
4  Apple Jacks   K   protein      2
```

And here is what happens when we use the same arguments as before:

``` python
cereal_problem.pivot(index='name', columns='nutrition', values='value')
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): ValueError: Index contains duplicate entries, cannot reshape

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/frame.py", line 5923, in pivot
    return pivot(self, index=index, columns=columns, values=values)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/reshape/pivot.py", line 448, in pivot
    return indexed.unstack(columns)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/series.py", line 3550, in unstack
    return unstack(self, level, fill_value)
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/reshape/reshape.py", line 419, in unstack
    constructor=obj._constructor_expanddim,
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/reshape/reshape.py", line 141, in __init__
    self._make_selectors()
  File "//anaconda3/lib/python3.7/site-packages/pandas/core/reshape/reshape.py", line 179, in _make_selectors
    raise ValueError("Index contains duplicate entries, cannot reshape")
```

We get the error message above. This is a useful error message, letting
us know that there are “duplicate entries, cannot reshape” which means
there are non-unique rows. We will need us to do something before going
any further.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`.pivot()` throws an error message. This is a useful error message,
letting us know that there are “duplicate entries, cannot reshape” which
means there are non-unique rows. We will need to do something before
going any further.

<center>

<img src='/module3/problem_pivot.png' width="100%">

</center>

\*Atribution: Nikolay Grozev,
<a href=" https://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/" target="_blank">RReshaping
in Pandas - Pivot, Pivot-Table, Stack, and Unstack explained with
Pictures</a>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s see what happens when we use `.pivot_table()`:

``` python
cereal_problem.pivot_table(index=['name', 'mfr'], columns='nutrition', values='value')
```

```out
nutrition        calories  protein
name        mfr                   
Apple Jacks K         110        2
Special K   K         115        6
```

Ok, that’s odd. We don’t get an error this time but instead get a
`calories` value of 115 which is neither of the original values of 130
or 100.

`.pivot_table()` instead by default takes the average of the duplicated
columns and continues to execute.

<center>

<img src='/module3/problem_pivot_table.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we use `.pivot_table()` we recommend checking if there are
duplicate values in columns we use in the `index` and `columns`
arguments before we proceed. We can do this with the `.duplicated()`
verb by putting the columns from the `index` and `columns` arguments in
a `subset` argument. We set the argument `keep` to `False` to make sure
all the rows are identified and not just the repeated ones.

``` python
cereal_problem.duplicated(subset=['name', 'nutrition'], keep=False)
```

```out
0     True
1     True
2    False
3    False
4    False
dtype: bool
```

Without the `keep` argument, only index labeled `1` will be identified
as a duplicate.

``` python
cereal_problem.duplicated(subset=['name', 'nutrition'])
```

```out
0    False
1     True
2    False
3    False
4    False
dtype: bool
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal_problem.duplicated(subset=['name', 'nutrition'], keep=False)
```

```out
0     True
1     True
2    False
3    False
4    False
dtype: bool
```

We see that the 1st and 2nd rows are duplicates by the `True` values. We
obtain the rows from the original dataframe by filtering on the
duplicate information:

``` python
duplicate_info =cereal_problem.duplicated(subset=['name', 'nutrition'], keep=False)
cereal_problem[duplicate_info]
```

```out
        name mfr nutrition  value
0  Special K   K  calories    100
1  Special K   K  calories    130
```

Once we have decided which row we want to keep we can use `.drop()` that
we learned in the previous Module to remove it.

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
