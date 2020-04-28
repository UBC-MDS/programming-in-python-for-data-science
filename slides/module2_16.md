---
type: slides
---

# Conditional Value Replacement

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Building on things we know

Last module we explored `.loc[]` and how it can help slice and select
specific columns and rows in a dataframe. The power of it however is not
limited to just that. This section marks the return of `.loc[]` and how
it canreplace certain values within a dataframe that meet specified
conditions.

As routine practice, we are bringing in our cereal dataset in once
again. Are you starting to get familiar with it yet?

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

In the previous module we discussed how `.loc[]` take the *_location_*
of specified columns and rows labels of the dataframe and returns them.
In this module, loc will continue to locate specific rows conditionally
on certain column values similarly to how filter is used, however. now
we are replacing the column value.

In our cereal dataframe, the manufacturer value “Q” isn’t that
informative and it might be easier to understand if we change all these
values to something more understandable like “Quaker”.

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

You may look at the above syntax and think “Wait, we did something
similar when we were filtering in the last section?”. You’re right\!

We used simiar syntax when we filter, however, now we’ve added the verb
`.loc[]`. In order to replace “Q” with “Quaker”, however, we need to
indicate which column we are editing as the second argument (which we
can’t do, if we leave out `.loc[]`) . In this example we are editing the
`mfr` column. This code results in a single column dataframe with only
“Q” values.

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

Lastly, to complete our code we need to specify what we want to change
the values to\! What we want these values to *equal* to now.

``` python
df.loc[df['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Wait\! Nothing was outputted with this code\! What happened? Let’s take
a look at our dataframe

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

I can now see that `100% Natural Bran`’s manufacturer value has changed
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

Great, all the “Q” values have been replaced with “Quaker”. We see that
when we use this syntax, we do not need to save the results in a new
dataframe, like we had to with `.assign()` and `.drop()`.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

This also works for inequality conditions. Let’s say instead of
displaying the protein protein content numerically, we instead either
have high or low protein levels. Let’s classify 3 grams or larger as
“high” protein and anything less, as low.

Let’s change the “high” protein values first:

``` python
df.loc[df['protein'] >= 3, 'protein']  = 'High' 
```

Followed by the “low” values.

``` python
#df.loc[df['protein'] < 2, 'protein']  = 'low' 
```

``` python
df
```

```out
                              mfr  type  calories protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                          
100% Bran                       N  Cold        70    High    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran          Quaker  Cold       120    High    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                        K  Cold        70    High    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber       K  Cold        50    High    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight                  R  Cold       110       2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
...                           ...   ...       ...     ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Triples                         G  Cold       110       2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
Trix                            G  Cold       110       1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
Wheat Chex                      R  Cold       100    High    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
Wheaties                        G  Cold       100    High    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
Wheaties Honey Gold             G  Cold       110       2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 15 columns]
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
