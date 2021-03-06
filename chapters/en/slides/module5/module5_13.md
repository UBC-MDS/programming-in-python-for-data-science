---
type: slides
---

# Nested loops

Notes: <br>

---

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

Notes:

We’ve seen how loops can help us adhere to the DRY principle, but what
can we do if we are already using a loop, and there is still repetition
in our code?

For example: Let’s say we are trying to obtain all the red (♥️, ♦️)
suited face cards from a deck of cards into a list.

We are currently using a loop, but we keep repeating the same `faces[#]
+ ' of ' + suit` line.

In these types of situations, we can reduce redundancy by… you guessed
it, adding another loop\!

---

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

Notes:

Just like how we reduced the repetition by making the first loop, we can
make a second loop within the first one.

This is called a **nested loop** since we have a loop *nested* in an
existing one.

---

<center>

<img src='/module5/nested1.png' width="70%">

</center>

Notes:

We enter into the outer loop, where the first element in suits is `♥️`.

---

<center>

<img src='/module5/nested2.png' width="70%">

</center>

Notes:

The next line constructs the second loop, which iterates over the list
`faces`.

The first element in this list is `Jack`.

---

<center>

<img src='/module5/nested3.png' width="70%">

</center>

Notes:

The following indented line of code creates a string containing the suit
(`♥️`) and the face (`Jack`) in the current iterations and append it to
the list `cards`.

---

<center>

<img src='/module5/nested4.png' width="70%">

</center>

Notes:

Once we have appended this to `cards`, the inner loop moves onto the
second element in the `faces` list, which has the value `Queen`.

Notice how we are still on the first element (`♥️`) in the `suit` list.

---

<center>

<img src='/module5/nested5.png' width="70%">

</center>

Notes:

We create a string containing the suit (`♥️`) and the face (`Queen`) of
this current iteration, which is `Queen of ♥️` and add it to the list
`cards`.

---

<center>

<img src='/module5/nested6.png' width="70%">

</center>

Notes:

Since we finish all the code in the inner loop’s second iteration, we
can move on the third element in list `faces,` which is `King`.

---

<center>

<img src='/module5/nested7.png' width="70%">

</center>

Notes:

The string `King of ♥️` is added to the `cards` list.

It’s at this point that we have finished all the elements in the inner
loop; where do we go now?

---

<center>

<img src='/module5/nested8.png' width="70%">

</center>

Notes:

Now that all the elements in `faces` have been iterated over, can we
move on to the next iteration in the outer loop?

This involves of iterating to the next element (`♦️`) in the list
`suits`.

---

<center>

<img src='/module5/nested9.png' width="70%">

</center>

Notes:

We now restart iterating over `faces` again in the inner loop, starting
with `Jack`.

---

<center>

<img src='/module5/nested10.png' width="70%">

</center>

Notes:

We iterate over each element in `faces` again, appending the strings
`'Jack of ♦'`, `'Queen of ♦'`, `'King of ♦'` at each iteration until
reaching the end of the list `faces`.

---

<center>

<img src='/module5/nested11.png' width="70%">

</center>

Notes:

Since we have reached the end of both the lists `suits` and `faces`, all
the iterations in the inner and outer loops have finished.

We exit the loops and executes the next line of code, which displays the
list `cards`.

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

Notes:

By looking at the output, we notice that all the heart(♥️) face cards
are added to the list first.

That means the first iteration of the outer loop waits for the inner
loop to finish going through all the face elements before starting the
next element in `suit`.

Python then re-iterates over the inner loop again for the second element
(♦️) in the outer loop.

The outer loop cannot move onto its next iteration until the inner loop
has reached the last item in its collection.

---

<center>

<img src='/module5/loop33.gif' width="90%">

</center>

Notes:

Let’s see exactly what is happening again in the animation below.

---

# Let’s apply what we learned\!

Notes: <br>
