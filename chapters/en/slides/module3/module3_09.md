---
type: slides
---

# Reshaping with Melt

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last section we discussed how `pandas` provides 2 functions for
reshaping data;
<a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
and
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
. We are going to spend this next section discussing `.melt()` which is
simply the reverse transformation of `.pivot()`.

<center>

<img src="/module3/pivot_melt.gif" width="400">

</center>

“Source: Garrick Aden-Buie,
<https://github.com/gadenbuie/tidyexplain#spread-and-gather> and Tomas
Beuzen, DSCI 523 Data Wrangling”

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Melt

Similarly to `.pivot()`, `.melt()` can be used in situations where our
data may not meet criterion \#2: *Each variable is a single column*.

In this situation the code converted the 2 columns `chocolate`and
`white_chocolate`into a single column named `chocolate_type`.

``` python
melted_candy = (candy.reset_index()
                   .melt(id_vars=['name', 'weight','multi',
                                  'available_canada_america'] , 
                        value_vars=['chocolate', 'white_chocolate'], 
                        var_name='chocolate_type', 
                        value_name='present')
)
melted_candy.head()
```

```out
           name  weight  multi available_canada_america chocolate_type  present
0  Coffee Crisp      50      0                   Canada      chocolate        1
1  Butterfinger     184      0                  America      chocolate        1
2          Skor      39      0                     Both      chocolate        1
3      Smarties      45      1                   Canada      chocolate        1
4          Twix      58      1                     Both      chocolate        1
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take some time to fully understand the arguments this verb uses.

``` python
df.melt(id_vars=['identifier columns'],
        value_vars=['variable value1', 'variable value2'],
        var_name="new column name labels",
        value_name="new column name values")
```

  - `df`: The dataframe we want to melt.
  - `id_vars`: The key identifier column(s) of the dataframe.  
  - `value_vars`: The columns that exist but that we want to create a
    single column from with the labels as the values.
  - `var_name`: The name of the new column that will contain the
    `value_vars` column labels as values.
  - `value_name`: The name of the new column that will contain the
    values of the `value_vars` columns.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Thanks to
<a href="https://github.com/apreshill/teachthat" target="_blank"> Alison
Presmanes Hill</a>, we can see exactly what is happening when we
transform a dataframe using melt.

<center>

<img src='/module3/melt_py.gif'>

</center>

`cinnamon_1`, `cardamom_2` and `nutmeg_3` column labels are relocated to
the `spice` column and the values within the 3 columns are all melted
into the `correct` column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`.melt()` is the opposite transformation of `.pivot()`. In the last
section we saw our cereal dataset widen when we pivoted the dataframe,
however, melting elongates our dataframe.

<center>

<img src='/module3/piv_melt.png'>

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s sweeten this section up a bit and practice using `.melt()` with
our candy bar dataset.

``` python
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

We can see there are 25 rows in our dataframe. There are 2 columns for
“chocolate type”; `white_chocolate` and `chocolate`. Maybe for our
analysis a single column called `chocolate_type` is better suited.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To transform this and obtain our new `chocolate_type` column, we would
specify the following arguments:

  - to keep all our other columns, we need to specify them in the
    `id_vars` argument.

<!-- end list -->

``` python
id_vars=['name', 'weight', 'peanuts', 'caramel',
        'nougat', 'cookie_wafer_rice', 'coconut',
        'multi', 'available_canada_america'] 
```

  - The columns we are converting to a single one are named `chocolate`
    and `white_chocolate` resulting in `value_vars= ['chocolate',
    'white_chocolate']`.
  - We name our new column `chocolate_type`, which we assign to the
    `var_name` argument.
  - The values within those chocolate columns will go into a new column
    named `present` therefore `value_name='present'`.

Just like with `.pivot()`, we must reset our index before doing any type
of transformation.

(And since we want to keep the changes, we makes sure to assign it to an
object)

``` python
candy_melt = (candy.reset_index()
                   .melt(id_vars=['name', 'weight', 'peanuts', 'caramel',
                                  'nougat', 'cookie_wafer_rice', 'coconut',
                                  'multi', 'available_canada_america'] , 
                        value_vars=['chocolate', 'white_chocolate'], 
                        var_name='chocolate_type', 
                        value_name='present')
              )
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
melted_candy = (candy.reset_index()
                   .melt(id_vars=['name', 'weight', 'peanuts', 'caramel',
                                  'nougat', 'cookie_wafer_rice', 'coconut',
                                  'multi', 'available_canada_america'] , 
                        value_vars=['chocolate', 'white_chocolate'], 
                        var_name='chocolate_type', 
                        value_name='present')
)
melted_candy
```

```out
                 name  weight  peanuts  caramel  nougat  cookie_wafer_rice  coconut  multi available_canada_america   chocolate_type  present
0        Coffee Crisp      50        0        0       0                  1        0      0                   Canada        chocolate        1
1        Butterfinger     184        1        1       0                  0        0      0                  America        chocolate        1
2                Skor      39        0        1       0                  0        0      0                     Both        chocolate        1
3            Smarties      45        0        0       0                  0        0      1                   Canada        chocolate        1
4                Twix      58        0        1       0                  1        0      1                     Both        chocolate        1
..                ...     ...      ...      ...     ...                ...      ...    ...                      ...              ...      ...
45             Take 5      43        1        1       0                  1        0      0                  America  white_chocolate        0
46   Whatchamacallits      45        1        0       0                  1        0      0                  America  white_chocolate        0
47         Almond Joy      46        0        0       0                  0        1      0                  America  white_chocolate        0
48           Oh Henry      51        1        1       0                  0        0      0                     Both  white_chocolate        0
49  Cookies and Cream      43        0        0       0                  1        0      0                     Both  white_chocolate        1

[50 rows x 11 columns]
```

We have 50 rows in this new dataframe which makes sense since we now
have 2 chocolate types for each candy bar ( 25 candy bars \* 2 chocolate
types = 50 rows).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To finish things off let’s reassign our index back the cereal name using
`.set_index('name')`

``` python
melted_candy = melted_candy.set_index('name')
melted_candy
```

```out
                   weight  peanuts  caramel  nougat  cookie_wafer_rice  coconut  multi available_canada_america   chocolate_type  present
name                                                                                                                                     
Coffee Crisp           50        0        0       0                  1        0      0                   Canada        chocolate        1
Butterfinger          184        1        1       0                  0        0      0                  America        chocolate        1
Skor                   39        0        1       0                  0        0      0                     Both        chocolate        1
Smarties               45        0        0       0                  0        0      1                   Canada        chocolate        1
Twix                   58        0        1       0                  1        0      1                     Both        chocolate        1
...                   ...      ...      ...     ...                ...      ...    ...                      ...              ...      ...
Take 5                 43        1        1       0                  1        0      0                  America  white_chocolate        0
Whatchamacallits       45        1        0       0                  1        0      0                  America  white_chocolate        0
Almond Joy             46        0        0       0                  0        1      0                  America  white_chocolate        0
Oh Henry               51        1        1       0                  0        0      0                     Both  white_chocolate        0
Cookies and Cream      43        0        0       0                  1        0      0                     Both  white_chocolate        1

[50 rows x 10 columns]
```

Perfect\!

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
