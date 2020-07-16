---
type: slides
---

# Python data structures: Lists, Tuples and Sets

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Sequences

In the last section, we discussed the `str` data type. We described it
as *a sequence of characters*. In many cases, there is good reason to
split up a long text string into separate ones. Luckily, we have a
convenient verb to do that `.split()`.

``` python
sentence = "I always lose at least one sock when I do laundry." 
words = sentence.split()
words
```

```out
['I', 'always', 'lose', 'at', 'least', 'one', 'sock', 'when', 'I', 'do', 'laundry.']
```

This verb then splits up the string into separate words.  
We can change where to split the string as well.

``` python
sentence.split("e")
```

```out
['I always los', ' at l', 'ast on', ' sock wh', 'n I do laundry.']
```

This argument uses the character “e” to separate the string and discards
the separator.

Why is it returned in square brackets though?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Lists

The output from the `.split()` verb is called a **list**. Similarly to
how a string is a sequence of characters that depend on an order, a list
is a sequence of elements with a particular order. Lists can be
identified by their square brackets.

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

The elements in a list can be a combination of any of the data types.

``` python
my_list = [1.2, 3, None, True, 'One of the lost socks']
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

They can even have elements that are lists

``` python
lists_of_lists = [[1,2], ['buckle', 'My', 'Shoe'], 3, 4]
lists_of_lists
```

```out
[[1, 2], ['buckle', 'My', 'Shoe'], 3, 4]
```

We can get the length of a list, with `len()` like we did for strings.

``` python
my_list = [1.2, 3, None, True, 'One of the lost socks']
len(my_list)
```

```out
5
```

If your list contains lists, `len()` will return the number of elements
in the outer list (not the total number of elements):

``` python
len(lists_of_lists)
```

```out
4
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

Similarly to how we can slice dataframes by columns and rows, we can
slice lists by elements

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

Slicing lists is similar to slicing with `iloc[]`; the start is
inclusive and the end is exclusive. So `my_list[1:3]` fetches elements 1
and 2, but not 3. In other words, it gets the 2nd and 3rd elements in
the list.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Mutable vs Immutable

A data structure is **mutable** if it can be modified.

Lists are mutable and we can assign new values for its various entries:

For example:

``` python
my_list
```

```out
[1.2, 3, None, True, 'One of the lost socks']
```

I can edit any entry in this list and replace it with a new value:

``` python
my_list[2] = "Ta Da!"
```

``` python
my_list
```

```out
[1.2, 3, 'Ta Da!', True, 'One of the lost socks']
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can also replace entries in a **nested** list (a list within a list).

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Strings can be sliced just like list:

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

But we cannot replace characters:

``` python
sentence[5] = "Z"
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'str' object does not support item assignment

Detailed traceback: 
  File "<string>", line 1, in <module>
```

That means values of type `str` are **immutable**.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# List Verbs

Unlike strings once again, lists have
<a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists" target="_blank">A
variety of different methods</a> for interacting with their data. Here
are just a few.

``` python
primes = [2,3,5,7,11]
```

We can add to the end of a list with `append()`:

``` python
primes.append(13)
primes
```

```out
[2, 3, 5, 7, 11, 13]
```

We can find the maximum value in the list with `max()`:

``` python
max(primes)
```

```out
13
```

And the sum of the list with `sum()`:

``` python
sum(primes)
```

```out
41
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Lists to Dataframes

Up until this point we have been working with dataframes that have been
read in and converted from different types of files. We, however, can
make dataframes from scratch using lists.  
Let’s say I wanted a dataframe of things I needed to purchase from the
store on my next grocery shopping trip.

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

We use a list for each row and a list for the column labels. We then use
a list of all the rows to make up the data.  
Now the shopping items are no longer in a structure type `list`, but in
a type `DataFrame`:

``` python
type(shopping_items)
```

```out
<class 'pandas.core.frame.DataFrame'>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Tuples

Tuples are a data structure very similar to lists but with the 2 main
differences:

1.  They are represented with parentheses, and
2.  They are immutable

<!-- end list -->

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
my_tuple
```

```out
('I', 'lose', None, 'socks', 'when', 1, 'do', 'laundry.', False)
```

Just to recap, immutable means that the elements withing the structure
cannot be edited, or changed:

``` python
my_tuple[2] = 'Many'
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'tuple' object does not support item assignment

Detailed traceback: 
  File "<string>", line 1, in <module>
```

We can cast objects from tuples into type `list`:

``` python
my_list = list(my_tuple)
type(my_list)
```

```out
<class 'list'>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Sets

Sets, not unlike lists and tuples, are a data structure that contains
elements. Sets differ such that:

  - They do not perserve the inserted order, and  
  - The containing values are unique - meaning there are no entries that
    are repeated.

Let’s explore this a bit.

Sets are made with curly brackets:

``` python
my_set = {1.0, 2, 'Buckle my shoe' }
my_set
```

```out
{'Buckle my shoe', 1.0, 2}
```

You’ll notice that the order is not the same as we inputted then in.
That’s because set’s do not preserve order.

What if I add more of the same entries:

``` python
my_set = {1.0, 2, 'Buckle my shoe', 1.0, 2 }
my_set
```

```out
{'Buckle my shoe', 1.0, 2}
```

This is still the same as before.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

What about the order? can I select a specific element?

``` python
my_set[1]
```

```out
Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'set' object is not subscriptable

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Remember this data structure does not perserve order, so Python displays
them according to some internal sorting scheme.  
We cannot select or slice from them, however, we can add to them with
`.add()`.

``` python
my_set.add(3)
my_set.add(4)
my_set
```

```out
{1.0, 2, 3, 4, 'Buckle my shoe'}
```

You’ll notice that unlike lists, the new entries are not added to the
end.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## All Together Now

<br>

| Data Structure | preserves order | Mutable |    Symbol    | Can contain duplicates |
| :------------- | :-------------: | :-----: | :----------: | :--------------------: |
| `str`          |        ✓        |    ☓    | `''` or `""` |           ✓            |
| `list`         |        ✓        |    ✓    |     `[]`     |           ✓            |
| `tuple`        |        ✓        |    ☓    |     `()`     |           ✓            |
| `set`          |        ☓        |    ✓    |     `{}`     |           ☓            |

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
