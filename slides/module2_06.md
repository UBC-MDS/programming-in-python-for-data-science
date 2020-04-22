---
type: slides
---

# Reading Arguments

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Arguments

We have talked about quite a few different arguments when reading in
different file types such as `index_col`, `delimiter` and for excel
files `sheet_name` but there are many others that are important to know
so we can to read in the file the way we want it to appear in our code.

To recap from the last module, `index_col` is an argument that indicates
which column will be acting as our index label. In most of the cases we
have encountered, it was the very first column.

We are going to introduce a few:

  - `header`
  - `nrows`
  - `usecols`
  - `true_values` and `false_values`

If you wish to know more, you can find the documentation at the
following links:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html" target="_blank">`pd.read_csv()`</a>
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html" target="_blank">`pd.read_excel()`</a>

*Please note that these arguments can be used for both `pd.read_csv()`
and `pd.read_excel()`.*

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## header

We have been lucky up until now that all the data we have loaded in has
been particularly straight forward. Sometimes with data, there are a few
lines of text explaining a few important points about the file. We do
not want to include this in our dataframe and therefore we need to
specify exactly when our dataframe begins. This is where `header` comes
in. Take a look at the
<a href="https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/blob/master/slides/candybars-h.csv" target="_blank">`candybars-h.csv`
file </a> as an example.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

If we look at the data with a regular text editor, the data doesn’t
start until line 3 which would be the equivalent of position 2 (since we
begin at index 0).

<img src='module2/header_textedit.png'  alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

If we load this data in without any arguments this is the result.

``` python
candybars = pd.read_csv('candybars-h.csv')
candybars.head()
```

```out
  This dataset was created by Hayley Boyce in February 2020. Unnamed: 1 Unnamed: 2 Unnamed: 3 Unnamed: 4 Unnamed: 5         Unnamed: 6 Unnamed: 7       Unnamed: 8 Unnamed: 9               Unnamed: 10
0  Note this is not a complete dataset and there ...                NaN        NaN        NaN        NaN        NaN                NaN        NaN              NaN        NaN                       NaN
1                                               name             weight  chocolate    peanuts    caramel     nougat  cookie_wafer_rice    coconut  white_chocolate      multi  available_canada_america
2                                       Coffee Crisp                 50          1          0          0          0                  1          0                0          0                    Canada
3                                       Butterfinger                184          1          1          1          0                  0          0                0          0                   America
4                                               Skor                 39          1          0          1          0                  0          0                0          0                      Both
```

We see that there are no clear column names and things are in quite a
disarray.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We use `header=2` to indicate where our dataframe begins. (2 being the
index position the column labels)

``` python
candybars = pd.read_csv('candybars-h.csv', header=2)
candybars.head()
```

```out
           name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0  Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1  Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2          Skor      39          1        0        1       0                  0        0                0      0                     Both
3      Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4          Twix      58          1        0        1       0                  1        0                0      1                     Both
```

That’s looking much better.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## nrows

nrows is useful when you only want to load in a portion of a file.
Perhaps the file you have is large and you only want a sample of it.
`nrows` will limit the of rows of file to read. Take our regular
`candybar.csv` file but perhaps we only want 7 of the rows.

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

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## usecols

Similarly to how `nrows` specifies how many rows to read in, `usecols`
selects which columns to load from the data. Perhaps the only columns
relevant to our analysis are the columns `name`, `weight` and
`available_canada_america`. We can forgo the other columns when reading
the data in. The `usecols` argument accepts either index positions or
labels. We put the desired column index positions in square brackets for
the argument.

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

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Or we could use the column labels, also in square brackets.

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

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## true\_values and false\_values

These 2 arguments can be useful if we want to add some clarity in our
dataframes. Bringing in new `candybars-tf.csv` we have several columns
that have binary values of `yes` and `no` such as `chocolate`,
`peanuts`, `caramel` and `nougat`.

``` python
candybars = pd.read_csv('candybars-tf.csv' )
candybars
```

```out
                 name  weight chocolate peanuts caramel nougat cookie_wafer_rice coconut white_chocolate multi available_canada_america
0        Coffee Crisp      50       yes      no      no     no               yes      no              no    no                   Canada
1        Butterfinger     184       yes     yes     yes     no                no      no              no    no                  America
2                Skor      39       yes      no     yes     no                no      no              no    no                     Both
3            Smarties      45       yes      no      no     no                no      no              no   yes                   Canada
4                Twix      58       yes      no     yes     no               yes      no              no   yes                     Both
..                ...     ...       ...     ...     ...    ...               ...     ...             ...   ...                      ...
20             Take 5      43       yes     yes     yes     no               yes      no              no    no                  America
21   Whatchamacallits      45       yes     yes      no     no               yes      no              no    no                  America
22         Almond Joy      46       yes      no      no     no                no     yes              no    no                  America
23           Oh Henry      51       yes     yes     yes     no                no      no              no    no                     Both
24  Cookies and Cream      43        no      no      no     no               yes      no             yes    no                     Both

[25 rows x 11 columns]
```

We can change these values to something more familiar to the Python
programming language such as `True` and `False`.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

To change the `yes` values to `True` and the `no` values to `False` we
need to specify **BOTH** arguments with the values we wish to change in
square brackets.

``` python
candybars = pd.read_csv('candybars-tf.csv', true_values= ['yes'], false_values= ['no'] )
candybars
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0        Coffee Crisp      50       True    False    False   False               True    False            False  False                   Canada
1        Butterfinger     184       True     True     True   False              False    False            False  False                  America
2                Skor      39       True    False     True   False              False    False            False  False                     Both
3            Smarties      45       True    False    False   False              False    False            False   True                   Canada
4                Twix      58       True    False     True   False               True    False            False   True                     Both
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
20             Take 5      43       True     True     True   False               True    False            False  False                  America
21   Whatchamacallits      45       True     True    False   False               True    False            False  False                  America
22         Almond Joy      46       True    False    False   False              False     True            False  False                  America
23           Oh Henry      51       True     True     True   False              False    False            False  False                     Both
24  Cookies and Cream      43      False    False    False   False               True    False             True  False                     Both

[25 rows x 11 columns]
```

This is now more familiar to Python.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can also specify multiple values as either `True` or `False`.

``` python
candybars = pd.read_csv('candybars-tf.csv', true_values= ['Canada', 'Both'], false_values= ['America'] ) 
candybars
```

```out
                 name  weight chocolate peanuts caramel nougat cookie_wafer_rice coconut white_chocolate multi  available_canada_america
0        Coffee Crisp      50       yes      no      no     no               yes      no              no    no                      True
1        Butterfinger     184       yes     yes     yes     no                no      no              no    no                     False
2                Skor      39       yes      no     yes     no                no      no              no    no                      True
3            Smarties      45       yes      no      no     no                no      no              no   yes                      True
4                Twix      58       yes      no     yes     no               yes      no              no   yes                      True
..                ...     ...       ...     ...     ...    ...               ...     ...             ...   ...                       ...
20             Take 5      43       yes     yes     yes     no               yes      no              no    no                     False
21   Whatchamacallits      45       yes     yes      no     no               yes      no              no    no                     False
22         Almond Joy      46       yes      no      no     no                no     yes              no    no                     False
23           Oh Henry      51       yes     yes     yes     no                no      no              no    no                      True
24  Cookies and Cream      43        no      no      no     no               yes      no             yes    no                      True

[25 rows x 11 columns]
```

Now all the `Canada` and `Both` values have been converted to `True` and
`America` values to `False`.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
