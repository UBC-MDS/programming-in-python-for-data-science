---
type: slides
---

# Working with Dates and Time

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

It wasn’t too long ago in Module 4, where we briefly mentioned another
column dtype called `datetime64`.

<center>

<img src='/module4/full.png' width="100%">

</center>

Dates and times can be a bit tricky and require a specific data type so
that analysis can be done correctly.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Parsing dates yourself can be difficult and time-consuming. To
demonstrate this, let’s make an attempt at parsing the `Date` column in
our `cycling` dataframe which currently has an `object`dtype.

``` python
cycling.head()
```

```out
               Date            Name  Type  Time  Distance                      Comments
0   2019-09-09 7:13    Morning Ride  Ride  2084     12.62                          Rain
1  2019-09-09 20:52  Afternoon Ride  Ride  2531     13.03                          rain
2   2019-09-10 7:23    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3  2019-09-10 21:06  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4   2019-09-11 7:28    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

First we would need to split the column separating the date and the time
and rename the labels:

``` python
dates = (cycling['Date'].str.split(' ', expand=True)
                           .rename(columns = {0:'Date',
                                              1:'Time'}))
dates.head()
```

```out
         Date   Time
0  2019-09-09   7:13
1  2019-09-09  20:52
2  2019-09-10   7:23
3  2019-09-10  21:06
4  2019-09-11   7:28
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Once again, we need to split the date column and separate it into
columns for the year, month and day:

``` python
dates = (dates['Date'].str.split('-', expand=True).rename(columns = {0:'Year',
                                                                     1:'Month',
                                                                     2:'Day'}))
dates.head()
```

```out
   Year Month Day
0  2019    09  09
1  2019    09  09
2  2019    09  10
3  2019    09  10
4  2019    09  11
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Currently the values in `dates` are of type `str` so we would not be
able to sort them in a temporal manner:

``` python
dates.iloc[0,0]
```

```out
'2019'
```

``` python
type(dates.iloc[0,0])
```

```out
<class 'str'>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We must convert the columns to integers values and add them to the
`cycling` dataframe.

``` python
cycling_dates = (cycling.assign(Year = dates['Year'].astype(int),
                                Month = dates['Month'].astype(int),
                                Day = dates['Day'].astype(int)))
cycling_dates.head(3)
```

```out
               Date            Name  Type  Time  Distance                   Comments  Year  Month  Day
0   2019-09-09 7:13    Morning Ride  Ride  2084     12.62                       Rain  2019      9    9
1  2019-09-09 20:52  Afternoon Ride  Ride  2531     13.03                       rain  2019      9    9
2   2019-09-10 7:23    Morning Ride  Ride  1863     12.52  Wet road but nice weather  2019      9   10
```

We are then going to select and reorder the columns in the dataframe so
the new date columns are on the left side.

``` python
cycling_dates = cycling_dates.loc[:, ['Year', 'Month', 'Day', 'Name',
                                      'Type', 'Time', 'Distance', 'Comments']]
cycling_dates.head(3)
```

```out
   Year  Month  Day            Name  Type  Time  Distance                   Comments
0  2019      9    9    Morning Ride  Ride  2084     12.62                       Rain
1  2019      9    9  Afternoon Ride  Ride  2531     13.03                       rain
2  2019      9   10    Morning Ride  Ride  1863     12.52  Wet road but nice weather
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

And now, can we sort them:

``` python
cycling_dates.sort_values(['Year', 'Month', 'Day']).head()
```

```out
   Year  Month  Day            Name  Type  Time  Distance                      Comments
0  2019      9    9    Morning Ride  Ride  2084     12.62                          Rain
1  2019      9    9  Afternoon Ride  Ride  2531     13.03                          rain
2  2019      9   10    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3  2019      9   10  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  2019      9   11    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

After doing all this, there are still a lot of limitations, We didn’t
even separate the time yet and calculating the time between dates now
can be extremely difficult. (The differing number of days in months is a
contributing factor.)

Now we can understand that we really don’t want to do it this way,
right?

Thankfully we don’t have to either. Pandas has some built-in functions
that will make our lives much easier.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pandas parse\_dates

Remember How Pandas is built using the NumPy library? Well in a similar
way, Pandas datetime verbs are built using the built-in Python
<a href="https://docs.python.org/3/library/datetime.html" target="_blank">`datetime`
library</a>.

We can parse our data at the same time as we read in our dataframe using
the argument `parse_dates`.  
Originally the `Date` column adopts a dtype of `object` when the data is
read in.

``` python
cycling = pd.read_csv('cycling_data.csv')
cycling.head(3)
```

```out
               Date            Name  Type  Time  Distance                   Comments
0   2019-09-09 7:13    Morning Ride  Ride  2084     12.62                       Rain
1  2019-09-09 20:52  Afternoon Ride  Ride  2531     13.03                       rain
2   2019-09-10 7:23    Morning Ride  Ride  1863     12.52  Wet road but nice weather
```

