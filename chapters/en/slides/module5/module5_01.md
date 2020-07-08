---
type: slides
---

# Making choices with conditionals

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last Module, we explored using different data structures and
types that Python offers. It’s at this point in the course where we
learn how to ask Python to take different actions, depending on a
condition, from these structures.

We did something similar when we filtered a dataframe using condition
such as:

``` python
cereal[cereal['mfr'] == 'K']
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3    1.00  0.50  93.704912
6                 Apple Jacks   K  Cold       110        2    0     125    1.0   11.0      14      30        25      2    1.00  1.00  33.174094
16                Corn Flakes   K  Cold       100        2    0     290    1.0   21.0       2      35        25      1    1.00  1.00  45.863324
17                  Corn Pops   K  Cold       110        1    0      90    1.0   13.0      12      20        25      2    1.00  1.00  35.782791
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
58                Raisin Bran   K  Cold       120        3    1     210    5.0   14.0      12     240        25      2    1.33  0.75  39.259197
60             Raisin Squares   K  Cold        90        2    0       0    2.0   15.0       6     110        25      3    1.00  0.50  55.333142
62              Rice Krispies   K  Cold       110        2    0     290    0.0   22.0       3      35        25      1    1.00  1.00  40.560159
66                     Smacks   K  Cold       110        2    1      70    1.0    9.0      15      40        25      2    1.00  0.75  31.230054
67                  Special K   K  Cold       110        6    0     230    1.0   16.0       3      55        25      1    1.00  1.00  53.131324

[23 rows x 16 columns]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s start with an example of what the syntax looks like.

Perhaps we want to introduce ourself in our code by using the object
called `my_name`. Here we use a verb called `print()` that simply prints
the object or string set as it’s argument:

``` python
my_name = 'Hayley' 

if my_name.lower() == 'hayley':
   print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
  print('Interesting, I loved that movie!')
else:
  print('Nice to meet you!')
```

```out
My name is Hayley too!
```

We can see that since the object `my_name` is equal to `hayley`, so it
makes sense that the output is `My name is Hayley too`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Syntax

``` python
my_name = 'Hayley' 

if my_name.lower() == 'hayley':
   print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
  print('Interesting, I loved that movie!')
else:
  print('Nice to meet you!')
```

```out
My name is Hayley too!
```

Python conditional statements contains 2 important things:

  - A strict structure.
  - The keyword `if` and optional keywords `else` and `elif`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Structure

``` python
my_name = 'Hayley' 

if my_name.lower() == 'hayley':
   print('My name is Hayley too!')
```

```out
My name is Hayley too!
```

The structure of a choice is as follows:

``` python
Some conditional expression:
    statement body 
```

Each conditional expression must end with a colon `:` and any code
directed at values that meet the expression, all must be indented with 4
spaces.  
In the example above,  
`if my_name.lower() == 'hayley'` is the conditional expression and,  
`print("My name is Hayley too!")` is the statement body.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

#### Keywords

  - An `if` expression is needed for any conditional. If the expression
    is true, the body of the statement (anything indented under it) will
    be executed. If the expression is false, the body of the statement
    is not executed and it continues to the next line of code outside
    the body of the if condition.  
  - The `else` expression will execute if the conditional expressions
    above it are false. Unlike `if` which can be executed many times,
    `else` can only occur once following an `if` condition.

<center>

<img src='/module5/ifelse.png' width="40%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`else` statements are optional. If you don’t want to assign a default
value, the code will still work without one.

``` python
my_name = 'Hayley' 

if my_name.lower() == 'hayley':
   print('My name is Hayley too!')
```

```out
My name is Hayley too!
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

  - `elif` stands for ***else if***. It allows us to check multiple
    conditions for true.
  - When the `elif` expression evaluates to true, then the body of the
    statement is executed, just like an `if` statement.
  - Unlike `else`, we can use as many `elif` statements in a decision
    process as we want.
  - `elif` statements **MUST** follow an `if` statement or an error will
    occur.

<!-- end list -->

``` python
my_name = 'Hayley' 

elif my_name.lower() == 'totoro':
    print("Interesting, I loved that movie!")
```

``` out
Error: invalid syntax (<string>, line 2)
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s look at the example in the diagram below:

<center>

<img src='/module5/condition1.png' width="40%">

</center>

We can look at each `if` and `elif` condition as a filter. For an object
that is <b><font color="#ea92b9">pink</font></b> , the body of the `if`
statement will execute and not see any further conditions down the
funnel.  
For a <b><font color="#a4cff4">blue</font></b> object, the item will
have seen the `if` condition but because it did not result in a true
value, it continued down the funnel. Since the `elif` condition results
in a true statement, it will not proceed to the `else` condition’s
body.  
<b><font color="#53d3dc">Any other colour</font></b> will pass the 2
conditions and proceed to the default `else` statement’s body.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Order matters

The order we chose for the statement for the `if` and `elif` statements
is important and can result in different outputs. Let’s explore this in
the next example:

``` python
item = 12 

if item > 10:
    magnitude = 'greater than 10'
elif item > 20:
    magnitude = 'greater than 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 10'
```

In this case, our `item` value is greater than 10 so our first
condition, holds true. But let’s see what happens with an `item` value
of 22.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
item = 22 

if item > 10:
    magnitude = 'greater than 10'
elif item > 20:
    magnitude = 'greater than 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 10'
```

The item is taken out of the stream at the first `if` condition and so
it doesn’t get a chance to see the `elif` statement even though it would
result in a true value.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/condition2.png' width="50%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

This can be fixed by rearranging the conditional statements:

``` python
item = 22 

if item > 20:
    magnitude = 'greater than 20'
elif item > 10:
    magnitude = 'greater than 10'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 20'
```

Now a value of 22 give the correct output, but what about a value of 12?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
item = 12 

if item > 20:
    magnitude = 'greater than 20'
elif item > 10:
    magnitude = 'greater than 10'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 10'
```

Since 12 doesn’t meet the first condition, it passes it, and moves onto
the second condition which it does meet.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/condition3.png' width="50%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## In line

In situation where we have only `if` and `else` statements, we have a
nice ability to put it all in a single line of code. We have a given
object, in this case we are using a list of words named `words`:

``` python
words = ['the', 'list', 'of', 'words']
```

The original conditional statements below checks if the list is longer
than 10 elements or not and gives it a `list_size` value.

``` python
if len(words) > 10:
    list_size = "long list"
else:
    list_size = "short list"
list_size
```

```out
'short list'
```

The 4 lines used for the conditional statements can be compressed into a
single one:

``` python
list_size = "long list" if len(words) > 10 else "short list"
list_size
```

```out
'short list'
```

Both syntaxes are acceptable depending on your preference.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

### Python Keyword “in”

Up to this point, we have been using equalities and inequalities for our
conditions, but we are not restricted to this. There are many different
keywords we can use in conditional statements but one that you may use
often is `in`.

We can use `in` to check if a certain value is contained in a list or
dictionary:

``` python
exercises = ['burpees', 'lunges', 'squats', 'curls', 'deadlifts']

if 'squats' in exercises:
  sore = True
else:
  sore = False
  
sore
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

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
