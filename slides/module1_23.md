---
type: slides
---

# Summary Statistics\!

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Now we’ve learned about how to get our dataframe how we want it, let’s
try and make some fun of it\!

We have our data, now what?

We usually like to learn from it. We want to find out about maybe some
summary statistics about the features of the data.

Let’s load in our cereal dataset again.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

``` python
df = pd.read_csv('cereal.csv', index_col = 0)
df.head(15)
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3    1.00  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3    1.00  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3    1.00  0.75  34.384843
Apple Cinnamon Cheerios     G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
Apple Jacks                 K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
Basic 4                     G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
Bran Chex                   R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
Bran Flakes                 P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
Cap'n'Crunch                Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
Cheerios                    G  Cold       110        6    2     290    2.0   17.0       1     105        25      1    1.00  1.25  50.764999
Cinnamon Toast Crunch       G  Cold       120        1    3     210    0.0   13.0       9      45        25      2    1.00  0.75  19.823573
Clusters                    G  Cold       110        3    2     140    2.0   13.0       7     105        25      3    1.00  0.50  40.400208
Cocoa Puffs                 G  Cold       110        1    1     180    0.0   12.0      13      55        25      2    1.00  1.00  22.736446
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Sorting

When we load in our data, it is generally ordered in the same way it is
stored. We can easily sort a dataframe based on it’s column values. The
tool for that? `df.sort_values()`.

As an example, if I wanted to order the cereals based on sugar content,
I could do the
    following:

``` python
df.sort_values(by="sugars")
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
Puffed Wheat                Q  Cold        50        2    0       0    1.0   10.0       0      50         0      3    0.50  1.00  63.005645
Cream of Wheat (Quick)      N   Hot       100        3    0      80    1.0   21.0       0       1         0      2    1.00  1.00  64.533816
Shredded Wheat              N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83  1.00  68.235885
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
Shredded Wheat 'n'Bran      N  Cold        90        3    0       0    4.0   19.0       0     140         0      1    1.00  0.67  74.472949
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Post Nat. Raisin Bran       P  Cold       120        3    1     200    6.0   11.0      14     260        25      3    1.33  0.67  37.840594
Apple Jacks                 K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
Total Raisin Bran           G  Cold       140        3    1     190    4.0   15.0      14     230       100      3    1.50  1.00  28.592785
Smacks                      K  Cold       110        2    1      70    1.0    9.0      15      40        25      2    1.00  0.75  31.230054
Golden Crisp                P  Cold       100        2    0      45    0.0   11.0      15      40        25      1    1.00  0.88  35.252444

[77 rows x 15 columns]
```

This allows us to see the cereals with lower sugar content on the top.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

What if I wanted the ones with a higher sugar on the top? Then I would
order them in `descending` order by setting the parameter `ascending` to
“False”:

``` python
df.sort_values(by="sugars", ascending=False)
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
Smacks                      K  Cold       110        2    1      70    1.0    9.0      15      40        25      2    1.00  0.75  31.230054
Golden Crisp                P  Cold       100        2    0      45    0.0   11.0      15      40        25      1    1.00  0.88  35.252444
Total Raisin Bran           G  Cold       140        3    1     190    4.0   15.0      14     230       100      3    1.50  1.00  28.592785
Post Nat. Raisin Bran       P  Cold       120        3    1     200    6.0   11.0      14     260        25      3    1.33  0.67  37.840594
Apple Jacks                 K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
...                        ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
Puffed Wheat                Q  Cold        50        2    0       0    1.0   10.0       0      50         0      3    0.50  1.00  63.005645
Puffed Rice                 Q  Cold        50        1    0       0    0.0   13.0       0      15         0      3    0.50  1.00  60.756112
Cream of Wheat (Quick)      N   Hot       100        3    0      80    1.0   21.0       0       1         0      2    1.00  1.00  64.533816
Shredded Wheat              N  Cold        80        2    0       0    3.0   16.0       0      95         0      1    0.83  1.00  68.235885

