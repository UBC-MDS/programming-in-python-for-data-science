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
not_squared_list = [ 1, 2, 3, 4]
```

We would have to do something like the following:

``` python
squared_list = []

squared_list.append(not_squared_list[0] ** 2)
squared_list.append(not_squared_list[1] ** 2)
squared_list.append(not_squared_list[2] ** 2)
squared_list.append(not_squared_list[3] ** 2)

squared_list
```

```out
[1, 4, 9, 16]
```

This is problematic for numerous reasons including that it’s time
consuming for long list.

Just like how we try to reduce, reuse and recycle waste, Python can
reuse and recycle code by repeating the interation in something called a
loop.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
not_squared_list = [ 1, 2, 3, 4]
```

We can create the same `squared_list` by looping over the same action:

``` python
squared_list = []

for element in not_squared_list: 
  squared_list.append(element ** 2)

squared_list
```

```out
[1, 4, 9, 16]
```

This only took 2 lines of code. Think how much code writing we would
avoid if the list had a length of 100?\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a closer look at the loop we just made:

``` python
squared_list = []

for element in not_squared_list: 
  squared_list.append(element ** 2)

squared_list
```

```out
[1, 4, 9, 16]
```

We start our loop with `for` and we created a new variable named
`element`. This refers to an item in the collection of items that we are
iterating over. We could name this new variable anything so long as we
reference the same name later on in the loop. For example the code below
would also run:

``` python
squared_list = []

for thingamajig in not_squared_list: 
  squared_list.append(thingamajig ** 2)

squared_list
```

```out
[1, 4, 9, 16]
```

You see how we changed the variable name in the `.append()` verb as
well?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
squared_list = []

for element in not_squared_list: 
  squared_list.append(element ** 2)

squared_list
```

```out
[1, 4, 9, 16]
```

For loops has a similar structure to conditions in that the first line
must end with a colon (`:`) and everything within the loop must have a 4
space indentation to differentiate it from code outside the loop.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## For (Each) Loop

This specific loop is call a ***For loop*** and can be iterated over any
type of *collection/sequence*: list, tuple, range, string.  
In the last case it was over the values in a list.

Block of code indented is executed for each value in the list (hence the
name “for” loops, sometimes also called “for each” loops) The loop ends
after the variable has taken all the values in the collection.

In the diagram below you can see more obviously where the looping occurs
as the green arrows make a clear loop.

<center>

<img src='/module5/loop1.png' width="50%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Here is another example:

``` python
word = "Pandas"
for letter in word:
    print("Gimme a " + letter + "!")
```

```out
Gimme a P!
Gimme a a!
Gimme a n!
Gimme a d!
Gimme a a!
Gimme a s!
```

``` python
print("What's that spell?!! " + word + "!")
```

```out
What's that spell?!! Pandas!
```

Here we took each character in the string, concatenated it with other
strings (we learned we can do that in the last Module) and printed an
output in a loop.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Looping in a dictionary

We can loop over the keys or values of a dictionary using `.keys()` and
`.values()` respectively:

``` python
cereals = {'Special K': 110, 'Lucky Charms': 150, 'Cheerios': 100, 'Wheaties': 120}

for key in cereals.keys():
  print(key)
```

```out
Special K
Lucky Charms
Cheerios
Wheaties
```

``` python
cereals = {'Special K': 110, 'Lucky Charms': 150, 'Cheerios': 100, 'Wheaties': 120}
calories = []

for val in cereals.values():
  calories.append(val)

calories
```

```out
[110, 150, 100, 120]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## range

Instead of looping over items in a collection we can iterate over a
sequence of numbers. `range()` is a verb that generates a sequence of
integers up to some value.

``` python
for i in range(5):
    print(i)
```

```out
0
1
2
3
4
```

We can also specify a start value, an end value and a skip-by value with
range:

``` python

for i in range(50,101,10):
    print(i)
```

```out
50
60
70
80
90
100
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The format is the starting integer first, the ending integer next and
the skip by integer last. Remember that similarly to slicing with
`.iloc[]` in pandas, the starting point of range is *inclusive* in the
sequence and the ending number is *exclusive*.

``` python
range(start,end,skip)
```

The skip-by variable is optional though. In `range`, the default skip
number is 1, so if we don’t include it, Python will assume increasing in
increments of 1.

``` python
for i in range(5,10):
    print(i)
```

```out
5
6
7
8
9
```

If we only include a single integer in the function, a sequence up to
the given number (not including it) will be generated starting from `0`.

``` python
for i in range(4):
    print(i)
```

```out
0
1
2
3
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`range()` only works for integers. If we attempt a loop with type
`float`, an error will occur:

``` python
for i in range(0.5,1.0,0.1):
    print(i)
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'float' object cannot be interpreted as an integer

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

## Comprehensions

We learned in the last Module that we can make and `if`/`else` condition
in a single line of code and we can do something similar with basic
loops. **Comprehensions** allow us to build
lists/tuples/sets/dictionaries in one convenient, compact line of code.

List comprehension can be done as so:

``` python
sentence = ['This', 'checks', 'the', 'number', 'of', 'letter', 'per', 'word']

word_length = [len(word) for word in sentence]
word_length
```

```out
[4, 6, 3, 6, 2, 6, 3, 4]
```

to write the same thing without comprehension would look like this:

``` python
word_length = []

for word in sentence:
  word_length.append(len(word))

word_length
```

```out
[4, 6, 3, 6, 2, 6, 3, 4]
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Dictionary comprehension can be done in a similar way but this time we
wrap the line with curly brackets and specify what our keys and values
are:

``` python
sentence = ['This', 'checks', 'the', 'number', 'of', 'letter', 'per', 'word']

word_length = {word : len(word) for word in sentence}
word_length
```

```out
{'This': 4, 'checks': 6, 'the': 3, 'number': 6, 'of': 2, 'letter': 6, 'per': 3, 'word': 4}
```

Both methods of building lists and dictionaries work and it’s down to
you to decide what works better for you.

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
