---
type: slides
---

# Column Arithmetic and Creation

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Doing some sort of transformation on the columns of a dataframe will
most likely come up in your analysis somewhere and it’s not always
straight forward.

Using only the first 5 rows of our cereal dataset, Let’s explore the
next few scenarios.

``` python
df = df.iloc[ 0: 5]
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

Perhaps the column `fat` was instead expressing the grams of fat above
2g. This means that the actual fat content of each cereal is actually an
additional 2 grams. How do we rectify this?

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We need to add 2 to each of the row’s fat value.

<center>

<img src='module2/plus2.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

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

Notice how each row has changed in value. Notice that for operations on
columns, we use single square brackets.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can do the same thing with multiplication/division too. let’s
multiply the rating of each cereal by 2. Note that `*` is used in Python
for multiplication.

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

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Every rows value is changed by the operation.

<center>

<img src='module2/times2.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We are not limited to simply taking a column and transforming it by a
single number. We can do operations involving multiple columns as well.
Perhaps we wanted to know the amount of sugar (`sugar`) per cup of
cereal (`cups`).

The expected result would look something like this:

<center>

<img src='module2/sugarcups.png'  alt="404 image" />

</center>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Keeping with the syntax of using only single square brackets on our
columns, to get our desired output we can do the following. Each sugar
row value is divided by its respected cups value.

``` python
df['sugars'] / df['cups']
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

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Just to stress the point of why we use single square brackets for our
operation here is what happens when we use double square brackets:

``` python
df[['sugars']] / df[['cups']]
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

Not very useful for us.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

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

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Column Creation

Now we have decided that we want a column in the dataframe that shows
the weight of each cereal in grams instead of ounces We can add this to
our current dataframe using the `assign` function.  
We are going to save the conversion factor of grams to ounces in an
object named `oz_to_g` to add some clarity and flexibility to our code.
The operation for this desired result would be:

``` python
oz_to_g = 28.3495
df['weight'] * oz_to_g
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

Let’s combine this with the `assign()` verb so that we can save this as
a new column in our dataframe named `weight_g`.

``` python
df = df.assign(weight_g=df['weight'] * oz_to_g)
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

Perfect\! Remember from earlier in module 2 how it’s important that we
always save the dataframe to an object when making changes involving
columns.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We learned how to do operations involving multiple columns in a
dataframe let’s implement this by saving the results as a new column.
This time adding a column indicating how many calories there are in 1
cup of each cereal.

The operation for this would be

``` python
df['calories'] / df['cups']
```

```out
name
100% Bran                    212.121212
100% Natural Bran            120.000000
All-Bran                     212.121212
All-Bran with Extra Fiber    100.000000
                                ...    
Trix                         110.000000
Wheat Chex                   149.253731
Wheaties                     100.000000
Wheaties Honey Gold          146.666667
Length: 77, dtype: float64
```

let’s combine this with `assign()` naming the column `cals_per_cup`.

``` python
df = df.assign(cals_per_cup=df['calories'] / df['cups'])
df.head()
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  ...  vitamins  shelf  weight  cups     rating  weight_g  cals_per_cup
name                                                                        ...                                                                  
100% Bran                   N  Cold        70        4    1     130   10.0  ...        25      3     1.0  0.33  68.402973   28.3495    212.121212
100% Natural Bran           Q  Cold       120        3    5      15    2.0  ...         0      3     1.0  1.00  33.983679   28.3495    120.000000
All-Bran                    K  Cold        70        4    1     260    9.0  ...        25      3     1.0  0.33  59.425505   28.3495    212.121212
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0  ...        25      3     1.0  0.50  93.704912   28.3495    100.000000
Almond Delight              R  Cold       110        2    2     200    1.0  ...        25      3     1.0  0.75  34.384843   28.3495    146.666667

[5 rows x 17 columns]
```

Great\! let’s put this to practice.

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

\<source src="place
