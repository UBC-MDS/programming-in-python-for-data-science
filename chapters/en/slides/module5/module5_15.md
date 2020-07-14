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
    magnitude = 'greater than 10'
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
    magnitude = 'greater than 10'
else:
    magnitude = '10 or less'
 
magnitude
```

```out
'greater than 10'
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
        magnitude = 'greater than 10'
    else:
        magnitude = '10 or less'
    magnitude
```

```out
'greater than 20'
'greater than 10'
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

Let’s have Python make some decisions using the keys in a dictionary.
The dictionary below contains cereals and their respective calorie
content.

``` python
cereals = {'Special K': 110, 'Lucky Charms': 150, 'Cheerios': 100, 'Wheaties': 120}
```

We want to determine if the cereals are low calorie. Any cereal with a
value less than 120 is considered low calorie and anything above is not.

``` python
for val in cereals.items():
    if val[1] < 120: 
        low_cal = True
    else: 
        low_cal = False
    low_cal
```

```out
True
False
True
False
```

See how little code it took to check each item in the dictionary?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Break

There are occasions that we may want to save on time by not iterating
over an entire sequence. Perhaps we need to locate the word “diamond” in
a list and return the index number (we can use `.index()` to return the
index location of a specified value in a list).

``` python
mine = [ 'rough', 'rocks', 'rough', 'sand', 'diamond', 'rough', 'dirt', 'stones']

for debris in mine: 
    print(debris)
    if debris == 'diamond':
        print(mine.index(debris))
```

```out
rough
rocks
rough
sand
diamond
4
rough
dirt
stones
```

We can see that even after we located the diamond in the rough (at index
position 4), the loop continues until it reaches the last element. If we
have a very large list, it’s inefficient to continue searching for
something we have already found.

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
mine = [ 'rough', 'rocks', 'rough', 'sand', 'diamond', 'rough', 'dirt', 'stones']

for debris in mine: 
    print(debris)
    if debris == 'diamond':
        print(mine.index(debris))
        break
```

```out
rough
rocks
rough
sand
diamond
4
```

Now we can see that as soon as we found the diamond location, all
subsequent iterations came to a halt.

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
