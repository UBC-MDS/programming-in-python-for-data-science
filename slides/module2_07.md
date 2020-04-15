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
you want want to change them. The proper syntax to do that is with
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

    columns={"old column name" : "new-column-name"}

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Creation

Creating a new column is extremely useful when we need to add additional
information. Perhaps we want to covert the weight from grams to ounces.
We can add that to our current dataframe using the `assign` function and
naming the column `weight_oz`. The conversion for 1 oz = 28.3495 g.

``` python
df = df.assign(weight_oz= df['weight']/28.3495)
df
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability  weight_oz
name                                                                                                                                      
Coffee Crisp           50          1        0        0       0                  1        0                0      0       Canada   1.763700
Butterfinger          184          1        1        1       0                  0        0                0      0      America   6.490414
Skor                   39          1        0        1       0                  0        0                0      0         Both   1.375686
Smarties               45          1        0        0       0                  0        0                0      1       Canada   1.587330
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...          ...        ...
Whatchamacallits       45          1        1        0       0                  1        0                0      0      America   1.587330
Almond Joy             46          1        0        0       0                  0        1                0      0      America   1.622604
Oh Henry               51          1        1        1       0                  0        0                0      0         Both   1.798974
Cookies and Cream      43          0        0        0       0                  1        0                1      0         Both   1.516782

[25 rows x 11 columns]
```

It’s important that we always save the dataframe to an object or the
column will not be saved in our dataframe.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Dropping

Ok, so we know how to create a new column but what if I want to drop 1
or multiple columns? In a similar way to `df.assign()`, `df,drop()` will
delete selected columns. Let’s delete the column `weight_oz` that we
just made.

``` python
df = df.drop( columns= 'weight_oz')
df
```

```out
                   weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
name                                                                                                                           
Coffee Crisp           50          1        0        0       0                  1        0                0      0       Canada
Butterfinger          184          1        1        1       0                  0        0                0      0      America
Skor                   39          1        0        1       0                  0        0                0      0         Both
Smarties               45          1        0        0       0                  0        0                0      1       Canada
...                   ...        ...      ...      ...     ...                ...      ...              ...    ...          ...
Whatchamacallits       45          1        1        0       0                  1        0                0      0      America
Almond Joy             46          1        0        0       0                  0        1                0      0      America
Oh Henry               51          1        1        1       0                  0        0                0      0         Both
Cookies and Cream      43          0        0        0       0                  1        0                1      0         Both

[25 rows x 10 columns]
```

Again make sure that we always save the dataframe to an object or the
column will not be deleted from the dataframe.

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
