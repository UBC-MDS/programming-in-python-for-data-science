---
title: 'Module 4: Python Without the "Eek" (Basic Python)'
description:
  'In this module you will learn about ...'
prev: /module3
next: /module5
type: chapter
id: 4
---

<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module4/module4_00" start="0:165" end="3:01">
</slides>

</exercise> 

<exercise id="1" title="Python Data Types" type="slides">

<slides source="module4/module4_01">
</slides>

</exercise>

<exercise id="2" title="Name That Data Type">

**Question 1**         


<choice id="1" >
<opt text='True'>


</opt>

<opt text= 'False' correct="true">

Good job!  

</opt>

</choice> 

**Question 2**          


<choice id="2" >
<opt text="">

You may want to look over this before moving forward.

</opt>

<opt text="Each column is a single variable">

You may want to look over this before moving forward.

</opt>

<opt text="Each value is a single cell" >

You may want to look over this before moving forward.

</opt>

<opt text="There are no <code>NaN</code> values in the dataset" correct="true">

You are right. 

</opt>

</choice> 

</exercise>

<exercise id="3" title=" Verbs with Data Types">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's convert the dataframe `lego` into tidy data using `.pivot()`.  

Tasks:

  

<codeblock id="03_10">

- Are you pivoting the correct column named `lego_info` with `values='value'`?
- Are you resetting your index after you pivot?

</codeblock>




</exercise>

<exercise id="4" title="Splitting Strings">



</exercise>

<exercise id="5" title="Wide and Long Dataframe" type="slides">

<slides source="module3/module3_05">

</slides>

</exercise>

<exercise id="6" title="Wide vs Long Questions">

Which of the following is the **wide** dataframe? 


**Dataframe A**
<center> <img src='/module3/Q5a.png'  alt="404 image" width="60%"/></center>


**Dataframe B**
<center> <img src='/module3/Q5b.png'  alt="404 image" width="60%"/></center>

<br>
<choice>
<opt text="Dataframe A">

Not quite! Maybe try re-reading over the content. 

</opt>

<opt text= "Dataframe B" correct="true">

Good job! 

</opt>

</choice> 

</exercise>


<exercise id="7" title="Wide vs Long Questions">

Is the following statement true or false?      

_A long dataframe is always a tidy dataframe._


<choice>
<opt text="True">

Did you read this section? 

</opt>

<opt text= "False" correct="true">

Good job! Of course it depends on the statistical question!

</opt>

</choice> 

</exercise>


<exercise id="8" title="Reshaping with Pivot" type="slides">

<slides source="module3/module3_08">

</slides>

</exercise>

<exercise id="9" title="Pivoting Questions">

**Question 1**          
We use `.pivot()` to convert a wide dataframe with multiple columns into a long dataframe with fewer columns.


<choice id="1" >
<opt text="True" >

The reverse is true.  Please review this section before continuing.

</opt>

<opt text="False" correct="true">

Great work!

</opt>

</choice> 

       
**Question 2**          
Which of the following will reset your index?

<choice id="2" >
<opt text="<code>.index_reset()</code>">

You may want to look over this before moving forward.

</opt>

<opt text="<code>.reset_index()</code>" correct="true">

You may want to look over this before moving forward.

</opt>

</choice> 

</exercise>


<exercise id="10" title="">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**







Tasks:




<codeblock id="04_10">


</codeblock>


</exercise>



<exercise id="30" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_30" start="0:165" end="3:01">>
</slides>
</exercise>

