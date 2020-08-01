---
type: slides
---

# Unit tests, corner cases

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last section, we learned about raising exceptions which in a lot
of cases helps the function user identify if they are using it
correctly.

But how can we be so sure that the code we wrote is doing what we want
it to?

Does our code work 100% of the time?

These questions can be answered by using something called ***`assert`
statements***.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Assert Statements

Unlike an`Exception` which force an error when the condition evaluates
to `True`, an `assert` statement cause our program to fail if the
condition evaluates to `False`.  
They can be used as sanity checks for our program.

When Python reaches an `assert` statement, it evaluates the condition to
a boolean value. If the statement is `True`, Python will continue to
run. However, if the boolean is `False`, the code stops running and an
error message is printed.

Let’s take a look at one:

``` python
assert 1 == 2 , "1 is not equal to 2."
print('Will this line execute?')
```

``` out
AssertionError: 1 is not equal to 2.

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

<center>

<img src='/module6/assert.png' width="75%">

</center>

``` out
AssertionError: 1 is not equal to 2.

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Here we have the keyword `assert` that checks if `1==2`. Since the
boolean is `False`, the message beside the condition `" 1 is not equal
to 2."` is outputted.

Let’s take a look at an example where the boolean is `True`:

``` python
assert 1 == 1 , "1 is not equal to 2."
print('Will this line execute?')
```

```out
Will this line execute?
```

Since the `assert` statement results in a `True` values, Python
continues to run and the next line of code is executed.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Why?

Where do assert statements come in handy?

Up to this point, we have been creating functions and only after we have
written them, we’ve tested if they work. Instead, programmers often use
a different approach. We recommend writing tests using `assert`
statements before our actual function. This is called Test-Driven
Development (TDD).

This may seem a little counter-intuitive, but we’re creating the
expectations of our function before the actual function code.

Often we have an idea of what our function should be able to do, and
what the function operation output is expected. If we write our tests
before the function it helps understand exactly what code we need to
write and it avoids encountering large time-consuming bugs down the
line.

<center>

<img src='/module6/why.png' width="75%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What to test?

So, what kind of tests do we want? We want to keep these tests simple -
things that we know are true or could be easily calculated by hand.  
For example, let’s look at our `exponent_a_list()` function:

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

Easy cases for this function would be lists containing numbers that we
can easily square, or cube.

For example, we expect the square output of `[1, 2, 4, 7]` to be
`[1, 4, 16, 49]`.  
The test for this would look like this:

``` python
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
```

It’s also good to do multiple test to for different list sizes as well
as different values for both inputs. Let’s make another test for
`exponent` = `3`. Again, we use numbers that we know the cube of.

``` python
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## False Positives

Just because all our tests pass, this does not mean our program is
necessarily correct. It’s common that our tests can pass but our code
contains errors.

``` python
def bad_function(numerical_list, exponent=2):
    new_exponent_list = list()
    for number in numerical_list:
        if len(numerical_list) >2:
            new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

``` python
assert bad_function([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert bad_function([2, 1, 3], 3) == [8, 1, 27], "incorrect output for exponent = 3"
```

Here, it looks like our tests pass\! But let’s try another test:

``` python
assert bad_function([5, 10], 2) == [1, 4, 16, 49], "incorrect output for list size 2"
```

``` out
AssertionError: incorrect output for list size 2

Detailed traceback: 
  File "<string>", line 1, in <module>
```

How do we deal with it?

Write a lot of tests and don’t be overconfident, even after writing a
lot of tests\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Corner Cases

Other tests that are good to include are tests that check ***corner
cases***. A corner case is an input that is reasonable but a bit unusual
and may trip up our code.

For example, taking the square of an empty list, or taking a 0 or
negative value exponent. Often it is desirable to add test cases to
address corner cases.

``` python
assert exponent_a_list([], 3) == [], "incorrect output for empty list"
assert exponent_a_list([0, 1, 3], 0) == [1, 1, 1], "incorrect output for empty list"
assert exponent_a_list([1, 2], -2) == [1, 0.25], "incorrect output for a negative exponent"
```

These corner cases pass, but let’s try another one:

``` python
assert exponent_a_list([0, 2, 4], -1) == [1, 0.5, 0.25], "incorrect output for a negative exponent"
```

