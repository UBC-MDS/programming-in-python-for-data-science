---
type: slides
---

# Concatenation

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Up until this moment, we have been working with a single dataframe.
Single dataframes can be great to see all your data in one convenient
place, however, this is less convenient when it comes to storage space.
Many companies split their data into multiple tables and join them
together depending on what columns they need for their analysis.  
There are 2 different verbs we use for joining dataframes together:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html" target="_blank">`pd.concat()`</a>
    - A way of joining dataframes across rows or columns.
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html" target="_blank">`.merge()`</a>
    - This approach can only combine data on common columns or indices
    but have different types of joining methods. We will look into this
    in the next section.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Concatenation

Concatenation works extremely well when you have similar dataframes
where both share identical column or row index labels.  
`.concat()` can stich the 2 dataframes together either horizontally or
vertically.

<center>

<img src='/module3/concat.gif' width="600">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

For the next couple of examples, we are going to look at our candy bars
dataframe.

``` python
candy = pd.read_csv('candybars.csv', index_col=0)
candy
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
name                                                                                                                                       
Coffee Crisp           50          1        0        0       0                  1        0                0      0                   Canada
Butterfinger          184          1        1        1       0                  0        0                0      0                  America
Skor                   39          1        0        1       0                  0        0                0      0                     Both
Smarties               45          1        0        0       0                  0        0                0      1                   Canada
Twix                   58          1        0        1       0                  1        0                0      1                     Both
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
Take 5                 43          1        1        1       0                  1        0                0      0                  America
Whatchamacallits       45          1        1        0       0                  1        0                0      0                  America
Almond Joy             46          1        0        0       0                  0        1                0      0                  America
Oh Henry               51          1        1        1       0                  0        0                0      0                     Both
Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 10 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Horizontal Concatenation

`candybars2.csv` has new nutritional information about each candy bar.

``` python
candy2 = pd.read_csv('candybars2.csv', index_col=0)
candy2
```

```out
                   calories   fat  sugar
name                                    
Coffee Crisp            260  13.0   25.0
Butterfinger            798  30.0   72.0
Skor                    209  12.0   23.0
Smarties                210   6.0   33.0
Twix                    250  12.0   25.0
...                     ...   ...    ...
Take 5                  200  11.0   18.0
Whatchamacallits        237  11.0   13.0
Almond Joy              234  13.0   24.0
Oh Henry                263  13.0   26.0
Cookies and Cream       220  12.0   13.0

[25 rows x 3 columns]
```

We want to combine `candy2` with `candy` horizontally.

Both `candy1` and `candy2` have 25 rows and it looks like the index name
in the `candy2` dataframe is identical as `candy`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can combine these two dataframes using `pd.concat()` but we need to
clarify which axes to combine. We use square brackets around the
dataframes we wish to combine and since we are combining horizontally we
need to use the argument `axis=1`.

``` python
pd.concat([candy, candy2], axis=1)
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar
name                                                                                                                                                              
Coffee Crisp           50          1        0        0       0                  1        0                0      0                   Canada       260  13.0   25.0
Butterfinger          184          1        1        1       0                  0        0                0      0                  America       798  30.0   72.0
Skor                   39          1        0        1       0                  0        0                0      0                     Both       209  12.0   23.0
Smarties               45          1        0        0       0                  0        0                0      1                   Canada       210   6.0   33.0
Twix                   58          1        0        1       0                  1        0                0      1                     Both       250  12.0   25.0
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...       ...   ...    ...
Take 5                 43          1        1        1       0                  1        0                0      0                  America       200  11.0   18.0
Whatchamacallits       45          1        1        0       0                  1        0                0      0                  America       237  11.0   13.0
Almond Joy             46          1        0        0       0                  0        1                0      0                  America       234  13.0   24.0
Oh Henry               51          1        1        1       0                  0        0                0      0                     Both       263  13.0   26.0
Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both       220  12.0   13.0

[25 rows x 13 columns]
```

This results in the same 25 rows but now we have 13 columns.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Vertical Concatenation

Our second example uses new dataset`candybars_more.csv` which has 3
additional candy bars that we wish to add to the original `candy`
dataframe.

``` python
candy_more = pd.read_csv('candybars_more.csv', index_col=0)
candy_more
```

```out
              weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
