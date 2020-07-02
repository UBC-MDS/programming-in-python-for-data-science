---
type: slides
---

# Wide and long dataframes

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the next few sections, we will explore two useful pandas functions
for reshaping our data that can be handy to convert it into tidy data.

  - <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
    to make a wide dataframe long (convert columns to row)
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
    to make a long dataframe wide (convert rows to columns)

Before going forward we should understand the difference between
***wide*** data and ***long*** data.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

## Wide and long dataframes

**Wide**

We are used to seeing the cereal data in a wide format, where there is a
column for each measurement. We’ve already experienced that not all wide
dataframes are tidy

<center>

<img src='/module3/wide.png' width="70%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

However the exact same information can be expressed in a structure
called a **Long** dataframe.

**Long**

A long dataframe would consist of the same information as contained in a
wide dataframe, however in this case, for each data point, there is a
row for each measurement. Similarly to how not all wide dataframes are
tidy, neither are all long dataframes.

<center>

<img src='/module3/long.png' width="60%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Can you see the difference?

**Wide**

<center>

<img src='/module3/wide.png' width="35%">

</center>

**Long**

<center>

<img src='/module3/long.png' width="35%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

As we discussed in the previous sections, tidy data is determined based
on what we are trying to figure out, eg: what our statistical question
is.

There are cases where a long dataframe is considered tidy data and in
other cases, a wide dataframe is tidy depending on what is being ask.

Let’s explore some examples.

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

We have some data obtain from the resource available
<a href="https://github.com/jvcasillas/untidydata#language_diversity" target="_blank">here</a>.
This shows the language diversity within different countries as well as
their population and area.

<center>

<img src='/module3/wide-long1.png' width="50%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module3/wide-long1.png' width="30%">

</center>

We are trying to answer the statistical question ***what factors are
associated with language diversity (as measured by the number of
languages spoken in a country)?***

In this case, it makes more sense to have our data displayed in a wide
format, so we can measure `area` and `population` as variables that may
or may not affect language diversity.

<center>

<img src='/module3/wide-long2.png' width="50%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

Let’s look at another example.

Here is the UNICEF dataset on under-five child mortality which is
available
<a href="https://sejdemyr.github.io/data-vis/mortality-wealth-time/" target="_blank">here</a>
It is based on data that can be found at www.childmortality.org. The
under-five mortality rate is expressed as the number of under-five
deaths per 1,000 live births.

<br>

<center>

<img src='/module3/wide-long3.png' width="60%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

<center>

<img src='/module3/wide-long3.png' width="35%">

</center>

The statistical question that we’d like to answer with this data set is:
***whether there a relationship between country and/or year on
under-five child mortality?***

We are intested in the variable `year` which makes a long dataframe
(with a single column for the variable `year`) tidy and the most
appropriate to use in our analysis.

<center>

<img src='/module3/wide-long4.png' width="30%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we learned\!

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />
