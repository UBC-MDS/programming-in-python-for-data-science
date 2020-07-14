---
type: slides
---

# Repeating iterations (loops)

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Repeating Code

There are times where we may want to repeat the same action multiple
times. Let’s say we want to add the square of every number in a list to
a new list.

``` python
numbers = [ 2, 3, 5]
```

We would have to do something like the following:

``` python
squared = list()

squared.append(numbers[0] ** 2)
squared.append(numbers[1] ** 2)
squared.append(numbers[2] ** 2)
squared
```

```out
[4, 9, 25]
```

This is problematic for numerous reasons.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Some of the reasons this exhibits bad coding practices are as followed:

  - **Difficult to scale**: It only works for a list with 4 elements. If
    we want to do this for a list of a different length, we need to add
    or remove code.

  - **Difficult to modify**: If we want to change its functionality, we
    need to change 4 similar lines of code.

  - **Clarity**: It is hard to understand what it does just by looking
    at it.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Don’t Repeat Yourself (DRY Principle)

Just like how we try to reduce, reuse and recycle waste, coding likes to
borrow a similar principle aimed at reducing repetitive code.

This motion is called the ***DRY principle*** otherwise known as the
“Don’t Repeat Yourself” principle. This premise of this principle to
avoid redundancy within code.

The method we discussed in the last slide is a violation of this
principle (known as a ***Wet Solution***). There is a much more
efficient method to obtain the same output that avoids typing out
multiple iterations of similar code.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Loops

Our example before takes 4 lines of code to make `squared` and violates
the DRY principle in the process:

``` python
squared = list()

squared.append(numbers[0] ** 2)
squared.append(numbers[1] ** 2)
squared.append(numbers[2] ** 2)
squared
```

```out
[4, 9, 25]
```

Instead, we can create `squared` by using something called a **loop** to
repeat the `.append()` action over the multiple elements:

``` python
squared = list()
for number in numbers: 
    squared.append(number ** 2)
squared
```

```out
[4, 9, 25]
```

This only took 3 lines of code but if the number of elements in the list
increase, the code remains the same. Think how much code writing we
would avoid if the list had a length of 1000?\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## For (Each) Loop

This specific loop is called a ***For loop*** and can be iterated over
any type of *collection/sequence*: list, tuple, range, string.  
In this case, it’s over the values in a list.

Block of code indented is executed for each value in the list (hence the
name “for” loops, sometimes also called “for each” loops).  
The loop ends after the variable has taken all the values in the
collection.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a closer look at exactly what is happening in this loop:

<center>

<img src='/module5/loop.gif' width="80%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Before entering the loop, we make an empty list named `squared`:

<center>

<img src='/module5/iter0.png' width="80%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We first start with the first number in `numbers`. We calculate the
square of `2` and append it to the empty list called `squared`.

<center>

<img src='/module5/iter1.png' width="80%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we have finished all the code for the first element, we move to the
second one valued at `3`:

<center>

<img src='/module5/iter2.png' width="80%">

</center>

This number gets squared and added to the existing lists `squared`.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We then move onto the last element valued at `5`. This is where the loop
ends and outputs `squared`.

<center>

<img src='/module5/iter3.png' width="80%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
squared = list()
numbers = [ 2, 3, 5]

for number in numbers: 
    squared.append(number ** 2)
squared
```

```out
[4, 9, 25]
```

Our loop begins with the keyword `for` and we make a new variable named
`number`. This refers to an element in the list `numbers`. We could name
this new variable anything so long as we reference the same name later
on in the loop.

``` python
squared = list()
numbers = [ 2, 3, 5]

for thingamajig in numbers: 
    squared.append(thingamajig ** 2)

squared
```

```out
[4, 9, 25]
```

You see how we changed the variable name in the construction of the loop
as well as in the `.append()`?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
squared = list()

for number in numbers: 
    squared.append(number ** 2)

squared
```

```out
[4, 9, 25]
```

Loops have a similar structure to conditions in that the first line must
end with a colon (`:`) and everything within the loop must have a
4-space indentation to differentiate it from code outside the loop.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Looping in a dictionary

We can also loop over the key-value pairs of a dictionary using
`.items()`. For example, a grocery store has the following cereal in
stock. `.items()` returns a tuple with the dictionary key at index 0 and
value at index 1. We can calculate the total stock quantity in an object
named `stock_total` by summing up all the values:

``` python
cereals = {'Special K': 4, 'Lucky Charms': 7, 'Cheerios': 2, 'Wheaties': 3}
stock_total = 0

for val in cereals.items():
    stock_total = stock_total + val[1]
    print(stock_total)
```

```out
4
11
13
16
```

Notice that we keep a running tally of the total stock at each iteration
with `stock_total` until we arrive at the final count of 16.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we are updating an existing object in a loop such as:

``` python
stock_total = stock_total + val[1]
```

Instead of writing the object name twice, we can shorten it to:

``` python
stock_total += val[1]
```

This simply means that we are adding `val[1]` to the `stock_total`
object.

If we replace this code into the loop from before, it works in exactly
the same way:

``` python
cereals = {'Special K': 4, 'Lucky Charms': 7, 'Cheerios': 2, 'Wheaties': 3}
stock_total = 0

for val in cereals.items():
    stock_total += val[1]
    print(stock_total)
```

```out
4
11
13
16
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
