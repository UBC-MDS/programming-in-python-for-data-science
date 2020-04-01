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
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8      -1        25      3    1.00  0.75  34.384843
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

## Pandas describe()

Pandas has a lot up it’s sleeve but one of the most useful functions is
called describe and it does exactly that. it *describes* your data.
Let’s try it
    out.

``` python
df.describe()
```

```out
         calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.597403   6.922078   96.077922   28.246753   2.207792   1.029610   0.821039  42.665705
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.278956   4.444885   71.286813   22.342523   0.832524   0.150477   0.232716  14.047289
min     50.000000   1.000000   0.000000    0.000000   0.000000  -1.000000  -1.000000   -1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
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
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.597403   6.922078   96.077922   28.246753   2.207792   1.029610   0.821039  42.665705
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.278956   4.444885   71.286813   22.342523   0.832524   0.150477   0.232716  14.047289
min     50.000000   1.000000   0.000000    0.000000   0.000000  -1.000000  -1.000000   -1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%    100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%    110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%    110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max    160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

This table will tell you about:

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

You can make change to either limit how much you show or extend it too
with the additional argument `include = "all"` in the `describe`
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
mean    NaN   NaN  106.883117   2.545455   1.012987  159.675325   2.151948  14.597403   6.922078   96.077922   28.246753   2.207792   1.029610   0.821039  42.665705
std     NaN   NaN   19.484119   1.094790   1.006473   83.832295   2.383364   4.278956   4.444885   71.286813   22.342523   0.832524   0.150477   0.232716  14.047289
min     NaN   NaN   50.000000   1.000000   0.000000    0.000000   0.000000  -1.000000  -1.000000   -1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
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
mean    NaN   NaN  106.883117   2.545455   1.012987  159.675325   2.151948  14.597403   6.922078   96.077922   28.246753   2.207792   1.029610   0.821039  42.665705
std     NaN   NaN   19.484119   1.094790   1.006473   83.832295   2.383364   4.278956   4.444885   71.286813   22.342523   0.832524   0.150477   0.232716  14.047289
min     NaN   NaN   50.000000   1.000000   0.000000    0.000000   0.000000  -1.000000  -1.000000   -1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
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

you can also get single statistics of each column using: either
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

If you want to get a frequency table of a categorical column, there are
a few steps that need to be followed. In the previous slides we talked
about getting a single column from a dataframe using double brackets
like `df[['column-name']]`. That’s great but in order to make a
frequency table we need to use a different structure which you’ll learn
in the next module. Instead of getting a single column with double
brackets we only use single brackets like so:

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
saved as `manufacturer_column` within the brackets.

``` python
manufacturer_freq = manufacturer_column.value_counts()
manufacturer_freq
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

We can then see the frequency of each qualitative value.  
*We can also use the argument `sort = True` within the brackets if we
want to sort the categories in frequency order*

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

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

This looks a bit funny though doesn’t it? That’s because this output
isn’t our usual dataframe type so we need to make it so. We can make
it prettier with `pd.DataFrame` and saving it as a new variable:

``` python
manufacturer_freq_df = pd.DataFrame(manufacturer_freq)
manufacturer_freq_df
```

```out
   mfr
K   23
G   22
P    9
R    8
Q    8
N    6
A    1
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Ah\! That’s what we are used to. The column name is specifying the
counts of the manufacturers, but maybe we should rename that column to
something that makes more sense.

let’s rename that column to `freq`. But how?

We use something called `rename` of course\! When we rename things it’s
especially important that we don’t forget to assign it to a variable or
the column name won’t stick\! Let’s assign it to `freq_mfr_df`.

``` python
freq_mfr_df = manufacturer_freq_df.rename(columns = {"mfr": "freq"})
freq_mfr_df
```

```out
   freq
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

``` python
freq_mfr_df = manufacturer_freq_df.rename(columns = {"mfr": "freq"})
```

This code uses something we’ve never seen before, `{}` curly
brackets\!  
These have a special meaning but for now you need to know that this
`columns` argument need to be set equal to  
`{"old column name" : "new-column-name"}` for us to rename the column.

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