name                                                                                                                                  
Kinder Bueno      43          1        0        0       0                  1        0                1      1                   Canada
5th Avenue        56          1        1        0       0                  0        0                0      0                  America
Crunch            44          1        0        0       0                  1        0                0      0                     Both
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we want to vertically combine dataframes, we use the argument
`axis=0` with `pd.concat()`.

``` python
pd.concat([candy, candy_more], axis=0)
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
name                                                                                                                                       
Coffee Crisp           50          1        0        0       0                  1        0                0      0                   Canada
Butterfinger          184          1        1        1       0                  0        0                0      0                  America
Skor                   39          1        0        1       0                  0        0                0      0                     Both
Smarties               45          1        0        0       0                  0        0                0      1                   Canada
Twix                   58          1        0        1       0                  1        0                0      1                     Both
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
Oh Henry               51          1        1        1       0                  0        0                0      0                     Both
Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both
Kinder Bueno           43          1        0        0       0                  1        0                1      1                   Canada
5th Avenue             56          1        1        0       0                  0        0                0      0                  America
Crunch                 44          1        0        0       0                  1        0                0      0                     Both

[28 rows x 10 columns]
```

After combining them now have 28 rows and the same 10 columns that all
align correctly.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Concatenating incomplete dataframes.

`pd.concat()` is not limited to complete dataframes. We can still add
dataframes together that do not have all the same rows or columns.  
Let’s take a selection of our `candy2` dataframe that we used to combine
horizontally with `candy` and save it as `slice_of_candy2`.

``` python
slice_of_candy2 = candy2.loc[['Coffee Crisp', 'Smarties', 'Take 5', 'Oh Henry']]
slice_of_candy2
```

```out
              calories   fat  sugar
name                               
Coffee Crisp       260  13.0   25.0
Smarties           210   6.0   33.0
Take 5             200  11.0   18.0
Oh Henry           263  13.0   26.0
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What happens when we concatenate `candy1` and `candy2` now that it has
fewer rows?

``` python
pd.concat([candy, slice_of_candy2], axis=1)
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar
Coffee Crisp           50          1        0        0       0                  1        0                0      0                   Canada     260.0  13.0   25.0
Butterfinger          184          1        1        1       0                  0        0                0      0                  America       NaN   NaN    NaN
Skor                   39          1        0        1       0                  0        0                0      0                     Both       NaN   NaN    NaN
Smarties               45          1        0        0       0                  0        0                0      1                   Canada     210.0   6.0   33.0
Twix                   58          1        0        1       0                  1        0                0      1                     Both       NaN   NaN    NaN
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...       ...   ...    ...
Take 5                 43          1        1        1       0                  1        0                0      0                  America     200.0  11.0   18.0
Whatchamacallits       45          1        1        0       0                  1        0                0      0                  America       NaN   NaN    NaN
Almond Joy             46          1        0        0       0                  0        1                0      0                  America       NaN   NaN    NaN
Oh Henry               51          1        1        1       0                  0        0                0      0                     Both     263.0  13.0   26.0
Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both       NaN   NaN    NaN

[25 rows x 13 columns]
```

If we scroll to the right we can see any rows that are not present in
both dataframes are replaced with `NaN`. That’s because we are using a
default argument `join='outer'`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## The Join Argument

Ok so what does `join` do then? `pd.concat()` take a specific argument
called `join` that can take the values `inner` or `outer`.

  - `inner`: Will return only the rows index values that are present in
    both the tables.
  - `outer`: Will return not only the rows that are present in both
    tables but also the rows in both tables that are unmatched.

Notice when I do the same join with `candy` and `slice_of_candy2` but
this time specifying `join='inner`.

``` python
pd.concat([candy, slice_of_candy2], axis=1, join='inner')
```

```out
              weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america  calories   fat  sugar
name                                                                                                                                                         
Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada       260  13.0   25.0
Smarties          45          1        0        0       0                  0        0                0      1                   Canada       210   6.0   33.0
Take 5            43          1        1        1       0                  1        0                0      0                  America       200  11.0   18.0
Oh Henry          51          1        1        1       0                  0        0                0      0                     Both       263  13.0   26.0
```

This only returns a dataframe with the matched rows from both columns.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

One key thing to remember that if you want to save the new dataframe,
don’t forget to assign your new dataframe to an object name. We did not
do it in this section since we didn’t need the new dataframes again\!
You’ll likely want to reuse your new dataframe unlike us so don’t forget
to save the new product\!

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
