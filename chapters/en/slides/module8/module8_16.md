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

It wasn’t too long ago in Module 4 where we briefly mention another
column dtype called `datetime64`.

<center>

<img src='/module4/full.png' width="100%">

</center>

Dates and times can we a bit tricky and require a specific data type so
that analysis can be done correctly.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Parse data yourself can be difficult and time consuming. Let’s make a
quick attempt at converting the `bite_date` column which is currently of
dtype `object` into separate numeric columns so we can sort them in a
temporal manner.

``` python
bites.head()
```

```out
     bite_date species   gender     color
70  2010-01-08     DOG   FEMALE  WHT-BUFF
88  2010-01-17     CAT     MALE     BROWN
94  2010-01-24     DOG     MALE       RED
22  1992-05-06     DOG  UNKNOWN       BLK
80  2010-01-12     DOG     MALE       BLK
```

First we would need to split them up and rename the columns:

``` python
dates = (bites['bite_date'].str.split('-', expand=True)
                           .rename(columns = {0:'Year',
                                              1:'Month',
                                              2:'Day'}))
dates.head()
```

```out
    Year Month Day
70  2010    01  08
88  2010    01  17
94  2010    01  24
22  1992    05  06
80  2010    01  12
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
'2010'
```

``` python
type(dates.iloc[0,0])
```

```out
<class 'str'>
```

We need to convert all the values to integers and add them to the
previous dataframe `bites`.

``` python
bites_dates = (bites.assign(Year = dates['Year'].astype(int),
                            Month = dates['Month'].astype(int),
                            Day = dates['Day'].astype(int)))
bites_dates.head()
```

```out
     bite_date species   gender     color  Year  Month  Day
70  2010-01-08     DOG   FEMALE  WHT-BUFF  2010      1    8
88  2010-01-17     CAT     MALE     BROWN  2010      1   17
94  2010-01-24     DOG     MALE       RED  2010      1   24
22  1992-05-06     DOG  UNKNOWN       BLK  1992      5    6
80  2010-01-12     DOG     MALE       BLK  2010      1   12
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
bites_dates.sort_values(['Year', 'Month', 'Day']).head()
```

```out
    bite_date species   gender       color  Year  Month  Day
0  1985-05-05     DOG   FEMALE  LIG. BROWN  1985      5    5
1  1986-02-12     DOG  UNKNOWN   BRO & BLA  1986      2   12
2  1987-05-07     DOG  UNKNOWN         NaN  1987      5    7
3  1988-10-02     DOG     MALE   BLA & BRO  1988     10    2
4  1989-08-29     DOG   FEMALE     BLK-WHT  1989      8   29
```

After doing all this, there are still a lot of limitations.

Luckily, Pandas has some built in functions we can use that will make
our lives much easier.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Pandas parse\_dates

Remember How Pandas is built using the `NumPy` library? Well in a
similar way, Pandas datetime verbs are build from the build in Python
<a href="https://docs.python.org/3/library/datetime.html" target="_blank">`Datetime`
library</a>.

We can parse our data at the same time as we read in our dataframe using
the argument `parse_date`. Let’s do it by reading in our
`animal_bites2.csv` file:

``` python
bites = pd.read_csv('animalbites.csv', parse_dates = ['bite_date'])
bites.head()
```

```out
   bite_date species   gender       color
0 1985-05-05     DOG   FEMALE  LIG. BROWN
1 1986-02-12     DOG  UNKNOWN   BRO & BLA
2 1987-05-07     DOG  UNKNOWN         NaN
3 1988-10-02     DOG     MALE   BLA & BRO
4 1989-08-29     DOG   FEMALE     BLK-WHT
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

```out
   bite_date species   gender       color
0 1985-05-05     DOG   FEMALE  LIG. BROWN
1 1986-02-12     DOG  UNKNOWN   BRO & BLA
2 1987-05-07     DOG  UNKNOWN         NaN
3 1988-10-02     DOG     MALE   BLA & BRO
4 1989-08-29     DOG   FEMALE     BLK-WHT
```

It looks like the same dataframe but now if we check the dtype of
`bite_date`, you’ll see it adopts a `datetime64` dtype.

``` python
bites.dtypes
```

```out
bite_date    datetime64[ns]
species              object
gender               object
color                object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Or perhaps our date is split between multiple columns and we want a
single datetime column. Take `bites_split.csv` for example:

``` python
pd.read_csv('bites_split.csv').head()
```

```out
   bite_year  bite_month  bite_day species   gender       color
0       1985           5         5     DOG   FEMALE  LIG. BROWN
1       1986           2        12     DOG  UNKNOWN   BRO & BLA
2       1987           5         7     DOG  UNKNOWN         NaN
3       1988          10         2     DOG     MALE   BLA & BRO
4       1989           8        29     DOG   FEMALE     BLK-WHT
```

We can convert this to a single column by using a dictionary within the
`parse_dates` column. The dictionary key, indicates the column name and
the dictionary value is a list containing multiple columns to use as the
new date column :

``` python
pd.read_csv('bites_split.csv', parse_dates={'bite_date': ['bite_year', 'bite_month', 'bite_day']}).head()
```

