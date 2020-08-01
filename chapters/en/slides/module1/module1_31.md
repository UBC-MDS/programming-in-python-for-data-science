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
pretty quickly and with little code\! Take `manufacturer_freq` object we
made in the last slide deck.

``` python
manufacturer_freq
```

```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64
```

This would be great to express as a bar chart. But how do we do it?

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

1.  We take the dataframe we wish to plot, in this case `freq_mfr_df`.  
2.  Next we add `.plot` since we want to plot it\!  
3.  But what kind of plot do we want?\! A bar chart in this case would
    work nicely so lets add `.bar()` after that.

<!-- end list -->

``` python
manufacturer_freq.plot.bar()
```

<img src="/module1/module1_31/unnamed-chunk-4-1.png" width="576" />
See how quick that was? The important things to notice here is that we
want to `.plot` a `.bar()` graph.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What else can we plot from our original cereal dataframe named `df`?
Maybe we want to see the relationship between `sugars` and `calories` in
cereals?  
This would require a `scatter` plot\!  
In the code we would need to specify the x and y axis which means we
would need to specify the column names for each axis; In this case the
x-axis is the `sugars` column and the y-axis is the `calories` column.

``` python
df.plot.scatter(x='sugars', y='calories')
```

<img src="/module1/module1_31/unnamed-chunk-5-1.png" width="576" />

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
Opacity is set with the argument `alpha` and accepts values between 0
and 1, with 1 being full intensity.

``` python
df.plot.scatter(x='sugars', y='calories', alpha=0.3)
```

<img src="/module1/module1_31/unnamed-chunk-6-1.png" width="576" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Look at that\! Now we can see there are multiple cereals that have 2.5g
of sugar with 100 calories. What if we wanted to change the colour to
purple? Enter parameter `color`\! We can also add a bit of readability
by separating the arguments into separate lines.

``` python
df.plot.scatter(x='sugars', 
                y='calories', 
                alpha=.3, 
                color='purple')
```

<img src="/module1/module1_31/unnamed-chunk-7-1.png" width="60%" />

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Those data points look pretty small. To enlarge them, the argument `s`
should do the trick. Also every good graph should have a title\! Let’s
take this opportunity to finish off this graph and set the argument
`title` to something as well.

``` python
df.plot.scatter(x="sugars",
                y="calories",
                alpha= 0.3, 
                color="purple",
                s=80, 
                title="The relationship between sugar and calories in cereals")
```

<img src="/module1/module1_31/unnamed-chunk-8-1.png" width="60%" />

---

``` python

source = pd.read_csv('cereal.csv')

chart1 = alt.Chart(source, width = 500, height = 300).mark_bar(color = 'red').encode(
    x='mfr',
    y='count()'
)
chart1
```

<img src="/module1/chart1.png"  width="50%" />

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
