---
type: slides
---

# Conditional Value Replacement and Assignment

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Building on things we know

In the last module, we explored `.loc[]` and how it can help slice and
select specific columns and rows in a dataframe, however, the power of
`.loc[]` does not stop there.  
This section marks the return of `.loc[]` and how it can replace certain
values within a dataframe that meet specified conditions.

Keeping with our routine, we are bringing in our cereal dataset in once
again. Are you starting to get familiar with this dataset yet?

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

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# The return of loc

We have discussed how `.loc[]` can select and return specified columns
and rows of the dataframe. In this module, `loc[]` will be used to
locate specific rows conditionally on their column values. This is done
similarly to how we filtered our dataframe but with 2 distinct
differences:

1.  We use `.loc[]` to find the rows specifying certain conditions.  
2.  Once we have obtained our desired rows we replace their values in
    either a specified column or create a new column altogether.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

In our cereal dataframe, the manufacturer value “Q” isn’t that
informative and it might be easier to understand our data if we change
all these values to something more complete like “Quaker”.

Let’s start by simply finding all the cereals made by the “Quaker Oats”
manufacturer:

``` python
df.loc[df['mfr'] == 'Q']
```

```out
                   mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                
100% Natural Bran    Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
Cap'n'Crunch         Q  Cold       120        1    2     220    0.0   12.0      12      35        25      2     1.0  0.75  18.042851
Honey Graham Ohs     Q  Cold       120        1    2     220    1.0   12.0      11      45        25      2     1.0  1.00  21.871292
Life                 Q  Cold       100        4    2     150    2.0   12.0       6      95        25      2     1.0  0.67  45.328074
Puffed Rice          Q  Cold        50        1    0       0    0.0   13.0       0      15         0      3     0.5  1.00  60.756112
Puffed Wheat         Q  Cold        50        2    0       0    1.0   10.0       0      50         0      3     0.5  1.00  63.005645
Quaker Oat Squares   Q  Cold       100        4    1     135    2.0   14.0       6     110        25      3     1.0  0.50  49.511874
Quaker Oatmeal       Q   Hot       100        5    2       0    2.7    1.0       1     110         0      1     1.0  0.67  50.828392
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

You may look at the above syntax and think “Wait, didn’t we do something
similar when we were filtering in the last section?”. You’re right\!

We used similar syntax when we filter, however, now we’ve added the verb
`.loc[]`.

To replace “Q” with “Quaker”, we indicate which column we are editing as
the second argument (which we can’t do, if we do not use `.loc[]`).  
In our scenario, we are editing the `mfr` column.  
This code results in a single column dataframe with only “Q” values.

``` python
df.loc[df['mfr'] == 'Q', 'mfr']  
```

```out
name
100% Natural Bran     Q
Cap'n'Crunch          Q
Honey Graham Ohs      Q
Life                  Q
Puffed Rice           Q
Puffed Wheat          Q
Quaker Oat Squares    Q
Quaker Oatmeal        Q
Name: mfr, dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Lastly, we need to specify yo what we want to change the values. In our
case, we are replacing “Q” with “Quaker”.

``` python
df.loc[df['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Wait\! Nothing was outputted with this code\! What happened? Let’s take
a look at our dataframe.

``` python
df.head()
```

```out
                              mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                           
100% Bran                       N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran          Quaker  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                        K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber       K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight                  R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

We can now see that `100% Natural Bran's` manufacturer value has changed
to `Quaker` but what about the rest of them?

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Let’s filter and see\!

``` python
df[df['mfr'] == 'Quaker']  
```

```out
                       mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                    
100% Natural Bran   Quaker  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
Cap'n'Crunch        Quaker  Cold       120        1    2     220    0.0   12.0      12      35        25      2     1.0  0.75  18.042851
Honey Graham Ohs    Quaker  Cold       120        1    2     220    1.0   12.0      11      45        25      2     1.0  1.00  21.871292
Life                Quaker  Cold       100        4    2     150    2.0   12.0       6      95        25      2     1.0  0.67  45.328074
Puffed Rice         Quaker  Cold        50        1    0       0    0.0   13.0       0      15         0      3     0.5  1.00  60.756112
Puffed Wheat        Quaker  Cold        50        2    0       0    1.0   10.0       0      50         0      3     0.5  1.00  63.005645
Quaker Oat Squares  Quaker  Cold       100        4    1     135    2.0   14.0       6     110        25      3     1.0  0.50  49.511874
Quaker Oatmeal      Quaker   Hot       100        5    2       0    2.7    1.0       1     110         0      1     1.0  0.67  50.828392
```

Great, all the “Q” values have been replaced with “Quaker”.  
When we use this syntax, we do not need to save the results in a new
object name like we had to with `.assign()` and `.drop()`.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Replacing with Inequalities.

This also works for inequality conditions.

If we are replacing numerical values with characters or words (or vice
versa) we need to assign our desired values to a **new column** and not
the existing one.  
Perhaps we want just 2 categories for protein levels -“high” and “low”.
Any cereal above 3 grams of protein will be considered a “high” protein
level and anything less, as a “low” protein level.

Let’s assign the “high” protein values first. The only difference here
from earlier is we now use an inequality for our condition and we
designate a new column name instead of an existing one. Let’s save the
values in a column named `protein_level`.

``` python
df.loc[df['protein'] >= 3, 'protein_level']  = 'High' 
```

Next by the “low” values.

``` python
df.loc[df['protein'] < 3, 'protein_level']  = 'low' 
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Let’s see the results by scrolling to the right of the dataframe.

``` python
df.head()
```

```out
                              mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating protein_level
name                                                                                                                                                         
100% Bran                       N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973          High
100% Natural Bran          Quaker  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679          High
All-Bran                        K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505          High
All-Bran with Extra Fiber       K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912          High
Almond Delight                  R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843           low
```

Super\!

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
