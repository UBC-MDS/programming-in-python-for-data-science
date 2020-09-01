---
type: slides
---

# Python data types

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Values and Objects

In the last few sections, you may have had questions like *“Why are some
values in quotations and why others are not?”*, *“What are these square
brackets we keep using in our verb arguments?”* or *“Why can we take the
mean of some columns and not others?”* . These are going to get answered
in this module.

Python needs to categorize things to make sense of them.

Let’s start with some basics.

  - We have been working with **values** which are pieces of data that a
    computer program works with such as a number or text.
  - We have been assigning a lot of these **values** (with the
    assignment `=` operator) to **objects**.

<!-- end list -->

``` python
pet = 'Fido' 
pet
```

```out
'Fido'
```

``` python
age = 6
age
```

```out
6
```

In these cases `pet` and `age` are **objects** and `Fido` and `6` are
**values.**

These objects can be named anything that begins with a letter and are
not “special python words” like **while**, **for**, **if**, **else**,
etc (we will talk about those in the next module).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Data Types

Values, as we saw in our `Fido` and `6` examples, can be a variety of
different things that get classified by Python as **Data Types**. Here
are some data types built-in to the Python language:

  - Integers - `int`
  - Floating-point numbers - `float`
  - Strings - `str`
  - Booleans -`bool`
  - Lists - `list`
  - Tuples - `tuple`
  - Sets - `set`
  - Dictionaries - `dict`

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Numerical Data Types

You’ve likely noticed that we have not needed to put any quotation marks
around number values. Python recognizes numbers as one of two possible
types.  
Either as an ***integer*** called an `int` type or a ***floating-point
number*** called a `float`.

### **Int**

An `int` value is a whole number that is either positive, negative, or
zero.

We can use the verb `type()` to find out how Python classifies the value
that was stored in an object.

``` python
age = 6 
type(age)
```

```out
<class 'int'>
```

`6` is of type `int`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

### **Float**

A `float` value is a real number in decimal form. That means even if we
have a whole number, if it contains a decimal point, it is considered a
`float`

``` python
age = 6.0
type(age)
```

```out
<class 'float'>
```

Something you may have noticed in our Pandas dataframes are values such
a `NaN`.

``` python
weather
```

```out
      month  season  31st
0  february  winter   NaN
1     march  spring  31.0
2     march  spring   NaN
```

This stands for **Not A Number** and it is a special value to represent
missing data.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

```out
      month  season  31st
0  february  winter   NaN
1     march  spring  31.0
2     march  spring   NaN
```

Contrary to its acronym it is considered a numeric, specifically of type
float\!

``` python
nan_value = weather.loc[2,'31st']
nan_value
```

```out
nan
```

``` python
type(nan_value)
```

```out
<class 'numpy.float64'>
```

Ignore the `numpy` and `64` for now and concentrate on the `float`
classification for now. We will be discussing this a bit more later on.

Unlike other values, `NaN` cannot be converted to any other type other
than a float.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## NoneType

`NoneType` is its own type, with only one possible value, `None`; on the
other hand `NaN` is actually a special `float` value. Pandas dataframes
tend to use `NaN` for missing values."

Let’s say I need to save the name of the monster living under my bed in
an object. Unfortunately, I have yet to introduce myself to him so I’m
not sure what his name is. I also need to keep track that this has not
been collected and we are missing this information.

``` python
name_of_bed_monster = None
```

``` python
type(name_of_bed_monster)
```

```out
<class 'NoneType'>
```

You’ve seen this data type in your assignments when you replace the
`None` provided, with your solution. Since we still need to have the
object created for the structure of our assignments, we simply use
`None` to indicate the object exists but is void of information.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Booleans

The Boolean (`bool`) type has two values: **True** and **False**.

We have seen this data type when we were filtering our dataframes with
conditions. A condition is evaluated and produces a column indicating
whether the condition was met or not.

```out
      month  season  31st
0  february  winter   NaN
1     march  spring  31.0
2     march  spring   NaN
```

``` python
weather['season'] == 'winter'
```

```out
0     True
1    False
2    False
Name: season, dtype: bool
```

In filtering and many scenarios in programming, the evaluation of code
can only be one of 2 options.

``` python
type(False)
```

