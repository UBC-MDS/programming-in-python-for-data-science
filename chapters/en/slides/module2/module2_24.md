---
type: slides
---

# Grouping and Aggregating

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Often, we are interested in examining specific groups in our data.
Perhaps the question we want to answer is:  
*_Which manufacturer has the highest mean sugar content?_*

We found in Module 1 using `.value_counts()` that there are 7 different
manufacturers; “K”, “G”, “P”, “R”, “Q”, “N” and “A”.

``` python
df['mfr'].value_counts()
```

```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To find the mean sugar content of each manufacturer, we could filter on
each manufacturer and calculate the mean sugar content using `.mean()`.
We can chain to make this process a little faster too.

Let’s start with K:

``` python
df[df['mfr'] == 'K'].mean().loc['sugars']
```

```out
7.565217391304348
```

Next “G”:

``` python
df[df['mfr'] == 'G'].mean().loc['sugars']
```

```out
7.954545454545454
```

We could do this for the remaining 5 manufacturers. However, it’s
obvious that it’s time-consuming and a lot of work to do this
repeatedly. Imagine how tedious this would be if we had 100 different
manufacturers?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Using groupby

Pandas has a solution for this. It’s not uncommon to be interested in
examining specific groups in our data hence there is a verb that is
helpful in grouping like-rows together. `df.groupby()` allows us to
group our data based on a specified column.

Let’s group our candybars dataframe on the `mfr` column and save it as
object `mfr_group`.

``` python
mfr_group = df.groupby(by='mfr')
mfr_group
```

```out
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x11de24b70>
```

This returns a `DataFrame GroupBy` object. What exactly is this?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

For example if we only had 2 manufacturers, this would be the output:

<center>

<img src='/module2/groupby.png'  alt="404 image" width = "70%" align="middle"/>

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

A `DataFrame GroupBy` object contains information about the groups of
the dataframe. We can access it with the `.groups` attribute (noun).

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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can obtain all the row index names of a group by specifying the group
name in square brackets after the `groups` method. Take the group `K` as
an example.

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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can get the full dataframe of the group `K` alone using the method
`get_group()`.

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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Summary Statistics with Groups

What now? Grouping doesn’t answer our initial question of ***Which
manufacturer has the highest mean sugar content?***  
Where do we go from here?  
We need to calculate the mean sugar content in each manufacturing
group\!

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

This answers the initial question and confirms that manufacturer “P” has
the highest mean sugar content across cereals. See how convenient this
was to do in comparison to our initial method? Not only does this give
us the result quicker, but it also gives us the mean of each column of
the dataframe. Think of how many filtering and mean calculations would
have to be done if we were to do this using our initial method.  
Of course, using groups is not limited to finding the only the mean, we
can do the same thing for other statistics too like `.min()` and
`.max()`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Aggregating dataframes

In situations where we want to collect multiple statistics together, we
can aggregate them in one step using a verb called `.agg()`.

`.agg()` can be used on its own using a single measurement, without
groupby:

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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

This is essentially the same thing as calling the statistic `mean()` on
the dataframe.

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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`.agg()` gets a chance to really shine when we want several specific
measures. Let’s say we want the `max`, `min` and `median`. We specify
them in square brackets within our `.agg()` method.

``` python
df.agg(['max', 'min', 'median'])
```

```out
        mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
max       R   Hot     160.0      6.0  5.0   320.0   14.0   23.0    15.0   330.0     100.0    3.0     1.5  1.50  93.704912
min       A  Cold      50.0      1.0  0.0     0.0    0.0    1.0     0.0     1.0       0.0    1.0     0.5  0.25  18.042851
median  NaN   NaN     110.0      3.0  1.0   180.0    2.0   14.0     7.0    90.0      25.0    2.0     1.0  0.75  40.400208
```

It produces a convenient dataframe giving the value for each statistic,
for each column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Aggregating groupby objects

`.agg()` is particularly useful with groupby objects. Let’s try it on
our manufacturer `groupby` object named `mfr_group`.

``` python
mfr_group.agg(['max', 'min', 'median'])
```

```out
    calories             protein            fat            sodium             fiber             carbo              sugars            potass            vitamins            shelf            weight               cups                  rating                      
         max  min median     max min median max min median    max  min median   max  min median   max   min median    max min median    max min median      max min median   max min median    max   min median   max   min median        max        min     median
