---
type: slides
---

# Introduction to Working with Strings

Notes: Script here

<html>

<audio controls>

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Although we have already introduced you to strings to a certain degree,
processing and working with this data type is an area that will require
a substantial amount of learning.

In this course, we will only scratch the surface when it comes to
strings. That being said, we do hope to provide you with an adequate
foundation in string processing.

Notes: Script here

<html>

<audio controls >

<source src="/module0/511_module0.mp3" />

</audio>

</html>

---

## Recap

Let’s first remind ourselves of some of the methods we’ve already
learned such as:

  - `.upper()`
  - `.lower()`
  - `.uppercase()`
  - `.count()`
  - `.split()`

When we work with just a general string, we can just use the function on
the end of the object name. For example, if our string object name was
`instrument`:

``` python
instrument = 'Violin'
instrument
```

```out
'Violin'
```

We could convert to all uppercase characters with:

``` python
instrument.upper()
```

```out
'VIOLIN'
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Convert the string to lowercase:

``` python
instrument.lower()
```

```out
'violin'
```

Count the number of occurrences of the letter “i”:

``` python
instrument.count('i')
```

```out
2
```

And split a string on a specified character (in this case “i”):

``` python
instrument.split('i')
```

```out
['V', 'ol', 'n']
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Processing String Columns

The only problem is that when we work with data, we will be applying
these transformations, not to a single string, but to a whole column of
them.

We saw back in Module 4 that string data is represented in a pandas
dataframe using the dtype `object`. This is the default dtype given to
columns that have a mix of different data types or if pandas cannot
identify the column as any other dtype.

Remember when we discussed datetimes columns and we applied time
functions to a whole column by adding `.dt` before the function?

We can use that same syntax style when applying string transformations
to entire columns but this time using `.str`.

Let’s bring back our `cycling` dataframe to demonstrate:

``` python
cycling.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

Notes: Script here

<html>

<audio controls  >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Perhaps we wanted the entire `Comments` column in upper case. We can use
`.assign()` and `.upper` paired with `.str` to transform the column.

``` python
upper_cycle = cycling.assign(Comments = cycling['Comments'].str.upper())
upper_cycle.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         RAIN 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          RAIN
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     WET ROAD BUT NICE WEATHER
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  STOPPED FOR PHOTO OF SUNRISE
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  TIRED BY THE END OF THE WEEK
```

Not too shabby\!

How about a new column that contains the number of times “RAIN” is
counted in `upper_cycle`:

``` python
rain_cycle = upper_cycle.assign(Rain = upper_cycle['Comments'].str.count('RAIN'))
rain_cycle.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments  Rain
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         RAIN      1
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          RAIN     1
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     WET ROAD BUT NICE WEATHER     0
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  STOPPED FOR PHOTO OF SUNRISE     0
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  TIRED BY THE END OF THE WEEK     0
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We’ve also seen this syntax when we used `str.split()` in Module 4 when
we learned about splitting our columns:

``` python
upper_cycle['Comments'].str.split(expand=True)
```

```out
          0        1       2        3        4       5     6     7
0      RAIN     None    None     None     None    None  None  None
1      RAIN     None    None     None     None    None  None  None
2       WET     ROAD     BUT     NICE  WEATHER    None  None  None
3   STOPPED      FOR   PHOTO       OF  SUNRISE    None  None  None
4     TIRED       BY     THE      END       OF     THE  WEEK  None
..      ...      ...     ...      ...      ...     ...   ...   ...
28     VERY   TIRED,  RIDING     INTO      THE    WIND  None  None
29   REALLY    COLD!     BUT  FEELING     GOOD    None  None  None
30  FEELING     GOOD   AFTER        A  HOLIDAY  BREAK!  None  None
31  STOPPED      FOR   PHOTO       OF  SUNRISE    None  None  None
32     BIKE  FEELING  TIGHT,    NEEDS       AN     OIL   AND  PUMP

[33 rows x 8 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Another operation that we’ve lightly touched on is contatenation of
strings. For instance when we add 2 strings together:

``` python
"My favourite colour" + "is Blue"
```

```out
'My favourite colouris Blue'
```

This can be implemented in dataframes too by concatenating 2 columns to
create a new one:

``` python
combined_cycle = cycling.assign(Distance_str = cycling['Distance'].astype('str') + ' km')
combined_cycle.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments Distance_str
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         Rain      12.62 km
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          rain     13.03 km
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather     12.52 km
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise     12.84 km
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week     12.48 km
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

