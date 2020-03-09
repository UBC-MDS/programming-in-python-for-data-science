---
title: 'Module 1: Python & Pandas - An Unexpected Friendship!'
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
It's index is labeled with the `name` of the fruit.
My column names in order are; `colour`, `location`, `seeds`, `shape`, `sweetness`, `water-content` and  `weight`.

**Question 1**

If I wanted all the rows and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would my code look like using index labels? 

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

If I wanted all the rows between `cantaloupe`  and `kiwi` and all the columns? What would my code look like using index labels? 

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

<exercise id="7" title="Practicing Slicing Using Index Labels">

Using our `hockey_players` data from the last few questions with the index labelled with `Player` name, Let's try slicing it.

Tasks:
- Select the players `Adam Gaudette` to `Brandon Sutter` and the columns `No.`, `Age`, `Height`,	`Weight` and `Country`. 
- Save the new sliced dataframe as object `benched_players`.
- Display it. 

<codeblock id="01_07">

- Are you using `df.loc[]`
- Are you using the correct dataframe labels? Check your spelling and punctuation in row and column labels. 
- Did you slice both columns and rows? 
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="8" title="Practice Slicing Using Index Labels">

This question is very similar to the previous question but now our dataframe index is labelled with numbers instead of names, Let's try slicing it.

Tasks:
- Selet the players `Adam Gaudette` to `Brandon Sutter` and the columns `Player`, `No.`, `Age`, `Height`,	`Weight` and `Country`.
- Save he new sliced dataframe as object `benched_players`.
- Display it.

<codeblock id="01_08">

- Are you using `df.loc[]`
- Are you using the correct dataframe labels? Are you using numbers as your row labels? 
- Did you slice both columns and rows? 
- Are you using "quotations" properly?

</codeblock>

</exercise>

<exercise id="9" title="Selecting Using df.loc[]" type="slides">
<slides source="module1_09">
</slides>
</exercise>

<exercise id="10" title="Practicing Selecting Using Index Labels">

Let's try selecting specific players and columns. 

