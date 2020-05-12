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

<exercise id="3" title="Is it tidy?">

Would this dataframe be defined as tidy?

<center> <img src='module3/crit3fail.png'  alt="404 image"/></center>

<choice>
<opt text="True">

Not quite!  

</opt>

<opt text= "False"" correct="true">

Good job!

</opt>

</choice> 

</exercise>

<exercise id="4" title="Is it tidy?">

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

<exercise id="5" title="Reshaping to Tidy Data" type="slides">

<slides source="module3/module3_05">

</slides>

</exercise>

<exercise id="7" title="Melting and Pivoting Questions">

**Question 1**          
What is required for .....?


<choice id="1" >
<opt text="1" correct="true">

Good job!

</opt>

<opt text="2">

You may want to look over this before moving forward.

</opt>

<opt text="3" >

You may want to look over this before moving forward.

</opt>

</choice> 


**Question 2**         


<choice id="2" >
<opt text='1'>

This is not specifying a sheet.  You may want to review this section. 

</opt>

<opt text= '2' correct="true">

Good job!

</opt>

<opt text='3' >

Not quite but you are on the right track. 

</opt>

</choice> 

</exercise>


<exercise id="8" title="Applying Melt">

.....     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:



<codeblock id="03_07">

</codeblock>

</exercise>

<exercise id="9" title="Applying Pivot">

Let's try reading in a `.txt` file.     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:


<codeblock id="03_08">

</codeblock>

</exercise>