---
title: 'Module 3: Tidy Data and Joining Dataframes'
description:
  'In this module you will learn about tidy data and how to transform your dataset into a tidy format. It will also focus on how to combine and stack multiple dataframes.'
prev: /module2
next: /module4
type: chapter
id: 3
---

<exercise id="0" title="Module Learning Outcomes" type="slides,video">

<slides source="module3/module3_00" start="0:165" end="3:01">
</slides>

</exercise> 

<exercise id="1" title="What is Tidy Data?" type="slides">

<slides source="module3/module3_01">
</slides>

</exercise>

<exercise id="2" title="Tidy Data Questions">

**Question 1**         

Tidy data is defined differently for every dataset.

<choice id="1" >
<opt text='True'>

All datasets although informatively different, all have the same anatomy. 

</opt>

<opt text= 'False' correct="true">

Good job! Although dataset can contain different information and data, they are consist of the same semantics. 

</opt>

</choice> 

**Question 2**          

Which of the following does not characterize a tidy dataset?

<choice id="2" >
<opt text="Each row is a single observation">

You may want to look over this before moving forward.

</opt>

<opt text="Each column is a single variable">

You may want to look over this before moving forward.

</opt>

<opt text="Each value is a single cell" >

You may want to look over this before moving forward.

</opt>

<opt text="There are no <code>NA</code> values in the dataset" correct="true">

You are right. It is possible to still have tidy data with missing values. 

</opt>

</choice> 

</exercise>

<exercise id="3" title="Is it Tidy I ?">

Would this dataframe be defined as tidy?

<center> <img src='module3/crit3fail.png'  alt="404 image"/></center>

<choice>

<opt text="True">

Not quite!  

</opt>

<opt text= "False" correct="true">

Good job!

</opt>

</choice> 

</exercise>

<exercise id="4" title="Is it Tidy II?">

Would this dataframe be defined as tidy?

<center> <img src='module3/Q4.png'  alt="404 image"/></center>

<choice>
<opt text="True">

Not quite!  

</opt>

<opt text= "False" correct="true">

Good job!

</opt>

</choice> 

</exercise>

<exercise id="5" title="Reshaping Using Pivot" type="slides">

<slides source="module3/module3_05">

</slides>

</exercise>

<exercise id="6" title="Pivoting Questions">

**Question 1**          
We use pivoting to convert a wide dataframe with multiple columns into a long dataframe with fewer columns.


<choice id="1" >
<opt text="True" >

The reverse is true. Please review this section before continuing.

</opt>

<opt text="False" correct="true">

Great work!

</opt>

</choice> 


**Question 2**         
What must you do before you use `.pivot()`?

<choice id="2" >
<opt text='Rename your column label to numbers'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'Reset your index' correct="true">

Good job!

</opt>

<opt text='Sort your dataframe by index' >

It may be a good idea to look over the last section again. 

</opt>

</choice> 

</exercise>


<exercise id="7" title="Applying Pivot I">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's convert the dataframe `lego` into tidy data using `.pivot()`.

Tasks:

- Convert the untidy data into tidy data using `.pivot()`.
- Name the new dataframe `tidied_lego`.


<codeblock id="03_07">
- Are you pivoting the correct column named `lego_info` with `values='value'`?
- Are you resetting your index before you pivot?

</codeblock>

</exercise>

<exercise id="8" title="Applying Pivot II">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's convert the dataframe `lego` into tidy data but this time preserve all the columns in the dataframe by using `.pivot_table()`.

Tasks:

- Convert the untidy data into tidy data using `.pivot_table()` making sure to keep all the columns. 
- Assign your new dataframe `set_num` as your index.
- Name the new dataframe `tidied_lego`.

<codeblock id="03_08">
- Are you using the correct arguments such as `index`, `columns`, and `values`?
- Are you pivoting the correct column named `lego_info` with `values='value'`?
- Are you resetting your index before you pivot?
- Are you making sure to use `index=['set_num', 'name', 'year']`
- Are you reseting and setting your index again after you pivot?

