---
type: slides
---

# Merge

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We discussed concatenation in the last section and it covers quite a
number of things so what would we need a second verb for?
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html" target="_blank">`.merge()`</a>
gives more joining options and unlike `pd.concat()`, where we identify
like rows purely on the index labels, `merge()` can select which column
to use as the identifer in each dataframe.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Column Identifier

`.merge` give mores versatility when assigning columns to act as
identifiers. For examples, we can use the index on one dataframe and a
column label on the other, indexes from both dataframes or no indexes at
all\!

Let bring back the candybar dataset to explain this concept further.

``` python
candy = pd.read_csv('candybars.csv', index_col=0)
candy.head()
```

```out
              weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
name                                                                                                                                  
Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
Butterfinger     184          1        1        1       0                  0        0                0      0                  America
Skor              39          1        0        1       0                  0        0                0      0                     Both
Smarties          45          1        0        0       0                  0        0                0      1                   Canada
Twix              58          1        0        1       0                  1        0                0      1                     Both
```

Candy clearly has an index label of `name` which has unique candy bar
names.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

With the next dataset, we load it without assigning an index.

``` python
candy2m = pd.read_csv('candybars_merge.csv')
candy2m
```

```out
    calories   fat  sugar chocolate_bar
0        798  30.0   72.0  Butterfinger
1        250  12.0   25.0          Twix
2        262   8.0   40.0  3 Musketeers
3        239  12.0   22.0        KitKat
4        275  13.0   32.0     Babe Ruth
5        220  12.0   25.0          Aero
6        228   8.5   30.5          Mars
7        210   8.0   22.0      Crunchie
8        310  18.0   19.0    Wonderbar 
9        263  13.0   26.0      Oh Henry
10       244  16.0   41.2  Kinder Bueno
11       270  13.0   26.0    5th Avenue
12       220  11.0   24.0        Crunch
```

This dataframe has new columns and three new rows not in the `candy`
dataframe (`Kinder Bueno`, `5th Avenue`, `Crunch`) The column name that
identifies the rows is named `chocolate_bar` something quite different
than `name` index from `candy`. If we were to use `pd.concat()` to join
`candy` and `candy2m` it would be a little challenging, however
`.merge()` makes this a little easier for us.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we use merge it’s quite different than `pd.concat()`. First we
decide which dataframe will be our left dataframe by implementing the
merge verb on the selected df.

``` python
candy.merge(...)
```

Next we specify the right dataframe as the first argument in `.merge()`

``` python
candy.merge(candy2m)
```

The last step, which is the bulk of the work, is specifying the
arguments. We need to make sure we indicate which columns are the
identifying columns for each dataframe and what type of joining we want
in our resulting dataframe.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Merge Arguments

  - `left_on` - indicates the left dataframe identifying column label.
  - `right_on` = indicate the right dataframe identifying column label.

Or if one of the columns is an index: - `left_index` - Set to `True` if
the identifying column is the index in the left dataframe. -
`right_index` - Set to `True` if the identifying column is the index in
the right dataframe.

In the example we are using, our left dataframe identifying column is
the index labeled `name` and the right dataframe’s identifying column is
`chocolate_bar`.

``` python
candy.merge(candy2m, left_index=True, right_on='chocolate_bar')
```

```out
   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar chocolate_bar
0     184          1        1        1       0                  0        0                0      0                  America       798  30.0   72.0  Butterfinger
1      58          1        0        1       0                  1        0                0      1                     Both       250  12.0   25.0          Twix
2      54          1        0        0       1                  0        0                0      0                  America       262   8.0   40.0  3 Musketeers
3      45          1        0        0       0                  1        0                0      1                     Both       239  12.0   22.0        KitKat
4      60          1        1        1       1                  0        0                0      0                  America       275  13.0   32.0     Babe Ruth
5      42          1        0        0       0                  0        0                0      0                   Canada       220  12.0   25.0          Aero
6      51          1        0        1       1                  0        0                0      0                     Both       228   8.5   30.5          Mars
7      26          1        0        0       0                  0        0                0      0                   Canada       210   8.0   22.0      Crunchie
8      58          1        1        1       0                  0        0                0      0                   Canada       310  18.0   19.0    Wonderbar 
9      51          1        1        1       0                  0        0                0      0                     Both       263  13.0   26.0      Oh Henry
```

Great\! we’ve combined the 2 dataframes horozontally (in the future we
will likely will want to rename `chocolate_bar` and assign it as an
index again). This join used the default `inner` join, which returns
only the rows present in both dataframes. We can change that with the
argument `how`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## how

We talked about `inner` and `outer` joins from the last section but we
have 2 more joins to discuss: - `left`: Will only output the rows that
are in the left dataframe and if they are missing from the right
dataframe, `NaN` values will occur.

``` python
candy.merge(candy2m, left_index=True, right_on='chocolate_bar', how='left')
```

