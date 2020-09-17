---
type: slides
---

# Good function design choices

Notes:

<br>

---

## How to write good functions

**What makes a function useful?**

**Is a function more useful when it does more operations?**

**Do adding parameters make your functions more or less functional?**

These are all questions we need to think about when writing functions.

Notes:

This has been quite a full module\!

We’ve learned how to make functions, how to handle errors gracefully,
how to test our functions and write the necessary documentation to keep
our code comprehensible.

These skills will all contribute to writing effective code.

One thing we have not discussed yet is the actual code within a
function.

**What makes a function useful?**

**Is a function more useful when it performs more operations?**

**Does adding parameters make your functions more or less useful?**

These are all questions we need to think about when writing functions.

We are going to list some habits to adopt when writing and designing
your functions.

---

## 1\. Avoid “hard coding”

**Hard coding** is the process of embedding values directly into your
code without saving them in objects.

``` python
def squares_a_list(numerical_list):
    new_squared_list = list()
    
    for number in numerical_list:
        new_squared_list.append(number ** 2)
    
    return new_squared_list
```

``` python
def exponent_a_list(numerical_list, exponent):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

Notes:

**Hard coding** is the process of embedding values directly into your
code without saving them in variables

When we hardcode values into our code, it decreases flexibility.

Being inflexible can cause you end up writing more functions and/or
violating the DRY principle.

This in turn can decreases the readability and makes code problematic to
maintain. In short, hard coding is a breeding ground for bugs.

Remember our function `squares_a_list()`?

In this function, we “hard-coded” in `2` when we calculated `number
** 2`.

There are a couple approaches to improving the situation. One is to
assign 2 to a variable in the function before doing this calculation.
That way, if you need to reuse that number later on, you can just refer
to the variable; and if you need to change the 2 to a 3, you only need
to change it in one place. Another benefit is that you’re giving it a
variable name, which acts as a little bit of documentation.

The other approach is to turn the value into an argument like we did
when we made `exponent_a_list()`.

This new function now gives us more flexibility with our code.

If we now encounter a situation where we need to calculate each element
to a different exponent like 4 or 0, we can do so without writing new
code and potentially making a new error in doing so.

We reduce our long term work load.

This version is more maintainable code, but it doesn’t give the function
caller any flexibility. What you decide depends on how you expect your
function to be used.

---

## 2\. Less is More

``` python
def load_filter_and_average(file, grouping_column, ploting_column):
    df = pd.read_csv(file)
    source = df.groupby(grouping_column).mean().reset_index()
    chart = alt.Chart(source, width = 500, height = 300).mark_bar().encode(
                      x=alt.X(grouping_column),
                      y=alt.Y(ploting_column)
            )
    return chart
```

``` python
bad_idea = load_filter_and_average('cereal.csv', 'mfr', 'rating')
bad_idea
```
<img src="/module6/chart_bad_idea.png"  width="40%" />

Notes:

Although it may seem useful when a function acts as a one-stop-shop that
does everything you want in a single function, this also limits your
ability to reuse code that lies within it.

Ideally, functions should serve a single purpose.

For example, let’s say we have a function that reads in a csv, finds the
mean of each group in a column and plots a specified variable.

Although this may seem nice, we may want to break this up into multiple
smaller functions. For example, what if we don’t want the plot? Perhaps
the plots is just something we wanted a single time and now we are
committed to it for each time we use the function.

Another problem with this function is that the means are only printed
and not returned. Thus, we have no way of accessing the statistics to
use further in our code (we would have to repeat ourselves and rewrite
it).

---

``` python
def grouped_means(df, grouping_column):
    grouped_mean = df.groupby(grouping_column).mean().reset_index()
    return grouped_mean
```

``` python
cereal_mfr = grouped_means(cereal, 'mfr')
cereal_mfr
```

```out
  mfr    calories   protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
