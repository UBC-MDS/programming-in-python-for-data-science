---
type: slides
---

# Reshaping with Melt

Notes: <br>

---

Instead of converting a long dataframe to a wider one as we do in
`.pivot()`, we do the opposite and convert a wide dataframe into a
longer one.

<center>

<img src='/module3/melt_piv.png' width="80%">

</center>

Notes: In the last section we discussed how `pandas` provides 2
functions for reshaping data;
<a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
and
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
.

We are going to spend this next section discussing `.melt()` which is
simply the reverse transformation of `.pivot()`.

---

``` python
cereal
```

```out
          name mfr  calories  protein
0    Special K   K       110        6
1  Apple Jacks   K       110        2
2  Raisin Bran   K       120        3
3     Cheerios   G       110        6
4     Wheaties   G       100        3
```

Notes:

Let’s take a look at a subset of our the cereal data we’ve been working
with.

We can see there are 5 rows and 2 numerical columns; `calories` and
`protein`.  
Perhaps we would prefer if this was transformed into a long dataframe.

How would we do it?

---

<br> <br>

<center>

<img src='/module3/melt_right.png' width="100%">

</center>

Notes: We can use melt\!

---

## Melt

``` python
melted_cereal  = (cereal.melt(id_vars=['name', 'mfr'] , 
                              value_vars=['calories', 'protein'], 
                              var_name='nutrition', 
                              value_name='value')
                  )
melted_cereal
```

```out
          name mfr nutrition  value
0    Special K   K  calories    110
1  Apple Jacks   K  calories    110
2  Raisin Bran   K  calories    120
3     Cheerios   G  calories    110
4     Wheaties   G  calories    100
5    Special K   K   protein      6
6  Apple Jacks   K   protein      2
7  Raisin Bran   K   protein      3
8     Cheerios   G   protein      6
9     Wheaties   G   protein      3
```

Notes:

Let’s attempt to melt the `calories` and `protein` columns into a single
one named `nutrition` with the values expressed in a column named
`value`. Exactly like we started with when we used `.pivot()` in the
last section.

It’s not quite in the same order, but we can agree that its what we
want.

---

<center>

<img src='/module3/melt_right.png' width="60%">

</center>

``` python
melted_cereal  = (cereal.melt(id_vars=['name', 'mfr'], 
                            value_vars=['calories', 'protein'], 
                            var_name='nutrition', 
                            value_name='value')
                )
```

Notes:

Let’s try to understand what happened.

  - The identifying column and the columns we wanted to keep, are
    specified in the `id_vars` argument.
  - the columns `calories` and `protein` are called in `value_vars` and
    melted down into a single column named `nutrition`.
  - We named the new column using the argument `var_name`.
  - The calorie and protein measurements are housed in the new column
    named `value` that we name using the `value_name` argument.

Although this verb takes 4 arguments and pivot only takes 3, we do not
need to reset our index after melting.

---

# Let’s apply what we learned\!

Notes: <br>
