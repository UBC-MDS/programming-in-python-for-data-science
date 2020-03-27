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
                          mfr  type  calories  ...  weight  cups     rating
name                                           ...                         
100% Bran                   N  Cold        70  ...     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120  ...     1.0  1.00  33.983679
All-Bran                    K  Cold        70  ...     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50  ...     1.0  0.50  93.704912
Almond Delight              R  Cold       110  ...     1.0  0.75  34.384843

[5 rows x 15 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Indexing Dataframes

We can see 7 of the 15 columns of the dataframe and the first 5 rows of
the data. Let’s say we only want certain rows of the whole dataframe or
certain columns.

We talked about how `df.head()` will generate the first few rows (5 as
default) of a dataframe but what if we wanted rows 5-10?

The first column of this dataframe is called the `index`. This is what
we specified with `index_col=0` when we read in our data. Each row is
given a label as well as a position. In this case, the label of an
observation is the cereal name and the index position is a number. In
other cases, the index label could be named with a number.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Here are the first 15 rows of the
    dataframe:

``` python
df.head(15)
```

```out
                          mfr  type  calories  ...  weight  cups     rating
name                                           ...                         
100% Bran                   N  Cold        70  ...    1.00  0.33  68.402973
100% Natural Bran           Q  Cold       120  ...    1.00  1.00  33.983679
All-Bran                    K  Cold        70  ...    1.00  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50  ...    1.00  0.50  93.704912
Almond Delight              R  Cold       110  ...    1.00  0.75  34.384843
Apple Cinnamon Cheerios     G  Cold       110  ...    1.00  0.75  29.509541
Apple Jacks                 K  Cold       110  ...    1.00  1.00  33.174094
Basic 4                     G  Cold       130  ...    1.33  0.75  37.038562
Bran Chex                   R  Cold        90  ...    1.00  0.67  49.120253
Bran Flakes                 P  Cold        90  ...    1.00  0.67  53.313813
Cap'n'Crunch                Q  Cold       120  ...    1.00  0.75  18.042851
Cheerios                    G  Cold       110  ...    1.00  1.25  50.764999
Cinnamon Toast Crunch       G  Cold       120  ...    1.00  0.75  19.823573
Clusters                    G  Cold       110  ...    1.00  0.50  40.400208
Cocoa Puffs                 G  Cold       110  ...    1.00  1.00  22.736446

[15 rows x 15 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

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

So now let’s say we want 5 rows past `Almond Delight`. That means we
want rows with the index labels `Apple Cinnamon Cheerios` to
`Cap'n'Crunch`.

``` python
df.loc[ "Apple Cinnamon Cheerios" : "Cap'n'Crunch"]
```

```out
                        mfr  type  calories  ...  weight  cups     rating
name                                         ...                         
Apple Cinnamon Cheerios   G  Cold       110  ...    1.00  0.75  29.509541
Apple Jacks               K  Cold       110  ...    1.00  1.00  33.174094
Basic 4                   G  Cold       130  ...    1.33  0.75  37.038562
Bran Chex                 R  Cold        90  ...    1.00  0.67  49.120253
Bran Flakes               P  Cold        90  ...    1.00  0.67  53.313813
Cap'n'Crunch              Q  Cold       120  ...    1.00  0.75  18.042851

[6 rows x 15 columns]
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

# let’s try it out\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
