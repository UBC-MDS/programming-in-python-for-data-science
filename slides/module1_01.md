---
type: slides
---

# What is a Dataframe?

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

When working with information, it must be stored in a manner that is
organized, readable and accessible.

A dataframe makes it easy to calculate statistics and clean and store
data.

From a data perspective, it is a rectangle where the rows are the
observations. (Essentially, they look like excel sheets)

<img src='module1/df_obs.png' width="50%" alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

The columns are the variables.

<img src='module1/df_vars.png' width="50%" alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Enter Pandas

<img src='module1/pandas.gif' width="50%" alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Importing Pandas

To analyze dataframes, we need to make sure that we import something
called `pandas`. This will help us store and manipulate dataframes.

Before we start writing any valuable code, we need to import pandas.

``` python
import pandas as pd
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in Data

Next we can bring in our data named `candybars` which is stored as a
`.csv` with the following code:

``` python
df = pd.read_csv('candybars.csv')
```

let’s break this up:

`pd`: this is the short form for pandas, which we are using to
manipulate our dataframes.  
`read_csv()`: The tool that does the job and, in this case, it is
reading in the `csv` file named `candybars.csv`.  
`df`: The dataframe is now saved as an object called `df`

In these slides you can differentiate between what we typed in (our
code) in light gray and the output of this will be coloured in a dark
grey background.

You can see what the object `df` looks like on the next slide.

Notes: Script
    here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

``` python
df
```

```out
                         name  chocolate  ...  multi  available_canada_america
0                Coffee Crisp          1  ...      0                    Canada
1                Butterfinger          1  ...      0                   America
2                        Skor          1  ...      0                      Both
3                    Smarties          1  ...      1                    Canada
4                        Twix          1  ...      1                      Both
5   Reeses Peanutbutter Cups           1  ...      1                      Both
6                3 Musketeers          1  ...      0                   America
7             Kinder Surprise          1  ...      0                    Canada
8                       M & M          1  ...      1                      Both
9                   Glosettes          1  ...      1                    Canada
10                     KitKat          1  ...      1                      Both
11                  Babe Ruth          1  ...      0                   America
12                   Caramilk          1  ...      0                    Canada
13                       Aero          1  ...      0                    Canada
14                       Mars          1  ...      0                      Both
15                     Payday          0  ...      0                   America
16                   Snickers          1  ...      0                      Both
17                   Crunchie          1  ...      0                    Canada
18                 Wonderbar           1  ...      0                    Canada
19                 100 Grand           1  ...      0                   America
20                     Take 5          1  ...      0                   America
21           Whatchamacallits          1  ...      0                   America
22                 Almond Joy          1  ...      0                   America
23                   Oh Henry          1  ...      0                      Both
24          Cookies and Cream          0  ...      0                      Both

[25 rows x 10 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

From this dataframe, we can see that there are 25 different candy bars
and 10 columns. We can obtain the names of the columns using this code:

``` python
df.columns
```

```out
Index(['name', 'chocolate', 'peanuts', 'caramel', 'nougat',
       'cookie_wafer_rice', 'coconut', 'white_chocolate', 'multi',
       'available_canada_america'],
      dtype='object')
```

Or if you wanted to see the dimensions of the whole dataframe you could
code the following:

``` python
df.shape
```

```out
(25, 10)
```

Breaking up this code it just means “From our dataframe that we saved as
`df` tell me the `columns` or tell me the `shape`”.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Another important method to know is what if we don’t want to output the
whole table  
We can then specify how many rows of the dataset to show with
`df.head()`

``` python
df.head(2)
```

```out
           name  chocolate  ...  multi  available_canada_america
0  Coffee Crisp          1  ...      0                    Canada
1  Butterfinger          1  ...      0                   America

[2 rows x 10 columns]
```

This specifies only 2 rows will be shown. We can specify any number of
rows within the brackets or we can leave it empty which will default to
5 rows.

``` python
df.head()
```

```out
           name  chocolate  ...  multi  available_canada_america
0  Coffee Crisp          1  ...      0                    Canada
1  Butterfinger          1  ...      0                   America
2          Skor          1  ...      0                      Both
3      Smarties          1  ...      1                    Canada
4          Twix          1  ...      1                      Both

[5 rows x 10 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# let’s apply what we learned\!

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
