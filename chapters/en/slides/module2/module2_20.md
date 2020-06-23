---
type: slides
---

# Conditional value replacement and assignment

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Building on things we know

So far, we have accumulated many different skills to wrangle our data.
One type of transformation that you may use often is replacing values
within a column depending on a certain condition. Let’s bring in a
smaller version of our cereal dataset.

``` python
df = pd.read_csv('cereal.csv',
                  usecols=['name', 'mfr', 'type', 'calories', 'protein', 'weight', 'rating'])
df.head()
```

```out
                        name mfr  type  calories  protein  weight     rating
0                  100% Bran   N  Cold        70        4     1.0  68.402973
1          100% Natural Bran   Q  Cold       120        3     1.0  33.983679
2                   All-Bran   K  Cold        70        4     1.0  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4     1.0  93.704912
4             Almond Delight   R  Cold       110        2     1.0  34.384843
```

In the dataframe, the manufacturer value “Q” isn’t that informative and
it might be easier to understand our data if we change all these values
to something more complete like “Quaker”.

This leads us toour task:  
***Replace the “Q” manufacturer values, with a new value of “Quaker”***

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Our first instinct may be to first filter those rows using the technique
we learned in our last section. From our new filtered selection, perhaps
we could assign values of “Quaker” to column `mfr` using similar code to
below:

``` python
df[df['mfr'] == 'Q'].assign(mfr = 'Quaker')
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

That looks like it did what we want but what happened to the rest of our
dataframe? Remember that we only want to replace the values in our
existing dataframe and not create a new one.

When we use the `.assign()` verb, it creates a new dataframe with only
the rows that meet the condition `df['mfr'] == 'Q'` . This is
problematic since we still want the original dataframe and the rows with
`mfr` values not equal “Q”. So what do we do?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Building on more things we know

Remember our friend `.loc[]`? We are going to get reacquainted with it.
Similarly, to how `.loc[]` can select and return specified columns and
rows of the dataframe, it can filter on conditions too.  
We are used to seeing code involving `.loc[]` like this:

``` python
df.loc[73] 
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

But we get introduced to a new side of it when we use it to filter as
well.

``` python
df.loc[df['mfr'] == 'Q']
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

We can use the same syntax (`df['mfr'] == 'Q'`) we normally would when
filtering, however this time, we wrap the whole thing within `.loc[]`

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Some people may be asking, “Why don’t we do all our filtering like this
then?” Well, the answer is, you can, but we prefer not to. Filtering
without `.loc[]` is a bit more readable and more efficient when doing
analysis.

Let’s concentrate back on our task of only replacing `mfr` values equal
to “Q” to “Quaker”. How can `.loc[]` help us with this?

Unlike with filtering, `.loc[]` accepts more arguments within it. We
have the ability to specify not only the target rows matching a specific
condition but our column of interest as well.

``` python
df.loc[df['mfr'] == 'Q', 'mfr']
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

Once we have that, we can then assign these rows the new values ‘Quaker’
in the `mfr` column.

``` python
df.loc[df['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Wait\! Nothing was outputted\! What happened?

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a look at the original dataframe

``` python
df.head(14)
```

```out
                         name     mfr  type  calories  protein  weight     rating
0                   100% Bran       N  Cold        70        4    1.00  68.402973
1           100% Natural Bran  Quaker  Cold       120        3    1.00  33.983679
2                    All-Bran       K  Cold        70        4    1.00  59.425505
3   All-Bran with Extra Fiber       K  Cold        50        4    1.00  93.704912
4              Almond Delight       R  Cold       110        2    1.00  34.384843
5     Apple Cinnamon Cheerios       G  Cold       110        2    1.00  29.509541
6                 Apple Jacks       K  Cold       110        2    1.00  33.174094
7                     Basic 4       G  Cold       130        3    1.33  37.038562
8                   Bran Chex       R  Cold        90        2    1.00  49.120253
9                 Bran Flakes       P  Cold        90        3    1.00  53.313813
10               Cap'n'Crunch  Quaker  Cold       120        1    1.00  18.042851
11                   Cheerios       G  Cold       110        6    1.00  50.764999
12      Cinnamon Toast Crunch       G  Cold       120        1    1.00  19.823573
13                   Clusters       G  Cold       110        3    1.00  40.400208
```

We can now see that the `Q` manufacturer values have changed to
`Quaker`.

When we use this syntax, we do not need to save the results in a new
object name like we had to with `.assign()` and `.drop()`.

Let’s discuss what really is happening behind the scenes.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Remember what the condition `df['mfr'] == 'Q'` returns?

It produces a dataframe containing all the rows with True/False values
depending on if the row meets the condition.

``` python
df['mfr'] == 'Q'
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

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Essentially our code is finding the rows with `True` values and
replacing the values in the `mfr` column (like we specified) the new
value of ‘Quaker’.

