---
type: slides
---

# Python operations

Notes:

<br>

---

| Operator |  Description   |
| :------: | :------------: |
|   `+`    |    addition    |
|   `-`    |  subtraction   |
|   `*`    | multiplication |
|   `/`    |    division    |
|   `**`   | exponentiation |

Notes:

We have already been a witness to a few of Python’s arithmetic
operators, but there are a few on this list that you have yet to see.

---

## Numeric Operations

``` python
6 + 5.7
```

```out
11.7
```

``` python
15 - 7
```

```out
8
```

``` python
4.5 * 4
```

```out
18.0
```

``` python
2 ** 3
```

```out
8
```

``` python
2.2 ** 5
```

```out
51.53632000000002
```

Notes:

Let’s apply these to the Python types we have learned and observe the
results.

These operators act as expected on numeric types.

An `int` plus a `float` results in a `float`.

And the subtraction of 2 values of type `int` results with a type `int`.

Multiplication with a `float` and an `int` will result in a `float` as
well.

Exponents can be calculated with `**` and applied with `int` as well as
`float` data types.

---

## Bool

``` python
True + True 
```

```out
2
```

``` python
True * 4
```

```out
4
```

``` python
False * 2 + True
```

```out
1
```

``` python
False + 4
```

```out
4
```

Notes:

We saw that addition, subtraction, multiplication and exponential
operations work as expected with numeric values but let’s put our
concentration on what happens with the other data types and structures.

What happens when we try to add up `bool` values?

We see that `True` values are cast as a value of `1` and `False` values
are cast as `0` when they undergo operations.

---

## Str

``` python
'The monster under my bed' + ' is named Mike' 
```

```out
'The monster under my bed is named Mike'
```

``` python
'The monster under my bed' - ' is named Mike' 
```

``` out
TypeError: unsupported operand type(s) for -: 'str' and 'str'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
'The monster under my bed' / ' is named Mike' 
```

``` out
TypeError: unsupported operand type(s) for -: 'str' and 'str'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

Strings react rather interestingly with the addition operator.

For instance, when we add strings we add the sequence from one end to
the other.

And we cannot multiply, divide or subtract them.

---

``` python
'The monster under my bed' + 1200
```

``` out
TypeError: can only concatenate str (not "int") to str

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
'The monster under my bed' + str(1200)
```

```out
'The monster under my bed1200'
```

``` python
'The monster under my bed' * 3
```

```out
'The monster under my bedThe monster under my bedThe monster under my bed'
```

We can multiply strings and it concatenates the strings together\! Since
we multiplied by 3, the string is repeated 3 times.

Notes:

We saw that we can operate on `float` and `int` values together but what
about `str` and numeric values?

That does not work, however, if we cast the number `1200` to a string,
we can concatenate the two together.

What about multiplication?

This will repeat the string by the number you are multiplying.

In this case, the string `'The monster under my bed'` is repeated 3
times.

---

## List

``` python
list1 = [1, 2.0, 3, 4.5] + ['nine', 'ten', 'eleven', 'twelve']
list1
```

```out
[1, 2.0, 3, 4.5, 'nine', 'ten', 'eleven', 'twelve']
```

``` python
[1, 2.0, 3, 4.5] - [3, 5, 2, 1]
```

``` out
TypeError: unsupported operand type(s) for -: 'list' and 'list'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
[1, 2.0, 3, 4.5] * [5, 6, 7, 8]
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: can't multiply sequence by non-int of type 'list'

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

How about with other data structure like **lists**, **tuples** and
**dictionaries**?

If we add lists, similarly to strings, the lists concatenate together to
create a single list containing the elements of both lists.

Other operators are not supported when working with lists.

---

## Boolean Operators

| Operator  | Description                      |
| :-------: | :------------------------------- |
| `x == y`  | is x equal to y?                 |
| `x != y`  | is x not equal to y?             |
|  `x > y`  | is x greater than y?             |
| `x >= y`  | is x greater than or equal to y? |
|  `x < y`  | is x less than y?                |
| `x <= y`  | is x less than or equal to y?    |
| `x is y`  | is x the same object as y?       |
| `x and y` | are x and y both true?           |
| `x or y`  | is at least one of x and y true? |
|  `not x`  | is x false?                      |

Notes:

When we’ve filtered our data we’ve seen different Boolean operators
however we have yet to see all that is available.

Let’s explores them.

---

``` python
'dogs' == 'cats'
```

```out
False
```

``` python
6 < 7
```

```out
True
```

``` python
(6 < 7) and ('dogs' == 'cats')
```

```out
False
```

``` python
(6 < 7) or ('dogs' == 'cats')
```

```out
True
```

Since one statement is true the combine “or” statement is True.

Notes:

Let’s start with 2 base statements;

  - dogs and cats are not equal results in a `False` statement and,
  - 6 being less than 7 produces a `True` statement.

We can combine them to explore `and`, `or` and `not` operators.

We can check if both statements are `True` using the keyword `and`.

In this case since both statements are not `True`, so combining them
with `and` will output `False`.

However, the keyword `or` checks if at least one of the statements is
`True` and since `6 < 7` is a `True` statement, the output of the `or`
statment is `True`.

---

``` python
not ('dogs' == 'cats')
```

```out
True
```

``` python
not  (6 < 7)
```

```out
False
```

Seeing if the statement is False will result in a `False` output since
`(6 < 7)` is True.

Notes:

We know that `('dogs' == 'cats')` is `False`, so a `not` operator gives
us a `True` value because it confirms the fact the statement is `False.`

While we know `(6 < 7)` is `True` the statement `not (6 < 7)` produces a
`False` value since `not` is checking for `False` statements.

How can we translate all this to dataframes now?

Have you ever wondered why we can do summary statistics on some columns
and not others? We are going to explore this in the next section.

---

# Let’s practice what we learned\!

Notes:

<br>
