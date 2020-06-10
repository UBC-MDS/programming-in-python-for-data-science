---
type: slides
---

# Column arithmetic and creation

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Doing some sort of transformation on the columns of a dataframe will
most likely come up in your analysis somewhere and it’s not always
straightforward. Let’s welcome back the `cereal.csv` data we have worked
with in Module 1.

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

To make things especially clear, for the next few scenarios let’s only
use the first 5 rows of the dataset.

``` python
df = df.iloc[:5]
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

Take this next scenario. Perhaps we recently read the cereal data’s
documentation explaining that the `fat` column is being expressed as
grams and we are interested in miligrams.  
How can we rectify this?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We need to multiply each of the row’s fat value by 1000.

<br>

<center>

<img src='/module2/times1000.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is where some magic happens. Python doesn’t require us to make a
whole column filled with 1000s to get the result we want. It would
simply multiply 1000 to each column. (In Python we use `*` for
multiplication.)

So our original fat column in the cereal dataframe:

``` python
df['fat']
```

```out
name
100% Bran                    1
100% Natural Bran            5
All-Bran                     1
All-Bran with Extra Fiber    0
Almond Delight               2
Name: fat, dtype: int64
```

Is transformed to this:

``` python
df['fat'] * 1000
```

```out
name
100% Bran                    1000
100% Natural Bran            5000
All-Bran                     1000
All-Bran with Extra Fiber       0
Almond Delight               2000
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

We can do the same thing with any operation too.  
Let’s divide the rating of each cereal by 10 so it lies on a 10 point
scale.

The ratings column

``` python
df['rating'] 
```

```out
name
100% Bran                    68.402973
100% Natural Bran            33.983679
All-Bran                     59.425505
All-Bran with Extra Fiber    93.704912
Almond Delight               34.384843
Name: rating, dtype: float64
```

Gets transformed to this:

``` python
df['rating'] / 10
```

```out
name
100% Bran                    6.840297
100% Natural Bran            3.398368
All-Bran                     5.942551
All-Bran with Extra Fiber    9.370491
Almond Delight               3.438484
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

<img src='/module2/divide10.png'  alt="404 image" />

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

<img src='/module2/sugarcups.png'  width="450" alt="404 image" />

</center>

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

Each sugar row value is divided by its respective cups value.

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
to our cereal dataframe. Let’s explore how we can add new columns to a
less detailed version of our cereal dataframe. Remember the argument
`use_cols`? We are going to use it bring in only a selection of columns
so it’s easier to follow the examples.

``` python
df = pd.read_csv('cereal.csv', usecols=['name', 'mfr','type', 'fat', 'sugars', 'weight', 'cups','rating'])
df
```

```out
                         name mfr  type  fat  sugars  weight  cups     rating
0                   100% Bran   N  Cold    1       6     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold    5       8     1.0  1.00  33.983679
2                    All-Bran   K  Cold    1       5     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold    0       0     1.0  0.50  93.704912
..                        ...  ..   ...  ...     ...     ...   ...        ...
73                       Trix   G  Cold    1      12     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold    1       3     1.0  0.67  49.787445
75                   Wheaties   G  Cold    1       3     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold    1       8     1.0  0.75  36.187559

[77 rows x 8 columns]
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
0     28.3495
1     28.3495
2     28.3495
3     28.3495
       ...   
73    28.3495
74    28.3495
75    28.3495
76    28.3495
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
                        name mfr  type  fat  sugars  weight  cups     rating  weight_g
0                  100% Bran   N  Cold    1       6     1.0  0.33  68.402973   28.3495
1          100% Natural Bran   Q  Cold    5       8     1.0  1.00  33.983679   28.3495
2                   All-Bran   K  Cold    1       5     1.0  0.33  59.425505   28.3495
3  All-Bran with Extra Fiber   K  Cold    0       0     1.0  0.50  93.704912   28.3495
4             Almond Delight   R  Cold    2       8     1.0  0.75  34.384843   28.3495
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
0     18.181818
1      8.000000
2     15.151515
3      0.000000
        ...    
73    12.000000
74     4.477612
75     3.000000
76    10.666667
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
                        name mfr  type  fat  sugars  weight  cups     rating  weight_g  sugar_per_cup
0                  100% Bran   N  Cold    1       6     1.0  0.33  68.402973   28.3495      18.181818
1          100% Natural Bran   Q  Cold    5       8     1.0  1.00  33.983679   28.3495       8.000000
2                   All-Bran   K  Cold    1       5     1.0  0.33  59.425505   28.3495      15.151515
3  All-Bran with Extra Fiber   K  Cold    0       0     1.0  0.50  93.704912   28.3495       0.000000
4             Almond Delight   R  Cold    2       8     1.0  0.75  34.384843   28.3495      10.666667
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
