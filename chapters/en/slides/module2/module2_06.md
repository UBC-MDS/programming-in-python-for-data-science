---
type: slides
---

# Reading arguments

Notes: <br>

---

## Arguments

Here, we are going to introduce different arguments for `pd.read_csv()`
and `pd.read_excel()`:

  - `index_col`
  - `header`
  - `nrows`
  - `usecols`

If you wish to know more, you can find the documentation at the
following links:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html" target="_blank">`pd.read_csv()`</a>
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html" target="_blank">`pd.read_excel()`</a>

Notes:

When we load in our data we use different arguments to make sure it’s
organized how we want it.

`delimiter` is an argument we have already discussed that instructs on
how to separate each value in the data.

This is only the tip of the iceberg. There are many others that are
helpful when reading in our data.

---

## index\_col

``` python
df = pd.read_csv('cereal.csv', index_col="name")
df.head()
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
df = pd.read_csv('cereal.csv', index_col=0)
df.head()
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

Notes: `index_col` is an argument that indicates which column will be
acting as the index label. In most of the cases we have encountered, we
did not use this argument. For the majority of the data we have seen,
each dataframe’s index was just a column of with a unique number for
each row.

We can, however, specify a column to be the index. It’s in our best
interest that the column we choose have unique values.  
For our `cereal.csv` let’s specify the `name` column as our index.

The `index_col` argument also take in positions. the `name` column in
our data in in the 0th position so we can also specify the index like we
show here.

---

## header

<img src='/module2/header_textedit.png'  alt="404 image"/>

Notes:

We have been lucky up until now that all the data we have loaded in has
been particularly straightforward. Sometimes with data, there are a few
lines of text explaining important points about the file. We do not want
to include this in our dataframe and therefore we need to specify
exactly when our dataframe begins. This is where `header` comes in.

Take a look at the
<a href="https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/blob/master/slides/candybars-h.csv" target="_blank">`candybars-h.csv`
file </a> as an example.

If we look at the data with a regular text editor, the data doesn’t
start until the 3rd line which would be the equivalent of position 2
(since we begin at index 0).

---

``` python
candybars = pd.read_csv('candybars-h.csv')
candybars
```

```out
   This dataset was created by Hayley Boyce in February 2020. Unnamed: 1 Unnamed: 2 Unnamed: 3 Unnamed: 4 Unnamed: 5         Unnamed: 6 Unnamed: 7       Unnamed: 8 Unnamed: 9               Unnamed: 10
0   Note this is not a complete dataset and there ...                NaN        NaN        NaN        NaN        NaN                NaN        NaN              NaN        NaN                       NaN
1                                                name             weight  chocolate    peanuts    caramel     nougat  cookie_wafer_rice    coconut  white_chocolate      multi  available_canada_america
2                                        Coffee Crisp                 50          1          0          0          0                  1          0                0          0                    Canada
3                                        Butterfinger                184          1          1          1          0                  0          0                0          0                   America
4                                                Skor                 39          1          0          1          0                  0          0                0          0                      Both
..                                                ...                ...        ...        ...        ...        ...                ...        ...              ...        ...                       ...
22                                             Take 5                 43          1          1          1          0                  1          0                0          0                   America
23                                   Whatchamacallits                 45          1          1          0          0                  1          0                0          0                   America
24                                         Almond Joy                 46          1          0          0          0                  0          1                0          0                   America
25                                           Oh Henry                 51          1          1          1          0                  0          0                0          0                      Both
26                                  Cookies and Cream                 43          0          0          0          0                  1          0                1          0                      Both

[27 rows x 11 columns]
```

Notes:

If we load this data without any arguments, we get this as the output.

We see that there are no clear column names and things are in quite a
disarray.

---

``` python
candybars = pd.read_csv('candybars-h.csv', header=2)
candybars
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2                Skor      39          1        0        1       0                  0        0                0      0                     Both
3            Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4                Twix      58          1        0        1       0                  1        0                0      1                     Both
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
20             Take 5      43          1        1        1       0                  1        0                0      0                  America
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0                  America
22         Almond Joy      46          1        0        0       0                  0        1                0      0                  America
23           Oh Henry      51          1        1        1       0                  0        0                0      0                     Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 11 columns]
```

Notes:

We use `header=2` to indicate where our dataframe begins (2 being the
index position or the row that contains the column labels).

That’s looking much better.

---

## nrows

``` python
candybars = pd.read_csv('candybars.csv', nrows=7)
candybars
```

```out
                        name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0               Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1               Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2                       Skor      39          1        0        1       0                  0        0                0      0                     Both
3                   Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4                       Twix      58          1        0        1       0                  1        0                0      1                     Both
5  Reeses Peanutbutter Cups       43          1        1        0       0                  0        0                0      1                     Both
6               3 Musketeers      54          1        0        0       1                  0        0                0      0                  America
```

Notes:

`nrows` is an argument that is useful when you only want to load in a
slice of the dataframe.

Perhaps the file you have is large and you only want a sample of it.
`nrows` will limit the number of rows from the file to read in.

Take our regular `candybar.csv` file, where we only want 7 of the rows
of data.

---

## usecols

``` python
candybars = pd.read_csv('candybars.csv', usecols=[0, 1, 10])
candybars
```

```out
                 name  weight available_canada_america
0        Coffee Crisp      50                   Canada
1        Butterfinger     184                  America
2                Skor      39                     Both
3            Smarties      45                   Canada
4                Twix      58                     Both
..                ...     ...                      ...
20             Take 5      43                  America
21   Whatchamacallits      45                  America
22         Almond Joy      46                  America
23           Oh Henry      51                     Both
24  Cookies and Cream      43                     Both

[25 rows x 3 columns]
```

Notes:

Similarly to how `nrows` specifies how many rows to read in, `usecols`
selects which columns to load from the data. Perhaps the only columns
relevant to our analysis are the columns `name`, `weight` and
`available_canada_america`. We can forgo the other columns when reading
the data in.

In a similar way to selecting columns using `.iloc[]`, we put the
desired column index positions in square brackets for the argument.

---

``` python
candybars = pd.read_csv('candybars.csv', usecols=['name', 'weight', 'available_canada_america'])
candybars
```

```out
                 name  weight available_canada_america
0        Coffee Crisp      50                   Canada
1        Butterfinger     184                  America
2                Skor      39                     Both
3            Smarties      45                   Canada
4                Twix      58                     Both
..                ...     ...                      ...
20             Take 5      43                  America
21   Whatchamacallits      45                  America
22         Almond Joy      46                  America
23           Oh Henry      51                     Both
24  Cookies and Cream      43                     Both

[25 rows x 3 columns]
```

Notes:

The `usecols` argument accepts either index positions or labels so we
could also use the column names in square brackets.

---

# Let’s apply what we learned\!

Notes:

<br>
