---
type: slides
---

# Column Arithmetic and Creation

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Doing some sort of transformation on the columns of a dataframe will
most likely come up in your analysis somewhere and it’s not always
straight forward. Let’s welcome back the `cereal.csv` data we have
worked with in Module 1.

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

Attribution:  
*“[80 Cereals](https://www.kaggle.com/crawford/80-cereals/)” (c) by
[Chris Crawford](https://www.linkedin.com/in/crawforc3/) is licensed
under [Creative Commons Attribution-ShareAlike 3.0
Unported](http://creativecommons.org/licenses/by-sa/3.0/)*

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To make things especially clear, for the next few scenarios let only use
the first 5 rows of the dataset.

``` python
df = df.iloc[0:5]
df
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

Let’s explore the next scenario. Perhaps we recently read the cereal
data’s documentation explaining that the `fat` column is being expressed
as the number of grams of fat above 2.  
This means that the fat content of each cereal is actually an additional
2 grams. How can we rectify this?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We need to add 2 to each of the row’s fat value.

<br>

<center>

<img src='/module2/plus2.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is where some magic happens. Python doesn’t require us to make a
whole column filled with 2s to get the result we want. It would simply
add 2 to each column.

``` python
df['fat'] + 2
```

```out
name
100% Bran                    3
100% Natural Bran            7
All-Bran                     3
All-Bran with Extra Fiber    2
Almond Delight               4
Name: fat, dtype: int64
```

See how each row has changed in value? When we do any type of operations
on columns, we use single square brackets.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can do the same thing with multiplication/division too.  
let’s multiply the rating of each cereal by 2.  
In Python we use `*` for multiplication.

``` python
df['rating'] * 2
```

```out
name
100% Bran                    136.805946
100% Natural Bran             67.967358
All-Bran                     118.851010
All-Bran with Extra Fiber    187.409824
Almond Delight                68.769686
Name: rating, dtype: float64
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Every row’s value is changed by the operation.

<center>

<img src='/module2/times2.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We are not limited to simply taking a column and transforming it by a
single number. We can do operations involving multiple columns as well.
Perhaps we wanted to know the amount of sugar (`sugar`) per cup of
cereal (`cups`).

The expected result would look something like this:

<center>

<img src='/module2/sugarcups.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Remember with any column operation we use only single square brackets on
our columns.  
To get our desired output of sugar content per cup our code looks like
this:

``` python
df['sugars']/df['cups']
```

```out
name
100% Bran                    18.181818
100% Natural Bran             8.000000
All-Bran                     15.151515
All-Bran with Extra Fiber     0.000000
Almond Delight               10.666667
dtype: float64
```

Each sugar row value is divided by its respected cups value.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Just to stress the point of why we use single square brackets for our
operations, here is what happens when we use double square brackets:

``` python
df[['sugars']]/df[['cups']]
```

```out
                           cups  sugars
name                                   
100% Bran                   NaN     NaN
100% Natural Bran           NaN     NaN
All-Bran                    NaN     NaN
All-Bran with Extra Fiber   NaN     NaN
Almond Delight              NaN     NaN
```

This doesn’t appear very useful.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Up until now, all of these operations have been done without being added
to our cereal dataframe. Let’s explore how we can add new columns to our
complete cereal dataframe.

``` python
df = pd.read_csv('cereal.csv', index_col=0)
df
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Trix                        G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
Wheat Chex                  R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
Wheaties                    G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
Wheaties Honey Gold         G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 15 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Column Creation

In the next scenario, we have decided that a column in the dataframe
that shows the weight of each cereal in grams instead of ounces is
needed.

We are going to save the conversion factor of grams to ounces in an
object named `oz_to_g` to add some clarity and flexibility to our code.

Let’s start with just the operation for this desired result:

``` python
oz_to_g = 28.3495
df['weight']*oz_to_g
```

```out
name
100% Bran                    28.3495
100% Natural Bran            28.3495
All-Bran                     28.3495
All-Bran with Extra Fiber    28.3495
                              ...   
Trix                         28.3495
Wheat Chex                   28.3495
Wheaties                     28.3495
Wheaties Honey Gold          28.3495
Name: weight, Length: 77, dtype: float64
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Next, we combine our operation with the implementation of adding it as a
new column to the dataframe. The verb `.assign()` allows us to specify a
column name to our operation using just an equal sign `=`.

We are going to name our new column `weight_g`.

``` python
df = df.assign(weight_g=df['weight']*oz_to_g)
df.head()
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  ...  potass  vitamins  shelf  weight  cups     rating  weight_g
name                                                                        ...                                                            
100% Bran                   N  Cold        70        4    1     130   10.0  ...     280        25      3     1.0  0.33  68.402973   28.3495
100% Natural Bran           Q  Cold       120        3    5      15    2.0  ...     135         0      3     1.0  1.00  33.983679   28.3495
All-Bran                    K  Cold        70        4    1     260    9.0  ...     320        25      3     1.0  0.33  59.425505   28.3495
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0  ...     330        25      3     1.0  0.50  93.704912   28.3495
Almond Delight              R  Cold       110        2    2     200    1.0  ...       1        25      3     1.0  0.75  34.384843   28.3495

[5 rows x 16 columns]
```

Just like we did earlier in the module, we need to save the dataframe to
an object when making changes involving columns. This will permanently
save the column `weight_g` to the dataframe `df`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s try another example. This time we want to save our sugar content
per cereal cup as a column in our existing dataframe. We established the
operation for this is:

``` python
df['sugars']/df['cups']
```

```out
name
100% Bran                    18.181818
100% Natural Bran             8.000000
All-Bran                     15.151515
All-Bran with Extra Fiber     0.000000
                               ...    
Trix                         12.000000
Wheat Chex                    4.477612
Wheaties                      3.000000
Wheaties Honey Gold          10.666667
Length: 77, dtype: float64
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now we combine it with `assign()` naming the column `sugar_per_cup`.

``` python
df = df.assign(sugar_per_cup=df['sugars']/df['cups'])
df.head()
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  ...  vitamins  shelf  weight  cups     rating  weight_g  sugar_per_cup
name                                                                        ...                                                                   
100% Bran                   N  Cold        70        4    1     130   10.0  ...        25      3     1.0  0.33  68.402973   28.3495      18.181818
100% Natural Bran           Q  Cold       120        3    5      15    2.0  ...         0      3     1.0  1.00  33.983679   28.3495       8.000000
All-Bran                    K  Cold        70        4    1     260    9.0  ...        25      3     1.0  0.33  59.425505   28.3495      15.151515
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0  ...        25      3     1.0  0.50  93.704912   28.3495       0.000000
Almond Delight              R  Cold       110        2    2     200    1.0  ...        25      3     1.0  0.75  34.384843   28.3495      10.666667

[5 rows x 17 columns]
```

Give it a shot in the exercises now on your own.

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
