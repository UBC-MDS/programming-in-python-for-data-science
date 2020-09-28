---
type: slides
---

# Working with Dates and Time

Notes:

<br>

---

<center>

<img src='/module4/full.png' width="100%">

</center>

Notes:

It wasn’t too long ago in Module 4, where we briefly mentioned another
column dtype called `datetime64` and `timedelta[ns]`.

Dates and times can be a bit tricky and require a specific data type so
that analysis can be done correctly.

---

``` python
cycling.head()
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
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

Notes:

Let’s take our cycling dataset as an example.

Our date column in our cycling dataframe currently has a dtype value of
`object`.

---

``` python
cycling.sort_values('Date').head(15)
```

```out
                 Date            Name  Type  Time  Distance                                   Comments
21  Oct-01-2019 06:53    Morning Ride  Ride  2118     12.71                  Rested after the weekend!
22  Oct-01-2019 17:15  Afternoon Ride  Ride  1732       NaN                       Legs feeling strong!
23  Oct-02-2019 06:45    Morning Ride  Ride  2222     12.82             Beautiful morning! Feeling fit
24  Oct-02-2019 17:13  Afternoon Ride  Ride  1756       NaN      A little tired today but good weather
25  Oct-03-2019 06:46    Morning Ride  Ride  2134     13.06           Bit tired today but good weather
26  Oct-03-2019 17:45  Afternoon Ride  Ride  1724     12.52                               Feeling good
27  Oct-04-2019 06:47    Morning Ride  Ride  2182     12.68                                   Wet road
28  Oct-04-2019 18:08  Afternoon Ride  Ride  1870     12.63           Very tired, riding into the wind
29  Oct-10-2019 07:55    Morning Ride  Ride  2149     12.70              Really cold! But feeling good
30  Oct-10-2019 18:10  Afternoon Ride  Ride  1841     12.59        Feeling good after a holiday break!
31  Oct-11-2019 07:47    Morning Ride  Ride  2463     12.79               Stopped for photo of sunrise
32  Oct-11-2019 18:16  Afternoon Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump
0   Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                                      Rain 
1   Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                                       rain
2   Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52                  Wet road but nice whether
```

Notes:

When we try to sort these values, it doesn’t recognize the day or month
values and will sort them in some ascending order that is not temporal.

We can see that this sorted starts with October 1st, 2019, followed by
September 10th, 2019, and then September 11th, 2019.

Python is purely sorting the rows by month and not taking the day into
consideration.

---

``` python
cycling.head()
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
```

``` python
dates = (cycling['Date'].str.split(' ', expand=True)
                           .rename(columns = {0:'Date',
                                              1:'Time'}))
dates.head()
```

```out
          Date   Time
0  Sep-10-2019  17:13
1  Sep-11-2019  06:52
2  Sep-11-2019  17:23
3  Sep-12-2019  07:06
4  Sep-12-2019  17:28
```

Notes:

We can try parsing dates ourselves, but that can be difficult and
time-consuming.

To demonstrate this, let’s make an attempt at parsing the `Date` column
in our `cycling` dataframe, which currently has an `object` dtype.

First, we would need to split the column separating the date and the
time and rename the labels 0 and 1 to `Date` and `Time` respectively.

---

``` python
dates = (dates['Date'].str.split('-', expand=True).rename(columns = {0:'Month',
                                                                     1:'Day',
                                                                     2:'Year'}))
dates.head()
```

```out
  Month Day  Year
0   Sep  10  2019
1   Sep  11  2019
2   Sep  11  2019
3   Sep  12  2019
4   Sep  12  2019
```

Notes:

Once again, we need to split the date column using `str.split(),` which
we learned in Module 4, and separate it into columns for the year, month
and day.

---

``` python
dates.iloc[0,1]
```

```out
'10'
```

``` python
type(dates.iloc[0,1])
```

```out
<class 'str'>
```

Notes:

Currently, the values in `dates` are of type `str`, so we would not be
able to sort them in a temporal manner.

---

``` python
cycling_dates = (cycling.assign(Year = dates['Year'].astype(int),
                                Month =  dates['Month'],
                                Day = dates['Day'].astype(int))
                                )
cycling_dates.head(3)
```

```out
                Date            Name  Type  Time  Distance                   Comments  Year Month  Day
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                      Rain   2019   Sep   10
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                       rain  2019   Sep   11
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52  Wet road but nice whether  2019   Sep   11
```

``` python
cycling_dates = cycling_dates.loc[:, ['Year', 'Month', 'Day', 'Name',
                                      'Type', 'Time', 'Distance', 'Comments']]
