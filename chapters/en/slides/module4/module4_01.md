---
type: slides
---

# Python data types

Notes: <br>

---

## Values and Objects

  - We have been working with **values** which are pieces of data that a
    computer program works with, such as a number or text.
  - We have been assigning a lot of these **values** (with the
    assignment operator `=`) to **objects**.

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

Notes:

In the last few sections, you may have had questions like:

***“Why are some values in quotation marks while others are not?”***,

***“What are these square brackets we keep using in our verb
arguments?”*** or

***“Why can we take the mean of some columns and not others?”*** .

We’ll be answering these questions in this module.

Python needs to categorize things to make sense of them.

Let’s start with some basics.

In these cases `pet` and `age` are **objects** and `Fido` and `6` are
**values.**

These objects can be named anything that begins with a letter and are
not “special python words” like **range**, **for**, **if**, **else**,
etc (we will talk about some of those in the next module).

---

## Data Types

Here are some data types built-in to the Python language:

  - Integers - `int`
  - Floating-point numbers - `float`
  - Strings - `str`
  - Booleans -`bool`
  - Lists - `list`
  - Tuples - `tuple`
  - Sets - `set`
  - Dictionaries - `dict`

Notes:

Values, as we saw in our `Fido` and `6` examples, can be a variety of
different things that get classified by Python as **data types**.

---

## Numerical Data Types

### **Int**

``` python
age = 6 
type(age)
```

```out
<class 'int'>
```

### **Float**

``` python
age = 6.0
type(age)
```

```out
<class 'float'>
```

Notes:

You’ve likely noticed that we have not needed to put any quotation marks
around number values. Python recognizes numbers as one of two possible
types.

Either as an ***integer*** called an `int` type or a ***floating-point
number*** called a `float`.

An `int` value is a whole number that is either positive, negative, or
zero.

We can use the verb `type()` to find out how Python classifies the value
that are stored in an object.

`6` is of type `int`.

A `float` value is a real number in decimal form. That means even if we
have a whole number, if it contains a decimal point, it is considered a
`float`.

In contrast, `6.0` is if type `float`.

---

## NaN

``` python
weather
```

```out
      month  season  31st
0  february  winter   NaN
1     march  spring  31.0
2     march  spring   NaN
```

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

Notes:

Something you may have noticed in our Pandas dataframes are `NaN`
values.

This stands for **Not A Number** and it is a special value used to
represent missing data in pandas.

Contrary to its acronym it is considered a numeric value, specifically
of type `float`\!

Ignore the `numpy` and `64` for now and concentrate on the `float`
classification for now. We will be discussing NumPy more in Module 8.

Unlike other values, `NaN` cannot be converted to any other type other
than a `float.`

---

## NoneType

``` python
name_of_bed_monster = None
```

``` python
type(name_of_bed_monster)
```

```out
<class 'NoneType'>
```

Notes:

Unlike `NaN` which is a special `float` value, `NoneType` is its own
type, with only one possible value, `None`.

Let’s say we need to save the name of the monster living under my bed in
an object. Unfortunately, we have yet to introduce ourselves to him so
we are not sure what his name is. We also need to keep track that we are
missing this information.

We’ve seen this data type in our assignments when we replace the `None`
provided, with our solution. Since we still need to have the object
created for the structure of our assignments, we simply use `None` to
indicate the object exists but is devoid of information.

---

## Booleans

The Boolean (`bool`) type has two values: **True** and **False**.

``` python
type(False)
```

```out
<class 'bool'>
```

``` python
weather
```

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

Notes:

The Boolean type has two values: **True** and **False**. As you can see
at the top, the value `False` is of type `bool` for Boolean.

We have seen this data type when we were filtering our dataframes with
conditions.

In pandas, a condition is evaluated and produces a column indicating
whether the condition was met or not for each row.

This column is a Boolean type.

---

## Strings

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

``` python
name_of_bed_monster = """Mike Wazowski"""
name_of_bed_monster
```

```out
'Mike Wazowski'
```

Notes:

Text is stored as a data type called a string (`str`).

We think of a string as a sequence of characters enclosed in some form
of quotations.

We’ve been mostly using single quotations for strings up until this
point but you can enclose them with different types of quotation marks,
as shown here.

---

