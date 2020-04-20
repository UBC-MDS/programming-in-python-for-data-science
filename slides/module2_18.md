---
type: slides
---

# Chaining Notation

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## What is Chaining?

Up until now, when we want to perform multiple actions on an object,
After each action we have been saving the results under a new object
name. Chaining allows us to do multiple actions in a single line of code
without these intermediate objects.

You can imagine that we are linking verbs together similar to a chain.

<img src='module2/chainsfinal.png'  alt="404 image" />  
[Attribution](https://unsplash.com/photos/42ui88Qrxhw)

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

When we made our frequency table in Module 1, we first saved the single
column as an object before we used `value_counts()` We can do this all
in one line with chaining:

``` python
df['mfr'].value_counts()
```

```out
K    23
G    22
P     9
Q     8
R     8
N     6
A     1
Name: mfr, dtype: int64
```

However, this is not the extent of chaining. Before we move forward,
it’s important we know the difference between functions and methods.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Methods vs Functions

Chaining is used specifically with methods and cannot be used with
functions. We have made the comparison that attributes are as nouns, as
methods and functions are to verbs. But what makes these two verbs
different?

**Functions**: Execute an action.  
**Methods**: Are functions that execute an action but are associated
with an object.

Let’s compare the function`pd.read_csv()` with the method `head()`.

In `pd.read_csv()` we add an argument instructing the file name we wish
to bring in.

Example:

    pd.read_csv('cereal.csv')

`head()` requires an object, specifically a dataframe, in order to
execute.

Example:

    df.head()

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Methods generally have the form `object-name.method()` whereas functions
can take in arguments that don’t necessarily have to be objects.
Functions will have the form `function-name(argument)`.

Here is an example of how a function does not need an object. `abs()` is
a function that will return the absolute value of a number. `abs()`
takes in an argument - in this case, a number.

``` python
abs(-6)
```

```out
6
```

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Chaining is the design of performing each method in a sequential manner.

Here is an example where we perform 4 actions all in a single chain.

1.  Filter our dataframe for cereals only from manufacturer “K” -\> The
    results of this action is our object for the next method.
2.  We select the columns `calories`, `sugars` and `rating` using the
    method `loc`.
3.  We then use the `describe` method to find some summary statistics.
4.  `head()` is the final method used to obtain the first 5 rows of the
    describe
dataframe.

<!-- end list -->

``` python
df[df['mfr'] == 'K'].loc[ : , ["calories", "sugars", "rating"]].describe().head()
```

```out
         calories     sugars     rating
count   23.000000  23.000000  23.000000
mean   108.695652   7.565217  44.038462
std     22.218818   4.500768  14.457434
min     50.000000   0.000000  29.924285
25%    100.000000   3.000000  34.478442
```

This chain avoided the use of 3 intermediate objects.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Ok so great, we can cut out creating intermediate variable but now we
just have a really long line of code and it’s a bit hard to read.

How can we make this easier to understand?  
In this course, we suggest giving a new line for each method. We can do
this by wrapping our code in parentheses and making a new line before
each period (`.`). It’s good practice to indent and have the methods
line up to make it especially clear.

``` python
(df[df['mfr'] == 'K'].loc[ : , ["calories", "sugars", "rating"]]
                     .describe()
                     .head()
)
```

```out
         calories     sugars     rating
count   23.000000  23.000000  23.000000
mean   108.695652   7.565217  44.038462
std     22.218818   4.500768  14.457434
min     50.000000   0.000000  29.924285
25%    100.000000   3.000000  34.478442
```

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
