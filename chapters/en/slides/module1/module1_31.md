---
type: slides
---

# Quick Viz with Altair\!

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to visualize things using different plots we can do that
pretty quickly and with little code\! Take `cereal` object we analyzed
in the last slide deck.

``` python
df
```

```out
                         name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
..                        ...  ..   ...       ...      ...  ...     ...  ...     ...     ...       ...    ...     ...   ...        ...
72                    Triples   G  Cold       110        2    1     250  ...       3      60        25      3     1.0  0.75  39.106174
73                       Trix   G  Cold       110        1    1     140  ...      12      25        25      2     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
75                   Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559

[77 rows x 16 columns]
```

Let say we are interested in the `manufacturer` column. This would be
great to express as a bar chart. But how do we do it?

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To do this, we are going to use a very nifty package called `altair`.
Altiar is a new data visualization tool that produces plots relatively
easily. Like any other packages we have seen so far, `altair` needs to
be imported before we can use it.

``` python
import altair as alt
from altair_saver import save
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To make a `bar` plot using `altair`, we follow the steps below:

1.  We take the dataframe we wish to plot, in this case `df`.
2.  We create an `altair` plot object using `alt.chart()`.
3.  We can pass the dataframe we’d like to plot by using `alt.chart(df)`
4.  But what kind of plot do we want?\! A bar chart in this case would
    work nicely so lets add `.mark_bar()` after that.
5.  Now that we have specified that we want a `bar` plot from our `df`,
    we need to specify what column. This is done using the
    `.encode(x='mfr', y='count()')`. The `count` here says that we would
    like to count up all the occurrences of the different manufacturers.
6.  Putting it all together, we have
    `alt.chart(df).mark_bar().encode(x='mfr', y='count()')`. Lets see
    how this looks on the next slide.

---

``` python
# Note that the setting the width and height is for consistency.

chart1 = alt.Chart(df, width=500, height=300).mark_bar().encode(
    x='mfr',
    y='count()'
)
chart1
```
<img src="/module1/chart1.png" alt="A caption" width="40%" />

See how quick that was? The important things to notice here is that we
want create a `alt.chart()` object and then specify that we want a
`.mark_bar()` graph and then specifying which column using `.encode()`.

---

What else can we plot from our original cereal dataframe named `df`?
Maybe we want to see the relationship between `sugars` and `calories` in
cereals?  
This would require a `scatter` plot which can be done by specifying
`mark_circle` after creating the `alt.chart()` object.  
In the `.encode()` function, we would need to specify the x and y axis
which means we would need to specify the column names for each axis; In
this case the x-axis is the `sugars` column and the y-axis is the
`calories` column.

``` python
chart2 = alt.Chart(df, width=500, height=300).mark_circle().encode(
    x='sugars',
    y='calories'
)
chart2
```
<img src="/module1/chart2.png" alt="A caption" width="45%" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Something you may have noticed is that there are 77 cereals but there
doesn’t seem to be 77 data points\! That’s because some of them are
lying on top of each other with the same sugar ar calorie values. It may
be of use to set an opacity to the graph to differential those points.
Opacity is set with the argument `opacity` in the
`mark_circle(opacity=...)` function and accepts values between 0 and 1,
with 1 being full intensity.

``` python
# lets set the opacity to 30%
chart3 = alt.Chart(df, width=500, height=300).mark_circle(opacity=0.3).encode(
    x='sugars',
    y='calories'
)
chart3
```
<img src="/module1/chart3.png" width="45%" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Look at that\! Now we can see there are multiple cereals that have 2.5g
of sugar with 100 calories. So what if you don’t fancy the color the
default color `blue`? Well that is okay, we can change the color using
the `color` argument in the `.mark_circle(color=...)` function. Lets
change the color to `red`(I like red) while keeping the same opacity.

``` python
# lets set the opacity to 30%
chart4 = alt.Chart(df, width=500, height=300).mark_circle(color='red', opacity=0.3).encode(
    x='sugars',
    y='calories'
)
chart4
```
<img src="/module1/chart4.png" width="45%" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Maybe I have bad eyes, but those data points look pretty small. Good
news though, we can make them bigger (bigger is better?) To enlarge
them, the argument `size` in the `mark_circle(size=..)` should do the
trick.

``` python
# lets set the opacity to 30%
chart5 = alt.Chart(df, width=500, height=300).mark_circle(color='red', size=12, opacity=0.3).encode(
    x='sugars',
    y='calories'
)
chart5
```
<img src="/module1/chart5.png" width="45%" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Also every good graph should have a title\! A title provides useful
information as to what the plot is about. Let’s take this opportunity to
finish off our scatter plot graph and set the argument `title` to
something as well. To set the `title`, we use the `title` argument to
the `.properties(title=..)` function.

``` python
# lets set the opacity to 30%
chart6 = alt.Chart(df, width=500, height=300).mark_circle(color='red', size=12, opacity=0.3).encode(
    x='sugars',
    y='calories'
).properties(title="Scatter plot sugars vs calories for different cereals")
chart6
```
<img src="/module1/chart6.png" width="45%" />

Notes: Script here.

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
