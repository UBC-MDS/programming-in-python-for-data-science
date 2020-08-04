---
type: slides
---

# Function Arguments

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we were introduced to functions in Module 5, arguments are
something we implemented into our functions without much discussion and
it’s time now that we address them.

Arguments play a paramont role when it comes to adhereing to the DRY
principle as well as adding flexibility to your code.

Let’s bring back the function we made named `squares_a_list()`.

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

The reason we made this function in the first place was to DRY out our
code and avoid repeating the same `for` loop for any additional list we
wished to operate on.

What happens now if we no longer wanted to square a number but calculate
a specified exponential of each element, perhaps `$$n^3$$`, or `$$n^4$$`
? Would we need a new function?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We could make a similar new function for cubing the numbers:

``` python
def cubes_a_list(numerical_list):
    new_cubed_list = list()
    
    for number in numerical_list:
        new_cubed_list.append(number ** 3)
    
    return new_cubed_list
```

But this feels repetitive.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

A better solution which adheres to the DRY principle, is to tweak our
original function but add an additional argument.  
Take a look at `exponent_a_list()` which now takes 2 arguments; the
original `numerical_list`, and now a new argument named `exponent`.

``` python
def exponent_a_list(numerical_list, exponent):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

``` python
numbers = [2, 3, 5]
exponent_a_list(numbers, 3)
```

```out
[8, 27, 125]
```

This gives us a choice of the exponent. We could use the same function
now for any exponent we want instead of making a new function for each.

``` python
exponent_a_list(numbers, 5)
```

```out
[32, 243, 3125]
```

This makes sense to do if we foresee needing this versatility, else the
additional argument isn’t necessary.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Default Values for Arguments

Python allows for optional arguments that take something call default
valuea. A default argument value allows a function to have an argument
however, if it is not specified when the function is called, a
pre-selected option is adopted.  
For example, in our `exponent_a_list()` function can use a default
argument value for `exponent`.

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

Now if we do not specify the exponent argument when we call our
function, it defaults to an exponent of 2:

``` python
numbers = [2, 3, 5]
exponent_a_list(numbers)
```

```out
[4, 9, 25]
```

However, we still get the convenience of changing the argument to
something else if we need to:

``` python
exponent_a_list(numbers, 5)
```

```out
[32, 243, 3125]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Functions can have any number of arguments and any number of optional
arguments but when we must be cafeful with order arguments they are
defined and called.

When we defined our arguments in a function, all arguments with default
values need to be defined ***after*** required arguments. If any
required arguments follow any arguments with default values, an error
will occur.  
Let’s take our original function and re-order it so the optional
`exponent` argument is defined first. We will see Python throw an error:

``` python
def exponent_a_list(exponent=2, numerical_list):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

``` out
Error: non-default argument follows default argument (<string>, line 1)
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Argument Ordering

Up to this point we have been calling functions with multiple arguments
in a single way. When we call our function, we have been ordering the
arguments in the order the function defined them in. So in
`exponent_a_list()`, the argument `numerical_list` is defined first,
followed by the argument `exponent`.

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

Naturally we have been calling our function with the arguments in this
order as well:

``` python
numbers = [2, 3, 5]
exponent_a_list(numbers, 5)
```

```out
[32, 243, 3125]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s see what happened we we switch up the arguments ordering when we
call `exponent_a_list()` and call the `exponent` value first followed by
the `numerical_list`:

``` python

exponent_a_list(5,  [2, 3, 5])
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'int' object is not iterable

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 4, in exponent_a_list
```

Our function doesn’t recognize the input arguments and an error occurs.

To get around this error, we can instead specify which arguments are
which when we call the argument:

``` python
exponent_a_list(exponent=5,  numerical_list=[2, 3, 5])
```

```out
[32, 243, 3125]
```

This order now executes without an error.

The rule of thumb to remember here is if you are going to call a
function where the arguments are in a different order from how they were
defined, you need to assign the argument name to the value when you call
the function.

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