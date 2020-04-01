---
title: 'Module 1: Python & Pandas - An Unexpected Friendship'
description:
  'In this module, you will be introduced to dataframes and the Pandas Python package.'
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

**What are dataframes comparable to?**


<choice id="1" >
<opt text="Text Documents">

Is this an easy way to organize data?

</opt>

<opt text="Excel Sheets" correct="true">

Good job!

</opt>

<opt text="Picture Frames" >

Are we storing pictures in a dataframe?

</opt>

</choice>

**What is Pandas?**   


<choice id="2">
<opt text="A useful tool for data manipulation in Python" correct="true">

Nice work! Pandas is a tool we use in conjunction with Python.

</opt>

<opt text="A programming language">

Are you sure you know the difference between Python and Pandas?

</opt>

<opt text="A datatype">

Not quite. You may want to review the module slides.

</opt>

</choice >

</exercise>

<exercise id="3" title="Your First Code!">

Let's try importing pandas and loading in our data.

**Instructions:**

When you run a coding exercise for the first time, it could take a bit of time for everything to load.

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:
- Import `pandas` as `pd`.
- Load in data named `canucks.csv`.
- Save the dataframe as `hockey_players`.
- Display the first 5 rows of the dataframe.

<codeblock id="01_03">

- Are you sure you are saving your dataframe as `hockey_players`?
- Are you using `pd.read_csv()`?

</codeblock>

</exercise>

<exercise id="4" title="Your Second Code!">


Let's display the column names of `hockey_players` and save it as `columns_hockey`.


<codeblock id="01_04">

- Are you sure you are saving your objects as `columns_hockey`?
- Are you using `df.columns`?

</codeblock>


What is the shape of the hockey dataframe? Save the result as `hockey_shape`.

<codeblock id="01_04b">

- Are you sure you are saving your objects as `hockey_shape`?
- Are you using `df.shape`?

</codeblock>

</exercise>

<exercise id="5" title="Slicing Rows Using df.loc[]" type="slides">

<slides source="module1_05">
</slides>

</exercise>


<exercise id="6" title="Slicing and Dicing Practice">

My dataframe object name is `fruit_salad` with the index label as the `name` column.

```out
        name     colour    location   seed   shape    sweetness   water-content  weight
       apple        red     canada    True   round       True          84         100
      banana     yellow     mexico   False    long       True          75         120
  cantaloupe     orange      spain    True   round       True          90        1360
dragon-fruit    magenta      china    True   round      False          96         600
  elderberry     purple    austria   False   round       True          80           5
         fig     purple     turkey   False    oval      False          78          40
       guava      green     mexico    True    oval       True          83         450
 huckleberry       blue     canada    True   round       True          73           5
        kiwi      brown      china    True   round       True          80          76
       lemon     yellow     mexico   False    oval      False          83          65
```

**Question 1**

If you wanted only the rows from `cantaloupe` to  `kiwi`, what would your code look like using index labels?

<choice id="1" >
<opt text='<code>fruit_salad.loc[ "cantaloupe", "kiwi"]</code>'>

This is not the right syntax or number of rows.

</opt>

<opt text='<code>fruit_salad[ "cantaloupe", "kiwi"]</code>' >

This is not using the right syntax.

</opt>

<opt text='<code>fruit_salad[ "cantaloupe": "kiwi"]</code>' >

This is missing something rather important.

</opt>

<opt text='<code>fruit_salad.loc["cantaloupe": "kiwi"]</code>' correct="true">

Good job! This has both `loc` and "quotation" which are both needed to slice here.

</opt>

</choice >

**Question 2**

If you wanted all the rows between `cantaloupe` and `fig` and only columns `name` to `seed`? What would your code look like using index labels?

<choice id="2" >
<opt text='<code>fruit_salad.loc[ "cantaloupe" : "fig", "name" : "seed"]</code>'>

Remember that the "name" column is the index and does not need to be specified.

</opt>

