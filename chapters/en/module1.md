---
title: 'Module 1: Python & Pandas - An Unexpected Friendship'
description:
  'In this module, you will be introduced to dataframes and the Pandas Python package.'
prev: module0
next: /module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes" type="slides,video">

<slides source="module1/module1_00" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="1" title="Introduction to Dataframes" type="slides">

<slides source="module1/module1_01">
</slides>

</exercise>

<exercise id="2" title="Describing a Dataframe">

**Question 1**          
What are dataframes comparable to?


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

**Question 2**         
If a `csv` file was opened in a plain text editor, what character would be separating the values of each column? 

<choice id="2">
<opt text='<code> : </code>'>

The "C" in `csv` does not stand for colon. 

</opt>

<opt text='<code> ; </code>'>

 `csv` is an acronym for _______ Separated Values format, so likely not "Semi-Colon".

</opt>

<opt text='<code> , </code>' correct="true">

Great! You have been paying attention.

</opt>

</choice >

</exercise>


<exercise id="3" title="Introduction to Pandas" type="slides">

<slides source="module1/module1_03">
</slides>

</exercise>


<exercise id="4" title="Definitions">

**Question 1**           
What is Pandas?


<choice id="1">
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


**Question 2**           
Which of the following statements is true?


<choice id="2">
<opt text="Attribute and methods can be thought of as nouns and functions as verbs" >

Functions can be compared to verbs but you may want to revisit methods.

</opt>

<opt text="Attribute can be thought of as nouns and functions and methods as verbs" correct="true">

You got it!

</opt>

<opt text="Functions and methods can be thought of as nouns and attributes as verbs">

It may be a good idea to look over this section. 

</opt>

</choice >

</exercise >

<exercise id="5" title="Your First Code!">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Let's try importing pandas and loading in our data.

Tasks:
- Import `pandas` as `pd`.
- Load in data named `canucks.csv`.
- Save the dataframe as `hockey_players`.
- Display the first 5 rows of the dataframe.

<codeblock id="01_05">

- Are you sure you are saving your dataframe as `hockey_players`?
- Are you using `pd.read_csv()`?

</codeblock>

</exercise>

<exercise id="6" title="Your Second Code!">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

What are the column names of the hockey_players dataframe?

Tasks:
- Find the column names of `hockey_players` and save it as `columns_hockey`.
- Display it.


<codeblock id="01_06a">

- Are you sure you are saving your objects as `columns_hockey`?
- Are you using `.columns`?

</codeblock>


What is the shape of the hockey dataframe?

Tasks:
- Find the shape of `hockey_players` and save the result as `hockey_shape`.
- Display it.


<codeblock id="01_06b">

- Are you sure you are saving your objects as `hockey_shape`?
- Are you using `.shape`?

</codeblock>

</exercise>

<exercise id="7" title="Slicing Rows Using df.loc[]" type="slides">

<slides source="module1/module1_07">
</slides>

</exercise>


<exercise id="8" title="Slicing and Dicing Practice">