```out
     weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar      chocolate_bar
NaN      50          1        0        0       0                  1        0                0      0                   Canada       NaN   NaN    NaN       Coffee Crisp
0.0     184          1        1        1       0                  0        0                0      0                  America     798.0  30.0   72.0       Butterfinger
NaN      39          1        0        1       0                  0        0                0      0                     Both       NaN   NaN    NaN               Skor
NaN      45          1        0        0       0                  0        0                0      1                   Canada       NaN   NaN    NaN           Smarties
1.0      58          1        0        1       0                  1        0                0      1                     Both     250.0  12.0   25.0               Twix
..      ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...       ...   ...    ...                ...
NaN      43          1        1        1       0                  1        0                0      0                  America       NaN   NaN    NaN             Take 5
NaN      45          1        1        0       0                  1        0                0      0                  America       NaN   NaN    NaN   Whatchamacallits
NaN      46          1        0        0       0                  0        1                0      0                  America       NaN   NaN    NaN         Almond Joy
9.0      51          1        1        1       0                  0        0                0      0                     Both     263.0  13.0   26.0           Oh Henry
NaN      43          0        0        0       0                  1        0                1      0                     Both       NaN   NaN    NaN  Cookies and Cream

[25 rows x 14 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

  - `right`: Will only output the rows that are in the right dataframe
    and if they are missing from the left dataframe, `NaN` values will
    occur.

<!-- end list -->

``` python
candy.merge(candy2m, left_index=True, right_on='chocolate_bar', how='right')
```

```out
    weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar chocolate_bar
0    184.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                  America       798  30.0   72.0  Butterfinger
1     58.0        1.0      0.0      1.0     0.0                1.0      0.0              0.0    1.0                     Both       250  12.0   25.0          Twix
2     54.0        1.0      0.0      0.0     1.0                0.0      0.0              0.0    0.0                  America       262   8.0   40.0  3 Musketeers
3     45.0        1.0      0.0      0.0     0.0                1.0      0.0              0.0    1.0                     Both       239  12.0   22.0        KitKat
4     60.0        1.0      1.0      1.0     1.0                0.0      0.0              0.0    0.0                  America       275  13.0   32.0     Babe Ruth
5     42.0        1.0      0.0      0.0     0.0                0.0      0.0              0.0    0.0                   Canada       220  12.0   25.0          Aero
6     51.0        1.0      0.0      1.0     1.0                0.0      0.0              0.0    0.0                     Both       228   8.5   30.5          Mars
7     26.0        1.0      0.0      0.0     0.0                0.0      0.0              0.0    0.0                   Canada       210   8.0   22.0      Crunchie
8     58.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                   Canada       310  18.0   19.0    Wonderbar 
9     51.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                     Both       263  13.0   26.0      Oh Henry
10     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN       244  16.0   41.2  Kinder Bueno
11     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN       270  13.0   26.0    5th Avenue
12     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN       220  11.0   24.0        Crunch
```

One thing that all 4 joins have in common, is they all will have the
same columns labels that came from both dataframes.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## indicator

If we want to do an outer join and show all the possible rows from both
dataframes. a useful argument is `indicator`. `indicator` makes a new
column name `_merge` and informs us from which dataframe the row
originated from.

``` python
candy.merge(candy2m, left_index=True, right_on='chocolate_bar', how='outer', indicator=True)
```

```out
      weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar      chocolate_bar      _merge
NaN     50.0        1.0      0.0      0.0     0.0                1.0      0.0              0.0    0.0                   Canada       NaN   NaN    NaN       Coffee Crisp   left_only
0.0    184.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                  America     798.0  30.0   72.0       Butterfinger        both
NaN     39.0        1.0      0.0      1.0     0.0                0.0      0.0              0.0    0.0                     Both       NaN   NaN    NaN               Skor   left_only
NaN     45.0        1.0      0.0      0.0     0.0                0.0      0.0              0.0    1.0                   Canada       NaN   NaN    NaN           Smarties   left_only
1.0     58.0        1.0      0.0      1.0     0.0                1.0      0.0              0.0    1.0                     Both     250.0  12.0   25.0               Twix        both
...      ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...       ...   ...    ...                ...         ...
9.0     51.0        1.0      1.0      1.0     0.0                0.0      0.0              0.0    0.0                     Both     263.0  13.0   26.0           Oh Henry        both
NaN     43.0        0.0      0.0      0.0     0.0                1.0      0.0              1.0    0.0                     Both       NaN   NaN    NaN  Cookies and Cream   left_only
10.0     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN     244.0  16.0   41.2       Kinder Bueno  right_only
11.0     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN     270.0  13.0   26.0         5th Avenue  right_only
12.0     NaN        NaN      NaN      NaN     NaN                NaN      NaN              NaN    NaN                      NaN     220.0  11.0   24.0             Crunch  right_only

[28 rows x 15 columns]
```

Here we can see three possible values `left_only`, `right_only` or
`both` which informs us if the row came from the left daframe, the right
dataframe or from both dataframes.

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
