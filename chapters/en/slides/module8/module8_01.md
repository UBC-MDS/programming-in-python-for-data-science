---
type: slides
---

# NumPy and 1D Arrays

Notes:

---

``` python
import numpy as np
```

Notes:

Although we have not formally introduced you to NumPy, the name may
sound familiar since we’ve been subtly hinting at its existence for a
little while now.

In the last Module, we’ve had you import this library for practice.

So what is NumPy?

---

## What is NumPy?

**NumPy** -\> **“Numerical Python extensions”**.

NumPy offers:

  - Arrays
  - Mathematical Constants
  - Mathematical Functions

Notes:

The name NumPy is derived from **“Numerical Python extensions”**.

NumPy is a Python library used primarily for computing involving
numbers. It is especially useful as it provides a multidimensional array
object, called an ***array***.

In addition, NumPy also offers numerous other mathematical functions
used in the domain of Linear Algebra and Calculus.

---

## So What is an Array?

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

``` python
type(my_array)
```

```out
<class 'numpy.ndarray'>
```

Notes:

A NumPy array is somewhat like a list.

They are considered their own data type.

We can see this by using `type` on an array.

---

``` python
my_list = [1,"hi"]
```

``` python
my_array = np.array((1, "hi"))
my_array
```

```out
array(['1', 'hi'], dtype='<U21')
```

Notes:

Soon, we’ll start to see that although lists and arrays appear quite
similar, they have some key differences.

A list can contain multiple data types, while an array cannot.

In this case, `1` was converted to a `'1'` in quotations, which
signifies that it is now a string.

---

## Creating 1D Arrays

``` python
my_array = np.array([1, 2, 3, 4])
my_array
```

```out
array([1, 2, 3, 4])
```

``` python
np.zeros(10)
```

```out
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

``` python
np.ones(4)
```

```out
array([1., 1., 1., 1.])
```

Notes:

We can make arrays from lists as well as tuples.

There are also several built-in NumPy functions that create different
arrays with patterns and requirements.

`np.zeros()` will create an array containing `0` for each element, and
the input argument specifies the size.

Here we specified 10, so our array has 10 elements.

Similarly, `np.ones()` does the same thing except with an array of
elements with `1` values.

Now we’ve specified 4 as the input, and so this array has 4 elements.

---

``` python
np.arange(5)
```

```out
array([0, 1, 2, 3, 4])
```

``` python
np.arange(0, 10, 2) 
```

```out
array([0, 2, 4, 6, 8])
```

Notes:

`np.arange()` similarly to `range()` can take 1, 2 or 3 input arguments
and will produce an array in a similar way that `range()` produces a
sequence.

If there are 3 input arguments, the first 2 are where the interval
values start and stop respectively, and the third argument gives the
step size between values.

---

``` python
np.linspace(1,5,10)
```

```out
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778, 3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

``` python
np.random.rand(5) 
```

```out
array([0.51939439, 0.84917657, 0.04400428, 0.68715007, 0.23389854])
```

Notes:

`np.linspace()` will produce an array containing the number of elements
specified by the 3rd argument’s value, containing values between the
first 2 arguments values.

For example, this code will produce 10, equally spaced values from 1 to
5.

Notice the elements in `np.linspace()` arrays are defaulted to type
`float`.

We can also produce an array with random values using
`np.random.rand()`.

Here, we have random numbers uniformly distributed from 0 to 1.

---

## Elementwise operations

``` python
array1 = np.ones(4)
array1
```

```out
array([1., 1., 1., 1.])
```

``` python
array2 = array1 + 1
array2
```

```out
array([2., 2., 2., 2.])
```

``` python
array1 + array2
```

```out
array([3., 3., 3., 3.])
```

``` python
array1 * array2
```

```out
array([2., 2., 2., 2.])
```

Notes:

Let’s talk about how operations are calculated with arrays.

We discussed that array and lists are similar but not quite the same.

Arrays are designed for convenience mathematically, so arrays operate in
an element-wise manner.

When we do operations, the operation is done to each element in the
array.

If we add to our array, 1 is added to each element in the array.

If we add two arrays together, the element at identical index positions
are added.

Similarly, if we multiply 2 arrays together, the index at each position
are multiplied together.

---

``` python
list_1 = [ 1, 1, 1, 1]
```

``` python
list_1 + 1
```

``` out
TypeError: can only concatenate list (not "int") to list

Detailed traceback: 
  File "<string>", line 1, in <module>
```

Notes:

This is much more convenient than using a list.

We can’t simply add 1 to a list. Instead, we get an error

---

``` python
list_1 = [ 1, 1, 1, 1]

list_2 =  [elem + 1 for elem in list_1]
list_2
```

```out
[2, 2, 2, 2]
```

``` python
list_3 = []

for index in range(len(list_1)):
  list_3.append(list_1[index] + list_2[index])
  
list_3
```

