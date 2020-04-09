---
type: slides
---

# Sorting Dataframes

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Sorting

When we load in our data, it is generally ordered in the same way it is
stored. We can easily sort a dataframe based on its column values. The
tool for that? `df.sort_values()`.

As an example, if we wanted to order the cereals based on sugar content,
we could do the
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

What if we wanted the ones with a higher sugar first? Then we would
order them in `descending` order by setting the parameter `ascending` to
“False”:

``` python
sorted_sugar = df.sort_values(by="sugars", ascending=False)
sorted_sugar
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

Perfect, now we have the high sugar content cereals at the top of the
dataframe.

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
