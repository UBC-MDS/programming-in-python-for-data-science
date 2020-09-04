---
type: slides
---

# Chaining notation

Notes:

<br>

---

## What is Chaining?

<br>

<br>

<img src='/module2/chainsfinal.png' width="110%" alt="404 image" />  
[Attribution](https://unsplash.com/photos/42ui88Qrxhw)

Notes:

Up until now, when we perform multiple actions on an object, we have
been saving the results under a new object name. Chaining allows us to
do multiple actions in a single line of code without the need to save
each action in an intermediate object.

You can imagine that we are linking verbs together similar to a chain.

---

``` python
manufacturer_column = cereal['mfr']
manufacturer_column.value_counts()
```

```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64
```

``` python
cereal['mfr'].value_counts()
```

```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64
```

Notes:

When we made our frequency table in Module 1, we first saved the single
column as an object before we used `value_counts()` like we show you
here.

Instead of saving the column in advance, we can skip this step and make
the frequency table in one line, with chaining.

The convenience doesn’t stop there either.

---

``` python
mfr_k = cereal[cereal['mfr'] == 'K']
csr_df = mfr_k.loc[:, ["calories", "sugars", "rating"]]
cereal_mean = csr_df.mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

``` python
cereal_mean = cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]].mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

Notes:

Chaining is the design of performing each method sequentially.

Let’s say we want to perform 3 actions:

1.  Filter the dataframe for cereals only from manufacturer “K”.

2.  Select the columns `calories`, `sugars` and `rating` using the verb
    `loc`.

3.  Find the mean of each column using `.mean()`.

Normally our code would need 3 different object to code this.

Instead we can chain them.

This chain avoided the use of 2 intermediate objects; `mfr_k` and
`csr_df`.

We cut out creating intermediate variables which is great but now we
have a really long line of code and it’s a bit hard to read.

How can we make this easier to understand?

---

``` python
cereal_mean = cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]].mean()

cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

``` python
cereal_mean = (cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]]
                                           .mean()
              )
              
cereal_mean.head()
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

Notes:

In this course, we suggest giving a new line for each verb.

We can do this by wrapping our code in parentheses and making a new line
before each period (`.`).

It’s a good habit to indent and have the verbs lined up for additional
clarity.

---

## Coding Preferences

  - Chaining has advantages and disadvantages.
  - Increases the readability of our code.
  - Comments are extremely important with of without chaining.

Notes:

Although we have seen how chaining has advantages, it’s a coding style
that is adopted by the person writing the code.

Some argue that it can add restrictions to your code. One thing that is
for certain the readability of the code written.

Someone else (or more often, future you\!) must be able to understand
what is being accomplished.

This is why comments (`#`) are so important. If a lot is going on in
your code, it’s good habits to explain it whether it’s with chaining, or
without.

---

# Let’s apply what we learned\!

Notes:

<br>
