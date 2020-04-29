---
type: slides
---

# Chaining Notation

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## What is Chaining?

Up until now, when we want to perform multiple actions on an object,
after each action we have been saving the results under a new object
name. Chaining allows us to do multiple actions in a single line of code
without these intermediate objects.

You can imagine that we are linking verbs together similar to a chain.

<img src='module2/chainsfinal.png'  alt="404 image" />  
[Attribution](https://unsplash.com/photos/42ui88Qrxhw)

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

When we made our frequency table in Module 1, we first saved the single
column as an object before we used `value_counts()`. We can do this all
in one line with chaining:

``` python
df['mfr'].value_counts()
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

However, this is not the extent of chaining.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Chaining is the design of performing each method in a sequential manner.
Let’s say we want to perform 3 actions:  
1\. Filter the dataframe for cereals only from manufacturer “K”.  
2\. Select the columns `calories`, `sugars` and `rating` using the verb
`loc`.  
3\. Find the mean of each column using `.mean()`.

Normally our code would look like this:

``` python
mfr_k = df[df['mfr'] == 'K']
csr_df = mfr_k.loc[ : , ["calories", "sugars", "rating"]]
cereal_mean = csr_df.mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Instead we can chain them:

``` python
cereal_mean = df[df['mfr'] == 'K'].loc[ : , ["calories", "sugars", "rating"]].mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

This chain avoided the use of 3 intermediate objects `mfr_k`, `csr_df`
and `cereal_stats`.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

Great, we can cut out creating intermediate variable but now we just
have a really long line of code and it’s a bit hard to read.

How can we make this easier to understand?  
In this course, we suggest giving a new line for each method. We can do
this by wrapping our code in parentheses and making a new line before
each period (`.`). It’s good practice to indent and have the methods
line up to make it especially clear.

``` python
(df[df['mfr'] == 'K'].loc[ : , ["calories", "sugars", "rating"]]
                     .describe()
                     .head()
)
```

```out
         calories     sugars     rating
count   23.000000  23.000000  23.000000
mean   108.695652   7.565217  44.038462
std     22.218818   4.500768  14.457434
min     50.000000   0.000000  29.924285
25%    100.000000   3.000000  34.478442
```

---

# Let’s apply what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
