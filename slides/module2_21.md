---
type: slides
---

# Grouping and Aggregating

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Grouping a Dataframe

Often, we are interested in examining specific groups in our data.
`df.groupby()` allows us to group our data based on a column

Let’s group our candybars dataframe on the `mfr` column and save it as
`mfr_group`.

``` python
mfr_group = df.groupby(by='mfr')
mfr_group
```

```out
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x11be23fd0>
```

This returns a `DataFrame GroupBy` object. What is that though?

Notes: Script
here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

<img src='module2/groupby.png'  alt="404 image" width = "80%" align="middle"/>

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

A `DataFrame GroupBy` object contains information about the groups of
the dataframe. We can access it with the `.groups` attribute
    (noun)

``` python
mfr_group.groups
```

```out
{'A': Index(['Maypo'], dtype='object', name='name'), 'G': Index(['Apple Cinnamon Cheerios', 'Basic 4', 'Cheerios', 'Cinnamon Toast Crunch', 'Clusters', 'Cocoa Puffs', 'Count Chocula', 'Crispy Wheat & Raisins', 'Golden Grahams', 'Honey Nut Cheerios', 'Kix', 'Lucky Charms', 'Multi-Grain Cheerios', 'Oatmeal Raisin Crisp', 'Raisin Nut Bran', 'Total Corn Flakes', 'Total Raisin Bran', 'Total Whole Grain',
       'Triples', 'Trix', 'Wheaties', 'Wheaties Honey Gold'],
      dtype='object', name='name'), 'K': Index(['All-Bran', 'All-Bran with Extra Fiber', 'Apple Jacks', 'Corn Flakes', 'Corn Pops', 'Cracklin' Oat Bran', 'Crispix', 'Froot Loops', 'Frosted Flakes', 'Frosted Mini-Wheats', 'Fruitful Bran', 'Just Right Crunchy  Nuggets', 'Just Right Fruit & Nut', 'Mueslix Crispy Blend', 'Nut&Honey Crunch', 'Nutri-Grain Almond-Raisin', 'Nutri-grain Wheat',
       'Product 19', 'Raisin Bran', 'Raisin Squares', 'Rice Krispies', 'Smacks', 'Special K'],
      dtype='object', name='name'), 'N': Index(['100% Bran', 'Cream of Wheat (Quick)', 'Shredded Wheat', 'Shredded Wheat 'n'Bran', 'Shredded Wheat spoon size', 'Strawberry Fruit Wheats'], dtype='object', name='name'), 'P': Index(['Bran Flakes', 'Fruit & Fibre Dates; Walnuts; and Oats', 'Fruity Pebbles', 'Golden Crisp', 'Grape Nuts Flakes', 'Grape-Nuts', 'Great Grains Pecan', 'Honey-comb', 'Post Nat. Raisin Bran'], dtype='object', name='name'), 'Q': Index(['100% Natural Bran', 'Cap'n'Crunch', 'Honey Graham Ohs', 'Life', 'Puffed Rice', 'Puffed Wheat', 'Quaker Oat Squares', 'Quaker Oatmeal'], dtype='object', name='name'), 'R': Index(['Almond Delight', 'Bran Chex', 'Corn Chex', 'Double Chex', 'Muesli Raisins; Dates; & Almonds', 'Muesli Raisins; Peaches; & Pecans', 'Rice Chex', 'Wheat Chex'], dtype='object', name='name')}
```

Reading carefully, we can see there are 7 groups: `A`, `G`, `K`, `N`,
`P`, `Q` and `R`, and it lists the index labels (cereal names) in each
group.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can obtain all the row index names of a group by specifying the group
name in square brakets after the `groups` method. Take the group `K` as
an
    example.

``` python
mfr_group.groups['K']
```

