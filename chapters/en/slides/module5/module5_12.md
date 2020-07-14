---
type: slides
---

# Nested loops

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Hi elijah We’ve seen how loops can help us adhere to the DRY principle,
but what can we do if we are already using a loop and there is still
repetition?  
For example: Let’s say we are trying to obtain all the red (♥️, ♦️)
suited face cards from a deck of cards into a list.

``` python
suits = ["❤︎","♦"]
faces = ['Jack', 'Queen', 'King']

cards = [ ]
for suit in suits:
    cards.append(faces[0] + ' of ' + suit)
    cards.append(faces[1] + ' of ' + suit)
    cards.append(faces[2] + ' of ' + suit)
cards
```

```out
['Jack of ❤︎', 'Queen of ❤︎', 'King of ❤︎', 'Jack of ♦', 'Queen of ♦', 'King of ♦']
```

We are currently using a loop but we keep repeating the same `faces[#] +
' of ' + suit` line.

In these types of situations, we can reduce redundancy by… you guessed
it, adding another loop\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Just like how we reduced the repetition by making a first loop we can
make a second loop within the first one.

``` python
suits = ["❤︎","♦︎"]
faces = ['Jack', 'Queen', 'King']

cards = [ ]
for suit in suits:
    for face in faces: 
        cards.append(face + ' of ' + suit)
cards
```

```out
['Jack of ❤︎', 'Queen of ❤︎', 'King of ❤︎', 'Jack of ♦︎', 'Queen of ♦︎', 'King of ♦︎']
```

This is called a **nested loop** since we have a loop *nested* in an
existing one.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s see exactly what is happening:

<center>

<img src='/module5/loop33.gif' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cards = [ ]
for suit in suits:
    print(suit)
    for face in faces: 
        print(face)
        cards.append(face + ' of ' + suit)
```

```out
❤︎
Jack
Queen
King
♦︎
Jack
Queen
King
```

``` python
cards
```

```out
['Jack of ❤︎', 'Queen of ❤︎', 'King of ❤︎', 'Jack of ♦︎', 'Queen of ♦︎', 'King of ♦︎']
```

By looking at the output, we notice that all the heart(♥️) face cards
are added to the list first. That means the first iteration of the outer
loop waits for the inner loop to finish going through all the faces
before starting the next suit iteration. Python then re-iterates over
the inner loop again for the second item (♦️) in the outer loop.

The outer loop cannot move onto its next iteration until the inner loop
has reached the last item in its collection.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s try another example:

In this case, we are given a list containing lists as elements that we
wish to “flatten” into a new list that contains all the individual
elements.

``` python
rhyme = [[1, 2, 'buckle my shoe'], [3, 4, 'slam the door'], [5, 6, 'pick up sticks']]

all_words = list()
for verse in rhyme: 
    for word in verse: 
      all_words.append(word)
all_words 
```

```out
[1, 2, 'buckle my shoe', 3, 4, 'slam the door', 5, 6, 'pick up sticks']
```

For each of the lists in `rhyme`, we go through a loop to append each
element in `verse` to a new list object named `all_words`. This sounds
like a mouthful so let’s clear this up.  
We use a loop to iterate over each list in the `rhyme` object.  
We use a second loop to iterate over each element in the `verse` list.

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
