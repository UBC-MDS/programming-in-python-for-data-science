---
type: slides
---

# Introduction to Functions

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Functions may feel like we are introducing something new but we have
been using them for the last 4 and a half modules.

Back in Module 1, we compared functions and methods to verbs as they
both complete actions.

`pd.read_csv()` is a function which reads in a dataframe:

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

And `sum()` is a function that adds all the values in a list:

``` python
addition = sum([1, 2, 3, 4, 5])
addition
```

```out
15
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Functions and the DRY principle

In the last section, we discussed how loops helped avoid redundant
code.  
We converted this code that creates a new list containing the square of
the elements:

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

into this:

``` python
squared = list()
for number in numbers: 
    squared.append(number ** 2)
squared
```

```out
[4, 9, 25]
```

This has helped us with some repetition, but what happens if we want to
do the same process to multiple lists all named differently?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Perhaps I have 3 other lists that I want to do the same operations on?

``` python
larger_numbers = [5, 44, 55, 23, 11]
promoted_numbers = [73, 84, 95]
executive_numbers = [100, 121, 250, 103, 183, 222, 214]
```

Now I will have to ***repeat*** the same code just so it applies to
these lists too.

``` python
squared2 = list()
for number in larger_numbers: 
    squared2.append(number ** 2)
squared2
```

```out
[25, 1936, 3025, 529, 121]
```

``` python
squared3 = list()
for number in promoted_numbers: 
    squared3.append(number ** 2)
squared3
```

```out
[5329, 7056, 9025]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

And again for `executive_list`.

``` python
squared4 = list()
for number in executive_numbers: 
    squared4.append(number ** 2)
squared4
```

```out
[10000, 14641, 62500, 10609, 33489, 49284, 45796]
```

This seems to have violated the DRY principle now.

The question now is “Is there must be a better way?” and luckily there
is\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can convert this into our very own function.

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Syntax

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

Let’s take a look at the structure:

<center>

<img src='/module5/function-def.png' width="55%">

</center>

  - `def`: This is a python keyword that tells Python that anything
    indented after this belongs to a function.
  - **Function name**: Like any object, we need to give our function a
    name. In our case, we have named our function `squares_a_list`. We
    cannot name it any existing function names.
  - **Parameters/Arguments**: Python calls these parameters however, we
    have been calling these arguments. This is what the function needs
    as an input in order for it to do any actions. We can have multiple
    parameters as well. In our function, we have a single parameter
    named `numerical_list`.
  - **Colon**: Just like loops and conditionals, a function required its
    first defining line to end with a colon.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module5/function-rest.png' width="60%">

</center>

In the body a function, all the code is indented 4 spaces and further
indented for loops and conditions.  
The `return` statement is crucial to a function for returning a desired
output. Here, our function returns a new list. If the function does not
return anything then you won’t get a value to assign to an object.

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

(See no value is returned\!)

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

We can now call this function as we did with other verbs and use each of
our lists of interest as the input argument:

``` python
numbers = [ 1, 2, 3, 4]
squares_a_list(numbers)
```

```out
[1, 4, 9, 16]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can reuse this function on all our other lists as well, while still
meeting our DRY principle:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

You could get even more fancy, and put all the list of numbers into a
list (so you have a list of lists). Then you could loop over the list
and call the function each time:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Designing Good Functions

There is some ambiguity for how and when to design a function. For
instance: - Should `squares_a_list()` be a function if I’m only ever
using it once? Twice? - Should the loop be inside the function, or
outside? - Or should there be two functions, one that loops over the
other?

This comes down to personal opinion.

Some may say that the function `squares_a_list()` does a bit too much to
keep things understandable.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Mike Gelbart, co-creator of this course may prefer something like this
instead:

``` python
def squares_a_number(digit):
    return digit ** 2 

squares_a_number(12)
```

```out
144
```

We then can use a loop or comprehension to apply `squares_a_number` to
every element of a list.

``` python
numbers
```

```out
[1, 2, 3, 4]
```

Let’s try it with comprehension:

``` python
[squares_a_number(number) for number in numbers]
```

```out
[1, 4, 9, 16]
```

Designing effective functions will be discussed in the next section.

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