```out
Index(['All-Bran', 'All-Bran with Extra Fiber', 'Apple Jacks', 'Corn Flakes', 'Corn Pops', 'Cracklin' Oat Bran', 'Crispix', 'Froot Loops', 'Frosted Flakes', 'Frosted Mini-Wheats', 'Fruitful Bran', 'Just Right Crunchy  Nuggets', 'Just Right Fruit & Nut', 'Mueslix Crispy Blend', 'Nut&Honey Crunch', 'Nutri-Grain Almond-Raisin', 'Nutri-grain Wheat',
       'Product 19', 'Raisin Bran', 'Raisin Squares', 'Rice Krispies', 'Smacks', 'Special K'],
      dtype='object', name='name')
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can get the full dataframe of just the group `K` using the method
`get_group()`

``` python
mfr_group.get_group('K')
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
Apple Jacks                 K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
Corn Flakes                 K  Cold       100        2    0     290    1.0   21.0       2      35        25      1    1.00  1.00  45.863324
Corn Pops                   K  Cold       110        1    0      90    1.0   13.0      12      20        25      2    1.00  1.00  35.782791
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Raisin Bran                 K  Cold       120        3    1     210    5.0   14.0      12     240        25      2    1.33  0.75  39.259197
Raisin Squares              K  Cold        90        2    0       0    2.0   15.0       6     110        25      3    1.00  0.50  55.333142
Rice Krispies               K  Cold       110        2    0     290    0.0   22.0       3      35        25      1    1.00  1.00  40.560159
Smacks                      K  Cold       110        2    1      70    1.0    9.0      15      40        25      2    1.00  0.75  31.230054
Special K                   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1    1.00  1.00  53.131324

