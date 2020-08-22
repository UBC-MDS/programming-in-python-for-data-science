---
type: slides
---

# Introduction to NumPy

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Although we have not formally introduced you to NumPy, The name may
sound familiar since we’ve been subtly hinting at its existence for a
little while now. In the last Module, we’ve had you import this library
for practice.

``` python
import numpy as np
```

So what is NumPy?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## What is Numpy

The name NumPy is derived from **“Numerical Python extensions”**.

NumPy is a Python library used primarily for numerical computing. It is
especially useful as it provides a multidimensional array object, called
an ***array***.

In addition, NumPy also offers numerous other mathematical functions
used in the domain of linear algebra and Calculus.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## So What is an Array?

A numpy array is somewhat like a list:

``` python
my_list = [1, 2, 3, 4, 5]
my_list
```

```out
[1, 2, 3, 4, 5]
```

``` python
my_array = np.array((1, 2, 3, 4, 5))
my_array
```

```out
array([1, 2, 3, 4, 5])
```

And arrays are considered their own data type:

``` python
type(my_array)
```

```out
<class 'numpy.ndarray'>
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

However, we’ll start to see that although lists and arrays appear quite
similar, they have some key differences. A list can contain multiple
data types:

``` python
my_list = [1,"hi"]
```

An array cannot:

``` python
my_array = np.array((1, "hi"))
my_array
```

```out
array(['1', 'hi'], dtype='<U21')
```

In this case, `1` was converted to `'1'` which is now a string.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Additionally, arrays are described as n-dimensional data structures -
meaning they can be any positive integer dimension.

<center>

<img src='/module8/arrays2.png' width="100%">

</center>

**Attribution:**
<a href="https://medium.com/datadriveninvestor/artificial-intelligence-series-part-2-numpy-walkthrough-64461f26af4f" target="_blank">medium.com</a>

We will discuss this further in the next set of slides.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Why NumPy?

  - Lists are often used with a similar purpose of arrays, but they are
    slow to process.
  - Because of this, NumPy is used to create many other structures.
  - In fact, let’s refresh ourselves on certain values in a dataframe:

<!-- end list -->

``` python
cereal.head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

Remember when we obtained the data type of a specific value in a
dataframe?

``` python
type(cereal.loc[3,'calories'])
```

```out
<class 'numpy.int64'>
```

We obtained this `<class 'numpy.int64'>` which we originally ignored.
It’s outputting a `numpy.int64` data type because pandas dataframes
are all built from NumPy arrays\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## NumPy Functions

NumPy also offers an assortment of handy mathematical constants and
functions.

<img src='/module8/pi.gif'  alt="404 image"/>

``` python
np.pi
```

```out
3.141592653589793
```

<img src='/module8/inf.gif'  alt="404 image"/>

``` python
np.inf
```

```out
inf
```

<img src='/module8/e.gif'  alt="404 image"/>

``` python
np.e
```

```out
2.718281828459045
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`np.prod()` calculates the product of values in an array:

``` python
np.prod([2, 3, 1])
```

```out
6
```

And `np.diff()` calculates the difference between element (left element
subtracted from the right element):

``` python
np.diff([7.0, 3.5, 4.0])
```

```out
array([-3.5,  0.5])
```

Other functions such as `np.log()` or trigonometric ones are also
available too:

``` python
np.log(np.e)
```

```out
1.0
```

The full list of mathematical functions are available at the
<a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy
website</a>.

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