My dataframe object name is `fruit_salad`.

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```

**Question 1**    
If you wanted only the rows from `cantaloupe` to  `kiwi`, what would your code look like using index labels?

<choice id="1" >
<opt text='<code>fruit_salad.loc[2, 8]</code>'>

This is not the right syntax or number of rows.

</opt>

<opt text='<code>fruit_salad[2, 8]</code>' >

This is not using the right syntax.

</opt>

<opt text='<code>fruit_salad[2:8]</code>' >

This is missing something rather important.

</opt>

<opt text='<code>fruit_salad.loc[2:8]</code>' correct="true">

Good job! 

</opt>

</choice >

**Question 2**    
If you wanted all the rows between `cantaloupe` and `fig` and only columns `name` to `seed`, what would your code look like using index labels?

<choice id="2" >
<opt text='<code>fruit_salad.loc[2:5, "colour":"seed"]</code>'>

I think you are missing the `name` column.

</opt>

<opt text='<code>fruit_salad.loc[2:5, "name":"seed"]</code>' correct="true">

Great!

</opt>

<opt text='<code>fruit_salad.loc["name":"seed", 2:5]</code>' >

This seems to be backward.

</opt>

<opt text= '<code>fruit_salad[2:8, "name":"seed"]</code>'  >

I think you are missing something important.  

</opt>

</choice >

</exercise>

<exercise id="9" title=" Practicing Rows Slicing">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes.   

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

This following code chunk will be used to give you an output of the data `hockey_players`. This will help answer and code in the exercises following it.

<codeblock id="hockey_players">


</codeblock>


Using our `hockey_players` data from the last few questions, let's try slicing it.


Tasks:
- Select the players `Guillaume Brisebois` to `Quinn Hughes`.
- Save the new sliced dataframe as object `benched_players`.
- Display it.



<codeblock id="01_09">

- Are you using `.loc[]`?
- Are you using the correct dataframe labels? Check your spelling and punctuation in row and column labels.

</codeblock>

</exercise>

<exercise id="10" title="Practicing Column Slicing">

**Instructions:**     
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Use the output of the following code chunk to help answer the next question.

<codeblock id="hockey_players">

</codeblock>


Using our `hockey_players` data from the last few questions, let's try slicing it.


Tasks:   
- Select the players `Adam Gaudette` to `Brandon Sutter` and the columns `Player`, `No.`, `Age`, `Height`, `Weight` and `Country`.
- Save the new sliced dataframe as object `star_players`.
- Display it.

<codeblock id="01_10">

- Are you using `.loc[]`?
- Are you using the correct dataframe labels? Check your spelling and punctuation in row and column labels.
- Did you slice both columns and rows?
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="11" title=" Slicing Columns Using .loc[]" type="slides">
<slides source="module1/module1_11">
</slides>
</exercise>

<exercise id="12" title="Slicing Columns Only">

Using my dataframe object named `fruit_salad`, let's answer some slicing questions.

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```


**Question**    
If you wanted all the rows and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would your code look like using index labels?

<choice id="1" >
<opt text='<code>fruit_salad.loc[:, "seed":"weight"]</code>'>

This is almost right but it may be good to check your columns.

</opt>

<opt text='<code>fruit_salad[:, "seeds":"water-content"]</code>' >

This is almost right but it's missing something important! Try looking at the title of the slides we just finished.

</opt>

<opt text='<code>fruit_salad[0:9, "seeds":"water-content"]</code>' >

This is almost right but it's missing something important and it could be condensed! Try looking at the title of the slides we just finished.

</opt>

<opt text='<code>fruit_salad.loc[:, "seeds":"water-content"]</code>' correct="true">

Good job! This has both `.loc[]` and includes the columns we wish to slice here.

</opt>

</choice >

</exercise>



<exercise id="13" title="Selecting Using df.loc[]" type="slides">
<slides source="module1/module1_13">
</slides>
</exercise>


<exercise id="14" title="Rearranging Columns and Rows">

