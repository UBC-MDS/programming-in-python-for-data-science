---
type: slides
---

# Reading in Different File Types

Notes: <br>

---

## Reading in Different File Types

`pandas` facilitates the loading of data from many different file types
including:

  - A URL
  - A `txt` file
  - An `xlsx` file

Notes:

In the last module, we learned how to read in a `csv` file but loading
in data is not restricted to this file type.

  - A URL: If the data is stored publicly on a webpage, pandas can read
    it directly in from the page address.
  - A `txt` file: We saw what a plain text file looked like in the last
    module and it is generally a simple manner of storing data.  
  - An `xlsx` file: This is a Microsoft Excel spreadsheet. This is
    different than a regular `csv` file as an Excel file can contain
    many different sheets and can be formatted uniquely and specifically
    for an individual’s needs.

Of course, there are many other file types but we will focus on these
for this course.

---

## Reading from a URL

<a href="https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-011-programming-in-python/master/data/candybars.csv" target="_blank">https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-011-programming-in-python/master/data/candybars.csv</a>.

<center>

<img src='/module2/url-samp.png'  alt="404 image"  width="50%"  align="middle"/>

</center>

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

Notes:

If the data is accessible publicly on a website, you can read in data
directly from the webpage it is stored on. For example, this code and
all the files that make up this course are all openly available and can
be
<a href="https://github.com/UBC-MDS/MCL-DSCI-011-programming-in-python" target="_blank">viewed
online</a>.

The `candybar.csv` file that we used in the last module is stored at
this URL.

You can see that it looks like a plain text file with each line being a
row and each column value separated with a comma.

The code required to read in this URL looks like this.

It uses the same `pd.read_csv()` function we saw when reading in csv
files locally.

---

## Reading in a Text File

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

Notes:

Reading in `txt` files can be a little less standard. Sometimes the
character separating column values are not always commas like we saw
before There are many different options and when we read in the data, we
need to specify how the data should be recognized.  
Let’s load in the `candybars-text.txt` file. This is the same as the
`candybars.csv` data but saved as a `txt` file. Look what happens when
we load it in using the same syntax we are used to.

This is not ideal. What you should notice is instead of each column
value being separated by a comma, it is now separated by `\t`.  
This is called the **delimiter**.

In this specific case, a `\t` delimiter is a “tab”.

We need to tell `pd.read_csv()` to separate each value on our delimiter
`\t`.

That’s much better.

The delimiter won’t always be `\t` for `txt` files. The most common
delimiters are `;`, `,`, `\t`, and sometimes even just spaces.

---

## Reading in an Excel File (`xlsx`)

``` python
candybars = pd.read_excel('foods.xlsx', sheet_name='chocolate')
candybars
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2                Skor      39          1        0        1       0                  0        0                0      0                     Both
3            Smarties      45          1        0        0       0                  0        0                0      1                   Canada
4                Twix      58          1        0        1       0                  1        0                0      1                     Both
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
20             Take 5      43          1        1        1       0                  1        0                0      0                  America
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0                  America
22         Almond Joy      46          1        0        0       0                  0        1                0      0                  America
23           Oh Henry      51          1        1        1       0                  0        0                0      0                     Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 11 columns]
```

Notes:

Excel files need special attention because they give the user the
capability of additional formatting including saving multiple dataframes
on different “sheets” within a single file. If this is the case, we need
to specify which sheet we want.

Since this is a new type of animal, we also need a new verb. Enter
`read_excel()`.

Our candybars dataframe is now saved as an excel spreadsheet named
`foods.xlsx` on a sheet named `chocolate`.

Here is how we would read it in.

---

## Reading in Data from a Different File

<center>

<img src='/module2/datafile.png'  alt="404 image"  width="70%" align="middle"/>

</center>

This translates to the syntax `data/canucks.csv`.

Notes:

Something you have seen in Module 1’s exercises is that when reading in
the data there is always a `data/` before the file name.  
This is because we are running the current code in a file that is
located in a different folder than the data.  
The `data` is specifying a folder in our current directory (folder). We
need to specify the path to the `csv` file through the subdirectory.

This translates to the syntax `data/canucks.csv`.

---

*_Example:_*

`data/module3/question2/candybars.csv`

<br> <br>

<center>

<img src='/module2/more_files.png'  alt="404 image"  width="80%" align="middle"/>

</center>

Notes: This syntax is not restricted to a single subdirectory and could
even have multiple folders between the current location and the final
file name.

---

<center>

<img src='/module2/online.png'  alt="404 image"  width="80%" align="middle"/>

</center>

Notes:

You can see the whole course structure and it’s subdirectories
<a href="https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python" target="_blank">openly
online</a>.

In this course, we save all our data in a folder called `data` so when
asked to read in data, take care in future exercises to add the full
path to the required file.

It may be a good idea to look in the
<a href="https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/tree/master/data" target="_blank">data
folder</a> to see exactly where the data you are loading in the
exercises is coming from.

---

# Let’s apply what we learned\!

Notes: <b>
