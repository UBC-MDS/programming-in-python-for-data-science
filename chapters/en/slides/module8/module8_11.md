---
type: slides
---

# Working with Null Values

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the real world of data analysis, it’s uncommon that we have a perfect
dataset ready to be used. In fact, in most cases, cleaning and wrangling
data will be an ongoing and time-consuming project. No matter how
complete or well planned a database may seem, a data analyst will almost
always encounter ***null*** values.

A “null” is the human-readable term of a value that is missing from the
dataframe. Remember in Module 4 we discussed `NaN` being of type
`float`? Python translates null values in numerical columns to `NaN`.
Well, `NaN` is a constant that comes from the NumPy library.

``` python
np.nan
```

```out
nan
```

In some cases, missing values are sometimes referred to as `NA` values
because of how they are handled in other programming languages. This is
reflected in some of the names of the functions we use to handle them.

In this course, we generally refer to them as both ***null*** and `NaN`
values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Info on missing values

A good rule of thumb when conducting an analysis is to check early on
how complete the dataset is. `.info()` is similar to `.dtypes` but in
addition to the dtype of each column, it includes the total number of
non-null values contained in each column.

Let’s try it out on a subset of our `cereal` dataset:

``` python
cereal.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77 entries, 0 to 76
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   name      77 non-null     object 
 1   mfr       77 non-null     object 
 2   calories  77 non-null     int64  
 3   fat       77 non-null     int64  
 4   fiber     77 non-null     float64
 5   rating    77 non-null     float64
dtypes: float64(2), int64(2), object(2)
memory usage: 3.7+ KB
```

Here we see the total number of rows at the top with `RangeIndex: 77
entries, 0 to 76`. The `Non-Null Count` column specifies the number of
non-null values. In this case, we have a complete dataframe with zero
null values for each column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a look at a case where we are not so lucky. `cycling` is a
subset of a dataset that contains the bicycling trips
<a href="https://www.tomasbeuzen.com/" target="_blank">Tomas Beuzen</a>,
a UBC postdoc rode his bike to campus and back during the fall 2019
semester.

``` python
cycling
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863       NaN                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Using `.info()` with this new data we get the following:

``` python
cycling.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 33 entries, 0 to 32
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype         
---  ------    --------------  -----         
 0   Date      33 non-null     datetime64[ns]
 1   Name      33 non-null     object        
 2   Type      33 non-null     object        
 3   Time      33 non-null     int64         
 4   Distance  30 non-null     float64       
 5   Comments  33 non-null     object        
dtypes: datetime64[ns](1), float64(1), int64(1), object(3)
memory usage: 1.7+ KB
```

We can see that there is a total of 33 entries (rows). We see that the
`Distance` column only contains 30 non-null values out of a possible 33.
This would mean that 3 values are missing from this column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can use `.isnull()` on a particular column to obtain a Boolean series
indicating if each row is a null value:

``` python
cycling['Distance'].isnull()
```

```out
0     False
1     False
2      True
3     False
      ...  
29    False
30    False
31    False
32    False
Name: Distance, Length: 33, dtype: bool
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can pair `.isnull()` with our filtering method to obtain the rows
that contain null values in the `Distance` column of the dataframe:

``` python
cycling[cycling['Distance'].isnull()]
```

```out
                  Date          Name  Type  Time  Distance                               Comments
2  2019-09-10 07:23:00  Morning Ride  Ride  1863       NaN              Wet road but nice weather
22 2019-09-30 07:15:00  Morning Ride  Ride  1732       NaN                   Legs feeling strong!
24 2019-10-01 07:13:00  Morning Ride  Ride  1756       NaN  A little tired today but good weather
```

Here, we see the 3 rows of our dataframe that contain null values.

If we wanted to filter all the rows that contain null values and not
just in the `Distance` column, we can use the verb `.any()`

``` python
cycling[cycling.isnull().any(axis=1)]
```

```out
                  Date          Name  Type  Time  Distance                               Comments
2  2019-09-10 07:23:00  Morning Ride  Ride  1863       NaN              Wet road but nice weather
22 2019-09-30 07:15:00  Morning Ride  Ride  1732       NaN                   Legs feeling strong!
24 2019-10-01 07:13:00  Morning Ride  Ride  1756       NaN  A little tired today but good weather
```