</codeblock>

</exercise>


<exercise id="9" title="Reshaping Using Melt" type="slides">

<slides source="module3/module3_09">

</slides>

</exercise>


<exercise id="10" title="Melting Questions">

**Question 1**          
We use melt to convert a wide dataframe with multiple columns into a long dataframe with fewer columns.


<choice id="1" >
<opt text="True"  correct="true" >

Great work! 

</opt>

<opt text="False">

It may be a good idea to look over the last section again. 

</opt>

</choice> 


**Question 2**         
`.melt()` has the same arguments as `.pivot()`.

<choice id="2" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job!

</opt>

</choice> 

**Question 3**     

`.melt()`  and `.pivot()` always transforms the data into "tidy data".

<choice id="3" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job! Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

</choice> 

</exercise>


<exercise id="11" title="Applying Melt">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's melt the `lego` dataframe. The `lego` dataframe has 2 new columns named `matte` and `transparent`. These columns refers to the opacity of the blocks and the values refer to the number of pieces of each included in the set. 

Tasks:

- `melt` the dataframe columns `matte` and `transparent` into a single column named `opacity` and name the values column `quantity`.
- Assign `set_num` ad the index in your new dataframe. 
- Name the new dataframe `tidied_lego`.

<codeblock id="03_11">

- Are you melting the correct columns named `matte` and `transparent`?
- Are you resetting your index before you pivot?
- Are you making sure to use all the columns (except `matte` and  `transparent` in the argument `id_vars`?
- Are you setting your index again after you melt?

</codeblock>

Have we made the data tidied by melting these 2 columns? 

<choice id="1">
<opt text='Yes' correct="true">

The data now meets all 3 criteria. 

</opt>

<opt text='No'>

Start by going through the tidy data criteria. Does this data meet all three? 

</opt>


</choice> 

</exercise>


<exercise id="12" title="Hierarchical Indexing" type="slides">

<slides source="module3/module3_12">

</slides>

</exercise>


<exercise id="13" title="Hierarchical Indexing Questions">

**Question 1**          

What verb is used to sort the values in the index? 

<choice id="1" >
<opt text="<code>.sort_index()</code>"  correct="true" >

Great work! 

</opt>

<opt text="<code>.sort_values()</code>">

This is used to sort columns. Index values are not recognized as a typical column. 

</opt>

<opt text="<code>.index_sort()</code>">

You are on the right track but I think you may have it backwards!

</opt>

<opt text="<code>.sort()</code>">

It may be a good idea to look over the last section again. 

</opt>

</choice> 


**Question 2**      

Is the following `fruit_salad` dataframe stacked or unstacked?

<center> <img src='module3/hi_fruit.png'  alt="404 image" /></center>


<choice id="2" >
<opt text='Stacked' correct="true">

Nice! The columns are stacked on top of each other.  

</opt>

<opt text= 'Unstacked'>

Do you notice anything interesting about the third column? 

</opt>

</choice> 

</exercise>
 
<exercise id="14" title="Hierarchical Indexing slicing">

Oh look it's time for dessert! Bring in the dataset `fruit_salad` . 

```out
                           location   seed   shape    sweetness   water-content  weight
        name      colour                    
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

It appears that there are 2 indexes this time around `name` ***and*** `colour`! How would you select the `guava` row now? 

<choice id="1" >

<opt text= "<code>fruit_salad.loc[['guava, 'green']]</code>">

hhhhmmm, something seems a little off with your parentheses. Are you sure they are all the right type? 

</opt>

<opt text= "<code>fruit_salad.loc['guava]</code>">

Good job! Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

<opt text= "<code>fruit_salad.loc[('guava, 'green')]</code>"  correct="true">

Nice work! You definitely paid attention!

</opt>

<opt text= "<code>fruit_salad[('guava, 'green')]</code>">

I think you are missing a verb in your sentence!  

</opt>

</choice> 

</exercise>


<exercise id="15" title="Setting Multiple Indexes">
   
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's start simple. Set multiple indexes for one of our lego dataframes. 


Tasks:
- Create hierarchical indexes from the columns `set_num` and `name`.
- Name the new dataframe `lego_build`.


<codeblock id="03_15">
- Are you using the verb `.set_index()`?
- Are you wrapping the column days with square brackets?

</codeblock>

</exercise>

<exercise id="16" title="Applying Stacking">
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's find the maximum and minimum number of pieces per set there are in each lego theme. 

Tasks:
- From the `lego` dataframe, make groups from the `theme_name` columns.
- Find the max and min values for the `num_parts` column only using `.agg()`.
- Stack the max and min values using `.stack()`.
- Name the new dataframe `stacked_lego`.


<codeblock id="03_16">
- Are you using the verb `.groupby()` witht the correct column named `theme_name`?
- Are you using arg where you can designate different statistics to different columns to obtain only the `num_parts` column?
- Are you remembering to `.stack()`?

</codeblock>

</exercise>

<exercise id="17" title="Concat" type="slides">

<slides source="module3/module3_16">

</slides>

</exercise>

<exercise id="18" title="Concat questions">

**Question 1**          

Which ways can we combine dataframes using `.concat()`?

<choice id="1" >

<opt text="Horizontally Only">

You are halfway there. You may want to think about why you chose this way and not vertically as well. 

</opt>

<opt text="Vertically Only">

You are halfway there. You may want to think about why you chose this way and not horozontally  as well. 


</opt>

<opt text="Neither Horizontally or Vertically" >

It may be a good idea to look over the last section again. 

</opt>

<opt text="Both Horizontally and Vertically" correct="true" >

Great work! We cann combine rows from two dataframes or combine columns. 

</opt>

</choice> 


**Question 2**     

 If we concatinated Dataframe A with Dataframe B using an **inner** join, What happens to the row indices only available in  Dataframe A?

<choice id="2" >
<opt text='They would appear in the new dataframe as <code>NaN</code> values'>

This would happen with an **outer** join.  

</opt>

<opt text= 'They would not appear in the new dataframe but all the columns from Dataframe B would.'  correct="true">

Good job!

</opt>

<opt text= 'They would not appear in the new dataframe and all the columns from Dataframe B would not be present in the final dataframe'  correct="true">

With any join type, All columns would be in the new dataframe.

</opt>


<opt text= 'An error message would occur and no new dataframe would be produced'  correct="true">

Why wouldn't the code work? 

</opt>

</choice> 

**Question 3**         

Which of the following are correct? 


<choice id="3" >
<opt text='Concatinating horizontally requires the argument <code>axis=1</code>', correct="true">

Good job! Maybe more solutions are correct...


</opt>

<opt text='Concatinating vertically requires the argument <code>axis=0</code>'  correct="true">

Good job! Did you get multiple correct answers? 

</opt>

<opt text='Concatinating vertically requires the argument <code>axis=1</code>'>

I think you got mixed up. Try reading over the notes again. 

</opt>

<opt text='Concatinating horizontally requires the argument <code>axis=0</code>'>

I think you got mixed up. Try reading over the notes again. 

</opt>

</choice> 

</exercise>


<exercise id="19" title="Concatenating Rows">
 
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_ 

Sometime we accumulate additional data that we need to combine with our exisiting data. In the following question, we need to combine our dataframes together to have a complete collection of all the lego sets that exist. 

Tasks:

- Combine the two dataframes `lego_top` and `lego_bottom` vertically to make 1 large complete dataframe.
- Name the new dataframe full_set.
- Save the new dimension of `full_set` in an object named `full_set_shape`.
- Display the new dataframe.


<codeblock id="03_19">
- Are you using `pd.concat()`?
- Are you concatenating in the correct order with `lego_top` first and `lego_bottom` second?
- Are you putting your dataframes within square brackets? 
- Are you using `axis=0`
- Are you using `.shape` to find the dimension of the new dataframe?

</codeblock>

</exercise>

<exercise id="20" title="Concatenating Columns">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_ 

Our goal is to obtain a dataframe with the lego_set names and the total amount of pieces in each set but we only have 2 lego dataframes (with the same indexes). One dataframe has the set names and the other contains information amount the number of matte and transparent pieces included in each set. Complete this question by using `pd.concat()` and techniques we learned in the previous model.

Tasks:

- Combine the two dataframes horizontally to make 1 large complete dataframe using an outer join.
- Name the new dataframe `lego_full`.
- Make a new column named `total_pieces` by adding up columns `matte` and `transparent`.
- Sort the dataframe by `total_pieces` in descending order.
- Save this in an object named `lego_details`.
- Display the new dataframe.


<codeblock id="03_20">

- Are you using `pd.concat()`?
- Are you concatenating the dataframes `lego_base` with `lego_opacity`?
- Are you putting your dataframes within square brackets? 
- Are you using `axis=1` and `join='outer'`
- Are you using `.assign()` to make a new column named `total_pieces`?
- Are you using using `.sort_values()` with the argument `ascending=False`

</codeblock>

</exercise>

<exercise id="21" title="Merge" type="slides">

<slides source="module3/module3_20">

</slides>

</exercise>


<exercise id="22" title="Merge Questions">

**Question 1**          

Which of the following are **not** ways in which you can join dataframes using `.merge()`

<choice id="1" >
<opt text="Vertically"  correct="true" >

Great work! We cannot join dataframes vertically with `.merge()`. 

</opt>

<opt text="Outer">

"Outer" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Inner">

"Inner" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Left">

"Left" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Right">

"Right" joins are possible with the `how` argument in `merge()`.

</opt>

</choice> 


**Question 2**    

Which join is defaulted when using `.merge()`

<choice id="2" >
<opt text='Outer'>

Are you confusing `.pd.concate()`'s default joining type?

</opt>

<opt text= 'Inner' correct="true">

Good job! Unlike `.pd.concate()`, "inner" is the default join for `.merge()`.

</opt>

<opt text='Left'>

This is an option for the argument `how` but not the default. 

</opt>


</opt>

<opt text='Vertical'>

Are you confusing `.merge()` with `.pd.concate()`?

</opt>

</choice> 

**Question 3**         

What is outcome that is similar between all 4 types of joins? 

<choice id="3" >
<opt text='They all need at least 1 of the dataframe's identifying key column to be an index.'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'They all will produce a new dataframe will columns from both of the initial dataframes' correct="true">

Good job! Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

<choice id="3" >
<opt text='They all produce rows with <code>NaN</code> values'>

What about inner joins that only result with the rows present in both dataframes?

</opt>

<choice id="3" >
<opt text='They all must be the same dimensions'>

It's still possible to have dataframes that have completely different dimensions joined together. 

</opt>


</choice> 

</exercise>


<exercise id="23" title="Merging I">

      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

In this exercise you are going to join the two dataframes `lego_base` and `lego_opacity` but this time you are going to want to use an outter join. Next we are going to make a scatter plot that 

Tasks:

- Combine the two dataframes horizontally to make 1 large complete dataframe using an inner join.
- Name the new dataframe `lego_full`.
- Make a new column named `total_pieces` by adding up columns `matte` and `transparent`.
- Sort the dataframe by `total_pieces` in descending order.
- Save this in an object named `lego_details`.
- Display the new dataframe.


<codeblock id="03_23">

</codeblock>


</exercise>

<exercise id="24" title="Merging II">

  
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:


<codeblock id="03_23">

</codeblock>

</exercise>


<exercise id="25" title="What Did We Just Learn?" type="slides,video">
<slides source="module3/module3_25" start="0:165" end="3:01">>
</slides>
</exercise>



