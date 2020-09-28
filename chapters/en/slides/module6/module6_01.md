---
type: slides
---

# DRY revisited and function fundamentals

Notes:

<br>

---

``` python
numbers = [2, 3, 5]
squared = list()
for number in numbers: 
    squared.append(number ** 2)
squared
```

```out
[4, 9, 25]
```

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
squares_a_list(numbers)
```

```out
[4, 9, 25]
```

Notes:

In the last module, we were introduced to the DRY principle and how
creating functions helps comply with it.

Let’s do a little bit of a recap.

**DRY** stands for Don’t Repeat Yourself.

We can avoid writing repetitive code by creating a function that takes
in arguments, performs some operations, and returns the results.

The example in Module 5 converted code that creates a list of squared
elements from an existing list of numbers into a function.

---

``` python
larger_numbers = [5, 44, 55, 23, 11]
promoted_numbers = [73, 84, 95]
executive_numbers = [100, 121, 250, 103, 183, 222, 214]
```

``` python
squares_a_list(larger_numbers)
```

```out
[25, 1936, 3025, 529, 121]
```

``` python
squares_a_list(promoted_numbers)
```

```out
[5329, 7056, 9025]
```

``` python
squares_a_list(executive_numbers)
```

```out
[10000, 14641, 62500, 10609, 33489, 49284, 45796]
```

Notes:

This function gave us the ability to do the same operation for multiple
lists without having to rewrite any code and just calling the function.

---

## Scoping

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
        print(new_squared_list)
    return new_squared_list
```

``` python
squares_a_list(numbers)
```

```out
[4]
[4, 9]
[4, 9, 25]
[4, 9, 25]
```

``` python
new_squared_list
```

``` out
NameError: name 'new_squared_list' is not defined

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

It’s important to know what exactly is going on inside and outside of a
function.

In our function `squares_a_list()` we saw that we created a variable
named `new_squared_list`.

We can print this variable and watch all the elements be appended to it
as we loop through the input list.

But what happens if we try and print this variable outside of the
function?

Yikes\! Where did `new_squared_list` go?

It doesn’t seem to exist\! That’s not entirely true.

In Python, `new_squared_list` is something we call a ***local
variable***.

Local variables are any objects that have been created within a function
and only exist inside the function where they are made.

Code within a function is described as a **local environment**.

Since we called `new_squared_list` outside of the function’s body,
Python fails to recognize it.

---

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
        print(new_squared_list)
    return new_squared_list
```

``` python
a_new_variable = "Peek-a-boo"
a_new_variable
```

```out
'Peek-a-boo'
```

Notes:

Let’s compare that with the variable `a_new_variable`.

`a_new_variable` is created outside of a function in what we call our
***global environment***, and therefore Python recognizes it as a
***global variable***.

---

## Global and Local Variables

``` python
def squares_a_list(numerical_list):

    print(a_new_variable)
    
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
squares_a_list([12, 5, 7, 99999])
```

```out
Peek-a-boo
[144, 25, 49, 9999800001]
```

Notes:

Global variables differ from local variables as they are not only
recognized outside of any function but also recognized inside functions.

Let’s take a look at what happens when we add `a_new_variable`, which is
a global variable,e and refer to it in the `squares_a_list` function.

The function recognizes the global variable\!

It’s important to note that, although functions recognize global
variables, it’s not good practice to have functions reference objects
outside of it.

We will learn more about this later in the module.

---

<br> <br> <br>

<center>

<img src='/module6/starbucks.png' width="100%" alt="404 image">

</center>

