---
type: slides
---

# Automatic style formatting

Notes: <br>

---

<br>

<center>

<img src='/module7/comp_hum.png'  width = "90%" alt="404 image" />

</center>

<a href="https://unsplash.com/@clemhlrdt" target="_blank">Photos/Images:
Clement H</a> <br>
<a href="www.wocintechchat.com" target="_blank">Photos/Images by
\#WOCinTech/\#WOCinTech Chat</a>.

Notes:

We’ve talked a lot about how to make sure our code works and that it
does what we want it to, but just because it works, doesn’t mean it’s
maintainable\!

Code has two “users” - the computer (which turns it into machine
instructions) and humans, who will likely read and/or modify the code in
the future.

This is why it’s important to make your code suitable to that second
audience, humans.

Writing readable and understandable code is important when sharing code
to other users and reading back as your future self\!

Remember: “Code is read much more often than it is written.”

---

### PEP8

PEP8 is a style guide that recommends formatting such as:

  - Indenting using 4 spaces
  - Having whitespace around operators, e.g. x = 1 not x=1
  - Avoiding extra whitespace such as f(1), not f (1)
  - Single and double quotes for strings, but only using “””triple
    double quotes”””, not ‘’’triple single quotes’’’
  - Variable and function names using underscores\_between\_words

### flake8

<br>

<center>

<img src='/module7/flake8.png'  width = "45%" alt="404 image" />

</center>

Notes:

PEP8 is one of the many style guides used in programming.

PEP8 recommends formatting such as:

  - Indenting using 4 spaces
  - Having whitespace around operators, e.g. x = 1 not x=1
  - But avoiding extra whitespace such as f(1), not f (1)
  - Single and double quotes both fine for strings, but only using
    “””triple double quotes”””, not ‘’’triple single quotes’’’
  - Variable and function names use underscores\_between\_words

We can check our code to see if it complies with PEP8 formatting using a
Python library called `flake8`.

Think of it as a grammar check but for your code.

`flake8` will tell us how and where our code is formatted poorly but it
won’t make any changes to it. That is up to us.

We will show you shortly, how to use `flake8` in your Jupyter notebooks.

---

## Black

**Before `black`**

``` python
def exponent_a_list(numerical_list   ,   exponent   =      2):

    if type(numerical_list         ) is    not list   :
                raise Exception(     "You are not using a list for the numerical_list input."   
                )

    new_exponent_list   = list()
    for   number_in_new_exponent_list in              numerical_list:
                new_exponent_list.append(                  number_in_new_exponent_list **  exponent  )
    return new_exponent_list
```

**After `black`**

``` python
def exponent_a_list(numerical_list, exponent=2):

    if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")

    new_exponent_list = list()
    for number_in_new_exponent_list in numerical_list:
        new_exponent_list.append(number_in_new_exponent_list ** exponent)
    return new_exponent_list
```

Notes:

Unlike PEP8 which is a style guide and flake8 which just tells you where
your code needs changes, `black` is a tool that will format your code.

Black will mostly follow the PEP8 style guide but with a few
differences.

When you use `black` with your code, you are wiping it of bad formatting
like trailing whitespace and poor indentation.

---

**After `black`**

``` python
def exponent_a_list(numerical_list, exponent=2):

    if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")

    new_exponent_list = list()
    for number_in_new_exponent_list in numerical_list:
        new_exponent_list.append(number_in_new_exponent_list ** exponent)
    return new_exponent_list
```

<br> <br> **Checking with `flake8` again**

<img src='/module7/flake8again.png'  width = "45%" alt="404 image" />

Notes:

It’s important to know that `flake8` and our formatter `black` are using
slightly different rules. Even after black is run on our code, flake8
still may point out issues and complain that it isn’t stylized
correctly.

We’re not going to worry about that for now. It can be fixed by
customizing `flake8` but that’s outside the scope of this course.

Now let’s see how we can use both of these in a Jupyter notebook.

---

Notes:

---

Notes:

---

# Let’s apply what we learned\!

Notes: <br>
