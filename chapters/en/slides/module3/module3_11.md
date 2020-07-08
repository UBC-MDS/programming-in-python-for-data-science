---
type: slides
---

# Reshaping with pivot\_table

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
cereal_wider = cereal_long.pivot_table(index=['name', 'mfr'], columns='nutrition', values='value')
cereal_wider
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal_wider = cereal_long.pivot_table(index=['name','mfr'], columns='nutrition', values='value')
```

``` python
cereal_wider
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
cereal_wider.reset_index().rename_axis('', axis='columns')
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

\*Attribution: Nikolay Grozev,
<a href=" https://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/" target="_blank">Reshaping
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

Without the `keep` argument, only index labelled `1` will be identified
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

Once we have decided which row we want to keep we can use `.drop()` that
we learned in the previous Module to remove it from our original
dataframe. We use the argument `axis=0` which refers to the rows in the
dataframe and `index` which specifies the row index that we want to
drop. In this case we are going to drop the row with calories equal to
130, which is index `1`.

``` python
cereal_no_problem = cereal_problem.drop(axis=0, index=1)
cereal_no_problem
```

```out
          name mfr nutrition  value
0    Special K   K  calories    100
2    Special K   K   protein      6
3  Apple Jacks   K  calories    110
4  Apple Jacks   K   protein      2
```

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

</audio>

</html>
