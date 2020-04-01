---
type: slides
---

# Selecting using df.loc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

So to answer the question where we left off, after giving it a try, you
know that rearranging column or row order is as easy as changing the
column name order\!

So if we wanted the rows to be in the order `Wheaties`, `Trix` and
`Clusters` and columns in the order `type`, `rating` and `sugars` from
our cereal dataframe, we would obtain it like
so:

``` python
df.loc[ ["Wheaties", "Trix", "Clusters"] , ["type", "rating", "sugars"] ]
```

```out
          type     rating  sugars
name                             
Wheaties  Cold  51.592193       3
Trix      Cold  27.753301      12
Clusters  Cold  40.400208       7
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Selecting a Single Column

Something extremely useful is getting a single column from a dataframe.
We can use `df.loc[]` which would look something like this:

    df.loc[ : , [ "column-name"] ]

For example, if we wanted the column `type` from our cereal dataframe.

``` python
df.loc[ : , [ "type"] ]
```

```out
                           type
name                           
100% Bran                  Cold
100% Natural Bran          Cold
All-Bran                   Cold
All-Bran with Extra Fiber  Cold
Almond Delight             Cold
...                         ...
Triples                    Cold
Trix                       Cold
Wheat Chex                 Cold
Wheaties                   Cold
Wheaties Honey Gold        Cold

[77 rows x 1 columns]
```

But there is a better way of doing this.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

You can omit `loc` altogether and use double square brackets:

``` python
df[['column-name']]
```

Selecting the column `type` would be as simple as so:

``` python
df[['type']]
```

```out
                           type
name                           
100% Bran                  Cold
100% Natural Bran          Cold
All-Bran                   Cold
All-Bran with Extra Fiber  Cold
Almond Delight             Cold
...                         ...
Triples                    Cold
Trix                       Cold
Wheat Chex                 Cold
Wheaties                   Cold
Wheaties Honey Gold        Cold

[77 rows x 1 columns]
```

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
