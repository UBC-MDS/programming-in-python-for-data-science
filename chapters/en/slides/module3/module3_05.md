---
type: slides
---

# Statistical questions and tidy data

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

In the last section we learned about tidy data and how it is determined
based on what we are trying to figure out, eg: what our statistical
question is.

There are cases where a longer dataframe is considered tidy data and in
other cases, a wider dataframe is tidy depending on what is being ask.

Let’s explore some more examples.

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

<img src='/module3/wide-long1.png' width="45%">

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

In this case, it makes the most sense for our data to have the
measurements `area` and `population` as variables that may or may not
affect language diversity. This would be considered tidy data and it is
stored as a wider dataframe than what what initially presented to us.

<center>

<img src='/module3/wide-long2.png' width="40%">

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
<a href="https://sejdemyr.github.io/data-vis/mortality-wealth-time/" target="_blank">here</a>.
It is based on data that can be found at www.childmortality.org. The
under-five mortality rate is expressed as the number of under-five
deaths per 1,000 live births.

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

We are interested in the variable `year`. Having a single variable for
year would be the most appropriate to use in this analysis and display
tidy data. This would correspond to a long dataframe.

<center>

<img src='/module3/wide-long4.png' width="35%">

</center>

Notes: Script here

<html>

<audio controls >

<source src="/placeholder_audio.mp3" />

</audio>

</html>

---

At this point you may be asking yourself the question *“Are there any
verbs, that would easily transform data into longer or wider
dataframes?”*

If you are, then you are ahead of the game\! We will discuss this in the
next section.

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