[Attribution - Starbucks](https://unsplash.com/photos/42ui88Qrxhw)

[Attribution - 49th and
Parallel](https://unsplash.com/photos/42ui88Qrxhw)

Notes:

I’m going to make an analogy comparing coffee stores to variables.

**Starbucks Coffee** is a ***globally*** recognized brand across the
world and is available in 70 different countries.

I can purchase a coffee from Starbucks in Vancouver (my local city), and
if I were to travel across the world to Sydney, Australia, I would still
be able to purchase a coffee from Starbucks there.

Starbucks Coffee is similar to a global variable as it is accessible and
recognized in both its local (Vancouver) and global environments.

**49th Parallel** is a ***local*** Vancouver coffee store.

Many people from Vancouver recognize it; however, purchasing a coffee
from 49th Parallel outside of Vancouver would be impossible as it is not
accessible past the City of Vancouver.

Just like Starbucks Coffee, global variables are recognized and
accessible in both their global and local environments, whereas local
variables like the coffee store 49th Parallel are only recognized and
accessible in the local environment it was created in.

---

## When things get tricky

``` python
a_new_variable = "Peek-a-boo"
```

``` python
def squares_a_list(numerical_list):
    a_new_variable = "Ta-Da!"
    print(a_new_variable)
    
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
squares_a_list([1, 2])
```

```out
Ta-Da!
[1, 4]
```

Notes:

Things can get unclear when we have variables that are named the same
way but come from two different environments.

What happens when 2 different objects share the same name, where one was
defined inside the function and the other in the global environment?

For instance, let’s say we defined a variable `a_new_variable` in our
global environment, and we’ve made a variable in a local environment
with the same name `a_new_variable` but with different values within our
`squares_a_list` function.

We can see that the locally created `a_new_variable` variable was
printed instead of the global object with the same name.

---

``` python
def squares_a_list(numerical_list):
    a_new_variable = "Ta-Da!"
    print(a_new_variable)
    
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
squares_a_list([1, 2])
a_new_variable
```

``` out
Ta-Da!
[1, 4]
'Peek-a-boo'
```

Notes:

What about if we output `a_new_variable` right after.

Our function prints the locally defined `a_new_variable`, and the global
environment prints the globally defined `a_new_variable`.

---

``` python
def squares_a_list(numerical_list, a_new_variable):
    print(a_new_variable)
    
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
a_new_variable = "Peek-a-boo"
squares_a_list([1,2], "BAM!")
```

```out
BAM!
[1, 4]
```

Notes:

What if `a_new_variable` was an argument?

Given a global variable `a_new_variable = "Peek-a-boo"`, what value will
the function print if we assign a value of `"BAM!"` to the input
argument `a_new_variable`?

Here we can see that the function uses the input argument value instead
of the global variable value.

---

## Modifying global variables

``` python
global_list = [50, 51, 52]
```

``` python
def squares_a_list(numerical_list):
    global_list.append(99)
    print("print global_list:", global_list)
    
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    return new_squared_list
```

``` python
squares_a_list([1, 2])
```

```out
print global_list: [50, 51, 52, 99]
[1, 4]
```

``` python
global_list
```

```out
[50, 51, 52, 99]
```

Notes:

So global variables are accessible inside functions - but what about
modifying them?

Let’s take a list that we define in our global environment called
`global_list` and add `99` to the list in the local environment.

The list that we defined globally was able to be modified inside the
function and have the changes reflected back in the global environment\!

What is going on?

Modifying objects like this within a function without returning them is
called a function **side effect**.

---

## Function Side Effects

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

  - `.drop()`
  - `.assign()`
  - `.sort_values()`
  - `.rename()`

Notes:

For this next concept, we are going to bring back our trusty cereal
dataframe.

Since the beginning of this course, we have been using verbs such as;

  - `.drop()`
  - `.assign()`
  - `.sort_values()`
  - `.rename()`

Where we modify a dataframe and save the modification as a new dataframe
object.

---

``` python
cereal_dropped = cereal.drop(columns = ['sugars','potass','vitamins', 'shelf', 'weight', 'cups'])
cereal_dropped.head(2)
```

```out
                name mfr  type  calories  protein  fat  sodium  fiber  carbo     rating
0          100% Bran   N  Cold        70        4    1     130   10.0    5.0  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0  33.983679
```

``` python
cereal.head(2)
```

```out
                name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0          100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
```

``` python
cereal.drop(columns = ['sugars','potass','vitamins', 'shelf', 'weight', 'cups'], inplace=True)
```

``` python
cereal.head(2)
```

```out
                name mfr  type  calories  protein  fat  sodium  fiber  carbo     rating
0          100% Bran   N  Cold        70        4    1     130   10.0    5.0  68.402973
1  100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0  33.983679
```

Notes:

For example, when we have been dropping columns from a dataframe, we
have been saving the changes with the assignment operator to a new
object.

In this example, we drop columns from `sugars` to `cups` and assign this
modified dataframe with the dropped columns to the object named
`cereal_dropped`.

If we look at the original `cereal` dataframe, we can see it was
unaffected by this transformation.

Many of the verbs that we use for our transformations, such as the ones
we mentioned on the previous slide, have an argument called `inplace`.

The `inplace` argument accepts a Boolean value where the dataframe
object is modified directly without the need to save the changes to an
object with the assignment operation. That means we can skip the part of
making a new object with the `=` sign.

Let’s try and drop the same columns as before but now using
`inplace=True`.

This time, nothing is returned when we execute this code; however, if we
look at the `cereal` dataframe now, we can see that it’s been altered,
and the columns have been dropped.

This transformation of the dataframe object is a **side effect** of the
function.

A side effect is when a function produces changes to global variables
outside the environment it was created, this means a function has an
observable effect besides the returning value.

It’s important to include that although `inplace` exists, there is a
reason we haven’t taught it, and it’s because we don’t recommend using
it. Overriding the object by saving it with the same object name is the
preferred coding technique.

---

``` python
cereal.to_csv('cereal.csv')
```

``` python
regular_list = [7, 8, 2020]
regular_list
```

```out
[7, 8, 2020]
```

``` python
regular_list.append(3)
```

``` python
regular_list
```

```out
[7, 8, 2020, 3]
```

Notes:

Although this appears to be new vocabulary, side effects have been
present since the beginning of this course, starting with `pd.to_csv()`.

`pd.to_csv()` is a function that we saw in module 1, that didn’t return
anything after we executed it but still produced a **side effect** of a
newly saved csv file on our computer.

Another example that we’ve seen when working with lists is the verb
`.append()`.

When we execute the code `.append(3)`, on our object `regular_list`,
nothing is returned from the function, and we have not used to
assignment operator to save any transformation to the list, however,
when we inspect `regular_list`, we can see that it has been modified and
included the new element `3`.

This would be another example of a function with a side effect.

The list was created in the global environment, but modified in
`.append()`’s local environment.

Side effects seem like fun, but they can be extremely problematic when
trying to debug (fix) your code.

When writing functions, it’s usually a good idea to avoid side effects.

If objects need to be modified, best practice is to modify them in the
environment they originated in.

---

## Side Effect Documentation

  - If your functions have side-effects, they should be documented.

Notes:

Although side effects are not recommended, there are cases where either
we must have side-effects in our functions, or there is no way to avoid
it. In these cases, it is extremely important that we document it.

This leads to the next question of *How*? Good news - the answer is
coming later on in this module\!

---

# Let’s apply what we learned\!

Notes:

<br>
