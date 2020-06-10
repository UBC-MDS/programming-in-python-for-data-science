---
type: slides
---

# Column renaming and column dropping

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Remember our `candybars.csv` dataframe? Let’s bring it back.

``` python
df = pd.read_csv('candybars.csv')
df
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Column Renaming

There will be times where you are unsatisfied with the column names and
you may want to change them. The proper syntax to do that is with
`df.rename()`.  
The column name `available_canada_america` is a bit long. Perhaps it
would be a good idea to change it to something shorter like
`availability`. Here is how we can accomplish that:

``` python
df = df.rename(columns={'available_canada_america':'availability'})
df.head()
```

```out
           name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp      50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger     184          1        1        1       0                  0        0                0      0      America
2          Skor      39          1        0        1       0                  0        0                0      0         Both
3      Smarties      45          1        0        0       0                  0        0                0      1       Canada
4          Twix      58          1        0        1       0                  1        0                0      1         Both
```

This code uses something we’ve never seen before - {} curly brackets.
These have a special meaning but for now, you only need to concentrate
your attention on the fact that the argument `columns` needs to have the
format:

``` python
 columns={'old column name':'new column name'}
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

You can also rename multiple columns at once by simple adding a comma
between the new and old column pairs within the curly brackets.

``` python
df = df.rename(columns={'available_canada_america':'availability',
                        'weight':'weight_g'})
df.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

It’s important that we always save the dataframe to an object when
making column changes or the changes will not be saved in our dataframe.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Column Dropping

`df.drop()` is our verb to delete columns in a dataframe.

Let’s delete the column `coconut`.

``` python
df.drop(columns='coconut')
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If you scroll back to the last slide you’ll notice we didn’t save over
the dataframe object, so the dataframe `df` still will contain
`coconut`.

``` python
df.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

Let’s overwrite this and remove multiple columns at the same time. Let’s
drop `nougat` and `coconut` together. We put the columns we want to drop
in square brackets and this time we will remember to overwrite over the
`df` object.

``` python
df = df.drop(columns=['nougat', 'coconut'])
df.head(3)
```

```out
           name  weight_g  chocolate  peanuts  caramel  cookie_wafer_rice  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0                  1                0      0       Canada
1  Butterfinger       184          1        1        1                  0                0      0      America
2          Skor        39          1        0        1                  0                0      0         Both
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