cycling_dates.head(3)
```

```out
   Year Month  Day            Name  Type  Time  Distance                   Comments
0  2019   Sep   10  Afternoon Ride  Ride  2084     12.62                      Rain 
1  2019   Sep   11    Morning Ride  Ride  2531     13.03                       rain
2  2019   Sep   11  Afternoon Ride  Ride  1863     12.52  Wet road but nice whether
```

Notes:

We must convert the columns to integers values and add them to the
`cycling_dates` dataframe.

We are then going to select and reorder the columns in the dataframe, so
the new date columns are on the left side.

---

``` python
cycling_dates.sort_values(['Year', 'Month', 'Day'])
```

```out
    Year Month  Day            Name  Type  Time  Distance                               Comments
21  2019   Oct    1    Morning Ride  Ride  2118     12.71              Rested after the weekend!
22  2019   Oct    1  Afternoon Ride  Ride  1732       NaN                   Legs feeling strong!
23  2019   Oct    2    Morning Ride  Ride  2222     12.82         Beautiful morning! Feeling fit
24  2019   Oct    2  Afternoon Ride  Ride  1756       NaN  A little tired today but good weather
25  2019   Oct    3    Morning Ride  Ride  2134     13.06       Bit tired today but good weather
..   ...   ...  ...             ...   ...   ...       ...                                    ...
16  2019   Sep   25  Afternoon Ride  Ride  1775     12.10                   Feeling really tired
17  2019   Sep   26    Morning Ride  Ride  2124     12.65           Stopped for photo of sunrise
18  2019   Sep   26  Afternoon Ride  Ride  1860     12.52                                raining
19  2019   Sep   27    Morning Ride  Ride  2350     12.91        Detour around trucks at Jericho
20  2019   Sep   27  Afternoon Ride  Ride  1712     12.47           Tired by the end of the week

[33 rows x 8 columns]
```

Notes:

Now we try to sort them, but how do we sort the `month` column?

It now incorrectly sorts the rows by listing the October rows before
September.

It must be quite evident that we really don’t want to do it this way,
right?

There are a lot of limitations, and we haven’t yet separated the time.

Calculating the time between dates now can also be extremely difficult.

(The differing number of days in months is a contributing factor.)

Thankfully we don’t have to do it this way.

Pandas have some built-in functions that will make our lives much
easier.

By the end of this slide deck, we will be able to answer the question of
*what was Tom’s longest time between rides*.

This is a question that without pandas, would have taken hours, instead
of minutes.

---

## Pandas parse\_dates

``` python
cycling = pd.read_csv('cycling_data.csv')
cycling.head(3)
```

```out
                Date            Name  Type  Time  Distance                   Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                      Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                       rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52  Wet road but nice whether
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

Notes:

Remember How Pandas is built using the NumPy library?

Well in a similar way, Pandas datetime verbs are built using the
built-in Python library;
<a href="https://docs.python.org/3/library/datetime.html" target="_blank">`datetime`
</a>.

We can parse our data at the same time as we read in our dataframe using
the argument `parse_dates`.

Originally the `Date` column adopts a dtype of `object` when the data is
read in.

---

``` python
cycling_dates = pd.read_csv('cycling_data.csv', parse_dates = ['Date'])
cycling_dates.head()
```

```out
                 Date            Name  Type  Time  Distance                       Comments
0 2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                          Rain 
1 2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                           rain
2 2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3 2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4 2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
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

Notes:

Using the `parse_dates`argument with `pd.read_csv()`, transforms the
column so that so that it now adopts a `datetime64` dtype.

---

``` python
cycling_dates.sort_values('Date')
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                                      Rain 
1  2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                                       rain
2  2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52                  Wet road but nice whether
3  2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84               Stopped for photo of sunrise
4  2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48              Tired by the end of the week.
..                 ...             ...   ...   ...       ...                                        ...
28 2019-10-04 18:08:00  Afternoon Ride  Ride  1870     12.63           Very tired, riding into the wind
29 2019-10-10 07:55:00    Morning Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-10 18:10:00  Afternoon Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-11 07:47:00    Morning Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-11 18:16:00  Afternoon Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

Notes:

Now that we have a datetime column which expresses when Tom began his
journey, we can sort our dataframe in a temporal manner, properly now:

---