A new function we haven’t discussed but is quite similar to `.upper()`
and `.lower()` is`.capitalize()` which capitalizes the first word of the
string:

``` python
cap_cycle = cycling.assign(Comments = cycling['Comments'].str.capitalize())
cap_cycle.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          Rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

Another is `.title()`, which capitalizes the first letter of every word
in a string:

``` python
cap_cycle = cycling.assign(Comments = cycling['Comments'].str.title())
cap_cycle.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          Rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet Road But Nice Weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped For Photo Of Sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired By The End Of The Week
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

One function that might not seem that pertinent but is extremely useful
is
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html" target="_blank">`.strip()`
</a>.

`strip()` removes characters starting or ending a string, with the
default being spaces.

For Example:

To us, reading “Sunshine” and " Sunshine " are the same thing, but to
Python, they are quite different because of the blank space surrounding
it.

``` python
"Sunshine" == " Sunshine "
```

```out
False
```

The blank space on either side of a string often needs to be removed
depending on the analysis. We can remove them in the example above using
`strip()`:

``` python
string1 = " Sunshine " 
new_string1 = string1.strip()
new_string1
```

```out
'Sunshine'
```

``` python
"Sunshine" == new_string1
```

```out
True
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

This can be especially frustrating when we are trying to filter
dataframes.

Let’s try to filter our data to find rows where the value for the
`Comments` column is “Rain”.

``` python
cycling.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                         Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

We can see that index 0 should be filtered out but we get the following:

``` python
cycling[cycling['Comments'] == 'Rain']
```

```out
Empty DataFrame
Columns: [Date, Name, Type, Time, Distance, Comments]
Index: []
```

No rows are outputted. That’s because there is a blank space following
“Rain”.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s now strip our column using `.strip()` and assigning the changes to
the `Comments` column of a dataframe named `stripped_cycling`. Since we
are using `.strip()` with a dataframe column we have to add `.str`.

``` python
stripped_cycling = cycling.assign(Comments = cycling['Comments'].str.strip())
stripped_cycling.head()
```

```out
                Date            Name  Type  Time  Distance                      Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          Rain
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                          rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

And what happens now when we filter on rain on our new
`stripped_cycling` dataframe:

``` python
stripped_cycling[stripped_cycling['Comments'] == 'Rain']
```

```out
                Date            Name  Type  Time  Distance Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62     Rain
```

Ahh that’s much better\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We are not limited to stripping the values of white space. We can also
strip any other character. Let’s try punctuation\!

``` python
stripped_cycling.tail(5)
```

```out
                 Date            Name  Type  Time  Distance                                   Comments
28  Oct-04-2019 18:08  Afternoon Ride  Ride  1870     12.63           Very tired, riding into the wind
29  Oct-10-2019 07:55    Morning Ride  Ride  2149     12.70              Really cold! But feeling good
30  Oct-10-2019 18:10  Afternoon Ride  Ride  1841     12.59        Feeling good after a holiday break!
31  Oct-11-2019 07:47    Morning Ride  Ride  2463     12.79               Stopped for photo of sunrise
32  Oct-11-2019 18:16  Afternoon Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump
```

We can see that index 30 has a value of `Feeling good after a holiday
break!` in the `Comments` column. After using `str.strip('!')` we can
see that it’s no loger has the exclamation mark\!

``` python
stripped_cycling['Comments'].str.strip("!").tail()
```

```out
28             Very tired, riding into the wind
29                Really cold! But feeling good
30           Feeling good after a holiday break
31                 Stopped for photo of sunrise
32    Bike feeling tight, needs an oil and pump
Name: Comments, dtype: object
```

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
