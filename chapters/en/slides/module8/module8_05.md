---
type: slides
---

# Multi-dimensional arrays

Notes:

<br>

---

## Creating 2D Arrays

``` python
my_array = np.array((1, 2, 3, 4))
my_array
```

```out
array([1, 2, 3, 4])
```

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

Notes:

We saw in the last set of slides that we can create 1D arrays using a
number of different functions such as `np.array()`.

We can also use the same functions to make multi-dimensional arrays
which are indicated by the multiple sets of square brackets `[[ ]]`.

In our 1D arrays, our arrays only have a single set of square brackets
whereas in multi-dimensional arrays we count multiple sets.

---

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
array([[0.12184308, 0.39989954],
       [0.84359779, 0.92901664],
       [0.77012836, 0.14674105],
       [0.75233526, 0.44412372]])
```

``` python
np.arange(0,12).reshape(3,4)
```

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

Notes:

Some of the functions that we use to create arrays have the ability for
us to specify them with multi-dimensions.

`np.zeros()` is an function that accepts a tuple with the shape of our
desired array.

In this case, an array with 3 rows and 4 columns.

In contract with `np.zeros()`, `np.random.rand()` accepts multiple
numeric values that correspond to the arrays shape.

So in the example, an array with 4 rows and 2 columns.

We can also use the verb `.reshape()` to tranform a 1D array into a
multi-dimension array.

---

## Array Shapes

<center>

<img src='/module8/arrays2.png' width="75%">

</center>

  - `.ndim`
  - `.shape`
  - `.size`

Notes:

We saw how to make multi-dimensional arrays but dimension is quite
different than what the shape of an array is.

Here are three main array nouns we need to know to understand the
characteristics of an array:

  - `.ndim`: the number of dimensions of an array

  - `.shape`: the number of elements in each dimension (like calling
    `len()` on each dimension)

  - `.size`: the total number of elements in an array (i.e., the product
    of `.shape`)

---

``` python
array1 = np.ones(4)
array1
```

```out
array([1., 1., 1., 1.])
```

``` python
array1.ndim
```

```out
1
```

``` python
array1.shape
```

```out
(4,)
```

``` python
array1.size
```

```out
4
```

Notes:

`array1` is an example of a 1d array.

We can use `.ndim` to check the number of dimensions and just as we
suspected it is 1.

We use `.shape` to find the number of elements in each dimension.

This returns a tuple with only 1 value which represents the 1 dimension.
This value gives the number of elements in the dimension.

Finally, `.size` will return the ***total*** number of values in the
array.

---

``` python
array_2d = np.ones((3, 2))
array_2d
```

```out
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
```

``` python
array_2d.ndim
```

```out
2
```

``` python
array_2d.shape
```

```out
(3, 2)
```

``` python
array_2d.size
```

```out
6
```

Notes:

Let’s try this again with a 2d array.

We can confirm the number of dimensions with `ndim`.

Here we have a 2 dimensional array as expected.

The shape of the array now consists of two elements, one for each
dimension.

The size is the product of the values in `.shape`.

---

``` python
array_2d.shape
```

```out
(3, 2)
```

``` python
len(array_2d.shape)
```

```out
2
```

``` python
np.prod(array_2d.shape)
```

```out
6
```

Notes:

If we have the `.shape` of the array, we can get both the `.ndim` of the
array with `len()`,

as well as the size by taking the product of the elements.

---

## Indexing and Slicing 2D arrays

``` python
arr2 = np.arange(0,12).reshape(3,4)
arr2
```

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

``` python
arr2[1, 2]
```

```out
6
```

``` python
arr2[1][2]
```

```out
6
```

Notes:

Slicing 2D arrays can be compared to slicing pandas dataframes (without
the `.iloc[]`).

Let’s say we want to select `6`. It’s located in row 1 and column 2
(remember that the index includes 0).

We could also do the same thing by putting the row and column index in
separate square brackets but it’s not recommended.

---

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

``` python
arr2[2]
```

```out
array([ 8,  9, 10, 11])
```

``` python
arr2[:,2]
```

```out
array([ 2,  6, 10])
```

``` python
arr2[:2,1:]
```

```out
array([[1, 2, 3],
       [5, 6, 7]])
```

Notes:

If we want a complete row of the array, we can specify with a single
number.

Here, we select the last row at index 2 that has the elements 8, 9, 10,
and 11.

If we only want a single column, we can use the same syntax we used with
`.iloc[]`.

This code selects the column at index 2, with the values 2, 6, and 10.

We can obtain specific slices by using a colon as well.

If we only wanted the first 2 rows and the last 3 columns, we could do
the following.

---

```out
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

``` python
arr2.T
```

```out
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

``` python

arr2[1,1] = 77777
arr2
```

```out
array([[    0,     1,     2,     3],
       [    4, 77777,     6,     7],
       [    8,     9,    10,    11]])
```

Notes:

If we want to
<a href=" https://en.wikipedia.org/wiki/Transpose" target="_blank">***transpose***</a>
our array we can use the verb, `.T`.

This converts the columns to rows and the columns to rows.

We can replace values in an array by specifying the element we wish to
replace in square brackets on the left side of the assignment operator
and our new desired value on the right of it.

Here we can see that that value 5, was replaced with 77,777.

---

# Let’s apply what we learned\!

Notes:

<br>
