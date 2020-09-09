---
type: slides
---

# Introduction to Functions

Notes: <br>

---

``` python
cereal = pd.read_csv('cereal.csv')
cereal.head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

``` python
addition = sum([1, 2, 3, 4, 5])
addition
```

```out
15
```

Notes:

Functions may feel like we are introducing something new but we have
been using them for the last 4 and a half modules.

Back in Module 1, we compared functions and methods to verbs as they
both complete actions.

`pd.read_csv()` is a function which reads in a dataframe.

And `sum()` is a function that adds all the values in a list.

---

## Functions and the DRY principle

``` python
numbers = [ 2, 3, 5]
squared = list()

squared.append(numbers[0] ** 2)
squared.append(numbers[1] ** 2)
squared.append(numbers[2] ** 2)
squared
```

```out
[4, 9, 25]
```

``` python
squared = list()
for number in numbers: 
    squared.append(number ** 2)
squared
```

```out
[4, 9, 25]
```

Notes:

In the last section, we discussed how loops helped avoid redundant code.

We wrote which created a new list containing the square of the elements
into code that was written with much less repeated code.

This helped our coding style somewhat but now we have a new problem.

What happens if we want to do the same process to multiple lists all
named differently?

---

``` python
larger_numbers = [5, 44, 55, 23, 11]
promoted_numbers = [73, 84, 95]
executive_numbers = [100, 121, 250, 103, 183, 222, 214]
```

Notes:

Perhaps I have 3 other lists that I want to do the same operations on?

---

``` python
larger_numbers_squared = list()
for number in larger_numbers: 
    larger_numbers_squared.append(number ** 2)
larger_numbers_squared
```

```out
[25, 1936, 3025, 529, 121]
```

``` python
even_larger_numbers_squared = list()
for number in promoted_numbers: 
    even_larger_numbers_squared.append(number ** 2)
even_larger_numbers_squared
```

```out
[5329, 7056, 9025]
```

``` python
extra_larger_numbers_squared = list()
for number in executive_numbers: 
    extra_larger_numbers_squared.append(number ** 2)
extra_larger_numbers_squared
```

```out
[10000, 14641, 62500, 10609, 33489, 49284, 45796]
```

Notes:

Now I will have to ***repeat*** the same code just so it applies to
these lists too.

This definitely violates the DRY principle. The question now is ***“Is
there a better way?”*** and luckily there is\!

---

``` python
squared = list()
for number in numbers: 
    squared.append(number ** 2)
squared
```

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

``` python
numbers = [ 2, 3, 5]
squares_a_list(numbers)
```

```out
[4, 9, 25]
```

Notes:

We have the ability to make our own function and use them just like how
we use functions like `pd.read_csv()` and `len()`.

We can convert the code in the last slide, into our very own function
and use it like we use Python built-in ones.

We can call our new function using the same syntax as a Python built-in
function too.

---

## Syntax

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

Let’s take a look at the how we define a function:

<center>

<img src='/module5/function-def.png' width="55%">

</center>

Notes:

Let’s take a look at the how we define a function:

  - `def` is a python keyword that tells Python that anything indented
    after this belongs to a function.

  - Next we give it a **Function name**. Like any object, we need to
    name it.
    
      - In this case, we have named our function `squares_a_list`.  
      - We cannot name it any existing function names.

  - Following our function name we specify any **Parameters/Arguments**
    that the function requires.
    
      - Python calls these “**parameters**” however, we have been
        calling these “**arguments**”.  
      - This is what the function needs as an input in order for us to
        perform some actions on an existing object.  
      - We can have multiple parameters or no parameters at all.
      - In our function, we have a single parameter named
        `numerical_list`.

  - Lastly, we end the line with a **Colon**
    
      - Just like loops and conditionals, a function required its first
        defining line to end with a colon.

---

<center>

<img src='/module5/function-rest.png' width="60%">

</center>

``` python
def not_a_great_function(numerical_list):
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    new_squared_list
```

``` python
not_a_great_function([1, 2, 3])
```

Notes:

In the body of a function, all the code is indented 4 spaces and further
indented for loops and conditions.

The `return` statement is crucial to a function for returning a desired
output.

In our previous function, a new list was returned.

If the function does not return anything then you won’t get a value to
assign to an object.

It does all the work, but never sends the result back to the code that
called it.

(See no value is returned when we call it\!)

---

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

Notes:

We can now call this function and specify each of our lists of interest
as the input argument:

  - `numbers`
  - `larger_numbers`
  - `promoted_numbers`
  - `executive_numbers`

---

``` python
numbers = [ 1, 2, 3, 4]
squares_a_list(numbers)
```

```out
[1, 4, 9, 16]
```

``` python
larger_numbers = [5, 44, 55, 23, 11]
squares_a_list(larger_numbers)
```

```out
[25, 1936, 3025, 529, 121]
```

``` python
promoted_numbers = [73, 84, 95]
squares_a_list(promoted_numbers)
```

```out
[5329, 7056, 9025]
```

``` python
executive_numbers = [100, 121, 250, 103, 183, 222, 214]
squares_a_list(executive_numbers)
```

```out
[10000, 14641, 62500, 10609, 33489, 49284, 45796]
```

Notes:

This function now is recycled on all of our lists and meets the DRY
principle.

---

``` python
numbers = [ 1, 2, 3, 4]
larger_numbers = [5, 44, 55, 23, 11]
promoted_numbers = [73, 84, 95]
executive_numbers = [100, 121, 250, 103, 183, 222, 214]
```

``` python
for list_of_numbers in [numbers, larger_numbers, promoted_numbers, executive_numbers]:
    print(squares_a_list(list_of_numbers))
```

```out
[1, 4, 9, 16]
[25, 1936, 3025, 529, 121]
[5329, 7056, 9025]
[10000, 14641, 62500, 10609, 33489, 49284, 45796]
```

Notes:

We could get even more fancy, and put all the lists into one large list
(so now you have a list of lists).

Then you could loop over the list and call the function each time.

This example leads us to our next point.

Just because we ***could*** do this, doesn’t necessarily mean we
***should***.

---

## Designing Good Functions

There is some ambiguity for how and when to design a function.

  - Should `squares_a_list()` be a function if I’m only ever using it
    once?
  - Should the loop be inside the function, or outside?

<!-- end list -->

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

Notes:

There is some ambiguity for how and when to design a function.  
For instance:

  - Should `squares_a_list()` be a function if I’m only ever using it
    once? What about Twice?
  - Should the loop be inside the function, or outside?

This comes down to personal opinion.

Some may say that the function `squares_a_list()` does a bit too much to
keep things understandable.

Designing effective functions will be discussed in Module 6.

---

# Let’s apply what we learned\!

Notes: <br>
