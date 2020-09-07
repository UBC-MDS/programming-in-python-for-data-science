---
type: slides
---

# Python data structures: Lists, Tuples and Sets

Notes:

<br>

---

## Sequences

``` python
sentence = "I always lose at least one sock when I do laundry." 
words = sentence.split()
words
```

```out
['I', 'always', 'lose', 'at', 'least', 'one', 'sock', 'when', 'I', 'do', 'laundry.']
```

``` python
sentence.split("e")
```

```out
['I always los', ' at l', 'ast on', ' sock wh', 'n I do laundry.']
```

Notes:

In the last section, we discussed the `str` data type.

We described it as *a sequence of characters*. In many cases, there is
good reason to split up a long text string into separate ones. Luckily,
we have a convenient verb to do that `.split()`.

This verb then splits up the string into separate words.

We can change where to split the string as well.

This argument uses the character “e” to separate the string and discards
the separator.

Why is it returned in square brackets though?

---

## Lists

``` python
words
```

```out
['I', 'always', 'lose', 'at', 'least', 'one', 'sock', 'when', 'I', 'do', 'laundry.']
```

``` python
type(words)
```

```out
<class 'list'>
```

``` python
my_list = [1.2, 3, None, True, 'One of the lost socks']
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

Notes:

The output from the `.split()` verb is called a **list**.

Similarly to how a string is a sequence of characters that depend on an
order, a list is a sequence of elements with a particular order.

Lists can be identified by their square brackets.

The elements in a list can be a combination of any of the data types.

---

``` python
lists_of_lists = [[1,2], ['buckle', 'My', 'Shoe'], 3, 4]
lists_of_lists
```

```out
[[1, 2], ['buckle', 'My', 'Shoe'], 3, 4]
```

``` python
my_list = [1.2, 3, None, True, 'One of the lost socks']
len(my_list)
```

```out
5
```

``` python
len(lists_of_lists)
```

```out
4
```

Notes:

They can even have elements that are lists.

We can get the length of a list, with `len()` like we did for strings.

If your list contains lists, `len()` will return the number of elements
in the outer list (not the total number of elements).

---

``` python
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

``` python
my_list[1]
```

```out
3
```

``` python
my_list[1:3]
```

```out
[3, None]
```

Notes:

Similarly to how we can slice dataframes by columns and rows, we can
slice lists by elements.

Slicing lists is similar to slicing with `iloc[]`; the start is
inclusive and the end is exclusive.

So `my_list[1:3]` fetches elements 1 and 2, but not 3.

In other words, it gets the 2nd and 3rd elements in the list.

---

## Mutable vs Immutable

``` python
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

``` python
my_list[2] = "Ta Da!"
```

``` python
my_list
```

```out
[1.2, 3, 'Ta Da!', True, 'One of the lost socks']
```

Notes:

A data structure is **mutable** if it can be modified.

Lists are mutable and we can assign new values for its various entries.

For example, we can edit any entry in this list and replace it with a
new value.

---

``` python
lists_of_lists
```

```out
[[1, 2], ['buckle', 'My', 'Shoe'], 3, 4]
```

``` python
lists_of_lists[1][2] = "Sandal"
lists_of_lists
```

```out
[[1, 2], ['buckle', 'My', 'Sandal'], 3, 4]
```

Notes:

We can also replace entries in a **nested** list (a list within a list).

---

``` python
sentence
```

```out
'I always lose at least one sock when I do laundry.'
```

``` python
sentence[27:35]
```

```out
'sock whe'
```

``` python
sentence[5] = "Z"
```

``` out
TypeError: 'str' object does not support item assignment

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

Strings can be sliced just like list.

But we cannot replace characters.

That means values of type `str` are **immutable**.

---

# List Verbs

``` python
primes = [2,3,5,7,11]
```

``` python
primes.append(13)
primes
```

```out
[2, 3, 5, 7, 11, 13]
```

``` python
max(primes)
```

```out
13
```

``` python
sum(primes)
```

```out
41
```

Notes:

Unlike strings once again, lists have
<a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists" target="_blank">A
variety of different methods</a> for interacting with their data. Here
are just a few.

We can add to the end of a list with `append()`.

We can find the maximum value in the list with `max()`.

And the sum of the list with `sum()`.

---

## Lists to Dataframes

