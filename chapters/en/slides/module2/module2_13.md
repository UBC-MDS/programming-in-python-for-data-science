---
type: slides
---

# Column arithmetic and creation

Notes:

<br>

---

``` python
cereal = pd.read_csv('cereal.csv')
cereal.head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[5 rows x 16 columns]
```

**Attribution:**  
*“[80 Cereals](https://www.kaggle.com/crawford/80-cereals/)” (c) by
[Chris Crawford](https://www.linkedin.com/in/crawforc3/) is licensed
under [Creative Commons Attribution-ShareAlike 3.0
Unported](http://creativecommons.org/licenses/by-sa/3.0/)*

Notes:

Doing some sort of transformation on the columns of a dataframe will
most likely come up in your analysis somewhere and it’s not always
straightforward.

Let’s welcome back the `cereal.csv` data we have been working with.

---

``` python
cereal= cereal.iloc[:5]
cereal
```

```out
                        name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843

[5 rows x 16 columns]
```

Notes:

To make things especially clear, for the next few scenarios let’s only
use the first 5 rows of the dataset.

---

<center>

<img src='/module2/times1000.png'  alt="404 image" />

</center>

Notes:

Take this next scenario.

Perhaps we recently read the cereal data’s documentation explaining that
the `fat` column is being expressed as grams and we are interested in
milligrams.

How can we rectify this?

We need to multiply each of the row’s fat values by 1000.

---

``` python
cereal['fat']
```

```out
0    1
1    5
2    1
3    0
4    2
Name: fat, dtype: int64
```

Is transformed to this:

``` python
cereal['fat'] * 1000
```

```out
0    1000
1    5000
2    1000
3       0
4    2000
Name: fat, dtype: int64
```

Notes:

Here is where some magic happens.

Python doesn’t require us to make a whole column filled with 1000s to
get the result we want.

It simply multiplies each value by 1000. (In Python we use `*` for
multiplication.)

So our original fat column in the cereal dataframe is transformed\!

See how each value has changed?

Note that when we do any type of operations on columns, we use single
square brackets.

---

``` python
cereal['rating'] 
```

```out
0    68.402973
1    33.983679
2    59.425505
3    93.704912
4    34.384843
Name: rating, dtype: float64
```

``` python
cereal['rating'] / 10
```

```out
0    6.840297
1    3.398368
2    5.942551
3    9.370491
4    3.438484
Name: rating, dtype: float64
```

Notes:

We can do the same thing with most operations. Let’s divide the rating
of each cereal by 10 so that it lies on a 10 point scale.

The ratings column gets transformed to single digits instead of double
digits now.

---

<center>

<img src='/module2/divide10.png'  alt="404 image" />

</center>

Notes:

Every row’s value is changed by the operation.

---

<center>

<img src='/module2/sugarcups.png'  width="60%" alt="404 image" />

</center>

``` python
cereal['sugars'] / cereal['cups']
```

```out
0    18.181818
1     8.000000
2    15.151515
3     0.000000
4    10.666667
dtype: float64
```

Notes:

We are not limited to simply taking a column and transforming it by a
single number, say by multiplying or dividing.

We can do operations involving multiple columns as well. Perhaps we
wanted to know the amount of sugar (`sugar`) per cup of cereal (`cups`).

The expected result would look something like this diagram.

Remember that with any column operation we use only single square
brackets on our columns.

To get our desired output of sugar content per cup our code looks like
this.

Each sugar row value is divided by its corresponding cups value.

---

``` python
cereal[['sugars']] / cereal[['cups']]
```

```out
   cups  sugars
0   NaN     NaN
1   NaN     NaN
2   NaN     NaN
3   NaN     NaN
4   NaN     NaN
```

Notes:

Just to stress the point of why we use single square brackets for our
operations, here is what happens when we use double square brackets.

This doesn’t appear very useful.

---

``` python
cereal = pd.read_csv('cereal.csv', usecols=['name', 'mfr','type', 'fat', 'sugars', 'weight', 'cups','rating'])
cereal
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

Notes:

Up until now, all of these operations have been done without being added
to our cereal dataframe.

Let’s explore how we can add new columns to a less detailed version of
our cereal dataframe.

We’ll be working with a smaller dataframe containing only a few columns
columns so that it’s easier to follow the examples.

---

## Column Creation

``` python
oz_to_g = 28.3495
cereal['weight'] * oz_to_g
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

``` python
cereal = cereal.assign(weight_g=cereal['weight'] * oz_to_g)
cereal.head()
```

```out
                        name mfr  type  fat  sugars  weight  cups     rating  weight_g
0                  100% Bran   N  Cold    1       6     1.0  0.33  68.402973   28.3495
1          100% Natural Bran   Q  Cold    5       8     1.0  1.00  33.983679   28.3495
2                   All-Bran   K  Cold    1       5     1.0  0.33  59.425505   28.3495
3  All-Bran with Extra Fiber   K  Cold    0       0     1.0  0.50  93.704912   28.3495
4             Almond Delight   R  Cold    2       8     1.0  0.75  34.384843   28.3495
```

Notes:

In the next scenario, we have decided that our `weight` column should
show the weight of each cereal in grams instead of ounces.

We are going to save the conversion factor of grams to ounces in an
object named `oz_to_g`.

Let’s start with just the operation for this.

Next, we combine our operation with the implementation of adding it as a
new column to the dataframe. The verb `.assign()` allows us to specify a
column name to our result using an equal sign `=`.

We are going to name our new column `weight_g` (for grams).

Just like we did earlier in the module, we need to save the dataframe to
an object when making changes involving columns. This will permanently
save the column `weight_g` to the dataframe `cereal`.

---

``` python
cereal['sugars'] / cereal['cups']
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

``` python
cereal = cereal.assign(sugar_per_cup=cereal['sugars'] / cereal['cups'])
cereal.head()
```

```out
                        name mfr  type  fat  sugars  weight  cups     rating  weight_g  sugar_per_cup
0                  100% Bran   N  Cold    1       6     1.0  0.33  68.402973   28.3495      18.181818
1          100% Natural Bran   Q  Cold    5       8     1.0  1.00  33.983679   28.3495       8.000000
2                   All-Bran   K  Cold    1       5     1.0  0.33  59.425505   28.3495      15.151515
3  All-Bran with Extra Fiber   K  Cold    0       0     1.0  0.50  93.704912   28.3495       0.000000
4             Almond Delight   R  Cold    2       8     1.0  0.75  34.384843   28.3495      10.666667
```

Notes:

Let’s try another example.

This time we want to save our sugar content per cereal cup as a column
in our existing dataframe.

At the top you can see the operation by itself, just for teaching
purposes. Then, below, we combine our calculation with `assign()`,
naming the column `sugar_per_cup`.

---

# Let’s apply what we learned\!

Notes:

<br>
