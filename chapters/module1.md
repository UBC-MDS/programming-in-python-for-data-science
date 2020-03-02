---
title: 'Module 1: Python & Pandas - an Unexpected Friendship!'
description:
  'In this module you will be introduced to dataframes and the pandas python package.'
prev: module0
next: /module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes" type="slides">

<slides source="module1_00">
</slides>

</exercise>


<exercise id="1" title="Introduction to Dataframes and Pandas" type="slides">

<slides source="module1_01">
</slides>

</exercise>

<exercise id="2" title="Describing a Dataframe">

**What are data frames comparable to?**


<choice id="1" >
<opt text="Text Documents">

Is this an easy way to organize data?

</opt>

<opt text="Excel Sheets" correct="true">

Good job!

</opt>

<opt text="Picture Frames" >

Are we storing pictures in a data frame?

</opt>

</choice>

**What is Pandas?**    


<choice id="2">
<opt text="A Python package needed for extra tools" correct="true">

Nice work! Pandas is a package we import so we can use additional features.

</opt>

<opt text="A programming language">

Are you sure you know the difference between Python and Pandas?

</opt>

<opt text=" Fluffy animals that eat bamboo">

Although that isn't wrong, we are studying Python and coding and in this course, the context is not quite right.

</opt>

</choice >

</exercise>

<exercise id="3" title="Your First Code!">

Let's try importing pandas and loading in our own dataset.

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load.

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**


- Import `pandas` as `pd`.
- Load in a dataset named `canucks.csv`.
- Save the dataframe as `hockey_players`.
- Display the first 5 rows of the  dataframe

<codeblock id="01_03">

- Are you sure you are saving your dataframe as `hockey_players` a
- Are you using `pd.read_csv()`

</codeblock>

</exercise>

<exercise id="4" title="Your Second Code!">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_04">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="5" title="Slicing Using df.loc[]" type="slides">

<slides source="module1_05">
</slides>

</exercise>

<exercise id="6" title="Slicing and Dicing Practice">

My dataframe object name is `fruit_salad`. my row names in order are `apple`, `banana`, `cantaloupe`, `dragon-fruit`, `elderberry`, `fig`, `Guava`, `huckleberry`, `kiwi` and `lemon`. 
My index is labeled with the `name` of the fruit.
My column names in order are; , `colour`, `location`, `seeds`, `shape`, `sweetness`, `water-content` and  `weight`.

**Question 1**

If I wanted all the rows and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would my code look like? 

<choice id="1" >
<opt text='fruit_salad.loc[  :  , seeds : water-content]'>

This is almost right but it's missing something important

</opt>

<opt text='fruit_salad[  :  , "seeds" : "water-content"]' >

This is almost right but it's missing something important! Try looking at the title of the slides we just finished. 

</opt>

<opt text='fruit_salad[ "apple": "lemon" , "seeds" : "water-content"]' >

This is almost right but it's missing something important! Try looking at the title of the slides we just finished. 

</opt>

<opt text='fruit_salad.loc[  :  , "seeds" : "water-content"]' correct="true">

Good job! This has both `loc` and "quotation" which are both needed to slice here. 

</opt>

</choice >

**Question 2**

If I wanted all the rows between `cantaloupe`  and `kiwi` and all the columns?  What would my code look like? 

<choice id="2" >
<opt text='fruit_salad.loc[ : , "cantaloupe" : "kiwi"]'>

Remember that rows are expressed first before columns. 

</opt>

<opt text='fruit_salad.loc[ "cantaloupe" : "kiwi" ]' correct="true">

Great! You don't need to specify the second column part because by default the code will slice all the columns. 

</opt>

<opt text='fruit_salad.loc[ : , cantaloupe : kiwi]' >

Remember that rows are expressed first before columns and you are missing something important!

</opt>

<opt text= 'fruit_salad[ cantaloupe : kiwi ]'  >

I think you are missing something inportant.  

</opt>

</choice >

</exercise>

<exercise id="7" title="Practicing Slicing">

Using our `hockey_players` data from the last few questions with the index labelled with `Player` name, Let's try slicing it.

We want 
- The rows `Adam Gaudette` to `Brandon Sutter`
- The rows `Age`, `Height`,	`Weight` and `Country`
- The new sliced dataframe saved as object `benched_players`

<codeblock id="01_07">

- Are you using `df.loc[]`
- Are you using the correct dataframe labels? Check your spelling and punctuation. 
- Did you slice both columns and rows? 

</codeblock>

</exercise>

<exercise id="8" title="Practicing Slicing Some More">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_08">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="9" title="Selecting Using df.loc[]" type="slides">
<slides source="module1_09">
</slides>
</exercise>

<exercise id="10" title="Practicing Selecting">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_10">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="11" title="Practicing Selecting">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_11">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>


<exercise id="12" title="Slicing and Selecting Using df.iloc[]" type="slides">
<slides source="module1_12">
</slides>
</exercise>

<exercise id="13" title="Slice and Dice Questions">

**Question**


<choice id="1" >
<opt text="Answer 1">

Let's look into this more

</opt>

<opt text="Answer 2" correct="true">

Good job!

</opt>

<opt text="Answer 3" >

Maybe not the right answer.

</opt>

</choice >

</exercise>

<exercise id="14" title="Practicing Slicing">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_14">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="15" title="Summary Statistics" type="slides">
<slides source="module1_15">
</slides>
</exercise>


<exercise id="16" title="Practice">

**Question**


<choice id="1" >
<opt text="Answer 1">

Let's look into this more

</opt>

<opt text="Answer 2" correct="true">

Good job!

</opt>

<opt text="Answer 3" >

Maybe not the right answer.

</opt>

</choice >

</exercise>

<exercise id="17" title="Practicing">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_17">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="18" title="Practicing">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_18">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="19" title="Quick Viz with Pandas" type="slides">
<slides source="module1_19">
</slides>
</exercise>

<exercise id="20" title="Practicing Viz">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_20">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="21" title="Practicing Viz">

- Now Let's display the column names of `hockey_players` and save it as `columns_hockey`.
- Save the number of rows `hockey_players` has in a variable called `hockey_rows`.
- The data frame dimension should be save as `hockey_dim`.


<codeblock id="01_21">

- Are you sure you are saving your objects correctly?
- Are you using `len()`, `df.shape` and `df.columns`?

</codeblock>

</exercise>

<exercise id="22" title="What Did We Just Learn?" type="slides">
<slides source="module1_22">
</slides>
</exercise>