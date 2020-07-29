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

We’ve seen how loops can help us adhere to the DRY principle, but what
can we do if we are already using a loop and there is still
repetition?  
For example: Let’s say we are trying to obtain all the red (♥️, ♦️)
suited face cards from a deck of cards into a list.

``` python
suits = ["❤︎","♦"]
faces = ['Jack', 'Queen', 'King']

cards = list()
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

cards = list()
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

We enter into the outer loop where the first element in suits is `♥️`:

<center>

<img src='/module5/nested1.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The next line indicates to enter a second loop, which iterate over the
list `faces`. The first element in this list is `Jack`:

<center>

<img src='/module5/nested2.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The next line of code creates a string containing the suit (`♥️`) and
the face (`Jack`) in the current iterations and append it to the list
`cards`:

<center>

<img src='/module5/nested3.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Once we have appended this to `cards`, the inner loop moves onto the
second element - `Queen` in the `faces` list.  
Notice how we are still on the first element (`♥️`) in the `suit` list.

<center>

<img src='/module5/nested4.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

. </audio>

</html>

---

We create a string containing the suit (`♥️`) and the face (`Queen`) of
this current iteration which is `Queen of ♥️` and add it to the list
`cards`:

<center>

<img src='/module5/nested5.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Since we finish all the code in the inner loop’s second iteration we can
move on the third element in `faces` which is `King`:

<center>

<img src='/module5/nested6.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

The string `King of ♥️` is added to the `cards` list:

<center>

<img src='/module5/nested7.png' width="70%">

</center>

Now we have finished all the elements in the inner loop, where do we go
now?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Only now, that all the elements in `faces` have been iterated over can
we move on to the next iteration in the outer loop. This consists of
iterating to the next element (`♦️`) in `suits`:

<center>

<img src='/module5/nested8.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We restart iterating over `faces` again in the inner loop, starting with
`Jack`:

<center>

<img src='/module5/nested9.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We iterate over each element in `faces` appending the strings `'Jack of
♦'`, `'Queen of ♦'`, `'King of ♦'` at each iteration until reaching
the end of `faces`:

<center>

<img src='/module5/nested10.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Since we have reached the end of both lists `suits` and `faces`, all the
iterations in the inner and outer loops have finished. We exit the loops
and executes the next line of code which outputs `cards`.

<center>

<img src='/module5/nested11.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
cards = list()
for suit in suits:
    print(suit)
    for face in faces: 
        print(face)
        cards.append(face + ' of ' + suit)
cards
```

``` out
Show in New WindowClear OutputExpand/Collapse Output
❤︎
Jack
Queen
King
♦
Jack
Queen
King
['Jack of ❤︎', 'Queen of ❤︎', 'King of ❤︎', 'Jack of ♦', 'Queen of ♦', 'King of ♦']
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

Let’s see exactly what is happening again in the animation below:

<center>

<img src='/module5/loop33.gif' width="90%">

</center>

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