<img src='/module2/tf_quaker.png'  alt="404 image" />

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

You can split up how this code works into 3 steps:

1.  We use `.loc[]` to find the rows specifying certain conditions:

<!-- end list -->

``` python
df.loc[df['mfr'] == 'Q']
```

2.  We next indicate which column we wish to replace with the new
    values:

<!-- end list -->

``` python
df.loc[df['mfr'] == 'Q', 'mfr'] 
```

3.  Once we have obtained our desired rows and the column which we are
    editing, we assign a value to the row meeting the condition (a
    “True” value):

<!-- end list -->

``` python
df.loc[df['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Does this work without using `.loc[]`? Let’s give it a try.

``` python
df[df['mfr'] == 'Q', 'mfr'] = 'Quaker'
```

``` out
TypeError: 'Series' objects are mutable, thus they cannot be hashed
```

Unfortunately, we are not able to replace values in this manner and it
results in an error since filtering this way does not allow us to
specify columns like this.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Replacing with Inequalities.

This syntax also works for inequality conditions.

If we are replacing numerical values with characters or words (or vice
versa) we need to assign our desired values to a **new column** and not
the existing one.  
Perhaps we want just 2 categories for protein levels - “high” and “low”.
Any cereal above 3 grams of protein will be considered a “high” protein
level and anything less, as a “low” protein level.

Let’s assign the “high” protein values first. The only difference here
from earlier is we now use an inequality for our condition and we
designate a new column name instead of an existing one. Let’s save the
values in a column named `protein_level`.

``` python
df.loc[df['protein'] >= 3, 'protein_level']  = 'high' 
```

Next by the “low” values.

``` python
df.loc[df['protein'] < 3, 'protein_level']  = 'low' 
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s take a look at the dataframe now:

``` python
df.head(10)
```

```out
                        name     mfr  type  calories  protein  weight     rating protein_level
0                  100% Bran       N  Cold        70        4    1.00  68.402973          high
1          100% Natural Bran  Quaker  Cold       120        3    1.00  33.983679          high
2                   All-Bran       K  Cold        70        4    1.00  59.425505          high
3  All-Bran with Extra Fiber       K  Cold        50        4    1.00  93.704912          high
4             Almond Delight       R  Cold       110        2    1.00  34.384843           low
5    Apple Cinnamon Cheerios       G  Cold       110        2    1.00  29.509541           low
6                Apple Jacks       K  Cold       110        2    1.00  33.174094           low
7                    Basic 4       G  Cold       130        3    1.33  37.038562          high
8                  Bran Chex       R  Cold        90        2    1.00  49.120253           low
9                Bran Flakes       P  Cold        90        3    1.00  53.313813          high
```

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Creating new columns

You may have noticed we did not use `.assign()` to create our new
column. That’s because as we mentioned earlier, when we use `.assign()`
it creates a brand new dataframe. When we are replacing values, we don’t
want a new dataframe and instead, we just want to alter the current
values in the existing dataframe.

When we are not doing conditional value replacement, we could create new
columns with a similar syntax. Take the example of converting the weight
from ounces into grams and making a new column named `weight_g`.

``` python
oz_to_g = 28.3495
df['weight_g'] = df['weight']*oz_to_g
df.head()
```

```out
                        name     mfr  type  calories  protein  weight     rating protein_level  weight_g
0                  100% Bran       N  Cold        70        4     1.0  68.402973          high   28.3495
1          100% Natural Bran  Quaker  Cold       120        3     1.0  33.983679          high   28.3495
2                   All-Bran       K  Cold        70        4     1.0  59.425505          high   28.3495
3  All-Bran with Extra Fiber       K  Cold        50        4     1.0  93.704912          high   28.3495
4             Almond Delight       R  Cold       110        2     1.0  34.384843           low   28.3495
```

This syntax is editing the existing dataframe `df` instead of creating a
new one. We prefer `.assign()` where possible since it provides more
flexibility. It gives us an opportunity to name the new dataframe
something different and keep our original dataframe untransformed. This
prevents the need to re-read in our data to get our original dataframe
back (which could take a long time if the dataset is large).

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>
