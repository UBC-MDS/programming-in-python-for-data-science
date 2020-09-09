---
type: slides
---

# Repeated iterations with conditions

Notes:

<br>

---

``` python
item = 25 

if item > 20:
    magnitude = 'greater than 20'
elif item > 10:
    magnitude = 'between 10 and 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 20'
```

Notes:

We know that we can have loops contained in another loop so it should be
no surprise that we can combine loops with conditional arguments that we
learned at the beginning of this module.

Similarly to how we can have a loop nested in an existing loop, we can
have conditional statements within a `for` loop.

When we learned about conditions we had the following code.

We checked the object `item` with a value of 25 to see if it met the
`if` condition, the `elif` condition and if it didn’t meet either of
those then it would undergo the code in the `else` statement body.

---

``` python
item = 13 

if item > 20:
    magnitude = 'greater than 20'
elif item > 10:
    magnitude = 'between 10 and 20'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'between 10 and 20'
```

Notes:

Then we had to repeat and rewrite the same conditional statements code
to check `item` with a new value of 13 which violated the DRY principle
since we repeated and copied the code again.

---

``` python
item_list = [25, 13]

for item in item_list:
    if item > 20:
        magnitude = 'greater than 20'
    elif item > 10:
        magnitude = 'between 10 and 20'
    else:
        magnitude = '10 or less'
    print(magnitude)
```

```out
greater than 20
between 10 and 20
```

Notes:

Instead, we could put the values 13, and 25 in a list and used a `for`
loop containing the conditional statements.

This small change helped us adhere to the DRY principle and avoided
repeating redundant code and now we iterate over each element in the
list and assigns the object `magnitude` a different value depending on
which condition was met.

---

## Break

``` python
item_list = [25, 13, 21, 8, 17, 11, 4]

for item in item_list:
    if item > 20:
        magnitude = 'greater than 20'
    elif item > 10:
        magnitude = 'between 10 and 20'
    else:
        magnitude = '10 or less'
    print(magnitude)
```

```out
greater than 20
between 10 and 20
greater than 20
10 or less
between 10 and 20
between 10 and 20
10 or less
```

Notes:

There are occasions where we may want to save on time by not iterating
over an entire sequence.

Perhaps we only need to find one number that is `10 or less` in a list.

We can see that even after we located a number that is 10 or less, the
loop continues until it reaches the last element. If we have a very
large list, it’s inefficient to continue searching for something we have
already found.

---

``` python
item_list = [25, 13, 21, 8, 17, 11, 4]

for item in item_list:
    if item > 20:
        magnitude = 'greater than 20'
    elif item > 10:
        magnitude = 'between 10 and 20'
    else:
        magnitude = '10 or less'
        break
        
    print(magnitude)
```

```out
greater than 20
between 10 and 20
greater than 20
```

Notes:

Instead, we can use something called a **break**. A `break` will stop
the loop from continuing.

Now we can see that as soon as we found a value with `magnitude` equal
to `10 or less`, all subsequent iterations came to a halt and Python
exits the loop.

Not even the last `print(magnitude)` in the loop is returned.

---

## A styalizing side point

``` python
item_list = [25, 13, 21, 8, 17, 11, 4]
```

``` python
number_over_20 = 0

for item in item_list:
    if item > 20:
        number_over_20 = number_over_20 + item
        
number_over_20
```

```out
46
```

Instead of writing this line:

``` python
number_over_20 = number_over_20 + item
```

We can write:

``` python
number_over_20 +=  item
```

Notes:

You’ve seen that we often add to an existing object when we use loops.

For instance when we count the number of items that are over 20 in the
list `item_list`.

We keep the object name `number_over_20` and just add to it while
iterating through the loop.

Instead of writing the line:

``` python
number_over_20 = number_over_20 + item
```

We can avoid writing the object name twice and write a more stylized
approach:

``` python
number_over_20 +=  item
```

This simply means that we are adding `item` to the `number_over_20`
object.

---

``` python
item_list = [25, 13, 21, 8, 17, 11, 4]
number_over_20 = 0

for item in item_list:
    if item > 20:
        number_over_20 += item

number_over_20
```

```out
46
```

Notes:

If we replace this code into the loop from before, it works in exactly
the same way.

---

# Let’s apply what we learned\!

Notes:

<br>
