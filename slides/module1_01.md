type: slides

# What is a Dataframe?

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

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

-----

The columns are the variables.

<img src='module1/df_var.png' width="50%" alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

# Enter Pandas

<img src='module1/pandas.gif' width="50%" alt="404 image"/>

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

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

-----

## Reading in Data

Next we can bring in our data named `candybars` which is stored as a
`.csv` with the following code:

``` python
df = pd.read_csv('candybars.csv', index_col =0)
```

let’s break this up:

`pd`: this is the short form for pandas, which we are using to
manipulate our dataframes.  
`read_csv()`: The tool that does the job and, in this case, it is
reading in the `csv` file named `candybars.csv`.  
`index_col =0`: This specifies to use the first column in the csv as an
index (we will talk about this in a moment) `df`: The dataframe is now
saved as an object called `df`

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

-----

``` python
df
```

    ##                            weight  chocolate  ...  multi  available_canada_america
    ## name                                          ...                                 
    ## Coffee Crisp                   50          1  ...      0                    Canada
    ## Butterfinger                  184          1  ...      0                   America
    ## Skor                           39          1  ...      0                      Both
    ## Smarties                       45          1  ...      1                    Canada
    ## Twix                           58          1  ...      1                      Both
    ## Reeses Peanutbutter Cups       43          1  ...      1                      Both
    ## 3 Musketeers                   54          1  ...      0                   America
    ## Kinder Surprise                20          1  ...      0                    Canada
    ## M & M                          48          1  ...      1                      Both
    ## Glosettes                      50          1  ...      1                    Canada
    ## KitKat                         45          1  ...      1                      Both
    ## Babe Ruth                      60          1  ...      0                   America
    ## Caramilk                       52          1  ...      0                    Canada
    ## Aero                           42          1  ...      0                    Canada
    ## Mars                           51          1  ...      0                      Both
    ## Payday                         52          0  ...      0                   America
    ## Snickers                       48          1  ...      0                      Both
    ## Crunchie                       26          1  ...      0                    Canada
    ## Wonderbar                      58          1  ...      0                    Canada
    ## 100 Grand                      43          1  ...      0                   America
    ## Take 5                         43          1  ...      0                   America
    ## Whatchamacallits               45          1  ...      0                   America
    ## Almond Joy                     46          1  ...      0                   America
    ## Oh Henry                       51          1  ...      0                      Both
    ## Cookies and Cream              43          0  ...      0                      Both
    ## 
    ## [25 rows x 10 columns]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

From this dataframe, we can see that there are 25 different candy bars
and 10 columns. We can obtain the names of the columns using this code:

``` python
df.columns
```

    ## Index(['weight', 'chocolate', 'peanuts', 'caramel', 'nougat',
    ##        'cookie_wafer_rice', 'coconut', 'white_chocolate', 'multi',
    ##        'available_canada_america'],
    ##       dtype='object')

Or if you wanted to see the dimensions of the whole dataframe you could
code the following:

``` python
df.shape
```

    ## (25, 10)

Breaking up this code it just means “From our dataframe that we saved as
`df` tell me the `columns` or tell me the `shape`”.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

Another important method to know is what if we don’t want to output the
whole table  
We can then specify how many rows of the dataset to show with
`df.head()`

``` python
df.head(2)
```

    ##               weight  chocolate  ...  multi  available_canada_america
    ## name                             ...                                 
    ## Coffee Crisp      50          1  ...      0                    Canada
    ## Butterfinger     184          1  ...      0                   America
    ## 
    ## [2 rows x 10 columns]

This specifies only 2 rows will be shown. We can specify any number of
rows within the brackets or we can leave it empty which will default to
5
    rows.

``` python
df.head()
```

    ##               weight  chocolate  ...  multi  available_canada_america
    ## name                             ...                                 
    ## Coffee Crisp      50          1  ...      0                    Canada
    ## Butterfinger     184          1  ...      0                   America
    ## Skor              39          1  ...      0                      Both
    ## Smarties          45          1  ...      1                    Canada
    ## Twix              58          1  ...      1                      Both
    ## 
    ## [5 rows x 10 columns]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

-----

# let’s apply what we learned\!

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
