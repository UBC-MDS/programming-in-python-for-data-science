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

We are used to seeing the cereal data in a wide format, where there is a
column for each measurement. We’ve already experienced that not all wide
dataframes are tidy

<center>

<img src='/module3/wide.png' width="30%">

</center>

#### Long

A long dataframe would consist of the same information as contained in a
wide dataframe, however in this case, for each data point, there is a
row for each measurement. Similarly to how not all wide dataframes are
tidy, neither are all long dataframes.

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

`.pivot()` can be used in situations to transform our long dataframes
into wide ones.  
Consider the dataframe below:

<center>

<img src='/module3/cereal_long2.png' width="60%">

</center>

How can we convert it though? Notes: Script here

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

``` python
cereal_long.head(2)
```

```out
        name mfr nutrition  value
0  Special K   K  calories    110
1  Special K   K   protein      6
```

We use `pivot` in the following way to transform it into a wide
dataframe.

  - Set `index` as the `name` column.
  - Target the column `nutrition` with the values contained as new
    columns labels.  
  - Specify `value` as the `values` argument.

<!-- end list -->

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
cereal_wide = cereal_long.pivot(index='name', columns='nutrition', values='value')
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

Let’s take a brief detour and discuss resetting the index.

Here is our dataset `cereal_wide`:

``` python
cereal_wide.head(2)
```

```out
nutrition    calories  protein
name                          
Apple Jacks       110        2
Cheerios          110        6
```

While pivoting we transformed the `name` column as our index.

We can remove the `name` index by doing the following:

``` python
cereal_wide_messy = cereal_wide.reset_index()
cereal_wide_messy.head(2)
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

If we want to remove the `nutrition` label that is in the top left of
the dataframe, we can rename the “axis” using `.rename_axis()`. We
simple add in quotations what we want to rename the index label as the
first argument (we are going to rename it to something blank hence empty
quotations) and specify that in the `axis` argument that we are renaming
the “columns” index.

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

That looks all cleaned up\!

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