<opt text='<code>fruit_salad.loc[ "cantaloupe" : "fig", "colour": "seed" ]</code>' correct="true">

Great! This is correct since we don't need to start our slicing at name since it is our index.

</opt>

<opt text='<code>fruit_salad.loc["colour": "seed", cantaloupe : "fig"]</code>' >

This seems to be backward.

</opt>

<opt text= '<code>fruit_salad[ "cantaloupe" : "kiwi", "colour": "seed"  ]</code>'  >

I think you are missing something important.  

</opt>

</choice >

</exercise>

<exercise id="7" title=" Practicing Rows Slicing">


**Instructions:**

When you run a coding exercise for the first time, it could take a bit of time for everything to load.

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**


This following code chunk will be used to give you an output of the data `hockey_players`. This will help answer and code in the exercises following it.

<codeblock id="hockey_players">


</codeblock>


Using our `hockey_players` data from the last few questions with the index labeled with `Player` name, Let's try slicing it.


Tasks:
- Select the players `Guillaume Brisebois` to `Quinn Hughes`
- Save the new sliced dataframe as object `benched_players`.
- Display it.




<codeblock id="01_07">

- Are you using `df.loc[]`?
- Are you using the correct dataframe labels? Check your spelling and punctuation in row and column labels.
- Did you slice both columns and rows?
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="8" title="Practicing Column Slicing">

**Instructions:**

When you run a coding exercise for the first time, it could take a bit of time for everything to load.

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**


Use the output of the following code chunk to help answer the next question.

<codeblock id="hockey_players">

</codeblock>


Using our `hockey_players` data from the last few questions with the index labeled with `Player` name, Let's try slicing it.


Tasks:
- Select the players `Adam Gaudette` to `Brandon Sutter` and the columns `No.`, `Age`, `Height`, `Weight` and `Country`.
- Save the new sliced dataframe as object `star_players`.
- Display it.

<codeblock id="01_08">

- Are you using `df.loc[]`?
- Are you using the correct dataframe labels? Check your spelling and punctuation in row and column labels.
- Did you slice both columns and rows?
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="9" title=" Slicing Columns Using df.loc[]" type="slides">
<slides source="module1_08">
</slides>
</exercise>

<exercise id="10" title="Slicing Columns Only">

Using my dataframe object name is `fruit_salad` with the index label as the `name` column, Let's answer some slicing questions.

```out
        name     colour    location   seed   shape    sweetness   water-content  weight
       apple        red     canada    True   round       True          84         100
      banana     yellow     mexico   False    long       True          75         120
  cantaloupe     orange      spain    True   round       True          90        1360
dragon-fruit    magenta      china    True   round      False          96         600
  elderberry     purple    austria   False   round       True          80           5
         fig     purple     turkey   False    oval      False          78          40
       guava      green     mexico    True    oval       True          83         450
 huckleberry       blue     canada    True   round       True          73           5
        kiwi      brown      china    True   round       True          80          76
       lemon     yellow     mexico   False    oval      False          83          65
```

**Question 1**

If you wanted all the rows and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would your code look like using index labels?

<choice id="1" >
<opt text='<code>fruit_salad.loc[  :  , "seed" : "weight"]</code>'>

This is almost right but it may be good to check your columns.

</opt>

<opt text='<code>fruit_salad[  :  , "seeds" : "water-content"]</code>' >

This is almost right but it's missing something important! Try looking at the title of the slides we just finished.

</opt>

<opt text='<code>fruit_salad[ "apple": "lemon" , "seeds" : "water-content"]</code>' >

This is almost right but it's missing something important! Try looking at the title of the slides we just finished.

</opt>

<opt text='<code>fruit_salad.loc[  :  , "seeds" : "water-content"]</code>' correct="true">

Good job! This has both `loc` and "quotation" which are both needed to slice here.

</opt>

</choice >

</exercise>



<exercise id="11" title="Selecting Using df.loc[]" type="slides">
<slides source="module1_11">
</slides>
</exercise>