[23 rows x 15 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Summary Statistics with Groups

What now? We have this new groupby object, what do we do with it? We can
calculate some summary statistics with
    them\!

``` python
mfr_group.mean()
```

```out
       calories   protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
mfr                                                                                                                                           
A    100.000000  4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
G    111.363636  2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
K    108.695652  2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
N     86.666667  2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
P    108.888889  2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
Q     95.000000  2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
R    115.000000  2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997
```

This shows up the mean value of each column for each group, we can do
the same thing for other statistics too.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Let’s try it with the minimum values using
    `min()`

``` python
mfr_group.min()
```

```out
     type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
mfr                                                                                                              
A     Hot       100        4    1       0    0.0   16.0       3      95        25      2    1.00  1.00  54.850917
G    Cold       100        1    1     140    0.0   10.5       1      25        25      1    1.00  0.50  19.823573
K    Cold        50        1    0       0    0.0    7.0       0      20        25      1    1.00  0.33  29.924285
N    Cold        70        2    0       0    1.0    5.0       0       1         0      1    0.83  0.33  59.363993
P    Cold        90        1    0      45    0.0   11.0       3      25        25      1    1.00  0.25  28.025765
Q    Cold        50        1    0       0    0.0    1.0       0      15         0      1    0.50  0.50  18.042851
R    Cold        90        1    0      95    0.0   14.0       2       1        25      1    1.00  0.67  34.139765
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Aggregating dataframes

“Aggregating” means to combine elements. Luckily there is a particular
method that allows us to collect multiple statistics together-
aggregating them in 1 step. `df.agg()` can be used on its own:

``` python
df.agg('mean')
```

```out
calories    106.883117
protein       2.545455
fat           1.012987
sodium      159.675325
fiber         2.151948
carbo        14.623377
sugars        6.948052
potass       96.129870
vitamins     28.246753
shelf         2.207792
weight        1.029610
cups          0.821039
rating       42.665705
dtype: float64
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

but then it is essentially the same thing as calling the statistic
`mean()` on the dataframe.

``` python
df.mean()
```

```out
calories    106.883117
protein       2.545455
fat           1.012987
sodium      159.675325
fiber         2.151948
carbo        14.623377
sugars        6.948052
potass       96.129870
vitamins     28.246753
shelf         2.207792
weight        1.029610
cups          0.821039
rating       42.665705
dtype: float64
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

`df.agg()` gets a chance to shine when we want several specific
measures. Let’s say we want just the `max` `min` and `median`. We
specify them in square brackets within our `df.agg()`
    method.

``` python
df.agg(['max', 'min', 'median'])
```

```out
        mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
max       R   Hot     160.0      6.0  5.0   320.0   14.0   23.0    15.0   330.0     100.0    3.0     1.5  1.50  93.704912
min       A  Cold      50.0      1.0  0.0     0.0    0.0    1.0     0.0     1.0       0.0    1.0     0.5  0.25  18.042851
median  NaN   NaN     110.0      3.0  1.0   180.0    2.0   14.0     7.0    90.0      25.0    2.0     1.0  0.75  40.400208
```

It produces a nice dataframe giving the value for each statistic, for
each column.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Aggregating groupby objects

`df.agg()` is particularly useful with groupby objects. Let’s try it on
our `mfr_group` `DataFrame GroupBy`
    object.

``` python
mfr_group.agg(['max', 'min', 'median'])
```

```out
              calories           protein           fat              sodium               fiber               carbo              sugars            potass             vitamins            shelf              weight                cups                       rating                      
         max   min   median   max min median  max  min  median    max  min median   max   min  median    max  min  median    max min median    max min median      max min median    max  min median    max   min  median    max  min  median        max      min       median
mfr                                                                                                                                                                                                                                                                
A        100   100     100     4   4    4.0     1   1    1        0     0    0.0    0.0   0.0    0.0    16.0  16.0  16.00      3   3    3.0     95  95   95.0       25  25   25.0     2   2    2.0     1.00   1.00  1.0     1.00  1.00  1.000    54.850917  54.850917  54.850917
G        140   100     110     6   1    2.0     3   1    1       290  140  200.0    4.0   0.0    1.5    21.0  10.5  14.25     14   1    8.5    230  25   80.0      100  25   25.0     3   1    2.0     1.50   1.00  1.0     1.50  0.50  0.875    51.592193  19.823573  36.181877
K        160    50     110     6   1    3.0     3   0    0       320    0  170.0   14.0   0.0    1.0    22.0   7.0  15.00     15   0    7.0    330  20   60.0      100  25   25.0     3   1    3.0     1.50   1.00  1.0     1.00  0.33  0.750    93.704912  29.924285  40.560159
N        100    70      90     4   2    3.0     1   0    0       130    0    7.5   10.0   1.0    3.0    21.0   5.0  17.50      6   0    0.0    280   1  107.5       25   0    0.0     3   1    1.5     1.00   0.83  1.0     1.00  0.33  0.835    74.472949  59.363993  68.319429
P        120    90     110     3   1    3.0     3   0    1       210   45  160.0    6.0   0.0    3.0    17.0  11.0  13.00     15   3   10.0    260  25   90.0       25  25   25.0     3   1    3.0     1.33   1.00  1.0     1.33  0.25  0.670    53.371007  28.025765  40.917047
Q        120    50     100     5   1    2.5     5   0    2       220    0   75.0    2.7   0.0    1.5    14.0   1.0  12.00     12   0    6.0    135  15   72.5       25   0   12.5     3   1    2.5     1.00   0.50  1.0     1.00  0.50  0.875    63.005645  18.042851  47.419974
R        150    90     110     4   1    2.0     3   0    1       280   95  200.0    4.0   0.0    2.0    23.0  14.0  16.50     11   2    5.5    170   1   97.5       25  25   25.0     3   1    2.0     1.00   1.00  1.0     1.13  0.67  0.875    49.787445  34.139765  41.721976
```

This gives a value for each group and for each statistic we specified.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Extra Fancy Aggregation

You might have noticed that when we used `df.agg()`, we calculated the
same 3 statistics for every column in the dataframe. This doesn’t have
to be the case. We can calculate different statistics for different
columns.

Let’s say we are concerned about the `max` and `min` calorie values, the
total `sum` of the ratings and the `mean` and `median` sugar content for
each manufacturing group.

``` python
mfr_group.agg({"calories": ['max', 'min'], 
         "rating": ['sum'],  
         "sugars": ['mean', 'median']})
```

```out
         calories      rating         sugars       
         max  min       sum        mean   median
mfr                                            
A        100  100    54.850917  3.000000    3.0
G        140  100   758.688737  7.954545    8.5
K        160   50  1012.884634  7.565217    7.0
N        100   70   407.811403  1.833333    0.0
P        120   90   375.351697  8.777778   10.0
Q        120   50   343.327919  5.500000    6.0
R        150   90   332.343977  6.125000    5.5
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