Using my `fruit_salad` dataframe from earlier?

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```

**Question**    
If I wanted to make a tropical salad and the recipe calls for `kiwi`, `cantaloupe` and `guava` in this order and I am only interested in columns ordered as `sweetness`, `weight`, `seed` and  `location`, what would my code look like?

<choice >
<opt text='<code>fruit_salad.loc[8, 2, 6:"sweetness", "weight", "seed", "location"]</code>' >

Unfortunately, this code has many errors in it.

</opt>

<opt text='<code>fruit_salad.loc[[8, 2, 6]:["sweetness", "weight", "seed", "location"]]</code>' >

The way that the rows and columns are separated may need to be looked over.

</opt>

<opt text='<code>fruit_salad.loc[[8, 2, 6], ["sweetness", "weight", "seed", "location"]]</code>' correct="true">

Yes, this looks right!

</opt>

<opt text='<code>fruit_salad.loc[[2, 6, 8], ["location", "seed”, “sweetness", "weight"]]</code>'>

Remember we are rearranging here.

</opt>
</choice >
</exercise>


<exercise id="15" title="Practicing Selecting Using Index Labels">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Use the output of the following code chunk to help answer the next question.

<codeblock id="hockey_players">

</codeblock>


Let's select specific players and columns.

Tasks:
- Select the players `Zack MacEwan`, `Jake Virtanen` and `Jordie Benn` in that order and the columns `Height`, `Weight`, `Salary` and `Country` in that order.
- Save the new sliced dataframe as object `penalty_players`.
- Display it.


<codeblock id="01_15">

- Are you using `.loc[]`?
- Are you using the correct dataframe labels? Are you using names as your row labels?
- Did you slice both columns and rows?
- Are you using 2 sets of `[]` brackets?
- Are you using "quotations"?

</codeblock>

</exercise>


<exercise id="16" title="Selecting Values from a Dataframe" type="slides">
<slides source="module1/module1_16">
</slides>
</exercise>


<exercise id="17" title="Practicing Selecting Values">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes.   

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Use the output of the following code chunk to help complete the next tasks.

<codeblock id="hockey_players">

</codeblock>

Using our `hockey_players` data, try finding the following values and save them in their repective object names. 

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question. We have commented them so that the line won't execute and you can test your code after each step.**_ 

Tasks:
- Save`Thatcher Demko`'s salary in an object named`demko_paid`. 
- How old is `Zack MacEwen`? Save it as object `macewen_age`.
- What position does `Jacob Markstrom` play? Save this as object `markstrom_position`.
- When was `Justin Bailey` born? Save it as an object named `bailey_birth`. 


<codeblock id="01_17">

- Are you using `.loc[]` to select the specific values?
- Are you using single `[]` brackets?
- Are you using "quotations"?

</codeblock>

</exercise>


<exercise id="18" title="Selecting Single Columns" type="slides">
<slides source="module1/module1_18">
</slides>
</exercise>


<exercise id="19" title="Practicing Selecting">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Let's try selecting a specific column.

Tasks:
- Select all the rows from column `Salary` only and save it as `player salary`. (_Hint: you don't need `.loc[]` here_)
- Display it.


<codeblock id="01_19">

- Are you using the correct dataframe labels?
- Are you using double `[]` brackets?
- Are you using "quotations"?

</codeblock>

</exercise>

<exercise id="20" title="Slicing and Selecting Using df.iloc[]" type="slides">
<slides source="module1/module1_20">
</slides>
</exercise>

<exercise id="21" title="Practicing Slicing and Selecting Using Index Position">

Here is our `fruit_salad` data again:

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```


**Question 1**
If I wanted the rows `elderberry`  to `kiwi` and only columns `seeds`, `shape`, `sweetness` and  `water-content` what would my code look like if I was using index positions?

<choice id="1" >
<opt text='<code>fruit_salad.iloc[4:9, 3:]</code>' correct="true">

This is correct!

</opt>

<opt text='<code>fruit_salad.iloc[4:8, 3:7]</code>' >

Not quite, but you are halfway there. 

</opt>

<opt text='<code>fruit_salad.iloc[4:9, 4:7]</code>' >

Not quite, but you are halfway there. 

</opt>

<opt text='<code>fruit_salad.iloc[5:10, 4:8]</code>'>

Are you forgetting that in the Python language we start counting at 0?

</opt>

</choice >

**Question 2**
If I wanted the rows `lemon` and `cantaloupe`  but only the columns `colour`, `weight` and `seeds` in that order, what would my code look like if I was using index position?

<choice id="2" >
<opt text='<code>fruit_salad.iloc[[lemon, cantaloupe], [colour, weight, seeds]]</code>'>

We need to use the index position for this question and when using `.iloc[]`.

</opt>

<opt text='<code>fruit_salad.iloc[[10, 3], [2, 8, 4]]</code>' >

