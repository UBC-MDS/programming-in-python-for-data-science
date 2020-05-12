---
type: slides
---

# Reshaping using pivot

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

`pandas` provides 2 functions for reshaping data:

  - <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">`.melt()`</a>
    to make a wide dataframe long (convert columns to row)
  - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html" target="_blank">`.pivot()`</a>
    to make a long dataframe wide (convert rows to columns)

<center>

<img src='module3/spivot_melt.gif' width="400">

</center>

“Source: Garrick Aden-Buie,
<https://github.com/gadenbuie/tidyexplain#spread-and-gather> and Tomas
Beuzen, DSCI 523 Data Wrangling”

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## Pivot

`.pivot()` can be used in situations where our data may not meet
criterion \#2 \_ Each variable is a single column\_

It can be used to then elongate the dataframe: to convert the variables
to their own columns that were previously being stored in a single
column.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s practice what we know about Tidy Data first\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />
