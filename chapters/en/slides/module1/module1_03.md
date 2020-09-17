---
type: slides
---

# What is Pandas?

Notes:

<br>

---

<center>

<img src='/module1/pandas.gif'  alt="404 image"  width="50%" align="middle"/>

</center>

Notes:

Pandas is an add on library to Python.

It let’s us do more things with our code, specifically with dataframes.

---

## Importing pandas

``` python
import pandas as pd
```

Notes:

To analyze dataframes and load these `csv` files, we need to make sure
that we bring in this `pandas` library.

Before we start writing any valuable code, we import it with the
following code.

---

## Reading in Data

``` python
candy = pd.read_csv('candybars.csv')
```

``` python
candy
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

Notes:

Next we can bring in our data named `candybars` which is stored as a
`.csv` file.

let’s break this up:

  - `pd` is the short form for pandas, which we are using to manipulate
    our dataframes.  
  - `read_csv()` is the tool that does the job and, in this case, it is
    reading in the `csv` file named `candybars.csv`.  
  - `candy` is The dataframe is now saved as an object called `candy`.

The dataframe is stored in an object named `candy` and we can inspect in
by “calling” the object name.

In these slides we can differentiate between the code that we typed in
with a light grey background and it’s output which is coloured with a
dark grey background.

From this dataframe, we can see that there are 25 different candy bars
and 6 columns.

---

``` python
candy.columns
```

```out
Index(['name', 'weight', 'chocolate', 'peanuts', 'caramel', 'available_canada_america'], dtype='object')
```

``` python
candy.shape
```

```out
(25, 6)
```

Notes:

We can obtain the names of the columns using `.columns`, and if we
wanted to see the dimensions of the whole dataframe we could use
`.shape` after the dataframe name.

Breaking up the code, we interpret this as:

*“From our dataframe that we saved as `candy` tell me the `shape`”* or
*“From our dataframe that we saved as `candy` tell me the `column`
names”*

---

``` python
candy.head(2)
```

```out
           name  weight  chocolate  peanuts  caramel available_canada_america
0  Coffee Crisp      50          1        0        0                   Canada
1  Butterfinger     184          1        1        1                  America
```

``` python
candy.head()
```

```out
           name  weight  chocolate  peanuts  caramel available_canada_america
0  Coffee Crisp      50          1        0        0                   Canada
1  Butterfinger     184          1        1        1                  America
2          Skor      39          1        0        1                     Both
3      Smarties      45          1        0        0                   Canada
4          Twix      58          1        0        1                     Both
```

Notes:

What if we don’t want to output the whole table when displaying a
dataframe?

We can specify how many rows of the dataset to show with `.head()`.

`.head(2)` will output the first 2 rows of the dataframe.

We can specify any number of rows within the parentheses or we can leave
it empty which will default to the first 5 rows.

---

## Functions/Methods and Attributes

<center>

<img src='/module1/argument.png'  alt="404 image"  width="50%" align="middle"/>

</center>

### Attributes

Take `candy.shape` as an example.

In this case, our dataframe `candy` is our object and `.shape` is the
attribute describing it.

### Functions

In the example of `pd.read_csv()`, this function does the action of
reading in our data.

Notes:

Something you may have noticed is that when we use `pd.read_csv()` we
put our instructions within the parentheses, whereas, when we use
`.shape` or `.head()` the object comes before our desired command.

In Python, we use **functions**, **methods** and **attributes**. These
are special words in Python that takes in instructions (we call these
arguments) and do something.

Attributes can be distinguished from methods and functions as they do
not have parentheses.

They can be thought of as nouns or adjectives that describe an object.

Take `candy.shape` as an example.

In this case, our dataframe `candy` is our object and `.shape` is the
attribute describing it.

Functions and methods have parentheses.  
They can be thought of as verbs that complete an action.

In the example of `pd.read_csv()`, this function does the action of
reading in our data.

This is going to be discussed in more detail later in the course but
now, simply be aware of the way we write different instructions.

---

## Comments

``` python
# This line does not execute anything. 
```

``` python
candy.shape  # This will output the shape of the dataframe
```

Notes:

While we write code, it’s often useful to annotate it or include
information that we do not want to executed.

The easiest way to do this is with a hash (`#`) symbol. This creates a
single line comment and prevents anything written after it from being
executed.

We can also use it beside code.

We use comments frequently in the exercises.

It’s good practice to use them to explain our code so if we or someone
else wants to read it at a later date, it’s easier to understand.

---

# Let’s apply what we learned\!

Notes:

<br>