<exercise id="12" title="Rearranging Columns and Rows">

Using my `fruit_salad` dataframe from earlier?

```out
        name     colour    location   seed   shape    sweetness   water-content  weight
       apple        red     canada    True   round       True          84         100
      banana     yellow     mexico   False    long       True          75         120
  cantaloupe     orange      spain    True   round       True          90        1360
dragon-fruit    magenta      china    True   round      False          96         600
  elderberry     purple    austria   False   round       True          80           5
         fig     purple     turkey   False    oval      False          78          40
       guava      green     mexico    True    oval       True          83         450
 huckleberry       blue     canada    True   round       True          73           5
        kiwi      brown      china    True   round       True          80          76
       lemon     yellow     mexico   False    oval      False          83          65
```

If I wanted to make a tropical salad and the recipe calls for `kiwi`, `cantaloupe` and `guava` in this order and I am only interested in columns ordered as `sweetness`, `weight`, `seed` and  `location`, 
what would my code look like?

<choice >
<opt text='<code>fruit_salad.loc[ "kiwi", "cantaloupe", "guava" : "sweetness", "weight", "seed", "location"]</code>' >

Unfortunately, this code has many errors in it.

</opt>

<opt text='<code>fruit_salad.loc[ ["kiwi", "cantaloupe", "guava"] : ["sweetness", "weight", "seed", "location"] ]</code>' >

The way that the rows and columns are separated may need to be looked over

</opt>

<opt text='<code>fruit_salad.loc[["kiwi", "cantaloupe", "guava"] , ["sweetness", "weight", "seed", "location"] ]</code>' correct="true">

Ah, this looks right!

</opt>

<opt text='<code>fruit_salad.loc["cantaloupe", "kiwi", "guava"] , [ "weight", "seed”, “sweetness", "location"]]</code>'>

Remember we are rearranging here.

</opt>
</choice >
</exercise>


<exercise id="13" title="Selecting Single Columns" type="slides">
<slides source="module1_13">
</slides>
</exercise>


<exercise id="14" title="Practicing Selecting">

Let's try selecting a specific column.