```out
   bite_date species   gender       color
0 1985-05-05     DOG   FEMALE  LIG. BROWN
1 1986-02-12     DOG  UNKNOWN   BRO & BLA
2 1987-05-07     DOG  UNKNOWN         NaN
3 1988-10-02     DOG     MALE   BLA & BRO
4 1989-08-29     DOG   FEMALE     BLK-WHT
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What if we need to convert the column after reading in our data? That’s
not a problem\! We have `pd.to_datetime()` to convert columns of an
already existing dataframe.

Let’s use our original `bites` dataframe where `bite_date` is still of
dtype `object`.

``` python
bites = pd.read_csv('animalbites.csv')
bites.head()
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN         NaN
3  1988-10-02     DOG     MALE   BLA & BRO
4  1989-08-29     DOG   FEMALE     BLK-WHT
```

``` python
bites.dtypes
```

```out
bite_date    object
species      object
gender       object
color        object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to convert `bite_date` to a datetime dtype, we can do so
pairing `pd.to_datetime()` with `assign()`

``` python
new_bites = bites.assign(bite_date = pd.to_datetime(bites['bite_date']))
new_bites
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN         NaN
3  1988-10-02     DOG     MALE   BLA & BRO
4  1989-08-29     DOG   FEMALE     BLK-WHT
..        ...     ...      ...         ...
95 2010-01-25     CAT   FEMALE  GRAY-TORTI
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

``` python
new_bites.dtypes
```

```out
bite_date    datetime64[ns]
species              object
gender               object
color                object
dtype: object
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In a similar way we can also add a new column to the dataframe with a
part of the datetime value.There are a
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components" target="_blank">number
of different functions</a> that split up a datatime value:

  - `.dt.day_name()` for the day of the week

<!-- end list -->

``` python
new_bites.assign(weekday = new_bites['bite_date'].dt.day_name()).head()
```

```out
   bite_date species   gender       color    weekday
0 1985-05-05     DOG   FEMALE  LIG. BROWN     Sunday
1 1986-02-12     DOG  UNKNOWN   BRO & BLA  Wednesday
2 1987-05-07     DOG  UNKNOWN         NaN   Thursday
3 1988-10-02     DOG     MALE   BLA & BRO     Sunday
4 1989-08-29     DOG   FEMALE     BLK-WHT    Tuesday
```

  - `dt.month` for the month

<!-- end list -->

``` python
new_bites.assign(month = new_bites['bite_date'].dt.month).head()
```

```out
   bite_date species   gender       color  month
0 1985-05-05     DOG   FEMALE  LIG. BROWN      5
1 1986-02-12     DOG  UNKNOWN   BRO & BLA      2
2 1987-05-07     DOG  UNKNOWN         NaN      5
3 1988-10-02     DOG     MALE   BLA & BRO     10
4 1989-08-29     DOG   FEMALE     BLK-WHT      8
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There is some inconsistency of when to use `()` in our datetime actions
but here are some of the most common:

  - `dt.month`
  - `dt.month_name()`
  - `dt.day`
  - `dt.day_name()`
  - `dt.hour`
  - `dt.minute`

Using the `.dt` can only be used on a pandas Series. We can extract the
day, month, year hour, or minute from a single datetime value, using
similar nouns without the `.dt.`.

First let’s see how that’s possible.

If I select the first example in row 1, you’ll notice that it outputs
something called a `Timestamp`.

``` python
new_bites.loc[1,'bite_date']
```

```out
Timestamp('1986-02-12 00:00:00')
```

This is a Pandas datatype.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
timestamp_ex = new_bites.loc[1,'bite_date']
timestamp_ex
```

```out
Timestamp('1986-02-12 00:00:00')
```

Timestamps shows a complete time snapshot. It includes the seconds even
though there was never any time component in the initial dataframe.
Timestamps must be complete with both dates and time and if none was
provided, Python will fill in the unknown with default values, in this
case `00:00:00`.

To obtain the month\_name, day, or hour from the Timestamp, we can use
the same nouns in the previous slide without `.ts.`:

``` python
timestamp_ex.month_name()
```

```out
'February'
```

``` python
timestamp_ex.day
```

```out
12
```

``` python
timestamp_ex.hour
```

```out
0
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In our analysis it might be important to know how frequent events occur
and the time between each animal bite might help us in decreasing them
or staffing for them. `.diff()` is a useful function for that.

``` python
bite_intervals = new_bites['bite_date'].sort_values().diff()
bite_intervals
```

```out
0         NaT
1    283 days
2    449 days
3    514 days
4    331 days
       ...   
95     1 days
96     0 days
97     0 days
98     1 days
99     1 days
Name: bite_date, Length: 100, dtype: timedelta64[ns]
```

This outputs a pandas series with the time between occurences.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

You’ll now notice a new dtype at the bottom of our new pandas Series
<a href="https://docs.python.org/2/library/datetime.html" target="_blank">`timedelta64`</a>.

Unlike a `Timestamp` that represents a snapshot in time, `timedelta`
represents a duration of time.

This means that it is a measurement of time that can be extracted from
the object as a particular unit of time. Here we can obtain the number
of days between 2 bite cases.

``` python
bite_intervals[1].days
```

```out
283
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can find the maximum amount of time between cases:

``` python
bite_intervals.max()
```

```out
Timedelta('5579 days 00:00:00')
```

and the minimum time between cases:

``` python
bite_intervals.min()
```

```out
Timedelta('0 days 00:00:00')
```

And do simple operation with them:

``` python
interval_range = bite_intervals.max() - bite_intervals.min()
interval_range
```

```out
Timedelta('5579 days 00:00:00')
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We could even obtain the total days of the operation:

``` python
interval_range.days
```

```out
5579
```

and convert it into years

``` python

interval_range.days/365.25
```

```out
15.274469541409994
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