``` python
saying = '''Mike Wazowski said: "My name's Mike Wazowski!"'''
saying
```

```out
'Mike Wazowski said: "My name\'s Mike Wazowski!"'
```

``` python
missing_bed_monster = ''
missing_bed_monster
```

```out
''
```

``` python
type(missing_bed_monster)
```

```out
<class 'str'>
```

Notes:

If the string contains quotation marks or apostrophes, we can use double
quotes or triple single quotes, or triple double quotes to define the
string.

What about empty quotations? When we discussed `None` type and we didn’t
yet know the monster’s name, we could have also set it to an empty
string, as shown here. The benefit of this approach is that we’re
already setting the type of the object to string, rather than NoneType.

---

## String Verbs

There are
<a href="https://docs.python.org/3/library/stdtypes.html#string-methods" target="_blank">A
variety of different methods</a> to transform strings or extract
information from them.

``` python
name_of_bed_monster = 'Mike Wazowski'
```

  - `len()`:

<!-- end list -->

``` python
len(name_of_bed_monster)
```

```out
13
```

  - `.upper()`:

<!-- end list -->

``` python
name_of_bed_monster.upper()
```

```out
'MIKE WAZOWSKI'
```

  - `.lower()`:

<!-- end list -->

``` python
name_of_bed_monster.lower()
```

```out
'mike wazowski'
```

Notes:

There are
<a href="https://docs.python.org/3/library/stdtypes.html#string-methods" target="_blank">A
variety of different methods</a> to transform strings or extract
information from them. Here are a few of them.

  - We can obtain the number of characters in a string with `len()`.
  - We can change the cases to capitals with `.upper()`.
  - Or change the cases to lower case with `.lower()`.

---

``` python
name_of_bed_monster = 'Mike Wazowski'
```

``` python
name_of_bed_monster.count('k')
```

```out
2
```

``` python
name_of_bed_monster.count('K')
```

```out
0
```

Notes:

We can also count the number of times a substring or character is
present in a string with `.count()`.

It’s important to note that many of these verbs are case sensitive\!

---

## Casting

  - `int` to `float`:

<!-- end list -->

``` python
number_of_floating_balloons = float(5)
type(number_of_floating_balloons)
```

```out
<class 'float'>
```

  - An `int` to a `str`:

<!-- end list -->

``` python
number_of_balloon_strings = str(5)
type(number_of_balloon_strings)
```

```out
<class 'str'>
```

  - `float` to an `int` (it will round down to the nearest full
    integer).

<!-- end list -->

``` python
number_of_balloons = int(4.99)
number_of_balloons
```

```out
4
```

Notes:

Sometimes we need to explicitly transform an object from one type to
another, which is called ***casting***.

We can do this for some types, but not all.

To cast an object to a new type, we use verbs corresponding to the
desired type, such as `int()`, `float()`, `bool()` or `str()`.

---

``` python
bool(0)
```

```out
False
```

``` python
bool(5.0)
```

```out
True
```

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

Notes:

We can even convert `int` and `float` values to `bool` values.

Values of `0` or `0.0` are converted to `False` and all other numeric
are converted to `True`.

We can convert Boolean values to `int` and `float` values where `False`
is 0 or 0.0 respectively and `True` is 1 or 1.0.

---

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

Notes:

As suspected, the same applies to strings: Most data types can be
converted to strings easily.

We don’t even need to use `type()` here as we can see both values now
have quotations surrounding the value, meaning they are strings.

---

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

Notes:

Casting strings into other data types is a bit more problematic.

Sometimes it works correctly.

Other times it does not give us what we expected, as we can see here -
the string False is converted to the Boolean True. Be careful when
casting types\!

---

``` python
bool('Hello')
```

```out
True
```

``` python
bool('')
```

```out
False
```

``` python
float('five')
```

``` out
ValueError: could not convert string to float: 'five'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

In fact, only the empty string gets casted to False; every other string
is considered True when turned into a Boolean.

Often, we may not be able to cast a string at all.

---

``` python
bool(None)
```

```out
False
```

``` python
float(None)
```

``` out
TypeError: float() argument must be a string or a number, not 'NoneType'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

These nuisances can be expected with `NoneType` values as well.

In summary, take care when casting values.

---

# Let’s practice what we learned\!

Notes:

<br>
