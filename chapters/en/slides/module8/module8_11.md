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
dataset ready to be used. In fact, in a majority of cases, cleaning and
wrangling your data will be an ongoing and time consuming project. No
matter how complete or well planned a database may seem, a data analyst
will almost always encounter ***null*** values.

A null is the term used to represent a value missing from the data.
***Null*** is the human readable definition of a value that is not
included in the dataframe. Python translates this to a `NaN` value. When
we use Pandas you may see `NaN` which is actually a constant that comes
from the NumPy library.

``` python
np.nan
```

```out
nan
```

In some cases, missing values are sometimes refered to as `NA` values
because of how they are handled in other programming languages. This is
reflected in some of the names of the functions we use to handle them.

Not that in this section we generally refer to them as both ***null***
and `NaN` values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Info on missing values

A good rule of thumb when conducting an analysis, is to check early on
how complete your dataset is. `.info$$` is similar to `.dtype()` but in
addition to the dtype of each column, it includes the total number of
Non-null values each column contains.

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
entries, 0 to 76`. The `Non-Null Count` specifies the number of non-null
values. In this case we have a complete dataframe with zero null values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a look at a case where we are not so lucky. `bites` is a
subset of a new dataset that contains information about animal bites
occurring in Louisville, Kentucky from 1985 to 2017.

``` python
bites.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
Int64Index: 100 entries, 0 to 99
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype         
---  ------     --------------  -----         
 0   bite_date  100 non-null    datetime64[ns]
 1   species    100 non-null    object        
 2   gender     100 non-null    object        
 3   color      86 non-null     object        
dtypes: datetime64[ns](1), object(3)
memory usage: 3.9+ KB
```

We can see that there are a total of 100 entries (rows). We see that the
`color` column only contains 86 of 100 non null values. This would mean
that 14 values are missing from that column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can use `.isnull()` on a particular column to obtain a Boolean value
indicating if the row is a null value:

``` python
bites['color'].isnull()
```

```out
0     False
1     False
2      True
3     False
      ...  
96    False
97    False
98    False
99    False
Name: color, Length: 100, dtype: bool
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can pair `.isnull()` with our filtering method and the verb `.any()`
to obtain the rows that contain null values in the dataframe:

``` python
bites[bites.isnull().any(axis=1)]
```

```out
    bite_date species   gender color
2  1987-05-07     DOG  UNKNOWN   NaN
5  1989-11-24     DOG  UNKNOWN   NaN
16 1991-11-07     DOG  UNKNOWN   NaN
20 1992-03-18     CAT  UNKNOWN   NaN
..        ...     ...      ...   ...
39 1994-07-21     DOG  UNKNOWN   NaN
56 2010-01-02     DOG  UNKNOWN   NaN
57 2010-01-02     CAT   FEMALE   NaN
72 2010-01-09     CAT  UNKNOWN   NaN

[14 rows x 4 columns]
```

Here, we see the 14 rows of our dataframe that contain null values.

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

## Droping Null Values

The easiest and simplest way of handling nulls values are to remove
those rows from the dataset. In a fashion similar to dropping columns,
we can drop rows, if they contain a `NaN` value. It’s important that you
take some necessary precautions and not drop a large portion of your
dataset.

In our example above, if we were to remove the 14 rows we identified to
contain `NaN` values, we do it in the following way:

``` python
bites_removed = bites.dropna()
bites_removed
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
3  1988-10-02     DOG     MALE   BLA & BRO
4  1989-08-29     DOG   FEMALE     BLK-WHT
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[86 rows x 4 columns]
```

Notice that index=2 was removed.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

By default all the rows will be considered when dropping rows, however,
if we only want to drop rows with `NaN` values in certain columns we can
use the `subset` argument:

``` python
bites.dropna(subset=['species'])
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN         NaN
3  1988-10-02     DOG     MALE   BLA & BRO
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

Here, we can see that no rows were dropped as there are no `NaN` values
in the `species` column.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Replacing Null Values

Alternately, if we have a small dataset and we don’t want to rid
outselves of any data, We may prefer to replace `NaN` with a particular
value. We can do so will `.fillna()` Perhaps we want to replace the
values in `color` with the most frequent value (or if it was a numeric
value, the mean):

``` python
most_common_color = bites['color'].mode()[0]
most_common_color
```

```out
'BLK'
```

``` python
bites_mode_fill = bites.fillna(value=most_common_color)
bites_mode_fill
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN         BLK
3  1988-10-02     DOG     MALE   BLA & BRO
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

We see the value in `color` for index 2 change to `BLK`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can also replace it with a new value altogether, perhaps in this case
`UNKNOWN`:

``` python
bites_unknown_fill = bites.fillna(value='UNKNOWN')
bites_unknown_fill
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN     UNKNOWN
3  1988-10-02     DOG     MALE   BLA & BRO
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

Here, index 2 now has a color value of `UNKNOWN`. Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We could also fill using certain methods. ***“bfill”*** uses the next
valid observation to fill the `NaN`.

``` python
bites.fillna(method='bfill')
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN   BLA & BRO
3  1988-10-02     DOG     MALE   BLA & BRO
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

Now index 2 adopts the value `BLA & BRO` from index 3.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

“ffill” propagates the last valid observation forward to next

``` python
bites.fillna(method='ffill')
```

```out
    bite_date species   gender       color
0  1985-05-05     DOG   FEMALE  LIG. BROWN
1  1986-02-12     DOG  UNKNOWN   BRO & BLA
2  1987-05-07     DOG  UNKNOWN   BRO & BLA
3  1988-10-02     DOG     MALE   BLA & BRO
..        ...     ...      ...         ...
96 2010-01-25     DOG   FEMALE    FAWN-WHT
97 2010-01-25     DOG   FEMALE     BRN-WHT
98 2010-01-26     DOG     MALE   BROWN-BLK
99 2010-01-27     DOG     MALE       BLACK

[100 rows x 4 columns]
```

Now index 2 adopts the value `BRO & BLA` from index 1.

`bfill` and `ffill` are methods usually adopted when deeling with
columns organized by date. This way, an observation can adopt a similar
value to those are it. We will explore date columns in the next slide
deck.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Remember these are only a few methods that can be use in simple
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
