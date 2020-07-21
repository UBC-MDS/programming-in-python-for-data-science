---
type: slides
---

# Plotting Groupby Objects

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s return to the question we asked at the beginning slides of
exercise 25:

*_Which manufacturer has the highest mean sugar content?_*

A nice way of showing our results would be to graph this. A bar chart
like this should do the trick\!

<img src="/module2/module2_24/unnamed-chunk-2-1.png" width="576" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s go through the steps that are needed to make this plot.

  - We are going to save our plot as an object named `sugar_plot` and
    use our chaining technique as well.
  - We create a groupby object and calculate the mean for each column in
    the dataframe.  
  - Next, we take the single column we are interested in using
    `.loc[]`.  
  - Our last action is the plot everything using `.plot.bar()`.

<!-- end list -->

``` python
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar()
             )
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar()
             )
sugar_plot
```

<img src="/module2/module2_24/unnamed-chunk-3-1.png" width="576" />

This plot, however, looks a little unfinished. We need to add a title
and label our y-axis.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We’ve added a title before, so there is nothing new there but adding x
and y-axis labels is a little different. We can increase the label font
sizes using the argument `fontsize`. In this case, we reference our
initial plot and use the verb `.set_ylabel()` and `.set_xlabel()` with
the desired axis label as an argument and `fontsize` to assign a desired
label size. To avoid unnecessary information that will be returned
otherwise, whatever our last verb being used with our plot (named
\`sugar\_plot) has to be reassigned back to the object. If we did this
any other way, we would not have the ability to do more transformations
on our plot, or we would get additional information with the plot
output.

``` python
sugar_plot = (df.groupby(by='mfr')
                .mean()
                .loc[:,'sugars']
                .plot.bar(title='Mean sugar content among manufacturers')
              )
sugar_plot.set_ylabel('Sugar content (in grams)', fontsize=9)
sugar_plot = sugar_plot.set_xlabel('Manufacturer', fontsize=9)
sugar_plot
```

<img src="/module2/module2_24/unnamed-chunk-4-1.png" width="45%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last plot, we used `.loc[:,'sugars']` to select a single column
to the plot, however, we can show multiple mean column values in a
single plot by selecting more columns. The columns `fat`, `fiber` and
`protein` seem like good choices.

``` python
nutrition_plot = (df.groupby(by='mfr')
                    .mean()
                    .loc[:, ['fat', 'fiber', 'protein']]
                    .plot.bar(title='Mean nutritrion value over different manufacturers')
                 )
nutrition_plot.set_ylabel('Content (in grams)', fontsize=9)
nutrition_plot = nutrition_plot.set_xlabel('Manufacturer', fontsize=9)
nutrition_plot
```

<img src="/module2/module2_24/unnamed-chunk-5-1.png" width="60%" />

If you want high fibre and low fat, consider having N’s cereals for
breakfast (or lunch or dinner)\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Multiple Grouping

We can group by multiple columns as well. For example we can grouping by
not only manufacturer but also by cereal type\! All we do is put both
both column labels in square brackets within `.groupby()`.

``` python
mfr_type_group = df.groupby(by=['mfr', 'type'])
mfr_type_group.groups
```

```out
{('A', 'Hot'): Int64Index([43], dtype='int64'), ('G', 'Cold'): Int64Index([5, 7, 11, 12, 13, 14, 18, 22, 31, 36, 40, 42, 47, 51, 59, 69, 70, 71, 72, 73, 75, 76], dtype='int64'), ('K', 'Cold'): Int64Index([2, 3, 6, 16, 17, 19, 21, 24, 25, 26, 28, 38, 39, 46, 48, 49, 50, 53, 58, 60, 62, 66, 67], dtype='int64'), ('N', 'Cold'): Int64Index([0, 63, 64, 65, 68], dtype='int64'), ('N', 'Hot'): Int64Index([20], dtype='int64'), ('P', 'Cold'): Int64Index([9, 27, 29, 30, 32, 33, 34, 37, 52], dtype='int64'), ('Q', 'Cold'): Int64Index([1, 10, 35, 41, 54, 55, 56], dtype='int64'), ('Q', 'Hot'): Int64Index([57], dtype='int64'), ('R', 'Cold'): Int64Index([4, 8, 15, 23, 44, 45, 61, 74], dtype='int64')}
```

The attribute `ngroups` indicates how many groups there are.

``` python
mfr_type_group.ngroups
```

```out
9
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to get the dataframe of a specific group now, we put the
value of each column in parentheses.

``` python
mfr_type_group.get_group(('K', 'Cold'))
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
6                 Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
16                Corn Flakes   K  Cold       100        2    0     290    1.0   21.0       2      35        25      1    1.00  1.00  45.863324
17                  Corn Pops   K  Cold       110        1    0      90    1.0   13.0      12      20        25      2    1.00  1.00  35.782791
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
58                Raisin Bran   K  Cold       120        3    1     210    5.0   14.0      12     240        25      2    1.33  0.75  39.259197
60             Raisin Squares   K  Cold        90        2    0       0    2.0   15.0       6     110        25      3    1.00  0.50  55.333142
62              Rice Krispies   K  Cold       110        2    0     290    0.0   22.0       3      35        25      1    1.00  1.00  40.560159
66                     Smacks   K  Cold       110        2    1      70    1.0    9.0      15      40        25      2    1.00  0.75  31.230054
67                  Special K   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1    1.00  1.00  53.131324

[23 rows x 16 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can plot in the same way as before

``` python
type_plot = (df.groupby(by=['mfr', 'type'])
                    .mean()
                    .loc[:, ['sugars']]
                    .plot.bar(title='Mean sugar value over different manufacturers and types'))
type_plot.set_ylabel('Sugar (in grams)', fontsize=16)
type_plot.set_xlabel('Manufacturer and cereal type', fontsize=16)
type_plot
```

<img src="/module2/module2_24/unnamed-chunk-9-1.png" width="50%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Using `pandas` to plot groupby objects is very limited and is not
possible for many other plot types such as scatter plots.  
If you wish to learn more advanced visualization and Python plotting
package **Altair**, come back soon and visit our in development course
**DSCI-031 Exploratory Data Visualization**.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
