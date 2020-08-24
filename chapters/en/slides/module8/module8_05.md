---
type: slides
---

# NumPy Arrays

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Creating Arrays

We saw in the last set of slides that we can create arrays using
`np.array()`:

``` python
my_array = np.array((1, 2, 3, 4))
my_array
```

```out
array([1, 2, 3, 4])
```

We can also make them from lists instead of tuples too:

``` python
my_array = np.array([1, 2, 3, 4])
my_array
```

```out
array([1, 2, 3, 4])
```

We can also have multi-dimensional arrays which are indicated by double
square brackets `[[ ]]`:

``` python
list_2d = [[1, 2], [3, 4], [5, 6]]
array_2d = np.array(list_2d)
array_2d
```

```out
array([[1, 2],
       [3, 4],
       [5, 6]])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

There are also several built-in NumPy functions that create different
arrays with patterns and requirements:

`np.zeros()` will create an array containing `0` for each element and
the input argument specifies the size:

``` python
np.zeros(10)
```

```out
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

Similarly, `np.ones()` does the same thing except with an array of
elements with `1` values:

``` python
np.ones(4)
```

```out
array([1., 1., 1., 1.])
```

`np.arange()` similarly to `range()` can take 1, 2 or 3 input arguments
and will produce an array in a similar way that `range()` produces a
sequence.

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`np.linspace()` will produce an array containing the number of elements
specified by the 3rd argument’s value, containing values between the
first 2 arguments values. Example: 20, equally spaced values from 1 to
5:

``` python
np.linspace(1,5,20)
```

```out
array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526, 2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684, 3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842, 4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
```

The elements in `np.linspace()` arrays are defaulted to type `float`.  
We can also produce an array with random values using
`np.random.rand()`.  
Example: Random numbers uniformly distributed from 0 to 1

``` python
np.random.rand(5) 
```

```out
array([0.97677871, 0.72129283, 0.73853755, 0.19682806, 0.57534867])
```

We can also specify the number of dimensions for it:

``` python
np.random.rand(4, 2) 
```

```out
array([[0.77503175, 0.65381718],
       [0.10945072, 0.75250849],
       [0.32366273, 0.45019435],
       [0.52063676, 0.93510855]])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Elementwise operations

As we saw in Exercise 4, that arrays operate in an elementwise manner.

When we do many operations, the operation is done to each element in the
array.

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
array1 - array2
```

```out
array([-1., -1., -1., -1.])
```

``` python
array1 * array2
```

```out
array([2., 2., 2., 2.])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Array Shapes

<center>

<img src='/module8/arrays2.png' width="80%">

</center>

As we just saw above, arrays can be of any dimension, shape and size.

In fact, there are three main array nouns we need to know to understand
the characteristics of an array:

  - `.ndim`: the number of dimensions of an array

  - `.shape`: the number of elements in each dimension (like calling
    `len()` on each dimension)

  - `.size`: the total number of elements in an array (i.e., the product
    of `.shape`)

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

`array1` is an example of a 1d array:

``` python
array1
```

```out
array([1., 1., 1., 1.])
```

We can use `.ndim` to check the number of dimensions and just as we
suspected it is 1:

``` python
array1.ndim
```

```out
1
```

We use `.shape` to find the number of elements in each dimension:

``` python
array1.shape
```

```out
(4,)
```

This returns a tuple with only 1 value which represents the 1 dimension.
Finally, `.size` will return the ***total*** number of values in the
array.

``` python
array1.size
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

Let’s try this again with a 2d array.

``` python
array_2d = np.ones((3, 2))
array_2d
```

```out
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
```

The number of square brackets in an array depicts how many dimensions an
array consists of.

We can confirm the number of dimensions with `ndim`:

``` python
array_2d.ndim
```

```out
2
```

The shape of the array now consists of two elements, one for each
dimension:

``` python
array_2d.shape
```

```out
(3, 2)
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
array_2d.shape
```