Great! You don't need to specify the second column part because by default the code will slice all the columns.

</opt>

<opt text='<code>fruit_salad.iloc[[9, 2], [1, 7, 3]]</code>' correct="true">

Great Work!

</opt>

<opt text= '<code>fruit_salad[[9, 2], [1, 7, 3]]</code>'  >

I think you are missing something important!

</opt>

</choice >

</exercise>

<exercise id="22" title="Practicing Slicing Using Index Position">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Use the output of the following code chunk to help complete the next tasks.

<codeblock id="hockey_players_i">

</codeblock>

 In previous questions, we tried slicing using index labels on our Canack dataset. Let's try something similar but using the index positions.

Tasks:
- Slice the players `Jacob Markstrom` to `Tim Schaller` and the columns `Player` to `Height`.
- Save the new sliced dataframe as object `skilled_players`.
- Display it.


<codeblock id="01_22">

- Are you using `.iloc[]`?
- Are you using the correct dataframe positions? Are you counting starting from 0?
- Are you going 1 index past the bound you want?

</codeblock>

</exercise>

<exercise id="23" title="Practicing Selecting Using Index Position">

Use the output of the following code chunk to help complete the next tasks.

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

<codeblock id="hockey_players_i">

</codeblock>

These unfortunate Canuck players have various forms of injuries, so let's make a dataframe of players who have injuries by selecting them using their index position.

Tasks:
- Select `Antoine Roussel`, `Thatcher Demko`, `Jake Virtanen` and `Jay Beagle` with only columns `Player`, `Birth Date`, `Experience` and `Salary` in the specified order.
- Save this dataframe as object `injured_players`.
- Don't forget to display it.

<codeblock id="01_23">

- Are you using `.iloc[]`?
- Are you using the correct dataframe positions? Are you counting starting from 0?
- Are you using two sets of `[]` square brackets within your `iloc` brackets?

</codeblock>

</exercise>

<exercise id="24" title="Sorting Dataframes" type="slides">
<slides source="module1/module1_24">
</slides>
</exercise>

<exercise id="25" title="Practice Sorting">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Let's sort our hockey dataframe.

Tasks:
- Sort your `hockey_players` dataframe by Salary from most to least and name your new dataframe as `rich_players`.
- Display it.


<codeblock id="01_25">

- Are you sure you are using `sort_values`?
- Are you using the argument `ascending=False` to order `Salary` in descending order?

</codeblock>

</exercise>

<exercise id="26" title="Summary Statistics" type="slides">
<slides source="module1/module1_26">
</slides>
</exercise>

<exercise id="27" title="Fruit Bowl Statistics">

Bringing back our Fruit Salad dataframe

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```


**Question 1**

Which of the following columns contain numerical data?

<choice id="1" >
<opt text='<code>colour</code>, <code>shape</code>, <code>water-content</code>'>

Maybe it would be a good idea to take a look back at the slides again.

</opt>

<opt text='<code>colour</code>, <code>seed</code>, <code>water-content</code>, <code>weight</code>' >

Some of the columns maybe in here though!

</opt>

<opt text='<code>water-content</code>, <code>weight</code>' correct="true">

This looks great! Well done! 

</opt>

<opt text='All of the columns are categorical' >

Maybe it would be a good idea to take a look back at the slides again.

</opt>

</choice >


**Question 2**

We need summary statistics of both numerical and categorical columns of the dataframe `fruit_salad`. What code would be suitable for this?

<choice id="2" >
<opt text='<code>df.describe()</code>'>

Is our dataframe named `df`? Will this get summary statistics for all the columns?

</opt>

<opt text='<code>fruit_salad.describe()</code>' >

We want statistics of both quantitative and categorical columns.

</opt>

<opt text='<code>fruit_salad.describe(include="all")</code>' correct="true">

This looks great! Well done! 

</opt>

<opt text='<code>fruit_salad.summary(include="all")</code>' >

Is `summary` the correct command here?

</opt>

</choice >

</exercise>

<exercise id="28" title="Using df.describe()">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Try to obtain some statistics from the hockey data.

Tasks:   
- Find the statistics of both categorical and quantitative columns. Save the dataframe in an object called `hockey_stats`.
- Display it.


<codeblock id="01_28a">

- Are you sure you are saving your objects correctly?
- Are you using using `.describe(include="all")` ?

</codeblock>


Tasks:
- Find the total salary of the team and save it in an object called `player_cost`.


<codeblock id="01_28b">


- Are you using `df[["column-name"]].sum()` to find the total of a column?

</codeblock>

</exercise>


<exercise id="29" title="Frequency Tables and Writing CSVs" type="slides">
<slides source="module1/module1_29">
</slides>
</exercise>


<exercise id="30" title="Practicing Frequency Tables">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

    
_**Make sure you remove the hash (`#`) symbol in the coding portions of this question. We have commented them so that the line won't execute and you can test your code after each step.**_ 

