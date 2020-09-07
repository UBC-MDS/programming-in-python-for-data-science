---
type: slides
---

# Conditional value replacement and assignment

Notes: <br>

---

# Building on things we know

``` python
cereal = pd.read_csv('cereal.csv',
                  usecols=['name', 'mfr', 'type', 'calories', 'protein', 'weight', 'rating'])
cereal.head()
```

```out
                        name mfr  type  calories  protein  weight     rating
0                  100% Bran   N  Cold        70        4     1.0  68.402973
1          100% Natural Bran   Q  Cold       120        3     1.0  33.983679
2                   All-Bran   K  Cold        70        4     1.0  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4     1.0  93.704912
4             Almond Delight   R  Cold       110        2     1.0  34.384843
```

Notes:

So far, we have accumulated many different skills to wrangle our data.

One type of transformation that you may use often is replacing values
within a column depending on a certain condition.

Let’s bring in a smaller version of our cereal dataset.

In the dataframe, the manufacturer value “Q” isn’t that informative and
it might be easier to understand our data if we change all these values
to something more clear like “Quaker”.

This leads us to our task:

***Replace the `Q` manufacturer values with a new value of `Quaker`***

---

``` python
cereal[cereal['mfr'] == 'Q'].assign(mfr = 'Quaker')
```

```out
                  name     mfr  type  calories  protein  weight     rating
1    100% Natural Bran  Quaker  Cold       120        3     1.0  33.983679
10        Cap'n'Crunch  Quaker  Cold       120        1     1.0  18.042851
35    Honey Graham Ohs  Quaker  Cold       120        1     1.0  21.871292
41                Life  Quaker  Cold       100        4     1.0  45.328074
54         Puffed Rice  Quaker  Cold        50        1     0.5  60.756112
55        Puffed Wheat  Quaker  Cold        50        2     0.5  63.005645
56  Quaker Oat Squares  Quaker  Cold       100        4     1.0  49.511874
57      Quaker Oatmeal  Quaker   Hot       100        5     1.0  50.828392
```

Notes:

Our first instinct may be to first filter those rows using the technique
we learned in our last section.

From our new filtered selection, perhaps we could assign values of
“Quaker” to column `mfr` using similar code this.

The output looks like it did what we wanted but what happened to the
rest of our dataframe?

Remember that we only want to replace the values in our existing
dataframe and not create a new one.

When we use the `.assign()` verb like this, it creates a new dataframe
with only the rows that meet the condition `cereal['mfr'] == 'Q'` .

This is problematic since we still want the original dataframe and the
rows with `mfr` values not equal `Q`.

So what do we do?

---

# Building on more things we know

``` python
cereal.loc[73] 
```

```out
name           Trix
mfr               G
type           Cold
calories        110
protein           1
weight            1
rating      27.7533
Name: 73, dtype: object
```

``` python
cereal.loc[cereal['mfr'] == 'Q']
```

```out
                  name mfr  type  calories  protein  weight     rating
1    100% Natural Bran   Q  Cold       120        3     1.0  33.983679
10        Cap'n'Crunch   Q  Cold       120        1     1.0  18.042851
35    Honey Graham Ohs   Q  Cold       120        1     1.0  21.871292
41                Life   Q  Cold       100        4     1.0  45.328074
54         Puffed Rice   Q  Cold        50        1     0.5  60.756112
55        Puffed Wheat   Q  Cold        50        2     0.5  63.005645
56  Quaker Oat Squares   Q  Cold       100        4     1.0  49.511874
57      Quaker Oatmeal   Q   Hot       100        5     1.0  50.828392
```

Notes:

Remember our friend `.loc[]`? We are going to get reacquainted with it.

Similarly, to how `.loc[]` can select and return specified columns and
rows of the dataframe, it can filter on conditions too.

We are used to seeing code involving `.loc[]` like this.

But we’ll now get introduced to a new side of it when we use it to
filter as well.

We can use the same syntax, `cereal['mfr'] == 'Q'`, we normally would
when filtering. However, this time we wrap the whole thing within
`.loc[]`.