[77 rows x 15 columns]
```

Ahh, now we have the high sugar content cereals at the top.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Pandas describe()

Pandas has a lot up it’s sleeve but one of the most useful functions is
called describe and it does exactly that. it *describes* our data. Let’s
try it
    out.

``` python
df.describe()
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

Notes: Script
    here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

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

This table will tell us about:

  - `count`: The number of non-NA/null observations.
  - `mean`: The mean of column
  - `std` : The standard deviation of a column
  - `min`: The min value for a column
  - `max`: The max value for a column
  - By default the 25, 50 and 75 percentile of the observations

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can make changes to either limit how much is shown or extend it with
the additional argument `include = "all"` in the `describe`
    brackets.

``` python
df.describe(include = "all")
```

```out
        mfr  type    calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count    77    77   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
unique    7     2         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
top       K  Cold         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
freq     23    74         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
mean    NaN   NaN  106.883117   2.545455   1.012987  159.675325   2.151948  14.623377   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std     NaN   NaN   19.484119   1.094790   1.006473   83.832295   2.383364   4.188138   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min     NaN   NaN   50.000000   1.000000   0.000000    0.000000   0.000000   1.000000   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%     NaN   NaN  100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%     NaN   NaN  110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%     NaN   NaN  110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max     NaN   NaN  160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

Notes: Script
    here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

```out
        mfr  type    calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count    77    77   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
unique    7     2         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
top       K  Cold         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
freq     23    74         NaN        NaN        NaN         NaN        NaN        NaN        NaN         NaN         NaN        NaN        NaN        NaN        NaN
mean    NaN   NaN  106.883117   2.545455   1.012987  159.675325   2.151948  14.623377   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std     NaN   NaN   19.484119   1.094790   1.006473   83.832295   2.383364   4.188138   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min     NaN   NaN   50.000000   1.000000   0.000000    0.000000   0.000000   1.000000   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%     NaN   NaN  100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%     NaN   NaN  110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%     NaN   NaN  110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max     NaN   NaN  160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

Adding `include = "all"` within the brackets adds some additional
statistics about categorical columns.

  - `unique`: how many observations are unique
  - `top`: which observation value is most occuring
  - `freq`: what is the frequency of the most occuring observation

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can also get single statistics of each column using: either
`df.mean()`,`df.std()`, `df.count()`, `df.median()`, `df.sum()`.

Let’s see the sum of the cereal ratings.

``` python
ratings = df['rating'] 
ratings.sum()
```

```out
3285.259284
```

Or maybe the median calories of the cereals.

``` python
calories = df['calories'] 
calories.median()
```

```out
110.0
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Frequency Tables

If we want to get a frequency table of a categorical column, there are a
few steps that need to be followed. In the previous slides we talked
about getting a single column from a dataframe using double brackets
like `df[['column-name']]`. Instead of getting a single column with
double brackets we only use single brackets to get a column for
frequency tables.

``` python
manufacturer_column = df["mfr"]
manufacturer_column
```

```out
name
100% Bran                    N
100% Natural Bran            Q
All-Bran                     K
All-Bran with Extra Fiber    K
Almond Delight               R
                            ..
Triples                      G
Trix                         G
Wheat Chex                   R
Wheaties                     G
Wheaties Honey Gold          G
Name: mfr, Length: 77, dtype: object
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We saved the object in a variable called `manufacturer_column` in the
same way as we have other dataframes before.  
Next we cant use `pd.value_counts()` referencing that the column we
saved as `manufacturer_column`.

``` python
manufacturer_freq = manufacturer_column.value_counts()
manufacturer_freq
```

```out
K    23
G    22
P     9
Q     8
R     8
N     6
A     1
Name: mfr, dtype: int64
```

We can then see the frequency of each qualitative value.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Sometimes it’s useful to save a new dataframe as a `csv` file for future
use or to use in another application. We can save dataframes using the
function `df.to_csv()`. Simply put our desired `csv` file name in
quotations within the parentheses.

Notes: Script here.

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