Let's get the frequencies of some of our values! We spoke in the slides about the steps we needed to follow to get a frequency table.  

Tasks:
- Let's make an object named `position_column` that consists of just the `Position` column. Note we will be using this for `value_counts` so we must do this with only using single `[]` brackets.
- Find the frequencies of the position for the hockey team using `.value_counts()` and save it as `position_freq`.
- Export `position_freq`  to a csv named `position_frequencies.csv` using `.to_csv()`.
- Don't forget to display it.

_If you get a warning along with your output, that's fine. We will explain why this happens further in the course._

<codeblock id="01_30">

- Are you sure you are using single `[]` brackets for `position_column`?
- Are you using `.to_csv()` to save your `csv`?
- Are you naming your `csv` correctly as "position_frequencies.csv"?

</codeblock>

</exercise>

<exercise id="31" title="Quick Viz with Altair" type="slides">
<slides source="module1/module1_31">
</slides>
</exercise>

<exercise id="32" title="Practicing Bar Charts">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question. We have commented them so that the line won't execute and you can test your code after each step.**_ 

You are going to load the frequency table from the questions that we exported as a `csv` in the last section and plot it!

Tasks:
- Load in the csv named `position_frequencies.csv` you made in the earlier exercise and save it as `position_freq`. 
- Use `.plot.bar()` with `position_freq` and save the plot in an object named `position_bar`.
- Assign a `color` as `Teal`, set opacity to 0.5.
- Don't forget to add a title as "Canuck Player Positions".

<codeblock id="01_32">

- Are you sure you using `alpha` as opacify?
- Are you using the correct Dataframe?
- Did you assign the correct values to `color`, `title` and `alpha`?
- Are you spelling color in the American manner?

</codeblock>

</exercise>

<exercise id="33" title="Practicing Scatterplots">

**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Ok, let's try our luck with a scatterplot. We want to explore the relationship between `Age` and `Salary`.

Tasks:
- Plots x as `Age` and y as `Salary` using a scatterplot and save the plot in an object named `age_salary_scatter`.
- Set color to `Darkblue` and opacity to 0.4.
- Don't forget to assign a title as "Canuck players Age vs. Salary".

_After you successfully create this graph you may notice `1e6` on the top left of your graph. The letter `e` is the scientific notation meaning "10 to the power of". In this case, `1e6` means "to to the power of 6" which is 1,000,000. The `Salary` axis then is expressed with the unit of a million. _

<codeblock id="01_33">

- Are you using `.plot.scatter()`
- Are you sure you using `alpha` as opacity?
- Are you using the correct Dataframe?
- Are you assigning variables x and y to the correct columns
- Did you assign the correct values to color, title and alpha?
- Are you spelling color in the American manner?

</codeblock>

</exercise>

<exercise id="34" title="What Did We Just Learn?" type="slides,video">
<slides source="module1/module1_34" start="0:165" end="3:01">
</slides>
</exercise>