---

``` python
cereal.loc[cereal['mfr'] == 'Q', 'mfr']
```

```out
1     Q
10    Q
35    Q
41    Q
54    Q
55    Q
56    Q
57    Q
Name: mfr, dtype: object
```

``` python
cereal.loc[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Notes:

Some people may be asking, “Why don’t we do all our filtering like this
then?” Well, the answer is, you can, but we prefer not to.

Filtering without `.loc[]` is a bit more readable.

Let’s concentrate back on our task of only replacing `mfr` values equal
to `Q` to `Quaker`.

How can `.loc[]` help us with this?

Unlike our earlier approach, `.loc[]` accepts more arguments within it.

We have the ability to specify not only the target rows matching a
specific condition but our column of interest as well.

Once we have that, we can then assign these rows the new values `Quaker`
in the `mfr` column.

Wait\! Nothing was outputted with our code\! What happened?

---

``` python
cereal
```

```out
                         name     mfr  type  calories  protein  weight     rating
0                   100% Bran       N  Cold        70        4     1.0  68.402973
1           100% Natural Bran  Quaker  Cold       120        3     1.0  33.983679
2                    All-Bran       K  Cold        70        4     1.0  59.425505
3   All-Bran with Extra Fiber       K  Cold        50        4     1.0  93.704912
4              Almond Delight       R  Cold       110        2     1.0  34.384843
..                        ...     ...   ...       ...      ...     ...        ...
72                    Triples       G  Cold       110        2     1.0  39.106174
73                       Trix       G  Cold       110        1     1.0  27.753301
74                 Wheat Chex       R  Cold       100        3     1.0  49.787445
75                   Wheaties       G  Cold       100        3     1.0  51.592193
76        Wheaties Honey Gold       G  Cold       110        2     1.0  36.187559

[77 rows x 7 columns]
```

Notes:

Let’s take a look at the original dataframe.

We can now see that the `Q` manufacturer values have changed to
`Quaker`.

When we use this syntax, we do not need to save the results in a new
object like we had to with `.assign()` and `.drop()`.

Let’s discuss what really is happening behind the scenes.

---

``` python
cereal['mfr'] == 'Q'
```

```out
0     False
1     False
2     False
3     False
4     False
      ...  