``` out
ZeroDivisionError: 0.0 cannot be raised to a negative power

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 5, in exponent_a_list
```

Since 0 to the power of -1 is equal to 1/0, the correct answer is
infinity. In this case, we would need to correct the code in our
function to handle this weird case or inform the user using `Exceptions`
that our function cannot accept lists containing 0 if the exponent is
negative.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Testing Functions that Work with Data

Often, we will be making functions that work on data. In these
situations, we make some testing data also known as ***“helper”*** data.
Helper data is small in size and that we can easily work with and
calculate our functions return value from easily.

Helper data can be made from scratch using functions such as
`pd.DataFrame()` or `pd.DataFrame.from_dict()` which we learned about in
module 4. You can also upload a very small slice of an existing
dataframe.

For example, perhaps we want to write a function called `column_stats`
that returns some summary statistics in form of a dictionary. The
function below is something we might have envisioned (Note that at this
point it will not have been written out and it would just be an idea)

``` python
def column_stats(df, column):
   stats_dict = {'max': df[column].max(),
                 'min': df[column].min(),
                 'mean': round(df[column].mean()),
                 'range': df[column].max() - df[column].min()}
   return stats_dict
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We need to make my helper data so that we can easily calculate the max,
min, range, and mean easily on any columns. The values we chose in our
columns are easy to calculate the statistics from. The dataframe also
has a small dimension to keep the calculations simple.

``` python
data = { 'name': ['Cherry', 'Oak', 'Willow', 'Fir', 'Oak'], 
         'height': [15, 20, 10, 5, 10], 
         'diameter': [2, 5, 3, 10, 5], 
         'flowering': [True, False, True, False, False]}
         
forest = pd.DataFrame.from_dict(data)
forest
```

```out
     name  height  diameter  flowering
0  Cherry      15         2       True
1     Oak      20         5      False
2  Willow      10         3       True
3     Fir       5        10      False
4     Oak      10         5      False
```

The tests we write for the function `column_stats()` are now easy to
calculate:

``` python
assert column_stats(forest, 'height') == {'max': 20, 'min': 5, 'mean': 12.0, 'range': 15}
assert column_stats(forest, 'diameter') == {'max': 10, 'min': 2, 'mean': 5.0, 'range': 8}
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Systematic Approach

We use a **systematic approach** to design our function using a general
set of steps to follow when writing programs.

The approach we recommend includes 5 steps:

***1. Write the function stub: a function that does nothing but accepts
all input parameters and return the correct datatype.***

This means we are writing the skeleton of a function. We include the
line that defines the function with the input arguments and the return
statement returning the object with the desired data type.

Using our `exponent_a_list()` function as an example:

``` python
def exponent_a_list(numerical_list, exponent=2):
    return new_exponent_list
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

***2. Write tests to satisfy the design specifications.***

This is where our `assert` statements come in. We write tests that we
want our function to pass. In our `exponent_a_list()` example we expect
that our function will take in a list and an optional argument named
`exponent` and then returns a list with the exponential value of each
element of the input list.

``` python
def exponent_a_list(numerical_list, exponent=2):
    return new_exponent_list
    
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

``` out
NameError: name 'new_exponent_list' is not defined

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 2, in exponent_a_list
```

Here we can see our code fails since we have not function code yet\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

***3. Outline the program with pseudo-code.***

Pseudocode is an informal but high-level description of the code and
operations that we wish to implement. In this step, we are essentially
writing the steps that we anticipate needing to complete our function:

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    # loop through all the elements in numerical_list
    # For each element ** exponent
    # append it to the new_exponent_list list 
    
    return new_exponent_list
    
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

``` out
AssertionError: exponent_a_list, does not result in expected output when exponent = 2

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

***4. Write code and test frequently.***

Here is where we construct a function that no longer returns any errors
from our `assert` statements.

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
    
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

***5. Write documentation.***  
Finally, finish our function with a docstring.

``` python
def exponent_a_list(numerical_list, exponent=2):
    """ Creates a new list containing specified exponential values of the input list. 
    
    Parameters
    ----------
    numerical_list : list
        The list from which to calculate exponential values from
    exponent : int or float, optional
        The exponent value (the default is 2, which implies the square).
    
    Returns
    -------
    new_exponent_list : list
        A new list containing the exponential value specified of each of
        the elements from the input list 
        
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

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