mfr                                                                                                                                                                                                                                                                
A        100  100    100       4   4    4.0   1   1      1      0    0    0.0   0.0  0.0    0.0  16.0  16.0  16.00      3   3    3.0     95  95   95.0       25  25   25.0     2   2    2.0   1.00  1.00    1.0  1.00  1.00  1.000  54.850917  54.850917  54.850917
G        140  100    110       6   1    2.0   3   1      1    290  140  200.0   4.0  0.0    1.5  21.0  10.5  14.25     14   1    8.5    230  25   80.0      100  25   25.0     3   1    2.0   1.50  1.00    1.0  1.50  0.50  0.875  51.592193  19.823573  36.181877
K        160   50    110       6   1    3.0   3   0      0    320    0  170.0  14.0  0.0    1.0  22.0   7.0  15.00     15   0    7.0    330  20   60.0      100  25   25.0     3   1    3.0   1.50  1.00    1.0  1.00  0.33  0.750  93.704912  29.924285  40.560159
N        100   70     90       4   2    3.0   1   0      0    130    0    7.5  10.0  1.0    3.0  21.0   5.0  17.50      6   0    0.0    280   1  107.5       25   0    0.0     3   1    1.5   1.00  0.83    1.0  1.00  0.33  0.835  74.472949  59.363993  68.319429
P        120   90    110       3   1    3.0   3   0      1    210   45  160.0   6.0  0.0    3.0  17.0  11.0  13.00     15   3   10.0    260  25   90.0       25  25   25.0     3   1    3.0   1.33  1.00    1.0  1.33  0.25  0.670  53.371007  28.025765  40.917047
Q        120   50    100       5   1    2.5   5   0      2    220    0   75.0   2.7  0.0    1.5  14.0   1.0  12.00     12   0    6.0    135  15   72.5       25   0   12.5     3   1    2.5   1.00  0.50    1.0  1.00  0.50  0.875  63.005645  18.042851  47.419974
R        150   90    110       4   1    2.0   3   0      1    280   95  200.0   4.0  0.0    2.0  23.0  14.0  16.50     11   2    5.5    170   1   97.5       25  25   25.0     3   1    2.0   1.00  1.00    1.0  1.13  0.67  0.875  49.787445  34.139765  41.721976
```

This gives a value for each group and for each statistic we specified.
For example:

Look at the ‘150’ in the bottom row on the far left. The interpretation
is that, for cases where the manufacturer is ‘R’, the max number of
calories is 150. In a similar manner if the manufacturer is ‘P’ the
minumum amount of sodium, is 45.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Extra Fancy Aggregation

You might have noticed that when we used `.agg()`, we calculated the
same 3 statistics for every column in the dataframe but we can calculate
different statistics for different columns.  
Let’s say we are concerned about the `max` and `min` calorie values, the
total `sum` of the ratings and the `mean` and `median` sugar content for
each manufacturing group.  
We wrapped everything in curly brackets and we use a colon to separate
the column name from the statistics values. We need to put the
statistics within square brackets.

``` python
mfr_group.agg({"calories":['max', 'min'],
                 "rating":['sum'],  
                 "sugars":['mean', 'median']})
```

```out
    calories            rating    sugars       
         max  min          sum      mean median
mfr                                            
A        100  100    54.850917  3.000000    3.0
G        140  100   758.688737  7.954545    8.5
K        160   50  1012.884634  7.565217    7.0
N        100   70   407.811403  1.833333    0.0
P        120   90   375.351697  8.777778   10.0
Q        120   50   343.327919  5.500000    6.0
R        150   90   332.343977  6.125000    5.5
```

Now this is a bit easier to read.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Plotting Groupby Objects

Let’s return to the question we asked at the beginning of this section:

*_Which manufacturer has the highest mean sugar content?_*

A nice way of showing our results would be to graph this. A bar chart
like this should do the trick\!

<img src="/module2/module2_24/unnamed-chunk-15-1.png" width="576" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s go through the steps that are needed to make this plot.

  - We are going to save our plot as an object named `sugar_plot` and
    use our chaining technique as well.
  - We create a groupby object and calculate the mean for each column in
    the dataframe.  
  - Next, we take the single column we are interested in using
    `.loc[]`.  
  - Our last action is the plot everything using `.plot.bar()`.

<!-- end list -->

``` python
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar()
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
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar()
             )
sugar_plot
```

<img src="/module2/module2_24/unnamed-chunk-16-1.png" width="576" />

This plot, however, looks a little unfinished. We need to add a title
and label our y-axis.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We’ve added a title before, so there is nothing new there but adding x
and y-axis labels is a little different. We can increase the label font
sizes using the argument `fontsize`. In this case, we reference our
initial plot and use the verb `.set_ylabel()` and `.set_xlabel()` with
the desired axis label as an argument and `fontsize` to assign a desired
label size. To avoid unnecessary information that will be returned
otherwise, whatever our last verb being used with our plot (named
\`sugar\_plot) has to be reassigned back to the object. If we did this
any other way, we would not have the ability to do more transformations
on our plot, or we would get additional information with the plot
output.

``` python
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar(title='Mean sugar content among manufacturers')
              )
sugar_plot.set_ylabel('Sugar content (in grams)', fontsize=9)
sugar_plot = sugar_plot.set_xlabel('Manufacturer', fontsize=9)
sugar_plot
```

<img src="/module2/module2_24/unnamed-chunk-17-1.png" width="45%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last plot, we used `.loc[:,'sugars']` to select a single column
to the plot, however, we can show multiple mean column values in a
single plot by selecting more columns. The columns `fat`, `fiber` and
`protein` seem like good choices.

``` python
nutrition_plot = (df.groupby(by='mfr')
                    .mean()
                    .loc[:, ['fat', 'fiber', 'protein']]
                    .plot.bar(title='Mean nutritrion value over different manufacturers')
                 )
