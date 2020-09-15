---
type: slides
---

# Importing Python Libraries

Notes:

<br>

---

``` python
import pandas
```

``` python
pandas.read_csv('cereal.csv').head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

Notes:

All the way back in Module 1, we learned how to import the `pandas`
package for dataframe wrangling and `altair` to visualize our data with
plots.

We imported these packages because basic Python does not have all the
built-in tools that we need to accomplish what we what therefore, we
import other tools into our environment.

To import a package we saw that can use the keyword `import` followed by
the desired package name.

In this case, we are importing `pandas`

This now lets us use verbs that reside in the `pandas` package such as
`read_csv()`.

We need to specify the package name (`pandas`) and then the verb
(`read_csv()`):

---

``` python
import pandas as pd 
import altair as alt
```

``` python
pd.read_csv('cereal.csv').head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

Notes:

For efficiency, in the majority of this course we have been importing
our packages by assigning them a shorter condensed name or alias.

For example, in the assignments and practice exercises, we have been
importing `pandas` and `altair` with names such as `pd` and `alt`
respectively.

Now when we call functions from either of these packages we only type
the short form alias we assigned to the package name.

Now instead of writing `pandas.read_csv('cereal.csv')` we can shorten it
to `pd.read_csv('cereal.csv')`.

---

``` python
from pandas import read_csv
```

``` python
read_csv('cereal.csv').head()
```

```out
                        name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                  100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1          100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                   All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3  All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4             Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
```

This mostly helps if we only have a single function we wish to use
instead of importing the entire package.

Notes:

We can also import a single function from a package using the keyword
`from`.

If we only wanted the `read_csv()` function from the `pandas` package,
we could first specify the package the function belongs to, followed by
the function name:

Here it’s `from pandas import read_csv`.

Now when we call `read_csv()`, we don’t need to specify the package name
or alias before it.

This is all fun and dandy but how do we import functions we’ve made that
are located in another file?

If we want to reuse code to adhere to the DRY principle, what is our
next step?

This question will be answered in the screencast and slides of the next
section.

---

# Let’s apply what we learned\!

Notes:

<br>
