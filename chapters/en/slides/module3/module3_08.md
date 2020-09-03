---
type: slides
---

# Reshaping with pivot

Notes: <br>

---

## Pivot

<center>

<img src='/module3/cereal_long2.png' width="70%">

</center>

Notes: `.pivot()` can be used in situations to transform long dataframes
into wider ones.  
Consider the dataframe below.

How can we convert it?

---

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

Notes: Here is the same dataframe that we saw on the previous slide
named `cereal_long`. We can see there are 10 rows and the `nutrition`
column is made up of 2 variables; `calories` and `protein`.

That means there are 2 rows for each of the 5 kinds of cereal. This
explains the 10 rows (5 kinds of cereal \* 2 variables = 10 rows).

---

``` python
cereal_long.head(5)
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1    Special K   K   protein      6
2  Apple Jacks   K  calories    110
3  Apple Jacks   K   protein      2
4  Raisin Bran   K  calories    120
```

``` python
cereal_wide = cereal_long.pivot(index='name', columns='nutrition', values='value')
cereal_wide
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

Notes: We use `pivot()` in the following way to transform it into a
wider dataframe.

---

``` python
cereal_long.head(3)
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1    Special K   K   protein      6
2  Apple Jacks   K  calories    110
```

``` python
cereal_wide = cereal_long.pivot(index='name', columns='nutrition', values='value')
cereal_wide
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

`.pivot()` takes 3 arguments:

  - `index`: Used to make the new dataframe’s index.
  - `columns`: The column that currently exists but that we want to
    create new columns labels from. Each unique value in this column
    will become a new column label.
  - `values`: The name of the column that currently exists but that
    contains the cell values we want to relocate to new columns. These
    values will be displayed in the respective newly created columns.

Notes: Let’s take a closer look at the code.

---

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
cereal_wide
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

Notes: Can you see the difference?

---

<br> <br> <br> <br>

<center>

<img src='/module3/piv_cereal3.png' width="100%">

</center>

Notes: The following diagram explains what is happening in the
transformation.

---

<br> <br> <br>

<center>

<img src='/module3/piv_cereal3.png' width="100%">

</center>

``` python
cereal_wide = cereal_long.pivot(index='name', columns='nutrition', values='value')
```

Notes: Here are a few important things to notice:

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

---

## Resetting the Index

``` python
cereal_wide.head(5)
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

``` python
cereal_wide_messy = cereal_wide.reset_index()
cereal_wide_messy.head(5)
```

```out
nutrition         name  calories  protein
0          Apple Jacks       110        2
1             Cheerios       110        6
2          Raisin Bran       120        3
3            Special K       110        6
4             Wheaties       100        3
```

Notes:

Let’s take a brief detour and discuss resetting the index. Here is our
dataframe `cereal_wide`.

While pivoting we transformed the `name` column as our index.

We can transform the `name` index back into a regular column by using
the same `reset_index()` verb we learned when plotting grouped
dataframes in module 2:

---

``` python
cereal_wide_messy.head()
```

```out
nutrition         name  calories  protein
0          Apple Jacks       110        2
1             Cheerios       110        6
2          Raisin Bran       120        3
3            Special K       110        6
4             Wheaties       100        3
```

``` python
cereal_wide_cleaned = cereal_wide_messy.rename_axis('', axis='columns')
cereal_wide_cleaned.head()
```

```out
          name  calories  protein
0  Apple Jacks       110        2
1     Cheerios       110        6
2  Raisin Bran       120        3
3    Special K       110        6
4     Wheaties       100        3
```

Notes:

If we want to remove the `nutrition` label that is in the top left of
the dataframe, we can rename the “axis” using `.rename_axis()`. We
simple add in quotations what we want to rename the index label as the
first argument (we are going to rename it to something blank hence empty
quotations) and specify that in the `axis` argument that we are renaming
the “columns” index.

That looks all cleaned up\!

---

# Let’s practice what we learned\!

Notes: <br>
