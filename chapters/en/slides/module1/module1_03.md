---
type: slides
---

# What is Pandas?

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module1/pandas.gif'  alt="404 image"  width="50%" align="middle"/>

</center>

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Importing Pandas

To analyze dataframes and load these `csv` files, we need to make sure
that we import something called `pandas`.

Before we start writing any valuable code, we import it with the
following code:

``` python
import pandas as pd
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Reading in Data

Next we can bring in our data named `candybars` which is stored as a
`.csv`:

``` python
df = pd.read_csv('candybars.csv')
```

let’s break this up:

`pd`: this is the short form for pandas, which we are using to
manipulate our dataframes.  
`read_csv()`: The tool that does the job and, in this case, it is
reading in the `csv` file named `candybars.csv`.  
`df`: The dataframe is now saved as an object called `df`.

In these slides you can differentiate between what we typed in (our
code) in light gray and the output of it, which will be coloured with a
dark grey background.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The dataframe is stored in an object named `df` and looks like this:

``` python
df
```

```out
                 name  weight  chocolate  peanuts  caramel available_canada_america
0        Coffee Crisp      50          1        0        0                   Canada
1        Butterfinger     184          1        1        1                  America
2                Skor      39          1        0        1                     Both
3            Smarties      45          1        0        0                   Canada
4                Twix      58          1        0        1                     Both
..                ...     ...        ...      ...      ...                      ...
20             Take 5      43          1        1        1                  America
21   Whatchamacallits      45          1        1        0                  America
22         Almond Joy      46          1        0        0                  America
23           Oh Henry      51          1        1        1                     Both
24  Cookies and Cream      43          0        0        0                     Both

[25 rows x 6 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

From this dataframe, we can see that there are 25 different candy bars
and 6 columns. We can obtain the names of the columns using this code:

``` python
df.columns
```

```out
Index(['name', 'weight', 'chocolate', 'peanuts', 'caramel', 'available_canada_america'], dtype='object')
```

Or if you wanted to see the dimensions of the whole dataframe you could
code the following:

``` python
df.shape
```

```out
(25, 6)
```

Breaking up this code it just means “From our dataframe that we saved as
`df` tell me the `columns`/`shape`”.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What if we don’t want to output the whole table when displaying a
dataframe? We can specify how many rows of the dataset to show with
`.head()`. This will output the first few rows of the dataframe:

``` python
df.head(2)
```

```out
           name  weight  chocolate  peanuts  caramel available_canada_america
0  Coffee Crisp      50          1        0        0                   Canada
1  Butterfinger     184          1        1        1                  America
```

The above code specifies only 2 rows to display. We can specify any
number of rows within the parentheses or we can leave it empty which
will default to the first 5 rows.

``` python
df.head()
```

```out
           name  weight  chocolate  peanuts  caramel available_canada_america
0  Coffee Crisp      50          1        0        0                   Canada
1  Butterfinger     184          1        1        1                  America
2          Skor      39          1        0        1                     Both
3      Smarties      45          1        0        0                   Canada
4          Twix      58          1        0        1                     Both
```

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Functions/Methods and Attributes

Something you may have noticed is that when we use `pd.read_csv()` we
put our instructions within the parentheses, whereas, when we use
`.shape` or `.head()` the object comes before our desired command. In
Python, we use **functions**, **methods** and **attributes**. These are
special words in Python that takes in instructions (we call these
arguments) and do something.

<center>

<img src='/module1/argument.png'  alt="404 image"  width="50%" align="middle"/>

</center>

Attributes can be distinguished from methods and functions as they do
not have parentheses.  
They can be thought of as nouns or adjectives that describe an object.

Take `df.shape` as an example.  
In this case, our dataframe `df` is our object and `.shape` is the
attribute describing it.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<br>

<br>

Functions and methods have parentheses.  
They can be thought of as verbs that complete an action.  
In the example of `pd.read_csv()`, this function does the action of
reading in your data.

This is going to be discussed in more detail later in the course but
now, simply be aware of the way we write different instructions.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Comments

While we write code, it’s often useful to annotate it or include
information that you do not want to excuted. The easiest way to do this
is with a hash (`#`) symbol. This creates a single line comment and
prevents anything written after it from being executed.

``` python
# This line does not excute anything. 
```

You can also use it beside code.

``` python
df.shape  # This will output the shape of the dataframe
```

You’ll notice we use comments frequently in the exercises. It’s good
practice to use them to explain your code so if you or someone else
wants to read it at a later date, it’s easier to understand.

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here.

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
