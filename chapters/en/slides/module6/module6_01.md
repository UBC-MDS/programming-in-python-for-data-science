---
type: slides
---

# DRY revisited and function fundamentals

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last module, we were introduced to the DRY principle and how
creating functions helps comply with it. Let’s do a little bit of a
recap.

**DRY** stands for Don’t Repeat Yourself. We can avoid writing
repetitive code by creating a function that takes in arguments, performs
some operations and returns the results. In the last module, we
converted our code that creates a list of squared elements from an
existing list of numbers, into a function:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

This gave us the ability to do the same operation for multiple lists
without having to rewrite any code and just calling the function:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Scoping

It’s important to know what exactly is going on inside and outside of a
function. In our function `squares_a_list()` we saw that we created a
variable named `new_squared_list`. We can print this variable and watch
all the elements append to it as we loop through the input list:

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

But what happens if we try and print this variable outside of the
function?

``` python
new_squared_list
```

``` out
NameError: name 'new_squared_list' is not defined

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

## Global and Local Variables

``` python
new_squared_list
```

``` out
NameError: name 'new_squared_list' is not defined

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Yikes\! Where did `new_squared_list` go? It doesn’t seem to exist\!
That’s not entirely true.

In Python, `new_squared_list` is something we call a ***local
variable***. Local variables are any objects that have been created
within a function and only exist and accessible in the function where it
was made. Code within a function is described as a **local
environment**.

Since we called `new_squared_list` outside of the function’s body,
Python fails to recognize it.

Let’s compare that with the variable `a_new_variable`.

``` python
a_new_variable = "Peek-a-boo"
```

`a_new_variable` is created outside of a function in what we call our
***global environment*** and therefore Python recognizes it as a
***global variable***.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Global variables differ from local variables as they are not only
recognized outside of any function but also recognized inside
functions.  
Let’s take a look what happens when we add `a_new_variable` into the
`squares_a_list` function:

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

The function recognizes the global variable\! It’s important to note
that, although functions recognize global variables, it’s not good
practice to have functions reference objects outside of it. We will
learn more on this later in the module.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

I’m going to make an analogy comparing coffee stores to variables.

  - **Starbucks Coffee** is a ***globally*** recognized brand across the
    world and is available in 70 different countries. I can purchase a
    coffee from Starbucks in Vancouver (my local city) and if I were to
    travel across the world to Sydney, Australia, I would still be able
    to purchase a coffee from Starbucks there. Stackbucks Coffee is
    similar to a global variable as it is accessible and recognized in
    both its local (Vancouver) and global environments.
  - **49th Parallel** is a ***local*** Vancouver coffee store. Many
    people from Vancouver recognize it, however, purchasing a coffee
    from 49th Parallel outside of Vancouver would be impossible as it is
    not accessible past the City of Vancouver.

Just like Starbucks Coffee, global variables are recognized and
accessible in both their global and local environments, whereas local
variables like the coffee store 49th Parallel are only recognized and
accessible in the local environment it was created in.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## When things get tricky

Things can get unclear when we have variables that are named the same
way but come from two different environments. what happens when 2
different objects share the same name, where one was defined inside the
function and the other in the global environment?

For instance, let’s say we defined a variable `a_new_variable` in our
global environment:

``` python
a_new_variable = "Peek-a-boo"
```

And I made a variable in a local environment with the same name
`a_new_variable` but with different values within our `squares_a_list`
function:

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

We can see that the locally created `a_new_variable` variable was
printed instead of the global object with the same name.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What about if we output `a_new_variable` right after:

``` python
squares_a_list([1, 2])
```

```out
Ta-Da!
[1, 4]
```

``` python
a_new_variable
```

```out
'Peek-a-boo'
```

Our function prints the locally defined `a_new_variable`, and the global
environment prints the globally defined `a_new_variable`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Modifying global variables

So global variables are accessible inside functions but what about
modifying them?

Let’s take a list that we define in our global environment called
`global_list` and add `99` to the list in the local environment.

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

The list that we defined globally was able to be modified inside the
function and have the changes reflected back in the global environment\!
What is going on?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

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
print global_list: [50, 51, 52, 99, 99]
[1, 4]
```

``` python
global_list
```

```out
[50, 51, 52, 99, 99]
```

Modifying objects like this within a function without returning them is
called a function **side effect**.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Function Side Effects

Although this appears to be new vocabulary, side effects have been
present since the beginning of this course starting with `pd.to_csv()`.

Remember our cereal dataframe? Well we’ve edited it and now want to save
it to our computer. We can use `pd.to_csv()` like this:

``` python
cereal.to_csv('cereal.csv')
```

When we execute this code, nothing is returned but we get a **side
effect** of a newly saved csv file on our computer.

Printing anything in a function is also considered a function side
effect. Even though this operation doesn’t affect any of your global
variables, it does bring information from within the function to the
global environment.

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    for number in numerical_list:
        new_squared_list.append(number ** 2)
        print(new_squared_list)
    return new_squared_list
```