```out
(3, 2)
```

And the size is the product of the values in `.shape`:

``` python
array_2d.size
```

```out
6
```

If we have the `.shape()` of the array, we can get both the `.ndim` of
the array:

``` python
len(array_2d.shape)
```

```out
2
```

as well as the size:

``` python
np.prod(array_2d.shape)
```

```out
6
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Indexing and Slicing

1D arrays are sliced in the same manner that lists are.

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

The first value is included and the last value is excluded:

``` python
arr[2:6]
```

```out
array([2, 3, 4, 5])
```

To obtain elements from right to left, we use negative integers:

``` python
arr[-1]
```

```out
9
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Slicing 2D arrays can be compared to slicing pandas dataframes (without
the `.iloc[]`).

``` python
arr2 = np.arange(0,12).reshape(3,4)
arr2
```

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

In the code above, `.reshape` simply reshapes the original 1D array to a
2D array with a 3 x 4 shape.

Let’s say we want to select `6`. It’s located in row 1 and column 2
(remember that the index includes 0).

``` python
arr2[1, 2]
```

```out
6
```

We could also do the same thing using this notation but, it’s not
recommended.

``` python
arr2[1][2]
```

```out
6
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

If we want a complete row of the array, we can specify with a single
number:

``` python
arr2[2]
```

```out
array([ 8,  9, 10, 11])
```

And if we only want a single column we can use the same syntax we used
with `.iloc[]`:

``` python
arr2[:,2]
```

```out
array([ 2,  6, 10])
```

We can obtain specific slices by using a colon as well. If we only
wanted the first 2 rows and the last 3 columns, we could do the
following:

``` python
arr2[:2,1:]
```

```out
array([[1, 2, 3],
       [5, 6, 7]])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can take the
<a href=" https://en.wikipedia.org/wiki/Transpose" target="_blank">***transpose***</a>
of the array by using `.T`:

``` python
arr2.T
```

```out
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

This converts the columns to rows and the columns to rows.

We can replace values in an array with the assignment operator:

``` python

arr2[1,1] = 77777
arr2
```

```out
array([[    0,     1,     2,     3],
       [    4, 77777,     6,     7],
       [    8,     9,    10,    11]])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Boolean Indexing

Let’s take a 1D array that consists of 10 decimal elements.

``` python
decimal_array = np.random.rand(10)
decimal_array
```

```out
array([0.96676786, 0.59233035, 0.85265099, 0.49111948, 0.36634197, 0.61002155, 0.7001396 , 0.28430043, 0.11799399, 0.30684585])
```

Remember that when we do most operations, it occurs in an element-wise
manner:

``` python
decimal_array + 1
```

```out
array([1.96676786, 1.59233035, 1.85265099, 1.49111948, 1.36634197, 1.61002155, 1.7001396 , 1.28430043, 1.11799399, 1.30684585])
```

Let’s assign a threshold and find all the elements in `decimal_array`
greater than 0.5. We can name this new array that is made of Boolean
values `threshold`:

``` python
threshold = decimal_array > 0.5
threshold
```

```out
array([ True,  True,  True, False, False,  True,  True, False, False, False])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We now can replace all those values that have a `True` Boolean, a new
value, in this case let’s assign them a value of 0.5:

``` python
decimal_array[threshold] = 0.5 
decimal_array
```

```out
array([0.5       , 0.5       , 0.5       , 0.49111948, 0.36634197, 0.5       , 0.5       , 0.28430043, 0.11799399, 0.30684585])
```

We could also shorten the whole process and avoided making `threshold`
by using the following code:

``` python
new_decimal_array = np.random.rand(4)
new_decimal_array
```

```out
array([0.94830193, 0.51407743, 0.98474613, 0.85593942])
```

``` python
new_decimal_array[new_decimal_array>0.5] = 0.5
new_decimal_array
```

```out
array([0.5, 0.5, 0.5, 0.5])
```

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
