---
type: slides
---

# Column Renaming and Column Creation

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Remember our `candybars.csv` dataframe? Let’s bring it back.

``` python
df = pd.read_csv('candybars.csv', index_col=0)
df
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
name                                                                                                                                       
Coffee Crisp           50          1        0        0       0                  1        0                0      0                   Canada
Butterfinger          184          1        1        1       0                  0        0                0      0                  America
Skor                   39          1        0        1       0                  0        0                0      0                     Both
Smarties               45          1        0        0       0                  0        0                0      1                   Canada
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
Whatchamacallits       45          1        1        0       0                  1        0                0      0                  America
Almond Joy             46          1        0        0       0                  0        1                0      0                  America
Oh Henry               51          1        1        1       0                  0        0                0      0                     Both
Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 10 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Renaming

There will be times where you are unsatisfied with the column names and
you may want to change them. The proper syntax to do that is with
`df.rename()`.  
The column named `available_canada_america` is a bit long. Perhaps it
would be a good idea to change it something shorter like `availability`.
Here is the code to do that:

``` python

df = df.rename(columns={'available_canada_america' : 'availability'})
df.head()
```

```out
              weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
name                                                                                                                      
Coffee Crisp      50          1        0        0       0                  1        0                0      0       Canada
Butterfinger     184          1        1        1       0                  0        0                0      0      America
Skor              39          1        0        1       0                  0        0                0      0         Both
Smarties          45          1        0        0       0                  0        0                0      1       Canada
Twix              58          1        0        1       0                  1        0                0      1         Both
```

This code uses something we’ve never seen before - {} curly brackets.
These have a special meaning but for now, you only need to concentrate
your attention on the fact that the argument `columns` needs to have the
format:

``` 
 columns={'old-column-name' : 'new-column-name'}
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

You can also rename multiple columns at once by simple adding a comma
between the new and old column pairs between the curly brackets.

``` python
df = df.rename(columns={'available_canada_america' : 'availability',
                        'weight' : 'weight_g'})
df.head()
```

```out
              weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
name                                                                                                                        
Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
Butterfinger       184          1        1        1       0                  0        0                0      0      America
Skor                39          1        0        1       0                  0        0                0      0         Both
Smarties            45          1        0        0       0                  0        0                0      1       Canada
Twix                58          1        0        1       0                  1        0                0      1         Both
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Creation

Creating a new column is extremely useful when we need to add additional
information. Perhaps we want to convert the weight from grams to ounces.
We can add that to our current dataframe using the `assign` function and
naming the column `weight_oz`.  
First we are going to save the conversion factor of ounces to grams in
an object named `g_to_oz`.

``` python
g_to_oz = 28.3495
```

If we reference any of the dataframe’s columns in the the creation of a
new column, we use single square brackets.

``` python
df = df.assign(weight_oz= df['weight_g']/g_to_oz)
df
```

```out
                   weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability  weight_oz
name                                                                                                                                        
Coffee Crisp             50          1        0        0       0                  1        0                0      0       Canada   1.763700
Butterfinger            184          1        1        1       0                  0        0                0      0      America   6.490414
Skor                     39          1        0        1       0                  0        0                0      0         Both   1.375686
Smarties                 45          1        0        0       0                  0        0                0      1       Canada   1.587330
...                     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...        ...
Whatchamacallits         45          1        1        0       0                  1        0                0      0      America   1.587330
Almond Joy               46          1        0        0       0                  0        1                0      0      America   1.622604
Oh Henry                 51          1        1        1       0                  0        0                0      0         Both   1.798974
Cookies and Cream        43          0        0        0       0                  1        0                1      0         Both   1.516782

[25 rows x 11 columns]
```

It’s important that we always save the dataframe to an object when
renaming or adding a new column or the changes will not be saved in our
dataframe.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

On the topic of making new columns, we can sum multiple columns in a
dataframe and assign the results to a new column. Perhaps we want a
column named `ingredients` which shows the total number of ingredients.
This could be calculated by taking the sum of the columns from
`chocolate` to `white_chocolate`. We can do this in two ways.

The long way:

``` python
df.assign(ingredients= df['chocolate'] +  df['peanuts'] + df['caramel'] +
                       df['nougat'] + df['cookie_wafer_rice'] + df['coconut'] + df['white_chocolate'])
```

```out
                   weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability  weight_oz  ingredients