0   A  100.000000  4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
1   G  111.363636  2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
2   K  108.695652  2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
3   N   86.666667  2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
4   P  108.888889  2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
5   Q   95.000000  2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
6   R  115.000000  2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997
```

Notes:

In this case, you want to simplify the function.

Having a function that only calculates the mean values of the groups in
the specified column is much more usable.

A preferred function would look something like this, where the input is
a dataframe we have already read in, and the output is the dataframe of
mean values for all the columns.

---

``` python
def plot_mean(df, grouping_column, ploting_column):
    chart = alt.Chart(df, width = 500, height = 300).mark_bar().encode(
                      x=alt.X(grouping_column),
                      y=alt.Y(ploting_column)
            )
    return chart
```

``` python
plot1 = plot_mean(cereal_mfr, 'mfr', 'rating')
plot1
```
<img src="/module6/plot_better.png"  width="50%" />

Notes:

If we wanted, we could then make a second function that creates the
desired plot part of the previous function.

---

## 3\. Return a single object

``` python
def load_filter_and_average(file, grouping_column, ploting_column):
    df = pd.read_csv(file)
    source = df.groupby(grouping_column).mean().reset_index()
    chart = alt.Chart(source, width = 500, height = 300).mark_bar().encode(
                      x=alt.X(grouping_column),
                      y=alt.Y(ploting_column)
            )
    return chart, source
```

``` python
another_bad_idea = load_filter_and_average('cereal.csv', 'mfr', 'rating')
another_bad_idea
```

```out
(alt.Chart(...),   mfr    calories   protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
0   A  100.000000  4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
1   G  111.363636  2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
2   K  108.695652  2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
3   N   86.666667  2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
4   P  108.888889  2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
5   Q   95.000000  2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
6   R  115.000000  2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997)
```

Notes:

For the most part, we have only lightly touched on the fact that
functions can return multiple objects and it’s with good reason.

Although functions are *capable* of returning multiple objects, that
doesn’t mean that it’s the best option.

For instance, what if we converted our function
`load_filter_and_average()` so that it returns a dataframe ***and*** a
plot.

---

``` python
another_bad_idea[0]
```
<img src="/module6/plot_better.png"  width="55%" />

Notes:

Since our function returns a tuple we can obtain the plot by selecting
the first element of the output.

This can be quite confusing. We would recommend separating the code into
two functions and can have each one return a single object.

It’s best to think of programming functions in the same way as
mathematical functions where most times, mathematical functions return a
single value.

---

## 4\. Keep global variables in their global environment

``` python
def grouped_means(df, grouping_column):
    grouped_mean = df.groupby(grouping_column).mean().reset_index()
    return grouped_mean
```

``` python
cereal = pd.read_csv('cereal.csv')

def bad_grouped_means(grouping_column):
    grouped_mean = cereal.groupby(grouping_column).mean().reset_index()
    return grouped_mean
```

Notes:

It’s generally bad form to include objects in a function that were
created outside of it.

Take our `grouped_means()` function.

What if instead of including `df` as an input argument we just used
`cereal` that we loaded earlier?

The number one problem with doing this is now our function only works on
the cereal data - it’s not usable on other data.

---

``` python
bad_cereal_grouping = bad_grouped_means('mfr')
bad_cereal_grouping.head(3)
```

```out
  mfr    calories   protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
0   A  100.000000  4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
1   G  111.363636  2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
2   K  108.695652  2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
```

``` python
cereal = "let's change it to a string" 
bad_cereal_grouping = bad_grouped_means('mfr')
```

``` out
AttributeError: 'str' object has no attribute 'groupby'

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "<string>", line 2, in bad_grouped_means
```

Notes:

Ok let’s say we still use it, then what happens?

Although it does work, global variables have the opportunity to be
altered in the global environment.

When we change the global variable outside the function, and try to use
the function again, it will refer to the new global variable and
potentially no longer work.

Of course, like in any case, these habits are suggestions and not strict
rules.

There will be times where adhering to one of these may not be possible
or will hinder your code instead of enhancing it.

The rule of thumb is to ask yourself how helpful is your function if you
or someone else wishes to reuse it.

---

# Let’s apply what we learned\!

Notes:

<br>
