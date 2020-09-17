---
type: slides
---

# Summary Statistics

Notes:

<br>

---

``` python
cereal = pd.read_csv('cereal.csv')
cereal.head(15)
```

```out
                         name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3    1.00  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3    1.00  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3    1.00  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3    1.00  0.75  34.384843
5     Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6                 Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                     Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                   Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9                 Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813
10               Cap'n'Crunch   Q  Cold       120        1    2     220  ...      12      35        25      2    1.00  0.75  18.042851
11                   Cheerios   G  Cold       110        6    2     290  ...       1     105        25      1    1.00  1.25  50.764999
12      Cinnamon Toast Crunch   G  Cold       120        1    3     210  ...       9      45        25      2    1.00  0.75  19.823573
13                   Clusters   G  Cold       110        3    2     140  ...       7     105        25      3    1.00  0.50  40.400208
14                Cocoa Puffs   G  Cold       110        1    1     180  ...      13      55        25      2    1.00  1.00  22.736446

[15 rows x 16 columns]
```

Notes:

Now we’ve learned about how to get our dataframe how we want it, let’s
try have some fun with it\!

We have our data, now what?

We usually like to learn from it. We want to find out about maybe some
summary statistics about the features of the data.

Let’s load in our cereal dataset again.

---

## Numerical and Categorical Columns

### Categorical data

Consists of qualitative observations such as characteristics - things
generally containing names or words.

**Examples**

  - Colours
  - Names

<br>

### Numerical data

These data are usually expressed with numbers.

**Examples**

  - Measurements
  - Quantities

Notes:

Before we go further, let’s quickly discuss the 2 different types of
data.

Categorical data consists of qualitative observations such as
characteristics - things generally containing names or words. Examples
would be colours or names of things.

Numerical data are usually expressed with numbers such as measurements
or quantities.

Our columns in our dataframe are considered one of the two of these.

---

## Pandas describe()

``` python
cereal.describe()
```

```out
         calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.623377   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.188138   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min     50.000000   1.000000   0.000000    0.000000   0.000000   1.000000   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%    100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%    110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%    110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max    160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

Notes:

Pandas has a lot up its sleeve but one of the most useful methods is
called `.describe()` and it does exactly that. it *describes* our data.

Let’s try it out.

By default `df.describe()` only shows numerical columns.

---

``` python
cereal.describe()
```

```out
         calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.623377   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.188138   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min     50.000000   1.000000   0.000000    0.000000   0.000000   1.000000   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%    100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%    110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%    110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max    160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

  - `count`: The number of non-NA/null observations.
  - `mean`: The mean of column
  - `std` : The standard deviation of a column
  - `min`: The min value for a column
  - `max`: The max value for a column
  - By default the 25, 50 and 75 percentile of the observations

Notes:

This table will tell us about different summary statics including the
following.

  - `count`: The number of non-NA/null observations.
  - `mean`: The mean of the column
  - `std` : The standard deviation of a column
  - `min`: The min value for a column
  - `max`: The max value for a column
  - By default the 25, 50 and 75 percentile of the observations are also
    included.

---

``` python
cereal.describe(include='all')
```

```out
                       name  mfr  type    calories    protein        fat      sodium  ...     sugars      potass    vitamins      shelf     weight       cups     rating
count                    77   77    77   77.000000  77.000000  77.000000   77.000000  ...  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
unique                   77    7     2         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
top     Wheaties Honey Gold    K  Cold         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
freq                      1   23    74         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
mean                    NaN  NaN   NaN  106.883117   2.545455   1.012987  159.675325  ...   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std                     NaN  NaN   NaN   19.484119   1.094790   1.006473   83.832295  ...   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min                     NaN  NaN   NaN   50.000000   1.000000   0.000000    0.000000  ...   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%                     NaN  NaN   NaN  100.000000   2.000000   0.000000  130.000000  ...   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%                     NaN  NaN   NaN  110.000000   3.000000   1.000000  180.000000  ...   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%                     NaN  NaN   NaN  110.000000   3.000000   2.000000  210.000000  ...  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max                     NaN  NaN   NaN  160.000000   6.000000   5.000000  320.000000  ...  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912

[11 rows x 16 columns]
```

  - `unique`: how many observations are unique
  - `top`: which observation value is most occurring
  - `freq`: what is the frequency of the most occurring observation

Notes:

We can make changes to either limit how much is shown or include more
statistic in the dataframe with the additional argument `include =
"all"` in the `describe` brackets.

This expands the dataframe to contain both categorical and numerical
columns now.

Adding `include='all'` within the brackets adds some additional
statistics about categorical columns including:

  - `unique`: which indicates the number of unique observations
  - `top`: which tells up the observation value that is most occurring
  - `freq`: which informs us of the frequency of the most occurring
    observation

---

``` python
ratings = cereal[['protein']]
ratings.mean()
```

```out
protein    2.545455
dtype: float64
```

``` python
ratings = cereal[['rating']]
ratings.sum()
```

```out
rating    3285.259284
dtype: float64
```

``` python
calories = cereal[['calories']]
calories.median()
```

```out
calories    110.0
dtype: float64
```

Notes:

We can also get single statistics of each column using: either
`.mean()`,`.std()`, `.count()`, `.median()`, `.sum()`.

First segregate the column we want to explore further, then add the
verb.

As an example,

what is the mean protein content of the cereals?

Or what is the sum of the cereal ratings?

What about the median calories of the cereals?

---

``` python
cereal.mean()
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

Notes:

We can also use these summary statistic verbs on the entire dataframe.
This now shows the mean value of each column in the dataframe.

You’ll notice that only the numerical variables are calculated which
makes sense since we would not be able to calculate the mean of
categorical data.

---

# Let’s apply what we learned\!

Notes:

<br>