|   | item       | location      | price |
| - | ---------- | ------------- | ----- |
| 0 | toothpaste | London Drugs  | 3.99  |
| 1 | apples     | Produce Store | 4.00  |
| 2 | bread      | Bakery        | 3.50  |

``` python
item1 = ['toothpaste', 'London Drugs', 3.99]
item2 = ['apples', 'Produce Store', 4.00]
item3 = ['bread', 'Bakery', 3.50]
column_names = ['item', 'location', 'price']

shopping_items = pd.DataFrame(data=[item1, item2, item3], columns=column_names)
shopping_items
```

```out
         item       location  price
0  toothpaste   London Drugs   3.99
1      apples  Produce Store   4.00
2       bread         Bakery   3.50
```

``` python
type(shopping_items)
```

```out
<class 'pandas.core.frame.DataFrame'>
```

Notes:

Up until this point we have been working with dataframes that have been
read in and converted from different types of files.

We, however, can make dataframes from scratch using lists.

Let’s say we wanted a dataframe of things we needed to purchase from the
store on our next grocery shopping trip.

We use a list for each row and a list for the column labels. We then use
another list of all the rows to make up the data.

Now the shopping items are no longer in a structure type `list`, but in
a type `DataFrame`.

---

## Tuples

``` python
my_tuple = ('I', 'lose', None,  'socks', 'when', 1, 'do', 'laundry.', False)
my_tuple
```

```out
('I', 'lose', None, 'socks', 'when', 1, 'do', 'laundry.', False)
```

``` python
type(my_tuple)
```

```out
<class 'tuple'>
```

Notes:

Tuples are a data structure very similar to lists but with the 2 main
differences:

1.  They are represented with parentheses, and
2.  They are immutable

---

``` python
my_tuple
```

```out
('I', 'lose', None, 'socks', 'when', 1, 'do', 'laundry.', False)
```

``` python
my_tuple[2] = 'Many'
```

``` out
TypeError: 'tuple' object does not support item assignment

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
my_list = list(my_tuple)
type(my_list)
```

```out
<class 'list'>
```

Notes:

Just to recap, immutable means that the elements withing the structure
cannot be edited, or changed.

We can cast objects from tuples into type `list` by using the verb
`list()`.

---

## Sets

``` python
my_set = {2, 1.0, 'Buckle my shoe'}
my_set
```

```out
{1.0, 2, 'Buckle my shoe'}
```

``` python
my_set = {2, 1.0, 'Buckle my shoe', 1.0, 2}
my_set
```

```out
{1.0, 2, 'Buckle my shoe'}
```

Notes:

Sets, not unlike lists and tuples, are a data structure that contains
elements. Sets differ such that:

  - They do not perserve the inserted order, and  
  - The containing values are unique - meaning there are no entries that
    are repeated.

Let’s explore this a bit.

Sets are made with curly brackets

You’ll notice that the order is not the same as we inputted then in.
That’s because set’s do not preserve order.

If we have repeats of any entries, they only occur once in the set.

---

``` python
my_set
```

```out
{1.0, 2, 'Buckle my shoe'}
```

``` python
my_set[1]
```

``` out
TypeError: 'set' object is not subscriptable

Detailed traceback: 
  File "<string>", line 1, in <module>
```

``` python
my_set.add(3)
my_set.add(4)
my_set
```

```out
{1.0, 2, 3, 4, 'Buckle my shoe'}
```

Notes:

What about the order? can we select a specific element?

Remember this data structure does not perserve order, so Python displays
them according to some internal sorting scheme.

We cannot select or slice from them, however, we can add to them with
`.add()`.

You’ll notice that unlike lists, the new entries are not added to the
end of the structure.

---

## All Together Now

<br>

| Data Structure | preserves order | Mutable |    Symbol    | Can contain duplicates |
| :------------- | :-------------: | :-----: | :----------: | :--------------------: |
| `str`          |        ✓        |    ☓    | `''` or `""` |           ✓            |
| `list`         |        ✓        |    ✓    |     `[]`     |           ✓            |
| `tuple`        |        ✓        |    ☓    |     `()`     |           ✓            |
| `set`          |        ☓        |    ✓    |     `{}`     |           ☓            |

Notes:

We have condensed the data structures characteristics into 1 convenient
table for you.

---

# Let’s practice what we learned\!

Notes: <br>
