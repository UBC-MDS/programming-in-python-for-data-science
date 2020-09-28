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
pandas.read_csv('cereal.csv')
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
72                    Triples   G  Cold       110        2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
73                       Trix   G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
75                   Wheaties   G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 16 columns]
```

Notes:

All the way back in Module 1, we learned how to import the `pandas`
library for dataframe wrangling and `altair` to visualize our data with
plots.

We imported these libraries because basic Python does not have all the
built-in tools that we need to accomplish what we want; therefore, we
import other tools into our environment.

To import a library, we saw that we can use the keyword `import`
followed by the desired package name.

In this case, we are importing `pandas`.

This now lets us use verbs that reside in the `pandas` library, such as
`read_csv()`.

We need to specify the library name -`pandas` and then the verb -
`read_csv()`.

---

``` python
import pandas as pd 
import altair as alt
```

``` python
pd.read_csv('cereal.csv')
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
72                    Triples   G  Cold       110        2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
73                       Trix   G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
75                   Wheaties   G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 16 columns]
```

Notes:

For efficiency, in the majority of this course, we have been importing
our libraries by assigning them a shorter condensed name or alias.

For example, in the assignments and practice exercises, we have been
importing `pandas` and `altair` with names such as `pd` and `alt`,
respectively.

Now when we call functions from either of these libraries, we only type
the short form alias we assigned to the library name.

Now instead of writing `pandas.read_csv('cereal.csv')`, we can shorten
it to `pd.read_csv('cereal.csv')`.

---

``` python
from pandas import read_csv
```

``` python
read_csv('cereal.csv')
```

```out
                         name mfr  type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130   10.0    5.0       6     280        25      3     1.0  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15    2.0    8.0       8     135         0      3     1.0  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260    9.0    7.0       5     320        25      3     1.0  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140   14.0    8.0       0     330        25      3     1.0  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200    1.0   14.0       8       1        25      3     1.0  0.75  34.384843
..                        ...  ..   ...       ...      ...  ...     ...    ...    ...     ...     ...       ...    ...     ...   ...        ...
72                    Triples   G  Cold       110        2    1     250    0.0   21.0       3      60        25      3     1.0  0.75  39.106174
73                       Trix   G  Cold       110        1    1     140    0.0   13.0      12      25        25      2     1.0  1.00  27.753301
74                 Wheat Chex   R  Cold       100        3    1     230    3.0   17.0       3     115        25      1     1.0  0.67  49.787445
75                   Wheaties   G  Cold       100        3    1     200    3.0   17.0       3     110        25      1     1.0  1.00  51.592193
76        Wheaties Honey Gold   G  Cold       110        2    1     200    1.0   16.0       8      60        25      1     1.0  0.75  36.187559

[77 rows x 16 columns]
```

Notes:

We can also import a single function from a library using the keyword
`from`.

If we only want the `read_csv()` function from the `pandas` package, we
could first specify the library the function belongs to, followed by the
function name:

Here it’s `from pandas import read_csv`.

Now when we call `read_csv()`, we don’t need to specify the package name
or alias before it.

This mostly helps if we have only a single function we wish to use,
instead of importing the entire library.

This works for Python libraries, but how do we import functions we’ve
made that are located in another file?

If we want to reuse code to adhere to the DRY principle, what is our
next step?

This question will be answered in the next section of this module.

---

# Let’s apply what we learned\!

Notes:

<br>
