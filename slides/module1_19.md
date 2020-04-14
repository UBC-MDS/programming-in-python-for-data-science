---
type: slides
---

# Slicing and Selecting using df.iloc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Slicing Dataframe

Up to this point, we have been manipulating our dataframe with column
and row ***labels*** using `df. loc`.  
Slicing can also be done by the location position of each row with
`df.iloc`. `df.iloc` is very similar, however, the “i” in `iloc` refers
to the index ***integer*** position.

We are going to return to our cereal dataset and take a look at the
first 15 rows.

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

Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` but
we want to slice based on their position.  
Using Python’s counting method of starting at zero, we conclude
`All-Bran` to be at position to
    2.

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
100% Bran                   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
100% Natural Bran           Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
Apple Cinnamon Cheerios     G  Cold       110        2    2     180    1.5   10.5      10      70        25      1     1.0  0.75  29.509541
Apple Jacks                 K  Cold       110        2    0     125    1.0   11.0      14      30        25      2     1.0  1.00  33.174094
```

We get `Apple Cinnamon Cheerios` position to be 5 in the same way.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We can use the same coding structure we learned with `df.loc`, but this
time using row positions instead of labels with
    `df.iloc[]`

``` python
df.iloc[2:5]
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

But wait\! Something is missing here\!

Why doesn’t `Apple Cinnamon Cheerios` appear in the dataframe?

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

That’s because when we use slicing by index position, it will take all
the indices including the lower bound but *EXCLUDING* the upper bound.
If we wanted to include `Apple Cinnamon Cheerios` we would have to go 1
index position
    further.

``` python
df.iloc[2:6]
```

```out
                          mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
name                                                                                                                                       
All-Bran                    K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
Almond Delight              R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
Apple Cinnamon Cheerios     G  Cold       110        2    2     180    1.5   10.5      10      70        25      1     1.0  0.75  29.509541
```

If we reflect about this a bit a bit it actually make some sense. Think
about the calculation `6 - 2 = 4` . We get 4 items remaining which is
the amount of cereals we want in our in new dataframe.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

The same concepts can apply to the columns of the dataframe. Let’s say
we want all the rows but we only want the columns starting at `protein`
and ending (including) at column `sugars`.  
Using the logic we learned in the last set of slides, we would use the
following
    code:

``` python
df.iloc[ : ,  3:9 ]
```

```out
                           protein  fat  sodium  fiber  carbo  sugars
name                                                                 
100% Bran                        4    1     130   10.0    5.0       6
100% Natural Bran                3    5      15    2.0    8.0       8
All-Bran                         4    1     260    9.0    7.0       5
All-Bran with Extra Fiber        4    0     140   14.0    8.0       0
Almond Delight                   2    2     200    1.0   14.0       8
...                            ...  ...     ...    ...    ...     ...
Triples                          2    1     250    0.0   21.0       3
Trix                             1    1     140    0.0   13.0      12
Wheat Chex                       3    1     230    3.0   17.0       3
Wheaties                         3    1     200    3.0   17.0       3
Wheaties Honey Gold              2    1     200    1.0   16.0       8

[77 rows x 6 columns]
```

We would need to specify all rows using `:` as we did when we used
`df.loc[]`. The column `protein` is at index position 3 (we do not
include the index label as a column) and `sugars` is at index position
8, but since we want to include the 8th column we need to use the 9th
position to make sure we get all the columns *BEFORE* the upper bound.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

The same would apply if we only wanted certain rows with certain
columns. Let’s say we want the rows `All-Bran` to `Apple Cinnamon
Cheerios` and `protein` to `sugars`.  
**Rows**  
`All-Bran` located at position 2.  
`Apple Cinnamon Cheerios` is located at position 5.  
**Columns**  
`protein` is located at position 3.  
`sugar` is located at position
    8.

``` python
df.iloc[2:6, 3:9]
```

```out
                           protein  fat  sodium  fiber  carbo  sugars
name                                                                 
All-Bran                         4    1     260    9.0    7.0       5
All-Bran with Extra Fiber        4    0     140   14.0    8.0       0
Almond Delight                   2    2     200    1.0   14.0       8
Apple Cinnamon Cheerios          2    2     180    1.5   10.5      10
```

Both of our upper bound have been compensated with + 1 to make sure they
are included in the new dataframe.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Selecting with df.iloc\[\]

Selecting using `iloc` is done identically to `loc`, however, the items
within each set of square brackets **MUST** be integers, and not in
quotation marks.

Let’s say we want the rows `Cheerios`, `Basic 4` and `Apple Jacks` with
the columns `rating`, `fat` and `type` *in that order*.

**Rows**  
`Cheerios` is located at position 11.  
`Basic 4` is located at position 7.  
`Apple Jacks` is located at position 6.

**Columns**  
`rating` is located at position 14.  
`fat` is located at position 4.  
`type` is located at position 1.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Now let’s put those position into square backing within `df.iloc[]`

Recap the locations: `Cheerios` = 11, `Basic 4` = 7 and `Apple Jacks` =
6, `rating` = 14, `fat` = 4, `type` = 1.

``` python
df.iloc[[11, 7, 6], [14, 4, 1]]
```

```out
                rating  fat  type
name                             
Cheerios     50.764999    2  Cold
Basic 4      37.038562    2  Cold
Apple Jacks  33.174094    0  Cold
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Nice work\! Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