``` python
cycling.dtypes
```

```out
Date         object
Name         object
Type         object
Time          int64
Distance    float64
Comments     object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Using the `parse_dates`argument with `pd.read_csv()` changes that so
that it now adopts a `datetime64` dtype:

``` python
cycling_dates = pd.read_csv('cycling_data.csv', parse_dates = ['Date'])
cycling_dates.head()
```

```out
                 Date            Name  Type  Time  Distance                      Comments
0 2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                          Rain
1 2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                          rain
2 2019-09-10 07:23:00    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3 2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4 2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

``` python
cycling_dates.dtypes
```

```out
Date        datetime64[ns]
Name                object
Type                object
Time                 int64
Distance           float64
Comments            object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now that we have a datetime column which expresses when Tom began his
journey, we can the earliest tom left on one of his Morning Rides:

``` python
cycling_dates[cycling_dates['Name'] == 'Morning Ride'].min()
```

```out
Date                          2019-09-09 07:13:00
Name                                 Morning Ride
Type                                         Ride
Time                                         1712
Distance                                    11.79
Comments    A little tired today but good weather
dtype: object
```

We could als find the time

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

As another example, our date data may be split between multiple columns:

``` python
pd.read_csv('cycling_data_split_time.csv').head()
```

```out
   Year  Month  Day      Clock            Name  Type  Time  Distance                      Comments
0  2019      9   10   00:13:04  Afternoon Ride  Ride  2084     12.62                          Rain
1  2019      9   10   13:52:18    Morning Ride  Ride  2531     13.03                          rain
2  2019      9   11   00:23:50  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  2019      9   11   14:06:19    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  2019      9   12   00:28:05  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

We can combine the `Year`, `Month` and `Day` columns to a single
datetime column by using a dictionary within the `parse_dates` argument.
The dictionary key, indicates the new column name and the dictionary
value is a list with the multiple date columns to combine:

``` python
(pd.read_csv('cycling_data_split_time.csv',
              parse_dates={'Date': ['Year', 'Month', 'Day', 'Clock']})
              .head())
```

```out
                 Date            Name  Type  Time  Distance                      Comments
0 2019-09-10 00:13:04  Afternoon Ride  Ride  2084     12.62                          Rain
1 2019-09-10 13:52:18    Morning Ride  Ride  2531     13.03                          rain
2 2019-09-11 00:23:50  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3 2019-09-11 14:06:19    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4 2019-09-12 00:28:05  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What if we need to convert a column into dtype `datetime` after reading
in our data? That’s not a problem\! We have `pd.to_datetime()` to
transform columns of an already existing dataframe.

Let’s use our original `cycling` dataframe where `Date` is still of
dtype `object`.

``` python
cycling = pd.read_csv('cycling_data.csv')
cycling.head()
```

```out
               Date            Name  Type  Time  Distance                      Comments
0   2019-09-09 7:13    Morning Ride  Ride  2084     12.62                          Rain
1  2019-09-09 20:52  Afternoon Ride  Ride  2531     13.03                          rain
2   2019-09-10 7:23    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3  2019-09-10 21:06  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4   2019-09-11 7:28    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

``` python
cycling.dtypes
```

```out
Date         object
Name         object
Type         object
Time          int64
Distance    float64
Comments     object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

To convert `Date` to a datetime dtype, we use `pd.to_datetime()` and
`assign()`:

``` python
new_cycling = cycling.assign(Date = pd.to_datetime(cycling['Date']))
new_cycling.head()
```

```out
                 Date            Name  Type  Time  Distance                      Comments
0 2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                          Rain
1 2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                          rain
2 2019-09-10 07:23:00    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3 2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4 2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

``` python
new_cycling.dtypes
```

```out
Date        datetime64[ns]
Name                object
Type                object
Time                 int64
Distance           float64
Comments            object
dtype: object
```

Ok, but what if I don’t want the full datetime value and I want a column
with only a portion of it, like the month, or year?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

No worries, we can add a new column to our dataframe in a similar as we
did before but now we can extract a portion of the `datetime` column by
using
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components" target="_blank">one
of the many pandas datetime tools</a>. Here are a couple of examples:

  - `.dt.day_name()` for the day of the week:

<!-- end list -->

``` python
new_cycling['Date'].dt.day_name().head()
```

```out
0       Monday
1       Monday
2      Tuesday
3      Tuesday
4    Wednesday
Name: Date, dtype: object
```

We can pair this with `.assign()` to add this as a column in the
dataframe:

``` python
new_cycling.assign(weekday = new_cycling['Date'].dt.day_name()).head()
```

