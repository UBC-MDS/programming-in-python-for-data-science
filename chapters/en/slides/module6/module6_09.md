---
type: slides
---

# Function docstrings

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Functions can get very complicated, so it’s not always obvious what they
do just from looking at the name, arguments, or code. Therefore, people
like to explain what the function does. The standard format for doing
this is called a **docstring**. A **docstring** is a literal string that
comes directly after the function `def` and documents the function’s
purpose and usage

Writing a docstring for your functions informs on what your code does so
that collaborators (and you in 6 months’ time) are not struggling to
decipher and reuse your code.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last section we had our function `squares_a_list()`:

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

Although our function name is quite descriptive, it could mean various
things. How do we know what data type it takes in and returns?

Having documentation for it can be useful in answering these questions.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## NumPy Format

There are several styles of docstrings; the one we’ll use is called the
**NumPy** style.  
Writing documentation for `squares_a_list()` using the **NumPy style**
takes the following format:

``` python
def squares_a_list(numerical_list):
    """
    Squared every element in a list.
    
    Parameters
    ----------
    numerical_list : list
        The list from which to calculate squared values 
        
    Returns
    -------
    list
        A new list containing the squared value of each of the elements from the input list 
        
    Examples
    --------
    >>> squares_a_list([1, 2, 3, 4])
    [1, 4, 9, 16]
    """
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

All docstrings, not just the Numpy formatted ones, are contained within
3 sets of quotations`"""`. We discussed in module 4 that this was one of
the ways to implement string values:

``` python
string1 = """ This is a string"""
type(string1)
```

```out
<class 'str'>
```

Adding this additional string to our function has no effect on our code
and the sole purpose of the docstring is for human consumption.

The NumPy format includes 4 sections:  
\- **A brief description of the function**  
\- Explaining the input **Parameters**  
\- What the function **Returns**  
\- **Examples**

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Below is the general form of the NumPy docstring (reproduced from the
SciPy/NumPy docs):

``` python
def function_name(param1, param2):
    """The first line is a short description of the function.
    
    A paragraph describing in a bit more detail what the function
    does and what algorithms it uses and common use cases.
    
    Parameters
    ----------
    param1 : datatype
        A description of param1.
    param2 : datatype
        A longer description because maybe this requires
        more explanation and we can use several lines.
    
    Returns
    -------
    datatype
        A description of the output, datatypes and behaviours.
        Describe special cases and anything the user needs to know 
        to use the function.
    
    Examples
    --------
    >>> function_name(3, 8, -5)
    2.0
    """
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Default Arguments

If our function contains default arguments, we need to communicate this
in our docstring. Using `exponent_a_list()`, a function from the
previous section as an example, we include an *optional* note in the
parameter definition and an explanation of the default value in the
**parameter** description.

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
        
    Examples
    --------
    >>> squares_a_list([1, 2, 3, 4])
    [1, 4, 9, 16]
    """

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

## How to read a docstring

Ok great\! Now that we’ve written and explained our functions with a
standardized format, we can read it in our file easily but what if our
function is located in a different file? How can we learn what it does,
when reading our code?

We learned in the first assignment that we can learn more about built-in
functions using:

``` python
?function_name
```

For example, if we want the docstring for the function `len()`:

``` python
?len
```

``` out
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The same thing can be done to get the documentation of functions that we
have defined. Getting the documentation for our function
`squares_a_list()` is as easy as:

``` python
?squares_a_list
```

``` out
Signature: squares_a_list(numerical_list)
Docstring:
Creates a new list containing the square values of the input list. 

Parameters
----------
numerical_list : list
    The list from which to calculate squared values 
    
Returns
-------
list
    A new list containing the squared value of each of the elements from the input list 
    
Examples
--------
>>> squares_a_list([1, 2, 3, 4])
[1, 4, 9, 16]
File:      ~/<ipython-input-1-7e6e50ac7556>
Type:      function
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

\<source
