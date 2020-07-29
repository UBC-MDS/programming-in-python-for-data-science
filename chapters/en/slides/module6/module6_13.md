---
type: slides
---

# Defensive programming via exceptions

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We all know that mistakes are a regular part of life In coding, since
every line of code is at risk for potential errors, programmers now have
a method that is structured around the assumption that errors and bugs
will occur.

***Defensive programming*** is code written in such a way that if errors
do occur, they are handled in a graceful, fast and informative way.

If something goes wrong, we don’t want the code to crash - we want it to
fail gracefully.

To help with a softer landing, we use something called `Exceptions`.

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

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 4, in exponent_a_list
```

We get an error that explains a little bit of what’s causing the issue
but not directly. This is where raising an exception steps in to help.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Exception

Exceptions are keywords that disrupt the regular execution. So when we
raise an exception we are forcing our own error with our own information
to be executed if the condition is met.

If we wanted to raise an except to solve the problem on the last slide,
we could do the following:

``` python
def exponent_a_list(numerical_list, exponent=2):

    if not isinstance(numerical_list, list):
        raise Exception("Sorry, but you are not using a list for input like we asked.")

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
Exception: Sorry, but you are not using a list as an input like we asked.

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

``` python
if not isinstance(numerical_list, list):
        raise Exception("Sorry, but you are not using a list for input like we asked.")
```

The first line of code specifies our condition - what needs to occurs to
execute the body of the condition. This code translates to *“If
`numerical_list` is not of the instance type `int`…”*

The second line does the complaining, we tell it to `raise` it’s an
***Exception*** with a message of the problem.

Now we get an error message that is straight forward on why our code is
failing:

``` out
Exception: Sorry, but you are not using a list as an input like we asked.
```

We can agree that this message was much easier to decipher than the
original and the new message made the cause of the error much clearer to
the user. This, made our function much more usable.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Why raise exceptions

``` python
if not isinstance(numerical_list, list):
        raise Exception("Sorry, but you are not using a list for input like we asked.")
```

In the example we used a function called `isinstance()` which checks if
the first argument is of the same data type as the second argument.

Checking the datatype is a helpful exception since the user can quickly
correct for a simple mistake.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can also check if the input arguments chosen by the user make sense
with operations that will be conducting. For instance perhaps our
function is strict on accepting values for `exponent` that are \>0. We
can raise and exception if the user attempts to use anything else:

``` python
def exponent_a_list(numerical_list, exponent=2):
    
    if exponent <0:
        raise Exception("This function must have values for exponent larger than 0")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
numerical_list = [1, 2, 3]
exponent_a_list(numerical_list, -2)
```

``` out
Exception: This function must have values for exponent larger than 0

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

Another good thing to check for our function is if all the elements in
the list are of data type `int`:

We can use comprehension that we learned in the last module to check
that each element is of type `int`. If not all of them are, an exception
will be raised:

``` python
def exponent_a_list(numerical_list, exponent=2):
    
    if not all(type(element) is int for element in numerical_list):
        raise Exception("The elements in numerical_list must all be of type int")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
wrong_list = [1, 2, 3.4]
exponent_a_list(wrong_list, 2)
```

``` out
Exception: The elements in numerical_list must all be of type int

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

Checking the input values in functions in a good way to keep the user
informed and solve their problem quickly.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Raises

We discussed the conditional part of an exception, but now let’s learn
more about the possible different types of exceptions.

``` python
if exponent <0:
    raise Exception("This function must have values for exponent larger than 0")
```

There are many different types of exceptions and using `Exception` is
just one of
<a href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank">many</a>

`Exception` is a more generic message which is defined by the person who
writes code of the function.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The exception we wrote checking if `exponent` is greater than 0 is a
good example of a user defined exception where using `Exception` is
appropriate since Python is technically capable of doing this outside of
our function:

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
exponent_a_list( [1, 2, 4], -2)
```

```out
[1.0, 0.25, 0.0625]
```

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
if not isinstance(numerical_list, list):
   raise Exception("Sorry, but you are not using a list for input like we asked.")
```

Since this is a type error, a more suited Exception raise would be
`TypeError`.  
Let’s make our correction here:

``` python
def exponent_a_list(numerical_list, exponent=2):

    if not isinstance(numerical_list, list):
        raise TypeError("Sorry, but you are not using a list for input like we asked.")

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
TypeError: Sorry, but you are not using a list for input like we asked.

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

Let’s make the same change for the assertion that checks that each
element is of type `int` in the input list `numerical_list`:

``` python
def exponent_a_list(numerical_list, exponent=2):
    
    if not all(type(element) is int for element in numerical_list):
        raise TypeError("The elements in numerical_list must all be of type int")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

For the full list of exception types take a look at the ressource
<a href="https://docs.python.org/3/library/exceptions.html#Exception" target="_blank">here</a>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Exception Documentatio

We’ve learned that documenting your functions with docstrings is
important so it should come to no surprise that it’s a good idea to
include details of the exceptions we write in our function docstring.

Under the NumPy format, We explain our raised exception after the
“***Returns***” section. We first specify the exception type and then
an explanation of what causes the exception to be raised.

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

Our function would look like this:

``` python
def exponent_a_list(numerical_list, exponent=2):
    """
    Creates a new list containing specified exponential values of the input list. 
    
    Parameters
    ----------
    numerical_list : list
        The list from which to calculate exponential values from
    exponent : int or float, optional
        The exponent value (the default is 2, which implies the square).
        
    Returns
    -------
    new_exponent_list : list
        A new list containing the exponential value specified of each 
        of the elements from the input list 
        
    Raises
    ------
    TypeError
        If the input argument numerical_list is not of type list
        
    Examples
    --------
    >>> squares_a_list([1, 2, 3, 4])
    [1, 4, 9, 16]
    """

    if not isinstance(numerical_list, list):
        raise TypeError("Sorry, but you are not using a list for input like we asked.")

    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
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
