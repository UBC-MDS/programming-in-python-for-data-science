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

<img src='module3/pivot_melt.gif' width="400">

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
criterion \#2: \_ Each variable is a single column\_

It can be used to then elongate the dataframe: to convert the variables
to their own columns that were previously being stored in a single
column.

The code for this verb takes quite a few arguments that can be a bit
tricky so we are going to go through it.

    df.pivot(index=['index label'], columns='column_name', values='new_colum_name')
    )

  - `df` to express with dataframe we want to pivot
  - `index` is going to be use to make the new dataframe’s index.
  - `columns` is the column that currently exists but that you want to
    create new columns labels from. Each unique value in this column
    will become a new column label.
  - `values` is the name of the column that currently exists but that
    contains the cell values you want. These values will be display in
    the respective newly created columns.

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

This animation made by Alison Presmanes Hill “Source: Alison Presmanes
Hill, <https://github.com/apreshill/teachthat> explains well what is
happening.

<center>

<img src='module3/spread_py.gif' width="400">

</center>

# Let’s practice what we know about Tidy Data first\!

Notes: Script here

<html>

<audio controls >

<source src="placeholder_audio.mp3" />
