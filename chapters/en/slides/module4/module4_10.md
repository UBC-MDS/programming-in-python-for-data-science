---
type: slides
---

# Python data structures: Dictionaries

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Dictionaries

Dictionaries are used in different languages to look up definitions of
words. Python has a data structure by the same name that replicates this
“lookup” action.

A **dictionary** is a map between key-value pairs. For example:

A house can have 3 bedrooms.  
bedroom is the ***key*** and the number of bedrooms is the ***value***.

How does this look in terms of a data structure?

``` python
house = {'bedrooms': 3}
house
```

```out
{'bedrooms': 3}
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

This can be carried across any type of key-value pairs, with any data
type:

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

The keys (elements on the left of the colon) cannot contain duplicates,
but the values (elements on the right of the colon) can.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 2499999, 'date_sold': (1, 3, 2015)}
```

We can access a **value** of a dictionary with the **key** in square
brackets:

``` python
house['price']
```

```out
2499999
```

And since dictionaries are **mutable**, we can change them:

``` python
house['price'] = 7
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015)}
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015)}
```

We can add to the dictionary in the same way as we edit them, but using
a new **key** name:

``` python
house['bed monster'] = True
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True}
```

Keys are not limited to strings and can be many different data types
including numerical values and tuples (but not dictionaries or lists).
Values can contain most datatypes and structure such as lists, tuples
and even a dictionary:

``` python
house[9999] = ['age', 'old']
house[('trees', 'flower', 'vegetables')] = {'Garden': 3}
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True, 9999: ['age', 'old'], ('trees', 'flower', 'vegetables'): {'Garden': 3}}
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We can access all of the key-value pairs in a dictionary with the verb
`.items()`.

``` python
house
```

```out
{'bedrooms': 3, 'bathrooms': 2, 'city': 'Vancouver', 'price': 7, 'date_sold': (1, 3, 2015), 'bed monster': True, 9999: ['age', 'old'], ('trees', 'flower', 'vegetables'): {'Garden': 3}}
```

Let’s try it on our house dictionary above:

``` python
house.items()
```

```out
dict_items([('bedrooms', 3), ('bathrooms', 2), ('city', 'Vancouver'), ('price', 7), ('date_sold', (1, 3, 2015)), ('bed monster', True), (9999, ['age', 'old']), (('trees', 'flower', 'vegetables'), {'Garden': 3})])
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Dictionaries to Dataframes

What about making dataframes from dictionaries?

We are lucky enough to have 2 ways of making data from a dictionary
using the verb `pd.DataFrame.from_dict()`.  
For example, let’s try making the following table.

|   | name   | height | diameter | flowering |
| -: | :----- | -----: | -------: | :-------- |
| 0 | Cherry |      7 |       12 | True      |
| 1 | Oak    |     20 |       89 | False     |
| 2 | Willow |     12 |       30 | True      |
| 3 | Fir    |     16 |       18 | False     |

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

|   | name   | height | diameter | flowering |
| -: | :----- | -----: | -------: | :-------- |
| 0 | Cherry |      7 |       12 | True      |
| 1 | Oak    |     20 |       89 | False     |
| 2 | Willow |     12 |       30 | True      |
| 3 | Fir    |     16 |       18 | False     |

We can use the each key in the dictionary to depict a column:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

|   | name   | height | diameter | flowering |
| -: | :----- | -----: | -------: | :-------- |
| 0 | Cherry |      7 |       12 | True      |
| 1 | Oak    |     20 |       89 | False     |
| 2 | Willow |     12 |       30 | True      |
| 3 | Fir    |     16 |       18 | False     |

Or use each key in the dictionary to depict a row.  
We use the argument `orient` to explain the keys are the `index` and the
argument `columns` to label our columns:

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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

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

</audio>

</html>