``` python
pd.read_csv('cycling_data_split_time.csv').head()
```

```out
   Year Month  Day      Clock            Name  Type  Time  Distance                      Comments
0  2019   Sep   10   17:13:04  Afternoon Ride  Ride  2084     12.62                          Rain
1  2019   Sep   11   06:52:18    Morning Ride  Ride  2531     13.03                          rain
2  2019   Sep   11   17:23:50  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3  2019   Sep   12   07:06:19    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4  2019   Sep   12   17:28:05  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

``` python
(pd.read_csv('cycling_data_split_time.csv',
              parse_dates={'Date': ['Year', 'Month', 'Day', 'Clock']})
              .head())
```

```out
                 Date            Name  Type  Time  Distance                      Comments
0 2019-09-10 17:13:04  Afternoon Ride  Ride  2084     12.62                          Rain
1 2019-09-11 06:52:18    Morning Ride  Ride  2531     13.03                          rain
2 2019-09-11 17:23:50  Afternoon Ride  Ride  1863     12.52     Wet road but nice weather
3 2019-09-12 07:06:19    Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
4 2019-09-12 17:28:05  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week
```

Notes:

As another example, our date data may be split between multiple columns.

We can combine the `Year`, `Month`, and `Day` columns to a single
datetime column by using a dictionary within the `parse_dates` argument.

The dictionary key indicates the new column name, and the dictionary
value is a list with the multiple date columns to combine.

---

``` python
cycling = pd.read_csv('cycling_data.csv')
cycling.head()
```

```out
                Date            Name  Type  Time  Distance                       Comments
0  Sep-10-2019 17:13  Afternoon Ride  Ride  2084     12.62                          Rain 
1  Sep-11-2019 06:52    Morning Ride  Ride  2531     13.03                           rain
2  Sep-11-2019 17:23  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3  Sep-12-2019 07:06    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4  Sep-12-2019 17:28  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
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

Notes:

What if we need to convert a column into dtype `datetime` after reading
in our data?

That’s not a problem\! We have `pd.to_datetime()` to transform columns
of an already existing dataframe.

Let’s use our original `cycling` dataframe where `Date` is still of
dtype `object`.

---

``` python
new_cycling = cycling.assign(Date = pd.to_datetime(cycling['Date']))
new_cycling.head()
```

```out
                 Date            Name  Type  Time  Distance                       Comments
0 2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                          Rain 
1 2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                           rain
2 2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3 2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4 2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
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

Notes:

To convert `Date` to a datetime dtype, we use `pd.to_datetime()` and
`assign()`.

Now in the `new_cycling` dataframe, we see that the column `Date` is now
of type `datetime64[ns]`

Ok, but what if I don’t want the full datetime value, and I want a
column with only a portion of it, like the month or year?

---

<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components" target="_blank">
Pandas datetime tools</a>

  - `.dt.day_name()` for the day of the week:

<!-- end list -->

``` python
new_cycling['Date'].dt.day_name().head()
```

```out
0      Tuesday
1    Wednesday
2    Wednesday
3     Thursday
4     Thursday
Name: Date, dtype: object
```

``` python
new_cycling.assign(weekday = new_cycling['Date'].dt.day_name()).head()
```

```out
                 Date            Name  Type  Time  Distance                       Comments    weekday
0 2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                          Rain     Tuesday
1 2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                           rain  Wednesday
2 2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether  Wednesday
3 2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise   Thursday
4 2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.   Thursday
```

Notes:

No worries, we can add a new column to our dataframe in a similar as we
did before, but now we can extract a portion of the `datetime` column by
using
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components" target="_blank">one
of the many pandas datetime tools</a>.

Here are a couple of examples:

  - `.dt.day_name()` for the day of the week, which we can pair this
    with `.assign()` to add this as a column in the dataframe.

---

``` python
new_cycling['Date'].dt.day.head()
```

```out
0    10
1    11
2    11
3    12
4    12
Name: Date, dtype: int64
```

``` python
new_cycling.assign(day = new_cycling['Date'].dt.day).head()
```

```out
                 Date            Name  Type  Time  Distance                       Comments  day
