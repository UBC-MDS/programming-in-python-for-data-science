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
files `sheet_name` but there are mant others that are important to know
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
following
    links:

  - [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
  - [`pd.read_excel()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)

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

We have been pretty lucky up until now that all of the data we have
loaded in has been particularly straight forward. Sometimes with data,
there are a few lines of text explaining a few important points about
the file. We do not want to include this in our dataframe and therefore
we need to specify exactly when our dataframe begins. This is where
`header` comes in. Take the next file as an example `candybars-h.csv`.

``` python
candybars = pd.read_csv('candybars-h.csv')
candybars.head()
```

```out
           name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0  Coffee Crisp    50.0        1.0      0.0      0.0     0.0                1.0      0.0              0.0    0.0                   Canada
1  Butterfinger   184.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                  America
2          Skor    39.0        1.0      0.0      1.0     0.0                0.0      0.0              0.0    0.0                     Both
3      Smarties    45.0        1.0      0.0      0.0     0.0                0.0      0.0              0.0    1.0                   Canada
4          Twix    58.0        1.0      0.0      1.0     0.0                1.0      0.0              0.0    1.0                     Both
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

We use `header=2` to indicate where our dataframe begins.

``` python
candybars = pd.read_csv('candybars-h.csv', header=2)
candybars.head()
```

```out
                Butterfinger   184    1  1.1  1.2    0  0.1  0.2  0.3  0.4  America
0                       Skor  39.0  1.0  0.0  1.0  0.0  0.0  0.0  0.0  0.0     Both
1                   Smarties  45.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  1.0   Canada
2                       Twix  58.0  1.0  0.0  1.0  0.0  1.0  0.0  0.0  1.0     Both
3  Reeses Peanutbutter Cups   43.0  1.0  1.0  0.0  0.0  0.0  0.0  0.0  1.0     Both
4               3 Musketeers  54.0  1.0  0.0  0.0  1.0  0.0  0.0  0.0  0.0  America
```

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
selects which columns to use in the dataframe. Maybe all that’s relevant
to our analysis are the columns `name`, `weight` and
`available_canada_america`. Do you remember when we were selecting
columns using `iloc` in the last module we would specified the index
position? We use a similar syntax here. We put the desired column index
positions in square brackets for the argument.

``` python
candybars = pd.read_csv('candybars.csv', usecols=[0,1,10 ])
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

## usecols

Similarly to how `nrows` specifies how many rows to read in, `usecols`
selects which columns to use in the dataframe. Maybe all that’s relevant
to our analysis are the columns `name`, `weight` and
`available_canada_america`. Do you remember when we were selecting
columns using `iloc` in the last module we would specified the index
position? We use a similar syntax here. We put the desired column index
positions in square brackets for the argument.

``` python
candybars = pd.read_csv('candybars.csv', usecols=[0,1,10 ])
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

Let’s practice before

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## true\_values and false\_values

Here are 2 arguments that can be useful if we want to add some clarity
in our dataframes.

Bringing in new `candybars-tf.csv` we have a number of columns that have
binary values of `yes` and `no` such as `chocolate`, `peanuts`,
`caramel` and `nougat`.

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

We can changes these values to more direct values such as `True` and
`False` since these are more familiar to our Python programming
Language.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

In order to change our `yes`’s to `True` and the `no`s to `False` we
need to specify **BOTH** arguments with the values in square
brackets.

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

This is now more familiar to Python. For these arguments, mmultiple
values can also be specified too.

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
