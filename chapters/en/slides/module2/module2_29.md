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

Let’s learn some other useful abilities of `Altair`. When specifying `x`
and `y` in the `encode(..)` function, altair allows us to specify what
data type to expect. See the table below for a description of the data
types available and how to specify them.

| Data Type    | Shorthand Code | Description                   | Examples                               |
| ------------ | -------------- | ----------------------------- | -------------------------------------- |
| Quantitative | `Q`            | a continuous quantity         | 5, 5.0, 5.011                          |
| Ordinal      | `O`            | a discrete ordered quantity   | “dislike”, “neutral”, “like”           |
| Nominal      | `N`            | a discrete unordered quantity | eye color, postal code, university     |
| Temporal     | `T`            | a time or date value          | date (August 13 2020), time (12:00 pm) |

Ordinal values imply that there is some natural ordering to the values.
For example, the ratings a movie receives is on an ordinal scale since a
five star rating is better than a single star rating. In contrast, there
is no such natural ordering for nominal values. An example of this would
be someone’s eye color, their address or the university they attended.

Altair is sometimes smart enough to tell which data type the input is.
For example, the `color` of someone’s eyes are considered as `nominal`,
anything `numeric` will be considered as `quantitative` and `time` or
`date` values are considered as `temporal`. We will see examples of
temporal data types in module 8. However, these defaults may not always
be correct. In the next slide, we will see an example of specifying data
types when plotting.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now let’s say we are interested in plotting the sugar content in cereals
from each manufacturer. We do this using a `bar` plot Which we are
familiar with. We will be using the `mfr` column and the `sugars` column
from the `cereal` dataframe we have been using.

Here, `mfr` is a categorical column (remember this explanation from
module 1?). This is because there is no specific order in which cereal
type must come before another. For example, it is not the case that
“Kelloggs” must come before “Quaker”. Because of this, the `mfr`
column is categorized as a **nominal** data type. The `sugars` column in
contrast, is categorized as quantitative column. This is because the
values in the column are all quantitative measurement that takes on any
positive integer value.

``` python
chart1 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
    x='mfr:N', # set the manufacturer column as nominal
    y='sugars:Q' # set the sugars column as quantitative
).properties(title="Bar plot of manufacturer sugar content")
chart1
```
<img src="/module2/chart1.png" alt="A caption" width="40%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

So far when plotting with altair, we have been mapping our `x` and `y`
in the `encode(x=..,y=..)` function. However, doing so gives us very
little control on how exactly we would like to map our x and y values.
In order to have more control, we can map our x and y values using
`x=alt.X(...)` and `y=alt.Y(...)` respectively. This gives us a lot more
control over how values are mapped in the resulting plot. Let’s generate
the plot on the previous slide using the method.

``` python
chart2 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N'), # use alt.X() to map the x-axis
    y=alt.Y('sugars:Q') # use alt.Y() to map the y-axis
).properties(title="Bar plot of manufacturer sugar content")
chart2
```
<img src="/module2/chart2.png" alt="A caption" width="40%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There is another type of plot we can make using Altair. Let’s say we
were interested in visualizing a grouping of the number of `calories`
into various ranges from the cereal dataset. A `histogram` would be an
ideal plot for this type of task. A histogram is similar to a `bar`
chart except that it groups quantitative data into `ranges`, and the
height of each bar shows the frequency of each range. We demonstrate how
to create a `histogram` using Altair in the next slide.

---

For example, we can generate a `histogram` plot of the `calories` column
in the cereal dataframe. This will enable us to see the various values
of calories and how many times they occur. To make a histogram, we use
the `mark_bar()` function. In the `encode()` function, we specify the
x-axis as calories. However, since we are creating a histogram, we
specify the y-axis as `count:Q` to get the height of each calorie bar.

``` python
chart3 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
    x=alt.X('calories:Q'), # set x-axis as calories 
    y=alt.Y('count():Q') # set the y-axis as the occurrence count for each calorie value
).properties(title="Histogram plot of cereal calorie content")
chart3
```
<img src="/module2/chart3.png" alt="A caption" width="35%" />

Notice that we have used `count()` to compute the frequency of each of
the ranges of the calorie content in cereal dataframe.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Previously in module 1, when making bar plots, we used the `count()`
argument extensively. This argument helps us count the occurrences of
elements within the `x` variable. This is useful for creating both bar
plots and histograms. The count argument can be used to create both a
histogram and a bar plot since it is used to count the frequency of
elements within the `x` variable.

---

Altair also gives us the ability to change the ranges of the bar widths
or `bins` that the data is grouped into. This may be useful when viewing
a dataset with lots of different values. Also, having control over the
number of bins in a histogram may help to make visualization easier
which will make the plots easier to digest. If we wanted to change the
number of bins in the previous plot, we can use the
`bin=alt.Bin(maxbins=..)` in `alt.X()` argument to set a value for the
number of bins. Lets set the number of bins in the previous plot to `20`
by setting `bin=alt.Bin(maxbins=20)`.

``` python
chart4 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
    x=alt.X('calories:Q', bin=alt.Bin(maxbins=20)), # set max number of bins to 50
    y=alt.Y('count():Q')
).properties(title="Histogram of cereal calorie content with bins = 20")
chart4
```
<img src="/module2/chart4.png" alt="A caption" width="35%" />

Notice how the number of groups have changed and the histogram is much
easier to digest compared to the previous one.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When plotting with Altair, the `x` and `y` axis are labeled with the
default column names. However, this may not always be ideal since column
names may not always be informative. The plot below is an example of
this. Take the `mfr` column in our cereal dataframe as another example,
if we did not know beforehand that this meant manufacturer, it would be
hard to guess this from a plot. Luckily Altair allows us to set custom
axis `titles` using the `title=""` argument.

<img src="/module2/chart4.png" alt="A caption" width="35%" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s see how we can change the x and y axis titles using Altair. We
will see how this works by providing more informative axis titles to the
bar plot we made for the sugar content for each manufacturer previously.

``` python
chart5 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N', title="Cereal manufacturer"), # use alt.X() to map the x-axis
    y=alt.Y('sugars:Q', title="Sugar content") # use alt.Y() to map the y-axis
).properties(title="Bar plot of manufacturer sugar content")
chart5
```
<img src="/module2/chart5.png" alt="A caption" width="40%" />

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
like this should do the trick\! However, before doing this, we need a
few tricks under our belt. At the beginning slides of exercise 25, we
used the `groupby(by='mfr')` function and then took the `mean()` to
compute these values. Lets see what the resulting dataframe looks like.

``` python
sugar_df = pd.DataFrame(cereal.groupby(by='mfr').mean().loc[:, 'sugars'])
sugar_df
```

```out
       sugars
mfr          
A    3.000000
G    7.954545
K    7.565217
N    1.833333
P    8.777778
Q    5.500000
R    6.125000
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Notice in the previous slide that `mfr` has now moved to the left of the
dataframe and the label is lower now than the other column labels? This
is because when you apply `groupby()` to a column, this column becomes
the new dataframe index. Although this is a useful feature in many
cases, Altair cannot access the column names of index columns. To deal
with this, we use `reset_index()` which will convert `mfr` to a regular
column again. See below:

``` python
sugar_df = sugar_df.reset_index()
sugar_df
```

```out
  mfr    sugars
0   A  3.000000
1   G  7.954545
2   K  7.565217
3   N  1.833333
4   P  8.777778
5   Q  5.500000
6   R  6.125000
```

We can see that `mfr` column has now moved right and next to the
`sugars` column. The index has also been replaced with integers. Since
our dataframe in in this form, we are able to proceed in plotting the
mean sugar content for each manufacturer.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now that we have our `sugar_df` in the correct format, we can proceed.
Using Altair we can plot the `mfr` column which we’ve identified as a
nominal value on the x axis and `sugars` which we agreed was a
quantitative value on the y axis. (Also we can’t forget our title\!)

``` python
chart6 = alt.Chart(sugar_df, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N', title="Manufacturer"),
    y=alt.Y('sugars:Q', title="Mean sugar content")
).properties(title="Bar plot of manufacturers mean sugar content")
chart6
```
<img src="/module2/chart6.png" alt="A caption" width="40%" />

Notes: Script here

<html>

5 <audio controls > <source src="/placeholder_audio.mp3" /> </audio>

</html>

---

Let’s go through the steps that were needed to make the plot in the
previous slide.

  - We created a groupby object and calculated the mean for each column
    in the resulting dataframe.  
  - Next, we took the single column we are interested in using `.loc[]`.
  - Since grouping by made `mfr` the new index, we had to use
    `reset_index()` to make `mfr` a column again.
  - Our last action was to generate a bar plot using altair.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Sometimes sorting a dataframe by quantity helps us obtain observations
quicker. For example, if we sorted the mean sugar content for the
manufacturers before generating the previous plot, it would be easier to
identify which manufacturer produces cereals with the highest mean
calorie content. Altair allows us to sort a column while plotting it.
Sorting can be done on either the x or y axis using the `sort=` in the
`alt.x` or `alt.y` function.. The sort argument takes in either `x` or
`y` to specify which axis to sort by. To specify `descinding` order, we
use `-`, and nothing in order to specify ascending. See the example
below.

``` python
chart7 = alt.Chart(sugar_df, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N', sort="y", title="Manufacturer"),  # use sort="y" to sort in ascending order
    y=alt.Y('sugars:Q', title="Mean sugar content")
).properties(title="Bar plot of manufacturers mean sugar content sorted in ascending order")
chart7
```
<img src="/module2/chart7.png" alt="A caption" width="30%" />

This plot shows us immediately that cereals from manufacturer `p` have
the highest mean sugar content.

Notes: Script here

<html>

5 <audio controls > <source src="/placeholder_audio.mp3" /> </audio>

</html>

---

To generate a bar plot of mean calorie content sorted in `descending`
order, we recycle the code from the previous slide. However, we add a
`-` in the `sort=..` argument to specify that we would like to sort in
descending order.

``` python
chart8 = alt.Chart(sugar_df, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N', sort="-y", title="Manufacturer"),  # use sort="-y" to sort in descending order
    y=alt.Y('sugars:Q', title="Mean sugar content")
).properties(title="Bar plot of manufacturers mean sugar content sorted in descending order")
chart8
```
<img src="/module2/chart8.png" alt="A caption" width="40%" />

Notes: Script here

<html>

5 <audio controls > <source src="/placeholder_audio.mp3" /> </audio>

</html>

---

<!-- We've added a title before, so there is nothing new there but adding x and y-axis labels is a little different. We can increase the label font sizes using the argument `fontsize`. In this case, we reference our initial plot and use the verb `.set_ylabel()` and `.set_xlabel()` with the desired axis label as an argument and `fontsize` to assign a desired label size.  -->

<!-- To avoid unnecessary information that will be returned otherwise, whatever our last verb being used with our plot (named `sugar_plot) has to be reassigned back to the object. If we did this any other way, we would not have the ability to do more transformations on our plot, or we would get additional information with the plot output.  -->

<!-- ```{python  out.width = '45%', fig.asp = .40} -->

<!-- sugar_plot = (df.groupby(by='mfr') -->

<!--                 .mean() -->

<!--                 .loc[:,'sugars'] -->

<!--                 .plot.bar(title='Mean sugar content among manufacturers') -->

<!--               ) -->

<!-- sugar_plot.set_ylabel('Sugar content (in grams)', fontsize=9) -->

<!-- sugar_plot = sugar_plot.set_xlabel('Manufacturer', fontsize=9) -->

<!-- sugar_plot -->

<!-- ``` -->

<!-- Notes: Script here -->

<!-- <html> -->

<!-- <audio controls > -->

<!--   <source src="/placeholder_audio.mp3" /> -->

<!-- </audio></html> -->

<!-- --- -->

<!-- In the last plot, we used `.loc[:,'sugars']` to select a single column to the plot, however, we can show multiple mean column values in a single plot by selecting more columns. The columns `fat`, `fiber` and `protein` seem like good choices.  -->

<!-- ```{python out.width = '60%', fig.asp = .58} -->

<!-- nutrition_plot = (df.groupby(by='mfr') -->

<!--                     .mean() -->

<!--                     .loc[:, ['fat', 'fiber', 'protein']] -->

<!--                     .plot.bar(title='Mean nutritrion value over different manufacturers') -->

<!--                  ) -->

<!-- nutrition_plot.set_ylabel('Content (in grams)', fontsize=9) -->

<!-- nutrition_plot = nutrition_plot.set_xlabel('Manufacturer', fontsize=9) -->

<!-- nutrition_plot -->

<!-- ``` -->

<!-- If you want high fibre and low fat, consider having N's cereals for breakfast (or lunch or dinner)! -->

<!-- Notes: Script here -->

<!-- <html> -->

<!-- <audio controls > -->

<!--   <source src="/placeholder_audio.mp3" /> -->

<!-- </audio></html> -->

<!-- --- -->

<!-- ## Multiple Grouping  -->

<!-- We can group by multiple columns as well.  -->

<!-- For example we can grouping by not only manufacturer but also by cereal type! All we do is put both both column labels in square brackets within `.groupby()`. -->

<!-- ```{python} -->

<!-- mfr_type_group = df.groupby(by=['mfr', 'type']) -->

<!-- mfr_type_group.groups -->

<!-- ``` -->

<!-- The attribute `ngroups` indicates how many groups there are.   -->

<!-- ```{python} -->

<!-- mfr_type_group.ngroups -->

<!-- ``` -->

<!-- Notes: Script here -->

<!-- <html> -->

<!-- <audio controls > -->

<!--   <source src="/placeholder_audio.mp3" /> -->

<!-- </audio></html> -->

<!-- --- -->

<!-- If we want to get the dataframe of a specific group now, we put the value of each column in parentheses.  -->

<!-- ```{python} -->

<!-- mfr_type_group.get_group(('K', 'Cold')) -->

<!-- ``` -->

<!-- Notes: Script here -->

<!-- <html> -->

<!-- <audio controls > -->

<!--   <source src="/placeholder_audio.mp3" /> -->

<!-- </audio></html> -->

<!-- --- -->

<!-- We can plot in the same way as before  -->

<!-- ```{python fig.width = 13, fig.height = 9,  out.width = '50%'} -->

<!-- type_plot = (df.groupby(by=['mfr', 'type']) -->

<!--                     .mean() -->

<!--                     .loc[:, ['sugars']] -->

<!--                     .plot.bar(title='Mean sugar value over different manufacturers and types')) -->

<!-- type_plot.set_ylabel('Sugar (in grams)', fontsize=16) -->

<!-- type_plot.set_xlabel('Manufacturer and cereal type', fontsize=16) -->

<!-- type_plot -->

<!-- ``` -->

<!-- Notes: Script here -->

<!-- <html> -->

<!-- <audio controls > -->

<!--   <source src="/placeholder_audio.mp3" /> -->

<!-- </audio></html> -->

<!-- --- -->

If all this excites you and you wish to learn more advanced
visualization using **Altair**, come back soon and visit our in
development course **DSCI-031 Exploratory Data Visualization**.

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
