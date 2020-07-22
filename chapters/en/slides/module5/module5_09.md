---
type: slides
---

# Range and comprehensions

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Range

Often, we just want to do something 5 times without looping over a
collection. The most common way to do that is to use `range()`, which
automatically generates a collection of the integers 0, 1, 2, 3, 4, or
in general 0, 1, …, N-1 .

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

We can also specify a *start value*, an *end value* and a *skip-by
value* with range:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The format is the starting integer first, the ending integer next and
the skip by integer last. Similarly to slicing with `.iloc[]` in pandas,
the starting point of `range()` is *inclusive* in the sequence and the
ending number is *exclusive*.

``` python
range(start, end, skip)
```

The skip-by variable is optional. In `range()`, the default skip number
is 1, so if we don’t include it, Python will assume to increase in
increments of 1.

``` python
for i in range(7,10):
    print(i)
```

```out
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

## Looping in a dictionary

We can also loop over the key-value pairs of a dictionary using
`.items()`.

``` python
cereals = {'Special K': 4, 'Lucky Charms': 7, 'Cheerios': 2, 'Wheaties': 3}
cereals.items()
```

```out
dict_items([('Special K', 4), ('Lucky Charms', 7), ('Cheerios', 2), ('Wheaties', 3)])
```

Since each key-value pair has 2 elements in it, we need 2 specify 2
variables for each item in `cereal.items()` - One for the `key` in this
case the cereal name, and one for the value - the cereal stock total.

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
loops. **Comprehensions** allow us to build lists/sets/dictionaries in
one convenient, compact line of code.

As an example, let’s count the number of letters in each element of a
list. The list comprehension can be done as so:

``` python
numbers = [ 2, 3, 5]

squared = [number ** 2 for number in numbers]
squared
```

```out
[4, 9, 25]
```

We saw in the last section that to obtain the same resulted required the
following code:

``` python
squared = list()

for number in numbers: 
    squared.append(number ** 2)
    
squared
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

Dictionary comprehensions can be done in a similar way but this time we
wrap the line with curly brackets and specify what our keys and values
are: In this case we assign the number as the key and the square of it
as the value.

``` python
numbers = [ 2, 3, 5]

word_length = {number : number ** 2 for number in numbers}
word_length
```

```out
{2: 4, 3: 9, 5: 25}
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
