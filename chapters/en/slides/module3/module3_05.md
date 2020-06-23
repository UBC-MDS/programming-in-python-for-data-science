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

<img src='/module3/wide.png' width="30%">

</center>

**Long**

<center>

<img src='/module3/long.png' width="30%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

More slides here.

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
