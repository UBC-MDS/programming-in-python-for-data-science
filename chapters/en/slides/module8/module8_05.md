---
type: slides
---

# Multi-dimensional Arrays

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Creating 2D Arrays

We saw in the last set of slides that we can create 1D arrays using a
number of different functions such as `np.array()`:

``` python
my_array = np.array((1, 2, 3, 4))
my_array
```

```out
array([1, 2, 3, 4])
```

We can also use the same functions to make multi-dimensional arrays
which are indicated by double square brackets `[[ ]]`:

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

Some of the functions that we use to create arrays have the ability for
us to specify them with multi-dimensions:

``` python
np.zeros((3,4))
```

```out
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

``` python
np.random.rand(4, 2) 
```

```out
array([[0.44178539, 0.53025423],
       [0.06305543, 0.95343231],
       [0.81202769, 0.07093157],
       [0.98354928, 0.26847232]])
```

and if not, can use the verb `.reshape()` to tranform a 1D array into a
multi-dimension array:

``` python
np.arange(0,12).reshape(3,4)
```

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Array Shapes

We saw how to make multi-dimensional arrays but dimension is quite
different than what the shape of an array is?

<center>

<img src='/module8/arrays2.png' width="80%">

</center>

here are three main array nouns we need to know to understand the
characteristics of an array:

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
array1 = np.ones(4)
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

## Indexing and Slicing 2D arrays

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

Let’s say we want to select `6`. It’s located in row 1 and column 2
(remember that the index includes 0).

``` python
arr2[1, 2]
```

```out
6
```

We could also do the same thing using this notation, but it’s not
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

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