Tasks: 
- Select all the rows from column `Salary` only and save it as `player_salary` (_Hint: you don't need `loc` here_) 
- Select The players `Zack MacEwen`, `Jake Virtanen` and `Jordie Benn` in that order and the columns  `Height`, `Weight.`, `Salary` and  `Country` in that order.
- Save the new sliced dataframe as object `penalty_players`.
- Display it 


<codeblock id="01_10">

- Are you using `df.loc[]`
- Are you using the correct dataframe labels? Are you using names as your row labels? 
- Did you slice both columns and rows? 
- Are you using double `[]` brackets? 
- Are you using "quotations" ?

</codeblock>

</exercise>

<exercise id="11" title="Practicing Selecting Using Index Labels">

This question is very similar to the previous question but now our dataframe index is labelled with numbers instead of names. We now want to select the `Age` column to use at a future dat now too. 

Tasks:
- Select all the rows from column `Age` only and save it as `player_ages`. (_Hint: you don't need `loc` here_) 
- Select rhe players `Zack MacEwen`, `Jake Virtanen` and `Jordie Benn` in that order and the columns `Player`, `Height`, `Weight.`, `Salary` and  `Country` in that order.
- Save this new sliced dataframe as object `penalty_players`.
- Display it.

<codeblock id="01_11">

- Are you using `df.loc[]`
- Are you using the correct dataframe labels? Are you using numbers as your row labels? 
- Did you slice both columns and rows? 
- Are you using double `[]` brackets? 
- Are you using "quotations" where applicable?

</codeblock>

</exercise>


<exercise id="12" title="Slicing and Selecting Using df.iloc[]" type="slides">
<slides source="module1_12">
</slides>
</exercise>

<exercise id="13" title="Practicing Slicing and Selecting using index position">

Remember my `fruit_salad` dataset from earlier? 
It had row names; `apple`, `banana`, `cantaloupe`, `dragon-fruit`, `elderberry`, `fig`, `Guava`, `huckleberry`, `kiwi` and `lemon` (in that order). 
The index was labeled with the `name` of the fruit.
It's column names in order were; `colour`, `location`, `seeds`, `shape`, `sweetness`, `water-content` and  `weight`.

**Question 1**

If I wanted the rows `elderberry`  to `kiwi` and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would my code look like if I was using index positions? 

<choice id="1" >
<opt text='fruit_salad.iloc[4 : 9 , 2 : 6]' correct="true">

This is correct! We need to use `iloc` and go one position further then the last bound to select it 

</opt>

<opt text='fruit_salad.iloc[4 : 8 , 2 : 5]' >

I think you may be forgetting that the last interval value does not get selected. 

</opt>

<opt text='fruit_salad.iloc[5 : 9 , 3 : 6]' >

Are you forgetting that in the Python language we start counting at 0? You also may be forgetting that the last interval value does not get selected. 

</opt>

<opt text='fruit_salad.iloc[5 : 10 , 3 : 7]'>

Are you forgetting that in the Python language we start counting at 0? 

</opt>

</choice >

**Question 2**

If I wanted the rows `lemon` and `cantaloupe`  but only the columns `colour`, `weight` and `seeds` in that order using indec position. what would my code look like if I was using index position? 

<choice id="2" >
<opt text='fruit_salad.iloc[[lemon, cantaloupe], [colour, weight, seeds]]'>

We need to use the index position for this question and when using `iloc`.

</opt>

<opt text='fruit_salad.iloc[[10, 3], [1 ,7 ,3]]' >

Great! You don't need to specify the second column part because by default the code will slice all the columns. 

</opt>

<opt text='fruit_salad.iloc[[9, 2], [0 ,6 ,2]]' correct="true">

Great Work!

</opt>

<opt text= 'fruit_salad[[9, 2], [0 ,6 ,2]]'  >

I think you are missing something inportant!

</opt>

</choice >

</exercise>

<exercise id="14" title="Practicing Slicing Using Index Position">

 In previous questions we tried slicing using index labels on our Canack dataset. Let's try something similar but using the index positions.

Tasks:
- Select the players `Jacob Markstrom` to `Tim Schaller` and the columns `Player`, `No.`, `Age` and `Height`.
- Save the new sliced dataframe as object `skilled_players`.
- Display it 


<codeblock id="01_14">

- Are you using `df.iloc[]`
- Are you using the correct dataframe positions? Are you counting starting from 0? 
- Are you going 1 index past the bound you want?

</codeblock>

</exercise>

<exercise id="15" title="Practicing Selecting Using Index Position">

Now we need a table of just those who have injuries. These unfortunate Canuck players have various form of injuries, let's select them using their index position. 

Tasks: 
- Select `Antoine Roussel`, `Thatcher Demko`, `Jake Virtanen` and `Jay Beagle` with only columns `Player`, `Birth Date`, `Experience` and `Salary` in the specified order. 
- Save this dataframe as object `injured_players`.
- Don't forget to display it. 

<codeblock id="01_15">

- Are you using `df.iloc[]`
- Are you using the correct dataframe positions? Are you counting starting from 0? 
- Are you using two sets of `[]` square brackets withing your `iloc` brackets?

</codeblock>

</exercise>

<exercise id="16" title="Summary Statistics" type="slides">
<slides source="module1_16">
</slides>
</exercise>


<exercise id="17" title="Fruit Bowl Statistics">

**Question 1**

Let's say I have a dataframe named  `fruit_salad` with a column of interest named `colour`.  
If you want to get the frequency of occurances of `colour` using `pd.value_counts(X)` what is `X`? 

<choice id="1" >
<opt text='fruit_salad[colour]'>

Almost there. What is missing from this? 

</opt>

<opt text='fruit_salad["colour"]' correct="true">

Good job!

</opt>

<opt text='fruit_salad.loc["colour"]' >

We don't need to use `loc`. L et's try again. 

</opt>

<opt text='fruit_salad.loc[ : , ["colour"]]' >

This won't give us the correct output for `pd.value_counts()`. Check the slides to double check. 

</opt>

</choice >

**Question 2**

We need summary statictics of both quantitative and categorical columns of the dataframe `fruit_salad`. What code would be suitable for this? 

<choice id="2" >
<opt text='df.describe()'>

Is our dataframe named `df`? Will this get summary staticstics for all the columns? 

</opt>

<opt text='df.describe(include = "all")' >

Is our dataframe named `df`? 

</opt>

<opt text='fruit_salad.describe(include = "all")' correct="true">

This looks great! Well done!  

</opt>

<opt text='fruit_salad.summary(include = "all")' >

Is `summary` the correct command here? 

</opt>

</choice >

</exercise>

<exercise id="18" title="Using df.describe()">

Let's try and obtain some statistics from our hockey dataset we've been playing with. 

Task:
- Find the statistics of both categorical and quantitive columns. Save the dataframe in an object called `hockey_stats`
- Save the most prominent country in an object called `hockey_country` (_Don't forget to put it between "quotation"_)
- Save the value of the tallest play in `tallest_height`
- What is the youngest age? Save it in an object named `youngest_age`
- Find the total Salary of the team and save it in an object called `player_cost`



<codeblock id="01_18">

- Are you sure you are saving your objects correctly?
- Are you using using `df.describe(include = "all")` ? 
- For answers that are words make sure you surround them with quotations. You don't need quotes for number. 
- Are you using df[["column-name"]].sum() for find totals of a column? 
</codeblock>

</exercise>

<exercise id="19" title="Practicing">

Let's get the frequencies of some of our values! We spoke in lecture about the steps we needed to follow to get a frequency table.

Task:
- Let make an object named `position_column` that consists of just the `Position` column. Note we will be using this for `value_counts` so we must do this with only using single `[]` brackets. 
- Find the frequencies of the position for the hockey team using `df.value_counts()` and save it as `position_freq`. Make sure you sort it too! 
- Next let's convert that to a dataframe. and save it as object `temp_df`
- You will need to rename the column `Position` of `temp_df` to `freq` using `df.rename(columns = {})`. Save the object with the name `position_freq_df`. 


<codeblock id="01_19">

- Are you sure you are using single `[]` brackets for `position_column`?
- Are you using `pd.DataFrame()` to save `position_freq` as a dataframe? 
- Are you renaming your dataframe using the `{"old-column-name" : "new-column-name"}`?

</codeblock>

</exercise>

<exercise id="20" title="Quick Viz with Pandas" type="slides">
<slides source="module1_20">
</slides>
</exercise>

<exercise id="21" title="Practicing Bar Charts">

Now you are going to use the frequency table from the questions in the last section and plot it!

Tasks: 
- Use `plot.bar()` with `position_freq` and save the plot in an object named `position_bar`
- Assign a `color` as `Teal`, set opacity to 0.5 and don't forget to add a title as "Canuck Player Positions"  

<codeblock id="01_21">

- Are you sure you using `alpha` as opacify? 
- Are you using the correct Dataframe?
- Did you assign the correct values to color, title and alpha?
- Are you spelling color in the American manner? 

</codeblock>

</exercise>

<exercise id="22" title="Practicing Scatterplots">

Ok let's try our luck with a scatterplot. We want to explore the relationship between `Age` and `Salary`. 

Tasks:
- Plots x as `Age` and y as `Salary`. using a scatterplot and save the plot in an object named `age_salary_scatter`
- Set color to `Darkblue`, opacity to 0.4 and don't forget to assign a title as "Canuck players Age vs. Salary" 

<codeblock id="01_22">

- Are you using `df.plot.scatter()`
- Are you sure you using `alpha` as opacify? 
- Are you using the correct Dataframe?
- Are you assigning variables x and y to the correct columns 
- Did you assign the correct values to color, title and alpha?
- Are you spelling color in the American manner? 

</codeblock>

</exercise>

<exercise id="23" title="What Did We Just Learn?" type="slides">
<slides source="module1_23">
</slides>
</exercise>