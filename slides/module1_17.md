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

We can omit `loc` altogether and use double square brackets:

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
