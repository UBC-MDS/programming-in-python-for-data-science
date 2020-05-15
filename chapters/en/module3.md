---
title: 'Module 3: Tidy Data and Joining Dataframes'
description:
  'In this module you will learn about tidy data and how to transform your dataset into a tidy format. It will also focus on how to combine and stack multiple dataframes.'
prev: /module2
next: /module4
type: chapter
id: 3
---

<exercise id="0" title="Module Learning Outcomes" type="slides">

<slides source="module3/module3_00">
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

.....     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:



<codeblock id="module3/03_07">

</codeblock>

</exercise>

<exercise id="8" title="Applying Pivot II">

  
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:


<codeblock id="03_08">

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
`.melt()` has the same arguments as `.pivot()`?

<choice id="2" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job!

</opt>

</choice> 

</exercise>


**Question 3**         
`.melt()`  and `.pivot()` always transforms the data into "Tidy Data"

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

.....     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:



<codeblock id="03_11">

</codeblock>


Is this data tidy? 

<choice id="1">
<opt text='Yes' >


</opt>

<opt text='No' correct="true">

</opt>


</choice> 

</exercise>


<exercise id="12" title="Hierarchical Indexing" type="slides">

<slides source="module3/module3_12">

</slides>

</exercise>


<exercise id="13" title="Hierarchical Indexing Questions">

**Question 1**          



<choice id="1" >
<opt text="True"  correct="true" >

Great work! 

</opt>

<opt text="False">

It may be a good idea to look over the last section again. 

</opt>

</choice> 


**Question 2**         

<choice id="2" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job!

</opt>

</choice> 

</exercise>


**Question 3**         


<choice id="3" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job! Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

</choice> 

</exercise>


<exercise id="14" title="Setting Multiple Indexes">

.....     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:



<codeblock id="03_14">

</codeblock>


</exercise>

<exercise id="15" title="Applying Stacking">

  
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:


<codeblock id="03_15">

</codeblock>

</exercise>

<exercise id="16" title="Concate" type="slides">

<slides source="module3/module3_16">

</slides>

</exercise>





