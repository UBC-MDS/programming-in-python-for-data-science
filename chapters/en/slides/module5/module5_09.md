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

## range

Instead of looping over items in a collection, we can iterate over a
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

## Comprehensions

We learned in the last Module that we can make and `if`/`else` condition
in a single line of code and we can do something similar with basic
loops. **Comprehensions** allow us to build
lists/tuples/sets/dictionaries in one convenient, compact line of code.

As an example, let’s count the number of letters in each element of a
list. The list comprehension can be done as so:

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
word_length = list()

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