0 2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                          Rain    10
1 2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                           rain   11
2 2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether   11
3 2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise   12
4 2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.   12
```

Notes:

  - `.dt.day` for the day which we can again use with `.assign()` to add
    it to our dataframe.

---

Here are some of the most common useful datetime tools:

  - `.dt.year`
  - `.dt.month`
  - `.dt.month_name()`
  - `.dt.day`
  - `.dt.day_name()`
  - `.dt.hour`
  - `.dt.minute`

For a full list, refer to
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#:~:text=Timestamp%20is%20the%20pandas%20equivalent,oriented%20data%20structures%20in%20pandas.&text=Value%20to%20be%20converted%20to%20Timestamp.&text=Offset%20which%20Timestamp%20will%20have." target="_blank">the
attributes and methods section of the Timestamp documentation</a>.

Notes:

There is some inconsistency with these verbs. You can see that some use
parentheses `()` and some do not.

Using the `.dt` portion of these can only be used on a pandas Series. We
can extract the day, month, year, hour, or minute from a single datetime
value, using the same nouns but omitting the `.dt`.

Let’s see how that’s possible.

---

``` python
new_cycling.head()
```

```out
                 Date            Name  Type  Time  Distance                       Comments
0 2019-09-10 17:13:00  Afternoon Ride  Ride  2084     12.62                          Rain 
1 2019-09-11 06:52:00    Morning Ride  Ride  2531     13.03                           rain
2 2019-09-11 17:23:00  Afternoon Ride  Ride  1863     12.52      Wet road but nice whether
3 2019-09-12 07:06:00    Morning Ride  Ride  2192     12.84   Stopped for photo of sunrise
4 2019-09-12 17:28:00  Afternoon Ride  Ride  1891     12.48  Tired by the end of the week.
```

If I select the first example in row 1 of our `new_cycling` dataset,
you’ll notice that it outputs something called a `Timestamp`.

``` python
timestamp_ex = new_cycling.loc[1,'Date']
timestamp_ex
```

```out
Timestamp('2019-09-11 06:52:00')
```

Notes:

If I select the first example in row 1 of our `new_cycling` dataset,
you’ll notice that it outputs something called a `Timestamp`.

This is a pandas data type.

---

``` python
timestamp_ex
```

```out
Timestamp('2019-09-11 06:52:00')
```

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
11
```

``` python
timestamp_ex.hour
```

```out
6
```

Notes:

Timestamps show a snapshot of when an event has occurred. Timestamps are
complete with both dates and times. If the date and time are not
available in your original data, Python will fill in any temporal
unknowns with default values (often with `00:00:00` for time, if only
the date was provided).

To obtain the month name, day, or hour from the Timestamp, we can use
the same nouns in the previous slide without `.dt`.

Here we get the `.mount_name()`, the `.day` and the `.hour` of a single
value by using the same verbs as before but omitting the `.dt`

---

## .diff()

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
29   5 days 13:47:00
30   0 days 10:15:00
31   0 days 13:37:00
32   0 days 10:29:00
Name: Date, Length: 33, dtype: timedelta64[ns]
```

Notes:

In our analysis, it might be important to know how frequent events occur
and the time between them.

`.diff()` is a useful function for that.

This outputs a pandas Series with the time that occurs between rows. As
you can see, there was a 10 hour and 22minute gap between Tom’s third
and forth bike rides. Wow - that’s a long workday\!"

Here, you’ll now notice a new dtype at the bottom of our new pandas
Series named
<a href="https://docs.python.org/2/library/datetime.html" target="_blank">`timedelta64`</a>.

---

## timedelta

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

``` python
sec_per_hour = 60 * 60
cycling_intervals[1].seconds / sec_per_hour
```

```out
13.65
```

Notes:

Unlike a `Timestamp` that represents a snapshot in time, `timedelta`
represents a duration or an interval of time.

Here we can obtain the time between 2 trips.

Measurement can only be extracted from the timedelta object using either
`days`, `seconds`, and `microseconds` verbs.

Here we obtain the number of seconds.

We can convert them into other units by using simple operations.

In this case, we convert it to hours by dividing it by the number of
seconds in an hour.

---

``` python
cycling_intervals.max()
```

```out
Timedelta('5 days 13:47:00')
```

``` python
cycling_intervals.min()
```

```out
Timedelta('0 days 10:15:00')
```

``` python
interval_range = cycling_intervals.max() - cycling_intervals.min()
interval_range
```

```out
Timedelta('5 days 03:32:00')
```

Notes:

Timedelta objects have a lot of functionality.

We can use a summary statistic verbs with them.

For example, we can calculate the maximum amount of time between rides.

As well as the minimum.

We can also do a simple operation with them, like finding the range.

---

# Let’s apply what we learned\!

Notes:

<br>
