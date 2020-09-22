---
type: slides
---

# Selecting a Single Column

---

``` python
df.loc[:, ['column name']]
```

<br>

``` python
cereal.loc[:, ['type']]
```

```out
    type
0   Cold
1   Cold
2   Cold
3   Cold
4   Cold
..   ...
72  Cold
73  Cold
74  Cold
75  Cold
76  Cold

[77 rows x 1 columns]
```

Notes:

Something we often do in data analysis is obtaining a single column from
a dataframe. We can again use `.loc[]` to do this which would look
something like this in general:

`dataframe.loc[:, ['column name']]`

So if we here want the column named `type` from our cereal dataframe we
could use the syntax:

`cereal.loc[:, ['type']]`

This seems a bit long winded and since we do this type of thing often.
Luckily, Pandas has provided a quicker syntax to use to do the same
thing.

---

``` python
df[['column name']]
```

<br>

``` python
cereal[['type']]
```

```out
    type
0   Cold
1   Cold
2   Cold
3   Cold
4   Cold
..   ...
72  Cold
73  Cold
74  Cold
75  Cold
76  Cold

[77 rows x 1 columns]
```

Notes:

Instead, selecting a single column can be done without using `.loc[]`
and we can just specify the dataframe name, followed by double square
brackets containing the column of interest.

`cereal[['type']]`

This makes the syntax for selecting the column `type` from the `cereal`
dataframe very easy.

---

# Let’s apply what we learned\!

Notes: <br>
