---
type: slides
---

# Reading in Different File Types

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in Different File Types

In the last module we learned how to read in a `csv` file but we are not
restricted to that file type.  
`pandas` facilitates the loading of data from many different file types
including:

  - A `URL`: If the data is stored publicly on a webpage, pandas can
    read it directly in from the page address.
  - A `txt` file: We saw what a plain text file looked like in the last
    module and it is generally a simple manner of storing data.  
  - An `xlsx` file: This is a classic Excel spreadsheet. This is
    different than a regular `csv` file as an Excel file can contain
    many different sheets and can be formated uniquely and specifically
    for an idividual’s needs.

Of course there are many others , but we will focus on these for this
course.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading from a URL

If the data is accessible publicly on a website, you can read in data
directly from the webpage it is stored on. For example, this code and
all the files that make up this course is all open and can be [viewed
online](https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python).
The `candybar.csv` file that we used in the last module is stored at
this
url:  
<https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/candybars.csv>  
You can see that it looks like a plain `txt` file with each line being a
row and each column value separated with a comma.

The code required to read in this url looks like this:

``` python

candybars = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/candybars.csv')
candybars.head()
```

```out
           name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0  Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1  Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2          Skor      39          1        0        1       0                  0        0                0      0                     Both
3      Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4          Twix      58          1        0        1       0                  1        0                0      1                     Both
```

It uses the same `pd.read_csv()` function we saw when reading in `csv`
files.  
Pretty simple right?

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in a Text File

Reading in `txt` files can be a little less standard in nature.
Sometimes the character separating column values are not always commas
like we saw above. There are many different options and when we read in
the data, we need to specify how how data needs to be recognized. Let’s
load in the `candybars-text.txt` file. This is the same candybar data
but saved as a \`txt1 file. Let’s see what happen’s when we load it in
using the same syntax we are use to.

``` python
candybars = pd.read_csv('candybars-text.txt')
candybars.head()
```

```out
  name\tweight\tchocolate\tpeanuts\tcaramel\tnougat\tcookie_wafer_rice\tcoconut\twhite_chocolate\tmulti\tavailable_canada_america
0   Coffee Crisp\t50\t1\t0\t0\t0\t1\t0\t0\t0\tCanada                                                                             
1  Butterfinger\t184\t1\t1\t1\t0\t0\t0\t0\t0\tAme...                                                                             
2             Skor\t39\t1\t0\t1\t0\t0\t0\t0\t0\tBoth                                                                             
3       Smarties\t45\t1\t0\t0\t0\t0\t0\t0\t1\tCanada                                                                             
4             Twix\t58\t1\t0\t1\t0\t1\t0\t0\t1\tBoth
```

Oh no\! This is not ideal. What you should notice is instead of each
column value being separated by a column, it is now separated by `\t`.
This is called the *Delimiter*.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

We need to tell `pd.read_csv()` to separate each value on our delimiter
`\t`.

``` python
candybars = pd.read_csv('candybars-text.txt', delimiter='\t')
candybars.head()
```

```out
           name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0  Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1  Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2          Skor      39          1        0        1       0                  0        0                0      0                     Both
3      Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4          Twix      58          1        0        1       0                  1        0                0      1                     Both
```

Ah. That’s much better. We are not married to the delimiter being `\t`.
We can specify any character combination to accomodate other data files.
Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in an Excel File (`xlsx`)

Excel files need special attention because they give the user the
capability of additional formating including saving multiple dataframes
on different “sheets” within a single file. This means that if that is
the case, we need to specify which one we want. Since this is a new type
of animal we also need a new function. Enter `read_excel()`.

We have our candybars dataframe saved as an excel spreadsheet named
`foods.xlsx` on a sheet named `candybars`.  
Here is how we would read it in:

``` python

candybars = pd.read_excel('foods.xlsx', sheet_name='candybars')
candybars.head()
```

```out
  This dataset was created by Hayley Boyce in February 2020. Unnamed: 1 Unnamed: 2 Unnamed: 3 Unnamed: 4 Unnamed: 5         Unnamed: 6 Unnamed: 7       Unnamed: 8 Unnamed: 9               Unnamed: 10
0  Note this is not a complete dataset and there ...                NaN        NaN        NaN        NaN        NaN                NaN        NaN              NaN        NaN                       NaN
1                                               name             weight  chocolate    peanuts    caramel     nougat  cookie_wafer_rice    coconut  white_chocolate      multi  available_canada_america
2                                       Coffee Crisp                 50          1          0          0          0                  1          0                0          0                    Canada
3                                       Butterfinger                184          1          1          1          0                  0          0                0          0                   America
4                                               Skor                 39          1          0          1          0                  0          0                0          0                      Both
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in Data from a Different File

Something you’ve seen in the previous exercises is that when we read in
the data there is alway a `data/` before the file name.  
This is because the file we are running the current code in, is located
in a different folder than the data. The `data` folder is a folder in
our current directory (folder). We need to specify the path to the `csv`
file through the subfile.

<img src='module2/datafile.png'  alt="404 image" />

This translates to the syntax `data/canucks.csv`

This syntax is not restricted to a single subfolder and could even have
multiple folder between the current location and the final file name.
*Example:* `data/module1/question3/candybars.csv`

In this course we save all our data in a file called `data` so when
asked to read in data, take care in future exercises to add the full
path to the required file.

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