Tasks:
- Select all the rows from column `Salary` only and save it as `player salary`. (_Hint: you don't need `loc` here_)
- Display it.


<codeblock id="01_14">

- Are you using the correct dataframe labels?
- Are you using double `[]` brackets?
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="15" title="Practicing Selecting Using Index Labels">

Now let's select specific players and columns.

Tasks:
- Select the players `Zack MacEwan`, `Jake Virtanen` and `Jordie Benn` in that order and the columns 
`Height`, `Weight`, `Salary` and 
`Country` in that order.
- Save the new sliced dataframe as object `penalty players`.
- Display it.


<codeblock id="01_15">

- Are you using `df.loc[]`?
- Are you using the correct dataframe labels? Are you using names as your row labels?
- Did you slice both columns and rows?
- Are you using 2 sets of `[]` brackets?
- Are you using "quotations"?

</codeblock>

</exercise>


<exercise id="16" title="Slicing and Selecting Using df.iloc[]" type="slides">
<slides source="module1_16">
</slides>
</exercise>

<exercise id="17" title="Practicing Slicing and Selecting Using Index Position">

Here is our `fruit_salad` data again:


```out
        name     colour    location   seed   shape    sweetness   water-content  weight
       apple        red     canada    True   round       True          84         100
      banana     yellow     mexico   False    long       True          75         120
  cantaloupe     orange      spain    True   round       True          90        1360
dragon-fruit    magenta      china    True   round      False          96         600
  elderberry     purple    austria   False   round       True          80           5
         fig     purple     turkey   False    oval      False          78          40
       guava      green     mexico    True    oval       True          83         450
 huckleberry       blue     canada    True   round       True          73           5
        kiwi      brown      china    True   round       True          80          76
       lemon     yellow     mexico   False    oval      False          83          65

```

**Question 1**

If I wanted the rows `elderberry`  to `kiwi` and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would my code look like if I was using index positions?

<choice id="1" >
<opt text='<code>fruit_salad.iloc[4 : 9 , 2 : 6]</code>' correct="true">

This is correct! We need to use `iloc` and go one position further than the last bound to select it

</opt>

<opt text='<code>fruit_salad.iloc[4 : 8 , 2 : 5]</code>' >

I think you may be forgetting that the last interval value does not get selected.

</opt>

<opt text='<code>fruit_salad.iloc[5 : 9 , 3 : 6]</code>' >

Are you forgetting that in the Python language we start counting at 0? You also may be forgetting that the last interval value does not get selected.

</opt>

<opt text='<code>fruit_salad.iloc[5 : 10 , 3 : 7]</code>'>

Are you forgetting that in the Python language we start counting at 0?

</opt>

</choice >

**Question 2**

If I wanted the rows `lemon` and `cantaloupe`  but only the columns `colour`, `weight` and `seeds` in that order, what would my code look like if I was using index position?

<choice id="2" >
<opt text='<code>fruit_salad.iloc[[lemon, cantaloupe], [colour, weight, seeds]]</code>'>

We need to use the index position for this question and when using `iloc`.

</opt>

<opt text='<code>fruit_salad.iloc[[10, 3], [1, 7, 3]]</code>' >

Great! You don't need to specify the second column part because by default the code will slice all the columns.

</opt>

<opt text='<code>fruit_salad.iloc[[9, 2], [0, 6, 2]]</code>' correct="true">

Great Work!

</opt>

<opt text= '<code>fruit_salad[[9, 2], [0, 6, 2]]</code>'  >

I think you are missing something important!

</opt>

</choice >

</exercise>

<exercise id="18" title="Practicing Slicing Using Index Position">

 In previous questions, we tried slicing using index labels on our Canack dataset. Let's try something similar but using the index positions.
To make life a little easier for you we will be reading in the data without `index_loc=0`. This means that no column is being assigned as an index and will have an index labeled with row numbers.

Tasks:
- Slice the players `Jacob Markstrom` to `Tim Schaller` and the columns `Player` to `Height`.
- Save the new sliced dataframe as object `skilled_players`.
- Display it.


<codeblock id="01_18">

- Are you using `df.iloc[]`?
- Are you using the correct dataframe positions? Are you counting starting from 0?
- Are you going 1 index past the bound you want?

</codeblock>

</exercise>

<exercise id="19" title="Practicing Selecting Using Index Position">

These unfortunate Canuck players have various forms of injuries, so let's make a dataframe of players who have injuries by selecting them using their index position.

Tasks:
- Select `Antoine Roussel`, `Thatcher Demko`, `Jake Virtanen` and `Jay Beagle` with only columns `Player`, `Birth Date`, `Experience` and `Salary` in the specified order.
- Save this dataframe as object `injured_players`.
- Don't forget to display it.

<codeblock id="01_19">

- Are you using `df.iloc[]`?
- Are you using the correct dataframe positions? Are you counting starting from 0?
- Are you using two sets of `[]` square brackets within your `iloc` brackets?

</codeblock>

</exercise>

<exercise id="20" title="Summary Statistics" type="slides">
<slides source="module1_20">
</slides>
</exercise>


<exercise id="21" title="Fruit Bowl Statistics">

**Question 1**

Let's say I have a dataframe named  `fruit_salad` with a column of interest named `colour`.  
How would you find the frequency of the column `colour` using `pd.value_counts()`?

<choice id="1" >
<opt text='<code>fruit_salad[colour]</code>'>

Almost there. What is missing from this?

</opt>

<opt text='<code>fruit_salad["colour"]</code>' correct="true">

Good job!

</opt>

<opt text='<code>fruit_salad.loc["colour"]</code>' >

We don't need to use `loc`. Let's try again.

</opt>

<opt text='<code>fruit_salad.loc[ : , ["colour"]]</code>' >

This won't give us the correct output for `pd.value_counts()`. Check the slides to double-check.

</opt>

</choice >

**Question 2**

We need summary statistics of both quantitative and categorical columns of the dataframe `fruit_salad`. What code would be suitable for this?

<choice id="2" >
<opt text='<code>df.describe()</code>'>

Is our dataframe named `df`? Will this get summary statistics for all the columns?

</opt>

<opt text='<code>fruit_salad.describe()</code>' >

We want statistics of both quantitative and categorical columns.

</opt>

<opt text='<code>fruit_salad.describe(include = "all")</code>' correct="true">

This looks great! Well done! 

</opt>

<opt text='<code>fruit_salad.summary(include = "all")</code>' >

Is `summary` the correct command here?

</opt>

</choice >

</exercise>

<exercise id="22" title="Using df.describe()">

Let's try and obtain some statistics from our hockey data we've been playing with.

Task:
- Find the statistics of both categorical and quantitative columns. Save the dataframe in an object called `hockey_stats`


<codeblock id="01_22a">

- Are you sure you are saving your objects correctly?
- Are you using using `df.describe(include = "all")` ?

</codeblock>


Task:
- Find the total salary of the team and save it in an object called `player_cost`



<codeblock id="01_22b">


- Are you using df[["column-name"]].sum() for find totals of a column?
</codeblock>


</exercise>

<exercise id="23" title="Practicing Frequency Tables">

Let's get the frequencies of some of our values! We spoke in the slides about the steps we needed to follow to get a frequency table.

Task:
- Let's make an object named `position_column` that consists of just the `Position` column. Note we will be using this for `value_counts` so we must do this with only using single `[]` brackets.
- Find the frequencies of the position for the hockey team using `df.value_counts()` and save it as `position_freq`.
- Next, let's convert that to a dataframe. and save it as object `temp_df`.
- You will need to rename the column `Position` of `temp_df` to `freq` using `df.rename(columns = {})`. Save the object with the name `position_freq_df`.


<codeblock id="01_23">

- Are you sure you are using single `[]` brackets for `position_column`?
- Are you using `pd.DataFrame()` to save `position_freq` as a dataframe?
- Are you renaming your dataframe using the `{"old-column-name" : "new-column-name"}`?

</codeblock>

</exercise>

<exercise id="24" title="Quick Viz with Pandas" type="slides">
<slides source="module1_24">
</slides>
</exercise>

<exercise id="25" title="Practicing Bar Charts">

Now you are going to use the frequency table from the questions in the last section and plot it!

Tasks:
- Use `plot.bar()` with `position_freq` and save the plot in an object named `position_bar`
- Assign a `color` as `Teal`, set opacity to 0.5.
- Don't forget to add a title as "Canuck Player Positions".

<codeblock id="01_25">

- Are you sure you using `alpha` as opacify?
- Are you using the correct Dataframe?
- Did you assign the correct values to color, title and alpha?
- Are you spelling color in the American manner?

</codeblock>

</exercise>

<exercise id="26" title="Practicing Scatterplots">

Ok, let's try our luck with a scatterplot. We want to explore the relationship between `Age` and `Salary`.

Tasks:
- Plots x as `Age` and y as `Salary`. using a scatterplot and save the plot in an object named `age_salary_scatter`
- Set color to `Darkblue` and opacity to 0.4.
- Don't forget to assign a title as "Canuck players Age vs. Salary".

<codeblock id="01_26">

- Are you using `df.plot.scatter()`
- Are you sure you using `alpha` as opacify?
- Are you using the correct Dataframe?
- Are you assigning variables x and y to the correct columns
- Did you assign the correct values to color, title and alpha?
- Are you spelling color in the American manner?

</codeblock>

</exercise>

<exercise id="27" title="What Did We Just Learn?" type="slides">
<slides source="module1_27">
</slides>
</exercise>
