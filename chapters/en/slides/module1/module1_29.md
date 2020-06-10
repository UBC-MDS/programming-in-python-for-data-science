---
type: slides
---

# Frequency Tables and Writing CSVs

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is Frequency?

Before we explain what a frequency table is, you must know what
frequency means first.

*_Frequency_* is simply put, the number of times a value occurs within
the data. For example, let’s say we have a sample of our candybars data.

``` python
df_mini
```

```out
                        name  weight available_canada_america
0               Coffee Crisp      50                   Canada
1               Butterfinger     184                  America
2                       Skor      39                     Both
3                   Smarties      45                   Canada
4                       Twix      58                     Both
5  Reeses Peanutbutter Cups       43                     Both
6               3 Musketeers      54                  America
```

The frequency of the value `Both` in the `available_canada_america`
column is 3.

A frequency table is a manner of displaying all the possible values of a
column in our data and the number of occurrences (frequencies) each
value occurs. These are particularly useful when we want to visualize
our data.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is a Frequency Table?

*_A frequency Table_* is a manner of displaying all the possible values
of a column in our data and the number of occurrences (frequencies) each
value occurs. These are particularly useful when we want to visualize
our data.

For our sample data, a frequency table for the
`available_canada_america` column would look like this:

```out
Both       3
America    2
Canada     2
Name: available_canada_america, dtype: int64
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we want to get a frequency table of a categorical column, there are a
few steps that need to be followed. Up until now, we discussed getting a
single column from a dataframe using double brackets - `df[['column
name']]`. For frequency tables, however, we only use single brackets to
obtain the column values.

``` python
manufacturer_column = df['mfr']
manufacturer_column
```

```out
0     N
1     Q
2     K
3     K
4     R
     ..
72    G
73    G
74    R
75    G
76    G
Name: mfr, Length: 77, dtype: object
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We saved the object in a variable called `manufacturer_column` in the
same way we have saved objects before.  
Next we can use `.value_counts()` referencing that the column we saved
as `manufacturer_column`.

``` python
manufacturer_freq = manufacturer_column.value_counts()
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

We can then see the frequency of each categorical value. If we used
double square brackets with `pd.value_counts()` we would get an error
along the lines of `AttributeError: 'DataFrame' object has no attribute
'value_counts'`. Take care with using the correct number of square
brackets.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Sometimes it’s useful to save a new dataframe as a `csv` file for future
use or to use in another application. We can save dataframes using the
method `.to_csv()`. Simply put our desired `csv` file name in quotations
within the parentheses.

``` python
manufacturer_freq.to_csv('manufacturer_frequency.csv')
```

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