name                                                                                                                                                     
Coffee Crisp             50          1        0        0       0                  1        0                0      0       Canada   1.763700            2
Butterfinger            184          1        1        1       0                  0        0                0      0      America   6.490414            3
Skor                     39          1        0        1       0                  0        0                0      0         Both   1.375686            2
Smarties                 45          1        0        0       0                  0        0                0      1       Canada   1.587330            1
...                     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...        ...          ...
Whatchamacallits         45          1        1        0       0                  1        0                0      0      America   1.587330            3
Almond Joy               46          1        0        0       0                  0        1                0      0      America   1.622604            2
Oh Henry                 51          1        1        1       0                  0        0                0      0         Both   1.798974            3
Cookies and Cream        43          0        0        0       0                  1        0                1      0         Both   1.516782            2

[25 rows x 12 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

The faster way\!

``` python
df.assign(ingredients= df.loc[: , 'chocolate' : 'white_chocolate'].sum(axis=1))
```

```out
                   weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability  weight_oz  ingredients
name                                                                                                                                                     
Coffee Crisp             50          1        0        0       0                  1        0                0      0       Canada   1.763700            2
Butterfinger            184          1        1        1       0                  0        0                0      0      America   6.490414            3
Skor                     39          1        0        1       0                  0        0                0      0         Both   1.375686            2
Smarties                 45          1        0        0       0                  0        0                0      1       Canada   1.587330            1
...                     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...        ...          ...
Whatchamacallits         45          1        1        0       0                  1        0                0      0      America   1.587330            3
Almond Joy               46          1        0        0       0                  0        1                0      0      America   1.622604            2
Oh Henry                 51          1        1        1       0                  0        0                0      0         Both   1.798974            3
Cookies and Cream        43          0        0        0       0                  1        0                1      0         Both   1.516782            2

[25 rows x 12 columns]
```

We have seen `df.loc[: , 'chocolate' : 'white_chocolate']` before and we
know that this means we are selecting all the rows of a dataframe and
only the columns between `chocolate` and `white_chocolate`. We have seen
`df.sum()` calculate the sum of each dataframe column. `axis=1` is new
to us and simply means that instead of calculating the column total, it
calculates the row total.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Dropping

Ok, so we know how to create a new column but what if I want to drop one
or multiple columns? While `df.assign()` creates columns, `df,drop()`
will delete selected columns. Let’s delete the column `weight_oz` that
we just made.

``` python
df.drop( columns= 'weight_oz')
```

```out
                   weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
name                                                                                                                             
Coffee Crisp             50          1        0        0       0                  1        0                0      0       Canada
Butterfinger            184          1        1        1       0                  0        0                0      0      America
Skor                     39          1        0        1       0                  0        0                0      0         Both
Smarties                 45          1        0        0       0                  0        0                0      1       Canada
...                     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...
Whatchamacallits         45          1        1        0       0                  1        0                0      0      America
Almond Joy               46          1        0        0       0                  0        1                0      0      America
Oh Henry                 51          1        1        1       0                  0        0                0      0         Both
Cookies and Cream        43          0        0        0       0                  1        0                1      0         Both

[25 rows x 10 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

If you scroll back to the last slide you’ll notice we didn’t save over
the dataframe so the dataframe `df` still will contain `weight_oz`.

``` python
df.head()
```

```out
              weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability  weight_oz
name                                                                                                                                   
Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada   1.763700
Butterfinger       184          1        1        1       0                  0        0                0      0      America   6.490414
Skor                39          1        0        1       0                  0        0                0      0         Both   1.375686
Smarties            45          1        0        0       0                  0        0                0      1       Canada   1.587330
Twix                58          1        0        1       0                  1        0                0      1         Both   2.045891
```

Let’s overwrite this and remove `weight_oz` and `coconut` together. We
put the columns we want to drop in square brackets.

``` python
df = df.drop(columns=['weight_oz', 'coconut'])
df.head()
```

```out
              weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  white_chocolate  multi availability
name                                                                                                               
Coffee Crisp        50          1        0        0       0                  1                0      0       Canada
Butterfinger       184          1        1        1       0                  0                0      0      America
Skor                39          1        0        1       0                  0                0      0         Both
Smarties            45          1        0        0       0                  0                0      1       Canada
Twix                58          1        0        1       0                  1                0      1         Both
```

Notes: Script here

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
