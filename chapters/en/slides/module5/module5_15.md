---
type: slides
---

# Repeated iterations with conditions

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We know that we can have loops contained in another loop so it should be
no surprise that we can combine loops with conditional arguments that we
learned at the beginning of this module.

Similarly to how we can have a loop nested in an existing loop, we can
have conditional statements within a `for` loop.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

When we learned about conditional arguments, we checked the conditions
on a single data type such as a `str`, `float`, `int` or `bool`.
Combining loops with conditions, give us the ability to check multiple
elements in a sequence such as a `list` or `dict`.

For example:

When we learned about conditions we did the following:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Then we had to repeat the same conditional statements code to test an
item = 13 (violating the DRY principle).

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Instead, we could accomplish this by putting the values 13, and 25 in a
list and used a `for` loop containing the conditional statements.

``` python
item_list = [25, 13]

for item in item_list:
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
'between 10 and 20'
```

This small change helped us adhere to the DRY principle and avoided
repeating redundant code.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Break

There are occasions that we may want to save on time by not iterating
over an entire sequence. Perhaps we only need to find one number that is
`10 or less` in a list.

``` python
item_list = [25, 13, 21, 8, 17, 11, 4]

for item in item_list:
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
'between 10 and 20'
'greater than 20'
'10 or less'
'between 10 and 20'
'between 10 and 20'
'10 or less'
```

We can see that even after we located a number that is 10 or less, the
loop continues until it reaches the last element.If we have a very large
list, it’s inefficient to continue searching for something we have
already found.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Instead, we can use something called a **break**. A `break` will stop
the loop from continuing.

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
        
    magnitude
```

```out
'greater than 20'
'between 10 and 20'
'greater than 20'
```

Now we can see that as soon as we found a value that had was `10 or
less`, all subsequent iterations came to a halt and Python exists the
loop. Not even the last `magnitude` in the loop is returned.

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