72    False
73    False
74    False
75    False
76    False
Name: mfr, Length: 77, dtype: bool
```

Notes:

Remember what the condition `cereal['mfr'] == 'Q'` returns?

It produces an object containing all the rows with True/False values
depending on whether or not the row meets the condition.

---

<img src='/module2/tf_quaker.png'  alt="404 image" />

Notes:

Essentially our code is finding the rows with `True` values and
replacing the values in the `mfr` colum with the new value of `Quaker`.

---

1.  
<!-- end list -->

``` python
cereal.loc[cereal['mfr'] == 'Q']
```

<br>

2.  
<!-- end list -->

``` python
cereal.loc[cereal['mfr'] == 'Q', 'mfr'] 
```

<br>

3.  
<!-- end list -->

``` python
cereal.loc[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Notes:

You can split up how this code works into 3 steps:

1.  We use `.loc[]` to find the rows meeting certain conditions.

2.  We next indicate which column we wish to access.

3.  Once we have obtained our desired rows and the column which we are
    editing, we assign a value.

---

``` python
cereal[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

``` out
TypeError: 'Series' objects are mutable, thus they cannot be hashed

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.7/site-packages/pandas/core/frame.py", line 2938, in __setitem__
    self._set_item(key, value)
  File "/usr/local/lib/python3.7/site-packages/pandas/core/frame.py", line 3000, in _set_item
    value = self._sanitize_column(key, value)
  File "/usr/local/lib/python3.7/site-packages/pandas/core/frame.py", line 3666, in _sanitize_column
    if broadcast and key in self.columns and value.ndim == 1:
  File "/usr/local/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 3899, in __contains__
    hash(key)
  File "/usr/local/lib/python3.7/site-packages/pandas/core/generic.py", line 1799, in __hash__
    f"{repr(type(self).__name__)} objects are mutable, "
```

Notes:

Does this work without using `.loc[]`?

Let’s give it a try.

Unfortunately, we are not able to replace values in this manner and it
results in an error since filtering this way does not allow us to
specify a column.

---

# Replacing with inequalities.

``` python
cereal.loc[cereal['protein'] >= 3, 'protein_level']  = 'high' 
```

``` python
cereal.loc[cereal['protein'] < 3, 'protein_level']  = 'low' 
```

Notes:

This syntax using `.loc[]` also works for inequality conditions.

If we are replacing numerical values with characters or words (or vice
versa) we need to assign our desired values to a **new column** and not
the existing one, because the column type will be different.

Perhaps we want just two categories for protein levels - “high” and
“low”.

Any cereal above 3 grams of protein will be considered a “high” protein
level and anything less, as a “low” protein level.

Let’s assign the “high” protein values first.

The only difference here from earlier is we now use an inequality for
our condition and we designate a new column name instead of an existing
one.

Let’s save the values in a column named `protein_level`.

Next by the “low” values.

---

``` python
cereal
```

```out
                         name     mfr  type  calories  protein  weight     rating protein_level
0                   100% Bran       N  Cold        70        4     1.0  68.402973          high
1           100% Natural Bran  Quaker  Cold       120        3     1.0  33.983679          high
2                    All-Bran       K  Cold        70        4     1.0  59.425505          high
3   All-Bran with Extra Fiber       K  Cold        50        4     1.0  93.704912          high
4              Almond Delight       R  Cold       110        2     1.0  34.384843           low
..                        ...     ...   ...       ...      ...     ...        ...           ...
72                    Triples       G  Cold       110        2     1.0  39.106174           low
73                       Trix       G  Cold       110        1     1.0  27.753301           low
74                 Wheat Chex       R  Cold       100        3     1.0  49.787445          high
75                   Wheaties       G  Cold       100        3     1.0  51.592193          high
76        Wheaties Honey Gold       G  Cold       110        2     1.0  36.187559           low

[77 rows x 8 columns]
```

Notes:

Let’s take a look at the dataframe now.

---

## Creating new columns

``` python
oz_to_g = 28.3495
cereal['weight_g'] = cereal['weight'] * oz_to_g
cereal
```

```out
                         name     mfr  type  calories  protein  weight     rating protein_level  weight_g
0                   100% Bran       N  Cold        70        4     1.0  68.402973          high   28.3495
1           100% Natural Bran  Quaker  Cold       120        3     1.0  33.983679          high   28.3495
2                    All-Bran       K  Cold        70        4     1.0  59.425505          high   28.3495
3   All-Bran with Extra Fiber       K  Cold        50        4     1.0  93.704912          high   28.3495
4              Almond Delight       R  Cold       110        2     1.0  34.384843           low   28.3495
..                        ...     ...   ...       ...      ...     ...        ...           ...       ...
72                    Triples       G  Cold       110        2     1.0  39.106174           low   28.3495
73                       Trix       G  Cold       110        1     1.0  27.753301           low   28.3495
74                 Wheat Chex       R  Cold       100        3     1.0  49.787445          high   28.3495
75                   Wheaties       G  Cold       100        3     1.0  51.592193          high   28.3495
76        Wheaties Honey Gold       G  Cold       110        2     1.0  36.187559           low   28.3495

[77 rows x 9 columns]
```

Notes:

You may have noticed we did not use `.assign()` to create our new
column.

That’s because as we mentioned earlier, when we use `.assign()` it
creates a brand new dataframe.

When we are replacing values, we don’t want a new dataframe and instead,
we just want to alter the current values in the existing dataframe.

When we are not doing conditional value replacement, we could create new
columns with a similar syntax. Take the example of converting the weight
from ounces into grams and making a new column named `weight_g`.

This code edits the existing dataframe `cereal` instead of creating a
new one.

We prefer to use `.assign()` where possible as it can help avoid
unexpected errors and performance issues.

---

# Let’s apply what we learned\!

Notes:

<br>