```out
<class 'bool'>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Strings

Text is stored as a data type called a string (`str`). We think of a
string as a sequence of characters and can enclose in quotations. We’ve
been mostly using single quotations for strings up until this point but
you enclosed them with either:

  - Single quotes, e.g., `'Hello'`
  - Double quotes, e.g., `"Goodbye"`
  - Triple single quotes, e.g., `'''Yesterday'''`
  - Triple double quotes, e.g., `"""Tomorrow"""`

<!-- end list -->

``` python
name_of_bed_monster = 'Mike Wazowski'
name_of_bed_monster
```

```out
'Mike Wazowski'
```

``` python
name_of_bed_monster = "Mike Wazowski"
name_of_bed_monster
```

```out
'Mike Wazowski'
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If the string contains a quotation or apostrophe, we can use double
quotes or triple quotes to define the string.

``` python
saying = '''Mike Wazowski said: "My name's Mike Wazowski!"'''
saying
```

```out
'Mike Wazowski said: "My name\'s Mike Wazowski!"'
```

What about empty quotations? When we discussed `None` type and we didn’t
yet know the monster’s name, why didn’t we just put empty quotations?

``` python
missing_bed_monster = ''
missing_bed_monster
```

```out
''
```

That’s because the object is still recognized as a string.

``` python
type(missing_bed_monster)
```

```out
<class 'str'>
```

An empty string is similar to `NaN` values in that it has a type but no
data.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## String Verbs

There are
<a href="https://docs.python.org/3/library/stdtypes.html#string-methods" target="_blank">A
variety of different methods</a> to transform strings or extract
information from them. Here are a few of them:

``` python
name_of_bed_monster = 'Mike Wazowski'
```

We can obtain the number of characters in a string with `len()`:

``` python
len(name_of_bed_monster)
```

```out
13
```

We can change the cases to capitals with `.upper()`:

``` python
name_of_bed_monster.upper()
```

```out
'MIKE WAZOWSKI'
```

or lower case

``` python
name_of_bed_monster.lower()
```

```out
'mike wazowski'
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
name_of_bed_monster = 'Mike Wazowski'
```

We can count the number of times a substring or character is present in
a string.

``` python
name_of_bed_monster.count('k')
```

```out
2
```

But note that many of these verbs are case sensitive\!

``` python
name_of_bed_monster.count('K')
```

```out
0
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Casting

Sometimes we need to explicitly cast an object from one type to another.
We can do this for some types, but not all. We simply use their
corresponding verbs such as `int()`, `float()`, `bool()` or `str()`.

We can convert an object of type `int` to a float:

``` python
number_of_floating_balloons = float(5)
type(number_of_floating_balloons)
```

```out
<class 'float'>
```

An `int` to a `str`:

``` python
number_of_balloon_strings = str(5)
type(number_of_balloon_strings)
```

```out
<class 'str'>
```

We can also convert from a `float` to an `int` and it will round down to
the nearest full integer.

``` python
number_of_balloons = int(4.99)
number_of_balloons
```

```out
4
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can even convert `int` and `float` values to `bool` values

``` python
bool(5.0)
```

```out
True
```

``` python
bool(0)
```

```out
False
```

Note that values of `0` or `0.0` are converted to `False` and all other
numeric are converted to `True`.

And we can convert boolean values to `int` and `float` values where
`False` is 0/0.0 respectively and `True` is 1/1.0.

``` python
int(False)
```

```out
0
```

``` python
float(True)
```

```out
1.0
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

As suspected the same applies to strings: Most data types can be
converted to strings easily

``` python
str(True)
```

```out
'True'
```

``` python
str(None)
```

```out
'None'
```

``` python
str(3.2)
```

```out
'3.2'
```

We don’t even need to use `type()` here as we can see both values now
have quotations surrounding the value.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Casting strings into other data types, are a bit more problematic.  
Sometimes it works correctly:

``` python
float('0')
```

```out
0.0
```

``` python
bool('True')
```

```out
True
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Other times it does not give us what we expected:

``` python
bool('False')
```

```out
True
```

``` python
bool('0')
```

```out
True
```

When we cast a `str` to a `bool`, it will result in `True`, unless it’s
an empty `str`:

``` python
bool('')
```

```out
False
```

Often, we may not be able to cast a string at all:

``` python
float('five')
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): ValueError: could not convert string to float: 'five'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

These nuisances can be expected with `NoneType` values as well:

``` python
bool(None)
```

```out
False
```

``` python
float(None)
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: float() argument must be a string or a number, not 'NoneType'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

In summary, take care when casting values.

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

</audio>

</html>
