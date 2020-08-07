---
type: slides
---

# Defensive programming using exceptions

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We all know that mistakes are a regular part of life. In coding, every
line of code is at risk for potential errors, so naturally, we have a
way of defending our functions against potential issues.

***Defensive programming*** is code written in such a way that if errors
do occur, they are handled in a graceful, fast and informative way.

If something goes wrong, we don’t want the code to crash - we want it to
fail gracefully.

To help soften the landing, we use something called ***Exceptions***.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Before we dive into exceptions, let’s revisit our function
`exponent_a_list()`. It work somewhat well but what happens if we try to
use it with a input string instead of a list:

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
numerical_string = "123"
exponent_a_list(numerical_string)
```

``` out
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 4, in exponent_a_list
```

We get an error that explains a little bit of what’s causing the issue
but not directly. This is where raising an `Exception` steps in to help.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Exceptions

xceptions disrupt the regular execution of our code. When we raise an
`Exception` we are forcing our own error with our own message.

If we wanted to raise an exception to solve the problem on the last
slide, we could do the following:

``` python
def exponent_a_list(numerical_list, exponent=2):

    if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
numerical_string = "123"
exponent_a_list(numerical_string)
```

``` out
Exception: You are not using a list for the numerical_list input.

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 4, in squares_a_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a closer look:

<center>

<img src='/module6/exception2.png' width="100%">

</center>

The first line of code specifies our condition - what needs to occurs to
execute the body of the condition. This code translates to *“If
`numerical_list` is not of the type `list`…”*

The second line does the complaining. We tell it to `raise` an
`Exception` with a message of the problem.

Now we get an error message that is straightforward on why our code is
failing:

``` out
Exception: You are not using a list for the numerical_list input.
```

We can agree that this message was much easier to decipher than the
original. The new message made the cause of the error much clearer to
the user making our function much more usable.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Why raise Exceptions

``` python
if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")
```

Here we checks if `numerical_list` is of the type we expect it to be, in
this case a `list`. Checking the datatype is a helpful exception since
the user can quickly correct for a simple mistake.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Another good thing to check for our function is if all the elements in
the list are not negative numbers.

We can use comprehension that we learned in the last module to check
that each element is greater or equal to 0. If not all of them are, an
`Exception` will be raised:

``` python
def exponent_a_list(numerical_list, exponent=2):
    
    for element in numerical_list: 
        if not element >= 0:
            raise Exception("The elements in numerical_list must all be positive values")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
wrong_list = [1, -2, 3.4]
exponent_a_list(wrong_list, 2)
```

``` out
Exception: The elements in numerical_list must all be positive values

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 5, in exponent_a_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Raises

We discussed the conditional part of an exception, but now let’s learn
more about the possible different types of Exceptions.

``` python
if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")
```

The exception type called `Exception` is a generic, catch-all exception
type. There are also a
href=“<https://docs.python.org/3/library/exceptions.html#Exception>”
target="\_blank"\> many more </a>specific types of exceptions; for
example, you may have encountered `ValueError` or a `TypeError` at some
point.

The exception in our previous examples is a more generic type which is
defined by the person who writes code of the function. This isn’t
all-encompassing as other Exceptions are likely better suited for the
raises we made.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a look now at the exception we wrote that checks if the input
value for numerical\_list was the correct type:

``` python
if type(numerical_list) is not list:
       raise Exception("You are not using a list for the numerical_list input.")
```

Since this is a type error, a better raised exception over `Exception`
would be `TypeError`.  
Let’s make our correction here:

``` python
def exponent_a_list(numerical_list, exponent=2):

    if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
numerical_string = "123"
exponent_a_list(numerical_string)
```

``` out
TypeError: You are not using a list for the numerical_list input.

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 4, in exponent_a_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

For the full list of exception types take a look at
<a href="https://docs.python.org/3/library/exceptions.html" target="_blank">this
resource</a>.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Exception Documentation

We’ve learned that documenting your functions with docstrings is
important so it should come to no surprise that it’s a good idea to
include details of any included exceptions in our function docstring.

Under the NumPy format, we explain our raised exception after the
“***Returns***” section. We first specify the exception type and then
an explanation of what causes the exception to be raised.

For example:

``` python
"""
Raises
------
TypeError
    If the input argument numerical_list is not of type list
"""
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

/\> <source src="/placeholder_audio.mp3" />
