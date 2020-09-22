---
type: slides
---

# Slicing only columns using .loc\[\]

Notes:

<br>

---

``` python
cereal.loc[:, 'calories':'fiber']
```

```out
    calories  protein  fat  sodium  fiber
0         70        4    1     130   10.0
1        120        3    5      15    2.0
2         70        4    1     260    9.0
3         50        4    0     140   14.0
4        110        2    2     200    1.0
..       ...      ...  ...     ...    ...
72       110        2    1     250    0.0
73       110        1    1     140    0.0
74       100        3    1     230    3.0
75       100        3    1     200    3.0
76       110        2    1     200    1.0

[77 rows x 5 columns]
```

Notes:

What happens now if we wanted all the rows of the dataframe but only the
columns `calories` to `fiber`?

We can use `:` in the row postion of the `.loc[]` call to indicate we
want all the rows. So here we write `cereal.loc[:, 'calories':'fiber']`.

---

## So Far

  - `.loc[]` is used to slice columns and rows by **label** and within
    an interval.

  - We always specify **row** indexing first, then **columns**.

<!-- end list -->

``` python
cereal.loc['row name start':'row name end', 'column name start':'column name end']
```

  - If we aren’t slicing any columns, but we are slicing rows we can
    shorten that to

<!-- end list -->

``` python
df.loc[ 'row name start':'row name end']
```

  - However, the reverse is not true. If we want all the rows with only
    specific columns, we specify we want all the row first with just a
    colon `:` followed by interval of the columns:

<!-- end list -->

``` python
df.loc[:, 'column name start':'column name end']
```

  - We can read `:` as **“to”**.

  - If the indices are labeled with numbers, we do not need “quotations”
    when calling them. This is only when the labels are using letters.

Notes:

Let’s talk about what we have covered so far.

  - `.loc[]` is used to slice columns and rows by **label** and within
    an interval.

  - We always specify **row** indexing first, then **columns**.

  - If we are not slicing any columns, but we are slicing rows we only
    need to specify the row labels.

  - However, the reverse is not true. If we want all the rows with only
    specific columns, we specify rows first and therefore we would need
    to make it clear with a colon first that we are slicing all the rows
    followed by the column labels.

  - We can read `:` as **“to”**.

  - And finally, if the row index is labeled with numbers, we do not
    need “quotations” when slicing.

---

# Let’s apply what we learned\!

Notes:

<br>