```out
                 Date            Name  Type  Time  Distance                      Comments    weekday
0 2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                          Rain     Monday
1 2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                          rain     Monday
2 2019-09-10 07:23:00    Morning Ride  Ride  1863     12.52     Wet road but nice weather    Tuesday
3 2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise    Tuesday
4 2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48  Tired by the end of the week  Wednesday
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

  - `dt.day` for the day:

<!-- end list -->

``` python
new_cycling['Date'].dt.day.head()
```

```out
0     9
1     9
2    10
3    10
4    11
Name: Date, dtype: int64
```

Again using `.assign()` to add it to our dataframe:

``` python
new_cycling.assign(day = new_cycling['Date'].dt.day).head()
```

```out
                 Date            Name  Type  Time  Distance                      Comments  day
0 2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                          Rain    9
1 2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                          rain    9
2 2019-09-10 07:23:00    Morning Ride  Ride  1863     12.52     Wet road but nice weather   10
3 2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise   10
4 2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48  Tired by the end of the week   11
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There is some inconsistency with these verbs. You can see that some use
parentheses `()` and some do not. Here are some of the most common
useful datetime tools:

  - `dt.year`
  - `dt.month`
  - `dt.month_name()`
  - `dt.day`
  - `dt.day_name()`
  - `dt.hour`
  - `dt.minute`

For a full list refer to
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#:~:text=Timestamp%20is%20the%20pandas%20equivalent,oriented%20data%20structures%20in%20pandas.&text=Value%20to%20be%20converted%20to%20Timestamp.&text=Offset%20which%20Timestamp%20will%20have." target="_blank">the
attributes and methods section of the Timestamp documentation</a>.

Using the `.dt` portion of these can only be used on a pandas Series. We
can extract the day, month, year hour, or minute from a single datetime
value, using the same nouns but omiiting the `dt.`.

Let’s see how that’s possible.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
new_cycling.head()
```

```out
                 Date            Name  Type  Time  Distance                      Comments
0 2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                          Rain
1 2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                          rain
2 2019-09-10 07:23:00    Morning Ride  Ride  1863     12.52     Wet road but nice weather
3 2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84  Stopped for photo of sunrise
4 2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48  Tired by the end of the week
```

If I select the first example in row 1 of our `new_cycling` dataset,
you’ll notice that its outputs something called a `Timestamp`.

``` python
timestamp_ex = new_cycling.loc[1,'Date']
timestamp_ex
```

```out
Timestamp('2019-09-09 20:52:00')
```

This is a pandas data type.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
timestamp_ex
```

```out
Timestamp('2019-09-09 20:52:00')
```

Timestamps show a snapshot of when an event has occurred. Timestamps are
complete with both dates and times. If that’s not complete, Python will
fill in any unknowns with default values (often with `00:00:00` for
time, if only the date was provided).

To obtain the month\_name, day, or hour from the Timestamp, we can use
the same nouns in the previous slide without `.ts.`:

``` python
timestamp_ex.month_name()
```

```out
'September'
```

``` python
timestamp_ex.day
```

```out
9
```

``` python
timestamp_ex.hour
```

```out
20
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In our analysis it might be important to know how frequent events occur
and the time between them.  
`.diff()` is a useful function for that.

``` python
cycling_intervals = new_cycling['Date'].sort_values().diff()
cycling_intervals
```

```out
0                NaT
1    0 days 13:39:00
2    0 days 10:31:00
3    0 days 13:43:00
4    0 days 10:22:00
           ...      
28   0 days 11:21:00
29   5 days 12:47:00
30   0 days 10:15:00
31   0 days 13:37:00
32   0 days 10:29:00
Name: Date, Length: 33, dtype: timedelta64[ns]
```

This outputs a pandas Series with the time that occurs between rows.

Here, you’ll now notice a new dtype at the bottom of our new pandas
Series named
<a href="https://docs.python.org/2/library/datetime.html" target="_blank">`timedelta64`</a>.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## timedelta

Unlike a `Timestamp` that represents a snapshot in time, `timedelta`
represents a duration of time.

This means that it is a measurement of time. Here we can obtain the time
between 2 trips :

``` python
cycling_intervals[1]
```

```out
Timedelta('0 days 13:39:00')
```

``` python
cycling_intervals[1].seconds
```

```out
49140
```

Measures can only be extracted from the timedelta object using either
`days`, `seconds`, and `microseconds`. We can convert them into other
units by using simple operations.

``` python
sec_per_hour = 60 * 60
cycling_intervals[1].seconds / sec_per_hour
```

```out
13.65
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Timedelta objects have a lot of functionality. We can use summary
statistic verbs with them. For example, we can calculate the maximum
amount of time between rides:

``` python
cycling_intervals.max()
```

```out
Timedelta('5 days 12:47:00')
```

As well as the minimum:

``` python
cycling_intervals.min()
```

```out
Timedelta('0 days 10:15:00')
```

We can also do simple operation with them:

``` python
interval_range = cycling_intervals.max() - cycling_intervals.min()
interval_range
```

```out
Timedelta('5 days 02:32:00')
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
