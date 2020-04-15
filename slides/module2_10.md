---
type: slides
---

# Filtering

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Filtering is probably one of the most frequent data maniputation you
will do in data analysis. Filtering is often used when we are either
trying to rid the dataframe of unwanted rows, or analyze rows with a
particular column value.

Think of it as a sieve keeping only the rows matching conditions you
have set.

Let’s welcome back the `cereal.csv` data we have worked with in Module
1.

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

## Standard filtering

Suppose you are trying to find a cereal with a protein content greater
than 4g per serving. We can find those rows with the following
    code.

``` python
df[ df['protein'] > 4]
```

```out
               mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                            
Cheerios         G  Cold       110        6    2     290    2.0   17.0       1     105        25      1     1.0  1.25  50.764999
Quaker Oatmeal   Q   Hot       100        5    2       0    2.7    1.0       1     110         0      1     1.0  0.67  50.828392
Special K        K  Cold       110        6    0     230    1.0   16.0       3      55        25      1     1.0  1.00  53.131324
```

This is a little tricky because we first specify the dataframe `df` and
within it’s square brackets, we specify the column attempting to be
filtered with `df['protein']` followed by the condition.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can do with not only with inequalities but with equal to as
    well.

``` python
df[ df['protein'] == 4]
```

```out
                                  mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                               
100% Bran                           N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
All-Bran                            K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber           K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Life                                Q  Cold       100        4    2     150    2.0   12.0       6      95        25      2     1.0  0.67  45.328074
Maypo                               A   Hot       100        4    1       0    0.0   16.0       3      95        25      2     1.0  1.00  54.850917
Muesli Raisins; Dates; & Almonds    R  Cold       150        4    3      95    3.0   16.0      11     170        25      3     1.0  1.00  37.136863
Muesli Raisins; Peaches; & Pecans   R  Cold       150        4    3     150    3.0   16.0      11     170        25      3     1.0  1.00  34.139765
Quaker Oat Squares                  Q  Cold       100        4    1     135    2.0   14.0       6     110        25      3     1.0  0.50  49.511874
```

Now we get all the cereals with a protein content of 4g per serving. The
key point to remember here is that we use **2** equal signs, else our
code will return an error.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can filter on categorical columns too. In this example maybe I want
only cereals from the manufacturer “Q” (For
    Quackers)

``` python
df[ df['mfr'] == 'Q']
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

Here we are using the double equal signs we saw above.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Multiple Condition Filtering - “and”

We now know how to filter on one condition but how do we filter if we
have many? Let’s say we only wanted cereals with a protein content
between 4 to 5
    groms?

``` python
df[ (df['protein'] >= 4) & (df['protein'] <= 5) ]
```

```out
                                  mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                               
100% Bran                           N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
All-Bran                            K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber           K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Life                                Q  Cold       100        4    2     150    2.0   12.0       6      95        25      2     1.0  0.67  45.328074
...                                ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
Muesli Raisins; Dates; & Almonds    R  Cold       150        4    3      95    3.0   16.0      11     170        25      3     1.0  1.00  37.136863
Muesli Raisins; Peaches; & Pecans   R  Cold       150        4    3     150    3.0   16.0      11     170        25      3     1.0  1.00  34.139765
Quaker Oat Squares                  Q  Cold       100        4    1     135    2.0   14.0       6     110        25      3     1.0  0.50  49.511874
Quaker Oatmeal                      Q   Hot       100        5    2       0    2.7    1.0       1     110         0      1     1.0  0.67  50.828392

[9 rows x 15 columns]
```

Code Explained:  
We need to use the special symbol `&` meaning “and”. This means that
both conditions must hold true to be returned in the new dataframe. Each
condition is wrapped with parentheses to distinguish each condition from
one another.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Let’s try a case where we filter on 2 different columns. Let’s say we
only want hot cereals with a fiber content greater than
    2.

``` python
df[ (df['type'] == 'Hot') & (df['fiber'] > 2)]
```

```out
               mfr type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                           
Quaker Oatmeal   Q  Hot       100        5    2       0    2.7    1.0       1     110         0      1     1.0  0.67  50.828392
```

The same rules apply to 2 different column conditions.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Multiple Condition Filtering - or

Now suppose that we are interested in cereals that either have a fiber
content greater that 6 **OR** a protein content above 5. We only need
one of these conditions to hold to return a
    row.

``` python
df[ (df['fiber'] > 6) | (df['protein'] > 5)]
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Cheerios                    G  Cold       110        6    2     290    2.0   17.0       1     105        25      1     1.0  1.25  50.764999
Special K                   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1     1.0  1.00  53.131324
```

Instead of using the `&` symbol we use `|` which is called the “pipe
operator”. This means “or” in the Python programming language.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

If we wanted a dataframe that met both conditions using “and” (`&`).
This is what would happen

``` python
df[ (df['fiber'] > 6) & (df['protein'] > 5)]
```

```out
Empty DataFrame
Columns: [mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating]
Index: []
```

Since no rows meet both conditions, a dataframe with zero rows is
returned.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Multiple Condition Filtering

Let’s do one more examples where we use both “and” as well as “or”

Let’s build on condition of wanted cereals that either have a fiber
content greater that 6 **OR** a protein content above 5 but this time we
only want those cereals from the manufacturer “K”.

``` python

df[ ((df['fiber'] > 6) | (df['protein'] > 5)) & (df['mfr'] == 'K') ]
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Special K                   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1     1.0  1.00  53.131324
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We need to take great care on including parentheses when needed. If we
did not include parentheses around our “or” conditions, this is what
would have been
    returned:

``` python
df[ (df['fiber'] > 6) | (df['protein'] > 5) & (df['mfr'] == 'K') ]
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Special K                   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1     1.0  1.00  53.131324
```

Python will now move from left to right and in this case it will select
all the cereals with a fiber content greater than 6 *or* all the cereal
satisfying a protein content above 5 made by manufacturer “K”.

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