``` python
numbers = [2, 3, 5]
squares_a_list(numbers)
```

```out
[4]
[4, 9]
[4, 9, 25]
[4, 9, 25]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The same can be said anytime we modify a dataframe within a function
without returning anything. Let’s say we have the following function
that does conditional value replacement on a specified column.  
It takes as inputs:

  - The dataframe  
  - the column we want to edit  
  - the value that we wish to replace  
  - the new value we wish to use as a replacement

And returns nothing.

``` python
def value_change(data, column, old_value, new_value):
    data.loc[data[column] == old_value, column] = new_value
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Using a slice of our cereal dataset:

``` python
cereal.head()
```

```out
                        name mfr  type  calories
0                  100% Bran   N  Cold        70
1          100% Natural Bran   Q  Cold       120
2                   All-Bran   K  Cold        70
3  All-Bran with Extra Fiber   K  Cold        50
4             Almond Delight   R  Cold       110
```

Let’s change all the values that have `type` as `Cold` to `Unheated`
using the `value_change` function:

``` python
value_change(cereal, 'type', 'Cold', 'Unheated')
```

We can see that our function has no `return` statement and thus the code
above produces no output but let’s look at what happens when we look at
the cereal dataset after calling the function on it.

``` python
cereal.head()
```

```out
                        name mfr      type  calories
0                  100% Bran   N  Unheated        70
1          100% Natural Bran   Q  Unheated       120
2                   All-Bran   K  Unheated        70
3  All-Bran with Extra Fiber   K  Unheated        50
4             Almond Delight   R  Unheated       110
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cereal.head()
```

```out
                        name mfr      type  calories
0                  100% Bran   N  Unheated        70
1          100% Natural Bran   Q  Unheated       120
2                   All-Bran   K  Unheated        70
3  All-Bran with Extra Fiber   K  Unheated        50
4             Almond Delight   R  Unheated       110
```

It looks like our `Cold` values were changed even without returning
anything in our function\! This would be another example of a function
side effect. Variables are modified by the function outside the
environment the object originated from. The dataframe was created in the
global environment, but modified in the function’s local environment.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Good Habits

Side effects seem like fun but they can be extremely problematic when
trying to debug (fix) your code. It’s a general protocol to write
functions that avoid side effects. If objects need to be modified, best
practice is to modify them in the environment they originated in.

For example, you wish to write a better version of the `value_change()`
function above, a more acceptable way would be to return a new dataframe
that was produced and modified from a copy of the original dataframe in
the local environment. We can make a copy of the original dataframe
using `.copy()`:

``` python
def better_value_change(data, column, old_value, new_value):
    new_dataframe2 = data.copy()
    new_dataframe2.loc[new_dataframe2[column] == old_value, column] = new_value
    return new_dataframe2
    
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Our original dataframe looks like so:

``` python
cereal.head()
```

```out
                        name mfr  type  calories
0                  100% Bran   N  Cold        70
1          100% Natural Bran   Q  Cold       120
2                   All-Bran   K  Cold        70
3  All-Bran with Extra Fiber   K  Cold        50
4             Almond Delight   R  Cold       110
```

We can then call our function and see the new dataframe:

``` python
unheated_cereal = better_value_change(cereal, 'type', 'Cold', 'unheated')
unheated_cereal.head()
```

```out
                        name mfr      type  calories
0                  100% Bran   N  unheated        70
1          100% Natural Bran   Q  unheated       120
2                   All-Bran   K  unheated        70
3  All-Bran with Extra Fiber   K  unheated        50
4             Almond Delight   R  unheated       110
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

If we look at our original dataframe, we can see that cereal has not
been modified. No side effects here\!

``` python
cereal.head()
```

```out
                        name mfr  type  calories
0                  100% Bran   N  Cold        70
1          100% Natural Bran   Q  Cold       120
2                   All-Bran   K  Cold        70
3  All-Bran with Extra Fiber   K  Cold        50
4             Almond Delight   R  Cold       110
```

The new function lets `cereal` be kept unmodified in the global
environment and the modified dataframe was created and in the local
environment.

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
