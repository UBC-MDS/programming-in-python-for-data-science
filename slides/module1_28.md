---
type: slides
---

# Frequency Tables and Writing CSVs

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

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
                           weight available_canada_america
name                                                      
Coffee Crisp                   50                   Canada
Butterfinger                  184                  America
Skor                           39                     Both
Smarties                       45                   Canada
Twix                           58                     Both
Reeses Peanutbutter Cups       43                     Both
3 Musketeers                   54                  America
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

<source src="placeholder_audio.mp3" />

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

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

If we want to get a frequency table of a categorical column, there are a
few steps that need to be followed. Up untill now, we discussed getting
a single column from a dataframe using double brackets -
`df[['column-name']]`. For frequency tables, however, we only use single
brackets to obtain the column values.

``` python
manufacturer_column = df['mfr']
manufacturer_column
```

```out
name
100% Bran                    N
100% Natural Bran            Q
All-Bran                     K
All-Bran with Extra Fiber    K
Almond Delight               R
                            ..
Triples                      G
Trix                         G
Wheat Chex                   R
Wheaties                     G
Wheaties Honey Gold          G
Name: mfr, Length: 77, dtype: object
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We saved the object in a variable called `manufacturer_column` in the
same way we have saved objects before.  
Next we can use `pd.value_counts()` referencing that the column we saved
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

We can then see the frequency of each qualitative value. If we used
double square brackets with `pd.value_counts()` we would get an error
along the lines of `AttributeError: 'DataFrame' object has no attribute
'value_counts'`. Take care with using the correct number of square
brackets.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Sometimes it’s useful to save a new dataframe as a `csv` file for future
use or to use in another application. We can save dataframes using the
method `df.to_csv()`. Simply put our desired `csv` file name in
quotations within the parentheses.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