```out
[3, 3, 3, 3]
```

Notes:

If we wanted the same operations done with lists, we would have to use a
loop or list comprehension to obtain the same results.

---

## Slicing and Indexing 1D Arrays

``` python
arr = np.arange(10)
arr
```

```out
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

``` python
arr[7]
```

```out
7
```

``` python
arr[2:6]
```

```out
array([2, 3, 4, 5])
```

``` python
arr[-1]
```

```out
9
```

Notes:

When it comes to slicing, 1D arrays are sliced in the same manner that
lists are.

We can obtain an individual location by putting the index position in
square brackets.

And just like slicing dataframes with `.iloc[]`, when we want an
interval of values, the first value in the bracket is included, and the
last value is excluded.

To obtain elements from right to left, we use negative integers.

---

## Boolean Indexing

``` python
grade_array = np.array([98, 87, 103, 92, 67, 107, 78, 104, 85, 105])
grade_array
```

```out
array([ 98,  87, 103,  92,  67, 107,  78, 104,  85, 105])
```

``` python
threshold = np.array([98, 87, 103, 92, 67, 107, 78, 104, 85, 105]) > 100
threshold
```

```out
array([False, False,  True, False, False,  True, False,  True, False,  True])
```

``` python
grade_array[threshold] = 100
grade_array
```

```out
array([ 98,  87, 100,  92,  67, 100,  78, 100,  85, 100])
```

Notes:

Let’s now explore Boolean indexing.

Let’s take a 1D array that consists of 10 elements.

Remember that when we do most operations, it occurs in an element-wise
manner.

Perhaps we are grading exams that contain bonus marks.

The max possible allowed mark on the exam is 100%, so we must cap the
grades, so any mark greater than 100 is set to 100. First, we check
which values are greater than 100.

This produces an array containing Boolean values, which we store in the
object `threshold`.

The first and second elements are `False` since both 98 and 87 and not
larger than 100. However, the 3rd element is `True` since 103 is larger
than 100.

We now can replace all those values that have a `True` Boolean, with a
new value; in this case, let’s assign them a value of 100, the maximum
possible allowed grade.

---

``` python
new_grade_array = np.array([98,87,103, 92,67, 107, 78, 104, 85, 105])
new_grade_array
```

```out
array([ 98,  87, 103,  92,  67, 107,  78, 104,  85, 105])
```

``` python
new_grade_array[new_grade_array > 100] = 100
new_grade_array
```

```out
array([ 98,  87, 100,  92,  67, 100,  78, 100,  85, 100])
```

Notes:

We could also shorten the whole process and avoid making `threshold` by
using the following code.

You’ll notice that we use similar filtering square bracket notation that
we did using pandas\!

---

## Why NumPy?

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

``` python
type(cereal.loc[3,'calories'])
```

```out
<class 'numpy.int64'>
```

``` python
cereal['calories'].to_numpy()
```

```out
array([ 70, 120,  70,  50, 110, 110, 110, 130,  90,  90, 120, 110, 120, 110, 110, 110, 100, 110, 110, 110, 100, 110, 100, 100, 110, 110, 100, 120, 120, 110, 100, 110, 100, 110, 120, 120, 110, 110, 110, 140, 110, 100, 110, 100, 150, 150, 160, 100, 120, 140,  90, 130, 120, 100,  50,  50, 100, 100, 120, 100,  90, 110, 110,  80,  90,  90, 110, 110,  90, 110, 140, 100, 110, 110, 100, 100, 110])
```

Notes:

So why, NumPy?

Lists are often used with a similar purpose of arrays, but they are slow
to process.

Because of this, NumPy is used to create many other structures.

In fact, let’s refresh ourselves on certain values in a dataframe.

Remember when we obtained the data type of a specific value in a
dataframe?

We obtained this `<class 'numpy.int64'>`, which we originally ignored.

This is because a pandas dataframe is built off of a multidimensional
(2D specifically) array\!

We will explain more about multidimensional arrays in the next set of
slides.

We can actually convert an entire pandas column into an array pretty
easily using `np.to_numpy()`.

---

## NumPy Constants and Functions

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

Notes:

NumPy also offers an assortment of handy mathematical constants and
functions.

---

## NumPy Functions

``` python
np.prod([2, 3, 1])
```

```out
6
```

``` python
np.diff([2, 5, 20])
```

```out
array([ 3, 15])
```

``` python
np.log10(100)
```

```out
2.0
```

The full list of mathematical functions are available at this
<a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy
website</a>.

Notes:

NumPy’s functions include but are not limited to:

  - `np.prod()` which calculates the product of values in an array
  - `np.diff()` which calculates the difference between element (left
    element subtracted from the right element)
  - And other functions such as `np.log()` or trigonometric ones like
    `np.sin()`

---

# Let’s apply what we learned\!

Notes: <br>
