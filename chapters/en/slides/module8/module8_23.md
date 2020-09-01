---
type: slides
---

# More Advanced String Processing

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Ok, we have an idea of how we can do some fairly standard strings
processing, however; it’s time we dived a little deeper into this.

There are **MANY** different functions but we’ll concentrate on a couple
here that we will use often and provide a list of several that will be
useful in future string processing adventures.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Replace

Just like in regular text, there will be times in your data analysis
where you will want to replace some of the text within a string.  
That’s where `.replace()` comes in. We usually like our data to be
consistent, however; consistency is not always present even in the best
of dataframes. Let’s take a look at our cycling dataset:

``` python
cycling = pd.read_csv('cycling_data.csv')
cycling.head(10)
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
5  Sep-17-2019 06:57    Morning Ride  Ride  2272     12.45      Rested after the weekend!
6  Sep-17-2019 17:15  Afternoon Ride  Ride  1973     12.45           Legs feeling strong!
7  Sep-18-2019 06:43    Morning Ride  Ride  2285     12.60                        Raining
8  Sep-19-2019 06:49    Morning Ride  Ride  2903     14.57  Thankfully not raining today!
9  Sep-18-2019 17:15  Afternoon Ride  Ride  2101     12.48                Pumped up tires
```

In the first 10 rows of this dataset, there are multiple ways that
“rain” appears in the `Comments` column. Let’s attempt to add some
consistency to this.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Before we do anything, let’s convert this whole column to lowercase, to
make our life easier. This means we only need to be replacing 1 version
of a single word instead of taking consideration all different case
versions.

``` python
cycling_lower = cycling.assign(Comments = cycling['Comments'].str.lower())
cycling_lower.head(9)
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  tired by the end of the week.
5  Sep-17-2019 06:57    Morning Ride  Ride  2272     12.45      rested after the weekend!
6  Sep-17-2019 17:15  Afternoon Ride  Ride  1973     12.45           legs feeling strong!
7  Sep-18-2019 06:43    Morning Ride  Ride  2285     12.60                        raining
8  Sep-19-2019 06:49    Morning Ride  Ride  2903     14.57  thankfully not raining today!
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  tired by the end of the week.
```

You’ll notice in the third row, the word “whether” should have been
spelled “weather”. Let’s replace this word in the entire dataset with
the correct spelling of “weather”.  
In `replace()`, the first argument is the word we are identifying, and
the second is the one that we are replacing it with.

``` python
cycling_rain = cycling_lower.assign(Comments = cycling_lower['Comments'].str.replace('whether', 'weather'))
cycling_rain.head()
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      wet road but nice weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  tired by the end of the week.
```

We can see that the word `whether` has now been replaced with the more
appropriate spelling of `weather`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Contains

`contains()` can be used to filter our dataframe. Instead of checking if
a column equals an exact value, we can check in a pattern is
***contained*** in the column. For example, what if we want all the rows
that have some portion of “rain”.

``` python
cycling_lower['Comments'].str.contains('rain')
```

```out
0      True
1      True
2     False
3     False
4     False
      ...  
28    False
29    False
30    False
31    False
32    False
Name: Comments, Length: 33, dtype: bool
```

This will return a pandas series with Boolean values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cycling_lower[cycling_lower['Comments'].str.contains('rain')]
```

```out
                 Date            Name  Type  Time  Distance                       Comments
0   Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          rain 
1   Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
7   Sep-18-2019 06:43    Morning Ride  Ride  2285     12.60                        raining
8   Sep-19-2019 06:49    Morning Ride  Ride  2903     14.57  thankfully not raining today!
18  Sep-26-2019 17:13  Afternoon Ride  Ride  1860     12.52                        raining
```

Here we see all the rows that contain the pattern `rain` even if they
did not match directly. We can then use this subset to see if our
cyclist Tom was slower on average, on days that it rained\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`.replace()` can be somewhat limiting since we saw it can only replace
specific strings that we specify. What if we want to replace any of the
values in the entire dataframe that contains the word `"rain"` to the
word `"rained"`?

We actually know how to do this\! We can pair our `.contains()` function
with conditional value replacement using `.loc[]`\! We learned this back
in module 2. Let’s see what this looks like.

Let’s replace all rows with values that only contains `"rain"` with
`"rained"`:

``` python
cycling_lower.loc[cycling_lower['Comments'].str.contains('rain'), 'Comments'] = 'rained'
```

What does `cycling_lower` look like now?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The rows originally filtered with “rain” in the dataset:

```out
                 Date            Name  Type  Time  Distance                       Comments
0   Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          rain 
1   Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
7   Sep-18-2019 06:43    Morning Ride  Ride  2285     12.60                        raining
8   Sep-19-2019 06:49    Morning Ride  Ride  2903     14.57  thankfully not raining today!
18  Sep-26-2019 17:13  Afternoon Ride  Ride  1860     12.52                        raining
```

Have now been been been replaced with “rained” in the `Comments` column:

``` python
cycling_lower.head(9)
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         rained
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                         rained
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  tired by the end of the week.
5  Sep-17-2019 06:57    Morning Ride  Ride  2272     12.45      rested after the weekend!
6  Sep-17-2019 17:15  Afternoon Ride  Ride  1973     12.45           legs feeling strong!
7  Sep-18-2019 06:43    Morning Ride  Ride  2285     12.60                         rained
8  Sep-19-2019 06:49    Morning Ride  Ride  2903     14.57                         rained
```

rows 0, and 1 which both had values of `"rain"` and Rows 7 and 8 which
were both `"raining"` and `"raining today"` repectively have now all
been changed to the value `"rained"`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There are quite a few other string methods that are available but this
should get you started.

See the
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#method-summary" target="_blank">documentation
here</a> for a table of some of the other string processing
possibilities available.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
