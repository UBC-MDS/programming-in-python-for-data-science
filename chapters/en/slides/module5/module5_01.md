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
learn how to ask Python to make a decision, depending on conditions.

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

Perhaps we want to introduce ourselves in our code by using the object
called `my_name`. Here we use a verb called `print()` that simply prints
the object or string set as an argument:

``` python
my_name = 'Hayley' 

if my_name.lower() == 'hayley':
    print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
    print('Interesting, I loved that movie!')
else:
    print("That's a great name.")
  
print('Nice to meet you!')
```

``` out
My name is Hayley too!
Nice to meet you!
```

We can see that since the object `my_name` is equal to `hayley`, the
output is `My name is Hayley too`. It then continues to run the code
`'Nice to meet you!` which is outside any conditions.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/iftrue.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now what happens if the object was equal to something else?

``` python
my_name = 'Totoro' 

if my_name.lower() == 'hayley':
    print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
    print('Interesting, I loved that movie!')
else:
    print("That's a great name.")
  
print('Nice to meet you!')
```

``` out
Interesting, I loved that movie!
Nice to meet you!
```

The object `my_name` has a different value now, so the output
corresponds to a different `print()` statement. This time it prints
`Interesting, I loved that movie!` and the code `Nice to meet you!` that
follows the conditions.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/eliftrue.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Now we try something that meets neither of those conditions:

``` python
my_name = 'Desmond' 

if my_name.lower() == 'hayley':
    print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
    print('Interesting, I loved that movie!')
else:
    print("That's a great name.")
  
print('Nice to meet you!')
```

``` out
That's a great name.
Nice to meet you!
```

When `my_name` is `Desmond` the last possible output is returned and
prints `That's a great name.`. It resumes and executes the code
underneath as did each of the other values.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/elsetrue.png' width="100%">

</center>

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
    print("That's a great name.")
  
print('Nice to meet you!')
```

``` out
My name is Hayley too!
Nice to meet you!
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
if SOME_BOOLEAN:
    statement body 
```

Each conditional expression must end with a colon `:` and any code
directed at values that meet the expression, all must be indented with 4
spaces (or consistent indentation) .  
In the example above,  
`if my_name.lower() == 'hayley'` is the boolean statement `print("My
name is Hayley too!")` is the statement body.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

#### Keywords

  - An `if` is needed for any conditional. If the boolean value is
    `True`, the body of the statement (anything indented under it) will
    be executed. If the expression is `False`, the body of the statement
    is not executed and it continues to the next line of code outside
    the body.  
  - The `else` expression will execute if the conditional expressions
    above it are false. `else` can only occur once following an `if`
    condition.

`else` statements are optional.

``` python
my_name = 'Mia' 

if my_name.lower() == 'hayley':
   print('My name is Hayley too!')

print('Nice to meet you!')
```

``` out
Nice to meet you!
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

  - `elif` stands for ***else if***. It allows us to check multiple
    conditions if they are true.

  - When the `elif` expression evaluates to true, then the body of the
    statement is executed, just like an `if` statement.

In the case we saw before, `my_name.lower() == 'totoro'` is the second
condition which evaluates to “True”:

``` python
my_name = 'Totoro' 

if my_name.lower() == 'hayley':
    print('My name is Hayley too!')
elif my_name.lower() == 'totoro':
    print('Interesting, I loved that movie!')
else:
    print("That's a great name.")
  
print('Nice to meet you!')
```

``` out
Interesting, I loved that movie!
Nice to meet you!
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

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

## Order matters

The order we chose for the statement for the `if` and `elif` statements
is important and can result in different outputs. Let’s explore this in
the next example using inequalities with numbers:

``` python
item = 13 

if item > 10:
    magnitude = 'Between 10 and 20'
elif item > 20:
    magnitude = 'Greater than 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'Between 10 and 20'
```

In this case, our `item` value is greater than 10 so our first condition
holds true. But let’s see what happens with an `item` value of 25.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
item = 25 

if item > 10:
    magnitude = 'Between 10 and 20'
elif item > 20:
    magnitude = 'Greater than 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'Between 10 and 20'
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

<img src='/module5/order1.png' width="100%">

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
item = 25 

if item > 20:
    magnitude = 'Greater than 20'
elif item > 10:
    magnitude = 'Between 10 and 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'Greater than 20'
```

Now a value of 25 gives the desired output of `greater than 20`, but
what about a value of 13?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
item = 13 

if item > 20:
    magnitude = 'Greater than 20'
elif item > 10:
    magnitude = 'Between 10 and 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'Between 10 and 20'
```

Since 13 doesn’t meet the first condition, it passes it and moves onto
the second condition which it does meet.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/order2.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/order3.png' width="100%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Inline

In situations where we have only `if` and `else` statements, we have the
ability to put it all in a single line of code. Let’s test this on our
object `item`:

``` python
item = 13
```

The original conditional statements below checks if the item is greater
than 10 designating an object with the value `greater than 10` if it is
and `10 or less` otherwise:

``` python

if  item > 10:
    magnitude = 'Greater than 10'
else:
    magnitude = '10 or less'
    
magnitude
```

```out
'Greater than 10'
```

The 4 lines used for the conditional statements can be compressed into a
single one:

``` python
list_size = "Greater than 10" if item > 10 else "10 or less"
list_size
```

```out
'Greater than 10'
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

We’ve already seen that conditions evaluate to a boolean. So far we’ve
seen a lot of boolean evaluated from equalities and inequalities but
that’s not all.

There are many different keywords we can use in to obtain a boolean
value but one that you may use often is `in`.

We can use `in` to check if a certain value is contained in a list or
dictionary:

``` python
exercises = ['burpees', 'lunges', 'squats', 'curls', 'deadlifts']

'squats' in exercises
```

```out
True
```

And we can pair this with `if` to make a condition statement like we did
before:

``` python
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
