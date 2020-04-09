---
type: slides
---

# Slicing with Pandas Using df.loc

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Congratulations on writing your first code\! This is great\! We have
read in our data and know the dimensions. What now? Let’s go over how we
would **index**, **slice** and **select** certain columns or rows of our
data.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Cereal Data

Let’s import pandas and bring in our dataset named `cereal.csv` using
the name of the candy bar as the index like we did last time with
`index_col=0`.

``` python
import pandas as pd
  
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

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## The Index

We can see all the columns and the first 5 rows of the dataframe. Let’s
say we only want certain rows of the whole dataframe or certain columns.

We talked about how `df.head()` will generate the first few rows (5 as
default) of a dataframe but what if we wanted rows 5-10?

The first column of this dataframe is called the `index`. This is what
we specified with `index_col=0` when we read in our data with
`pd.read_csv()`. Each row has a label (the index) as well as a position.
In this case, the index label of an observation is the cereal name and
the index position is where it lies in the dataframe.The index label
doesn’t alway have to be named with words, they could be also named with
a number which can get confusing.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Here are the first 10 rows of the
    dataframe:

``` python
df.head(10)
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
```

Let’s talk about the observation named `Almond Delight`. Its index label
is `Almond Delight` but its index position is 4.  
If you just went and counted those again and started screaming “5\! It’s
the fifth position”, that’s ok. In the Python language, we start
counting at position 0 (then 1, 2, 3, and 4 for Almond Delight).

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

So now let’s say we want the 5 rows past `Almond Delight`. That means we
want rows with the index labels `Apple Cinnamon Cheerios` to
`Cap'n'Crunch`.

``` python
df.loc[ "Apple Cinnamon Cheerios" : "Cap'n'Crunch"]
```

```out
                        mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                     
Apple Cinnamon Cheerios   G  Cold       110        2    2     180    1.5   10.5      10      70        25      1    1.00  0.75  29.509541
Apple Jacks               K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
Basic 4                   G  Cold       130        3    2     210    2.0   18.0       8     100        25      3    1.33  0.75  37.038562
Bran Chex                 R  Cold        90        2    1     200    4.0   15.0       6     125        25      1    1.00  0.67  49.120253
Bran Flakes               P  Cold        90        3    0     210    5.0   13.0       5     190        25      3    1.00  0.67  53.313813
Cap'n'Crunch              Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2    1.00  0.75  18.042851
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3"/>

</audio>

</html>

---

`df.loc[ "Apple Cinnamon Cheerios" : "Cap'n'Crunch"]`

This essentially means the *dataframe location from `Apple Cinnamon
Cheerios` to `Cap'n'Crunch`.*

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3"/>

</audio>

</html>

---

Now what if we only wanted certain columns now?

Perhaps we were only interested in the `calories` to `fiber` columns of
those
rows?

``` python
df.loc[ "Apple Cinnamon Cheerios" : "Cap'n'Crunch", "calories" : "fiber"]
```

```out
                         calories  protein  fat  sodium  fiber
name                                                          
Apple Cinnamon Cheerios       110        2    2     180    1.5
Apple Jacks                   110        2    0     125    1.0
Basic 4                       130        3    2     210    2.0
Bran Chex                      90        2    1     200    4.0
Bran Flakes                    90        3    0     210    5.0
Cap'n'Crunch                  120        1    2     220    0.0
```

`loc` is used to slice columns and rows by **label** and within an
interval. The general format to slice both rows and columns together
looks like
this:

``` python
`df.loc[ row-name-start : row-name-end , "column name start" : "column name end"]`
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s try it out\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