We only have `NaN` values in the Distance column so the same 3 rows are
outputted as before.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now that we have identified that our dataframe contains null values,
what can we do about them?

There are many complex procedures in handling values that are missing
from a dataset, but we will discuss 2 simple options:

  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html" target="_blank">`.dropna()`</a>
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html" target="_blank">`.fillna()`</a>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Dropping Null Values

The easiest and simplest way of handling nulls values is to remove those
rows from the dataset. In a fashion similar to dropping columns, we can
drop rows, if they contain a `NaN` value. It’s important that we take
some necessary precautions and not drop a large portion of the data.

In our example above, if we were to remove the 3 rows we identified to
contain `NaN` values, we do it in the following way:

``` python
trips_removed = cycling.dropna()
trips_removed
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
4  2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48               Tired by the end of the week
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[30 rows x 6 columns]
```

Notice that index 2 was removed and we only have 30 rows in our
dataframe now.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

By default, all the rows with `NaN` values in any column will be
considered when dropping rows; however, if we only want to drop rows
with `NaN` values in certain columns, we can use the `subset` argument:

``` python
cycling.dropna(subset=['Type'])
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863       NaN                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

Here, we can see that no rows were dropped as there are no `NaN` values
in the `Type` column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

But, the rows do get dropped when we subset on the `Distance` column.

``` python
cycling.dropna(subset=['Distance'])
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
4  2019-09-11 07:28:00    Morning Ride  Ride  1891     12.48               Tired by the end of the week
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[30 rows x 6 columns]
```

Alternatively if you have a column missing a large portion of data, the
best option maybe to drop that column instead of the rows with missing
values. This will keep more of your data instead of dropping and losing
most of your data.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Replacing Null Values

Alternately, if we have a small dataset and we don’t want to rid
ourselves of any data, we may prefer to replace `NaN` with a particular
value. We can do so with `.fillna()`.

Perhaps it’s missing from the data because he didn’t cycle that
particular day. Replacing the `NaN` value with 0 in this case would make
sense:

``` python
cycling_zero_fill = cycling.fillna(value=0)
cycling_zero_fill
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863      0.00                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

Now index 2 now has a `Distance` of `0.00`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Maybe a better decision would be to replace the values in `Distance`
with the mean:

``` python
cycling['Distance'].mean().round(2)
```

```out
12.67
```

``` python
cycling_mean_fill = cycling.fillna(value=cycling['Distance'].mean().round(2))
cycling_mean_fill
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863     12.67                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

We see the value in `Distance` for index 2 change to `12.67`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We could also fill using certain methods.

***“bfill”*** uses the next valid observation to fill the `NaN`:

``` python
cycling.fillna(method='bfill')
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863     12.84                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

Index 2 adopts the value `12.84` from index 3.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

***“ffill”*** propagates the last valid observation forward to next:

``` python
cycling.fillna(method='ffill')
```

```out
                  Date            Name  Type  Time  Distance                                   Comments
0  2019-09-09 07:13:00    Morning Ride  Ride  2084     12.62                                       Rain
1  2019-09-09 20:52:00  Afternoon Ride  Ride  2531     13.03                                       rain
2  2019-09-10 07:23:00    Morning Ride  Ride  1863     13.03                  Wet road but nice weather
3  2019-09-10 21:06:00  Afternoon Ride  Ride  2192     12.84               Stopped for photo of sunrise
..                 ...             ...   ...   ...       ...                                        ...
29 2019-10-08 20:55:00  Afternoon Ride  Ride  2149     12.70              Really cold! But feeling good
30 2019-10-09 07:10:00    Morning Ride  Ride  1841     12.59        Feeling good after a holiday break!
31 2019-10-09 20:47:00  Afternoon Ride  Ride  2463     12.79               Stopped for photo of sunrise
32 2019-10-10 07:16:00    Morning Ride  Ride  1843     11.79  Bike feeling tight, needs an oil and pump

[33 rows x 6 columns]
```

We see thar index 2 adopts the value `13.03` from index 1.

`bfill` and `ffill` are methods usually adopted when dealing with
columns organized by date. This way, an observation can adopt a similar
value to those near it. We will explore date columns in the next slide
deck.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Remember these are only a few methods that can be used in simple
situations. In some scenarios, more complex methods of handling missing
values may need to be adopted for effective analysis.

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
