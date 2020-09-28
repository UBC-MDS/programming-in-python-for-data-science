---
type: slides
---

# Range, dictionaries and comprehensions

Notes:

<br>

---

## Range

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

``` python
for i in range(50, 101, 10):
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

Notes:

Often, we just want to do something 5 times without looping over a
collection.

The most common way to do that is to use `range()`, which automatically
generates a collection of the integers in some sort of sequence,
generally 0, to N-1.

We can also specify a *start value*, an *end value* and a *skip-by
value* with range.

---

``` python
range(start, end, skip)
```

``` python
for i in range(7,10):
    print(i)
```

```out
7
8
9
```

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

``` python
for i in range(0.5,1.0,0.1):
    print(i)
```

``` out
TypeError: 'float' object cannot be interpreted as an integer.

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

The range function specifies the starting integer first, the ending
integer next, and the skip by integer last.

Similarly to slicing with `.iloc[]` in pandas, the starting point of
`range()` is *included* in the sequence, and the ending number is
*excluded*.

The skip-by variable is optional.

In `range()`, the default skip number is 1, so if we don’t include it,
Python will assume to increase in increments of 1.

If we only include a single integer in the function, a sequence up to
the given number (but not including it) will be generated starting from
`0`.

`range()` only works for integers. If we attempt a loop with type
`float`, an error will occur:

---

## Looping in a dictionary

``` python
cereals = {'Special K': 4, 'Lucky Charms': 7, 'Cheerios': 2, 'Wheaties': 3}
cereals.items()
```

```out
dict_items([('Special K', 4), ('Lucky Charms', 7), ('Cheerios', 2), ('Wheaties', 3)])
```

``` python
cereals = {'Special K': 4, 'Lucky Charms': 7, 'Cheerios': 2, 'Wheaties': 3}

for cereal, stock in cereals.items():
    print( cereal  + " has " + str(stock) + " available")
```

```out
Special K has 4 available
Lucky Charms has 7 available
Cheerios has 2 available
Wheaties has 3 available
```

Notes:

We can also loop over the key-value pairs of a dictionary using
`.items()`.

We saw this verb back in module 4 when we learned about dictionaries.

Since each key-value pair has 2 elements in it, we need to specify a
variable for each item in the tuple:

  - One for the dictionary **key**
  - One for the dictionary **values**

Here we assign an object named `cereal` for the items in the first
position of the tuple, which are the dictionary keys, and an object
named `stock` for the second index in a tuple, which are the dictionary
values.

---

## Comprehensions

``` python
numbers = [2, 3, 5]
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

``` python
squared = [number ** 2 for number in numbers]
squared
```

```out
[4, 9, 25]
```

Notes:

We learned in the last Module that we can create `if` and `else`
conditions in a single line of code, and we can do something similar
with basic loops.

**Comprehensions** allow us to build lists/sets/dictionaries in one
convenient, compact line of code.

In the last set of slides, we made a loop that calculates the square of
each element from a list and adds them to a new list name `squared`.

This can be done using comprehension, so now it executes using the
single line of code.

---

``` python
numbers = [2, 3, 5]

word_length = {number : number ** 2 for number in numbers}
word_length
```

```out
{2: 4, 3: 9, 5: 25}
```

Notes:

Dictionary comprehensions can be done in a similar way, but this time we
wrap the line with curly brackets and specify what our keys and values
are.

In this case, we name the element in the list `number`.

We assign `number` as the dictionary key and the square of `number` as
the dictionary value.

Both methods of building lists and dictionaries work, and it’s down to
you to decide what works better for you.

---

# Let’s apply what we learned\!

Notes: <br>
