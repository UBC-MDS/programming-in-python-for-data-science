---
type: slides
---

# Column renaming and column dropping

Notes:

<br>

---

``` python
candy = pd.read_csv('candybars.csv')
candy
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2                Skor      39          1        0        1       0                  0        0                0      0                     Both
3            Smarties      45          1        0        0       0                  0        0                0      1                   Canada
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0                  America
22         Almond Joy      46          1        0        0       0                  0        1                0      0                  America
23           Oh Henry      51          1        1        1       0                  0        0                0      0                     Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 11 columns]
```

Notes:

Remember our `candybars.csv` dataframe? Let’s bring it back and save it
as object named `candy`.

---

## Column Renaming

``` python
candy = candy.rename(columns={'available_canada_america':'availability'})
candy
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0       Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0      America
2                Skor      39          1        0        1       0                  0        0                0      0         Both
3            Smarties      45          1        0        0       0                  0        0                0      1       Canada
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0      America
22         Almond Joy      46          1        0        0       0                  0        1                0      0      America
23           Oh Henry      51          1        1        1       0                  0        0                0      0         Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0         Both

[25 rows x 11 columns]
```

``` python
 columns={'old column name':'new column name'}
```

Notes:

There will be times where you are unsatisfied with the column names and
you may want to change them. The proper syntax to do that is with
`.rename()`.

The column name `available_canada_america` is a bit long. Perhaps it
would be a good idea to change it to something shorter like
`availability`.

Here is how we can accomplish that.

This code uses something we’ve never seen before - {} curly braces, also
called curly brackets. These have a special meaning but for now, you
only need to concentrate your attention on the fact that the argument
`columns` needs to have the format shown on the slide.

---

``` python
candy = candy.rename(columns={'available_canada_america':'availability',
                        'weight':'weight_g'})
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

Notes:

You can also rename multiple columns at once by adding a comma between
the new and old column pairs within the curly brackets.

It’s important that we always save the dataframe to an object when
making column changes or the changes will not be saved in our dataframe.

---

## Column Dropping

``` python
candy.drop(columns='coconut')
```

```out
                 name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  white_chocolate  multi availability
0        Coffee Crisp        50          1        0        0       0                  1                0      0       Canada
1        Butterfinger       184          1        1        1       0                  0                0      0      America
2                Skor        39          1        0        1       0                  0                0      0         Both
3            Smarties        45          1        0        0       0                  0                0      1       Canada
..                ...       ...        ...      ...      ...     ...                ...              ...    ...          ...
21   Whatchamacallits        45          1        1        0       0                  1                0      0      America
22         Almond Joy        46          1        0        0       0                  0                0      0      America
23           Oh Henry        51          1        1        1       0                  0                0      0         Both
24  Cookies and Cream        43          0        0        0       0                  1                1      0         Both

[25 rows x 10 columns]
```

Notes:

`.drop()` is the verb we use to delete columns in a dataframe.

Let’s delete the column `coconut` by specifying it in the `columns`
argument of the `drop` verb.

---

``` python
candy.drop(columns='coconut')
```

<br>

``` python
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

``` python
candy = candy.drop(columns=['nougat', 'coconut'])
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  cookie_wafer_rice  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0                  1                0      0       Canada
1  Butterfinger       184          1        1        1                  0                0      0      America
2          Skor        39          1        0        1                  0                0      0         Both
3      Smarties        45          1        0        0                  0                0      1       Canada
4          Twix        58          1        0        1                  1                0      1         Both
```

Notes:

If you look again at the code we just wrote you’ll notice we didn’t save
over the dataframe object, so the dataframe `candy` still will contain
the `coconut` column.

Let’s overwrite the dataframe and remove multiple columns at the same
time. Let’s drop `nougat` and `coconut` together.

We put the columns we want to drop in square brackets and this time we
will remember to overwrite over the `candy` object.

Now when we call `candy.head()` it reflects the dropped columns.

---

# Let’s apply what we learned\!

Notes:

<br>