nutrition_plot.set_ylabel('Content (in grams)', fontsize=9)
nutrition_plot = nutrition_plot.set_xlabel('Manufacturer', fontsize=9)
nutrition_plot
```

<img src="/module2/module2_24/unnamed-chunk-18-1.png" width="60%" />

If you want high fibre and low fat, consider having N’s cereals for
breakfast (or lunch or dinner)\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Multiple Grouping

We can group by multiple columns as well. For example we can grouping by
not only manufacturer but also by cereal type\! All we do is put both
both column labels in square brackets within `.groupby()`.

``` python
mfr_type_group = df.groupby(by=['mfr', 'type'])
mfr_type_group.groups
```

```out
{('A', 'Hot'): Index(['Maypo'], dtype='object', name='name'), ('G', 'Cold'): Index(['Apple Cinnamon Cheerios', 'Basic 4', 'Cheerios', 'Cinnamon Toast Crunch', 'Clusters', 'Cocoa Puffs', 'Count Chocula', 'Crispy Wheat & Raisins', 'Golden Grahams', 'Honey Nut Cheerios', 'Kix', 'Lucky Charms', 'Multi-Grain Cheerios', 'Oatmeal Raisin Crisp', 'Raisin Nut Bran', 'Total Corn Flakes', 'Total Raisin Bran', 'Total Whole Grain',
       'Triples', 'Trix', 'Wheaties', 'Wheaties Honey Gold'],
      dtype='object', name='name'), ('K', 'Cold'): Index(['All-Bran', 'All-Bran with Extra Fiber', 'Apple Jacks', 'Corn Flakes', 'Corn Pops', 'Cracklin' Oat Bran', 'Crispix', 'Froot Loops', 'Frosted Flakes', 'Frosted Mini-Wheats', 'Fruitful Bran', 'Just Right Crunchy  Nuggets', 'Just Right Fruit & Nut', 'Mueslix Crispy Blend', 'Nut&Honey Crunch', 'Nutri-Grain Almond-Raisin', 'Nutri-grain Wheat',
       'Product 19', 'Raisin Bran', 'Raisin Squares', 'Rice Krispies', 'Smacks', 'Special K'],
      dtype='object', name='name'), ('N', 'Cold'): Index(['100% Bran', 'Shredded Wheat', 'Shredded Wheat 'n'Bran', 'Shredded Wheat spoon size', 'Strawberry Fruit Wheats'], dtype='object', name='name'), ('N', 'Hot'): Index(['Cream of Wheat (Quick)'], dtype='object', name='name'), ('P', 'Cold'): Index(['Bran Flakes', 'Fruit & Fibre Dates; Walnuts; and Oats', 'Fruity Pebbles', 'Golden Crisp', 'Grape Nuts Flakes', 'Grape-Nuts', 'Great Grains Pecan', 'Honey-comb', 'Post Nat. Raisin Bran'], dtype='object', name='name'), ('Q', 'Cold'): Index(['100% Natural Bran', 'Cap'n'Crunch', 'Honey Graham Ohs', 'Life', 'Puffed Rice', 'Puffed Wheat', 'Quaker Oat Squares'], dtype='object', name='name'), ('Q', 'Hot'): Index(['Quaker Oatmeal'], dtype='object', name='name'), ('R', 'Cold'): Index(['Almond Delight', 'Bran Chex', 'Corn Chex', 'Double Chex', 'Muesli Raisins; Dates; & Almonds', 'Muesli Raisins; Peaches; & Pecans', 'Rice Chex', 'Wheat Chex'], dtype='object', name='name')}
```

The attribute `ngroups` indicates how many groups there are.

``` python
mfr_type_group.ngroups
```

```out
9
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to get the dataframe of a specific group now, we put the
value of each column in parentheses.

``` python
mfr_type_group.get_group(('K', 'Cold'))
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

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can plot in the same way as before

``` python
type_plot = (df.groupby(by=['mfr', 'type'])
                    .mean()
                    .loc[:, ['sugars']]
                    .plot.bar(title='Mean sugar value over different manufacturers and types')
            )
type_plot.set_ylabel('Sugar (in grams)', fontsize=16)
type_plot.set_xlabel('Manufacturer and cereal type', fontsize=16)
type_plot
```

<img src="/module2/module2_24/unnamed-chunk-22-1.png" width="70%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Using `pandas` to plot groupby objects is very limited and is not
possible for many other plot types such as scatter plots.  
If you wish to learn more advanced visualization and Python plotting
package **Altair**, come back soon and visit our in development course
**DSCI-531 Exploratory Data Visualization**.

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
