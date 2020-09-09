---
type: slides
---

# Python data structures: Dictionaries

Notes: <br>

---

## Dictionaries

A **dictionary** is a map between key-value pairs.

For example:

A house can have 3 bedrooms.  
‘bedrooms’ is the ***key*** and the number of bedrooms is the
***value***.

How does this look in terms of a data structure?

``` python
house = {'bedrooms': 3}
house
```

```out
{'bedrooms': 3}
```

Notes:

Dictionaries are used in different languages to look up definitions of
words.

Python has a data structure by the same name that replicates this
“lookup” action.

For example:

A house can have 3 bedrooms. bedroom is called the ***key*** and the
number of bedrooms is called the ***value***.

How does this look in terms of a data structure?

We use curly brackets and a colon that separates the key and its value.

---

``` python
house = {'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 2499999, 'date_sold': (1,3,2015)}
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 2499999, 'date_sold': (1, 3, 2015)}
```

``` python
condo = {'bedrooms' : 2, 
         'bathrooms': 1, 
         'kitchens' : 1, 
         'city'     : 'Burnaby', 
         'price'    : 699999, 
         'date_sold': (27,8,2011)
        }
condo
```

```out
{'bedrooms': 2, 'bathrooms': 1, 'kitchens': 1, 'city': 'Burnaby', 'price': 699999, 'date_sold': (27, 8, 2011)}
```

Notes:

This works with many different data types for the keys and values.

Here, we see the keys being of type `str` and the values being of type
`int`, `str` and even `tuples`.

The keys, which are the elements on the left of the colon, are unique
and cannot be duplicated since they are used to look up the value. The
values, which are the elements on the right of the colon, are not
unique.

We can see that in our `condo` dictionary where the keys `bathrooms` and
`kitchen` both have values of `1`.

---

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 2499999, 'date_sold': (1, 3, 2015)}
```

``` python
house['price']
```

```out
2499999
```

``` python
house['price'] = 7
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015)}
```

Notes:

We can access, or look up, a **value** of a dictionary with the **key**
in square brackets.

In this example, we obtain the value corresponding to the `price` key.

And since dictionaries are **mutable**, we can change the values. Let’s
change the existing `price` to `7`. That’s a bargain\!

---

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015)}
```

``` python
house['bed monster'] = True
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True}
```

``` python
house[9999] = ['age', 'old']
house[('trees', 'flower', 'vegetables')] = {'Garden': 3}
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True, 9999: ['age', 'old'], ('trees', 'flower', 'vegetables'): {'Garden': 3}}
```

Notes:

We can add to the dictionary in the same way as we edit them, but using
a new **key** name.

Here we add to the house dictionary a new key that respresents whether
or not a bed monster exists. We are giving this a value of `True`.

Keys are not limited to strings and can be many different data types
including numerical values and tuples (but they cannot be dictionaries
or lists).

Values can be of any type.

Here you can see that we have a key set as `9999` with a value of type
list `['age', 'old']`.

You have a lot of possibilities when making dictionaries.

---

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True, 9999: ['age', 'old'], ('trees', 'flower', 'vegetables'): {'Garden': 3}}
```

``` python
house.items()
```

```out
dict_items([('bedrooms', 3), ('bathrooms', 2), ('city', 'Vancouver'), ('price', 7), ('date_sold', (1, 3, 2015)), ('bed monster', True), (9999, ['age', 'old']), (('trees', 'flower', 'vegetables'), {'Garden': 3})])
```

Notes:

We can access all of the key-value pairs in a dictionary with the verb
`.items()`.

Let’s try it on our house dictionary.

Now we see tuples contained in a list, where each tuple contains the key
and its corresponding value.

---

## Dictionaries to Dataframes

|   | name   | height | diameter | flowering |
| -: | :----- | -----: | -------: | :-------- |
| 0 | Cherry |      7 |       12 | True      |
| 1 | Oak    |     20 |       89 | False     |
| 2 | Willow |     12 |       30 | True      |
| 3 | Fir    |     16 |       18 | False     |

``` python
data = { 'name': ['Cherry', 'Oak', 'Willow', 'Fir'], 
         'height': [7, 20, 12, 16], 
         'diameter': [12, 89, 30, 18], 
         'flowering': [True, False, True, False]}
         
forest = pd.DataFrame.from_dict(data)
forest
```

```out
     name  height  diameter  flowering
0  Cherry       7        12       True
1     Oak      20        89      False
2  Willow      12        30       True
3     Fir      16        18      False
```

Notes:

What about making dataframes from dictionaries?

We are lucky enough to have two ways of making data from a dictionary
using the verb `pd.DataFrame.from_dict()`.

First let’s try making this table into a dataframe where we insert our
data column-wise.

We can use the dictionary keys to represent the column names and the
dictionary values for the column values stored in a list.

---

|   | name   | height | diameter | flowering |
| -: | :----- | -----: | -------: | :-------- |
| 0 | Cherry |      7 |       12 | True      |
| 1 | Oak    |     20 |       89 | False     |
| 2 | Willow |     12 |       30 | True      |
| 3 | Fir    |     16 |       18 | False     |

``` python
data = {0: ['Cherry', 7, 12, True],
        1: ['Oak', 20, 89, False],
        2: ['Willow', 12, 30, True],
        3: ['Fir', 16, 18, False]}
column_names = ['name', 'height', 'diameter', 'flowering']

forest = pd.DataFrame.from_dict(data, orient='index', columns= column_names)
forest
```

```out
     name  height  diameter  flowering
0  Cherry       7        12       True
1     Oak      20        89      False
2  Willow      12        30       True
3     Fir      16        18      False
```

Notes:

The other option is to create the dataframe row-wise.

In this case we assign each row index as a dictionary key and the row
values as the dictionary’s values.

We use the argument `orient` to explain the keys are the `index` and the
argument `columns` to label our columns.

---

## Let’s add what we learned to our table

<br>

| Data Structure | preserves order | Mutable |    Symbol    | Can contain duplicates |
| :------------- | :-------------: | :-----: | :----------: | :--------------------: |
| `str`          |        ✓        |    ☓    | `''` or `""` |           ✓            |
| `list`         |        ✓        |    ✓    |     `[]`     |           ✓            |
| `tuple`        |        ✓        |    ☓    |     `()`     |           ✓            |
| `set`          |        ☓        |    ✓    |     `{}`     |           ☓            |
| `dictionary`   |        ✓        |    ✓    |    `{:}`     |  keys: ☓ , values: ✓   |

Notes:

Let’s add the dictionary data structure to our data structure summary
table.

---

# Let’s apply what we learned\!

Notes:

<br>
