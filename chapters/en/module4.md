---
title: 'Module 4: Python Without the "Eek" (Basic Python)'
description:
  'In this module you will learn about basic Python data types and  structures. You will explore what data types and structures are used to create Pandas Dataframe and how understanding column dtypes is important to data analysis.'
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

For the next few questions, name the data type of each value.

**Question 1**         

```python
question_1 = 'NaN'
````

<choice id="1" >
<opt text="<code>int</code>">

Do you notice the quotations? 

</opt>

<opt text="<code>float</code>">

Do you notice the quotations? 

</opt>

<opt text="<code>NoneType</code>">

Do you notice the quotations? 

</opt>

<opt text="<code>bool</code>">

Do you notice the quotations? 

</opt>

<opt text="<code>str</code>" correct="true">

Although, this spells out "NaN", The value is within quotations indicating it is a string. 

</opt>

</choice> 

**Question 2**          


```python
question_1 = 3.6
```

<choice id="2" >
<opt text="<code>int</code>">

We are not trying to trick you here. 

</opt>

<opt text="<code>float</code>" correct="true">

Nothing tricky about this one.  

</opt>

<opt text="<code>NoneType</code>">

We are not trying to trick you here. 

</opt>

<opt text="<code>bool</code>">

We are not trying to trick you here. 

</opt>

<opt text="<code>str</code>">

We are not trying to trick you here. 

</opt>

</choice> 


**Question 3**          


Which data type can only take on 1 value?

<choice id="3" >
<opt text="<code>int</code>">

You may want to look over this before moving forward.

</opt>

<opt text="<code>float</code>" >

You may want to look over this before moving forward. 

</opt>

<opt text="<code>NoneType</code>" correct="true">

Yes,this can only have the value `None`. 

</opt>

<opt text="<code>bool</code>">

This can actually take 2 values! 

</opt>

<opt text="<code>str</code>">

You may want to look over this before moving forward. 

</opt>

</choice> 

</exercise>

<exercise id="3" title=" String Verbs">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_



Tasks:
- Use some of the string verbs you learn in lecture to count all the times "let it be" (all upper and lower case versions) is said in the Beatles hit song. 
- Save it in an object named `letitbe_count`

  

<codeblock id="04_03">

- Are you using `.lower()`?
- Are you using `.count()` with the argument `let it be`?

</codeblock>




</exercise>

<exercise id="4" title="Casting Data Types">


**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_



Tasks:

- Convert `string1` to a `float` in an object named `pi`.
- Convert the object `pi` now into an `int` named `pi_slice`.

  

<codeblock id="04_04">

- Are you using `float()`?
-  Are you using `int()`?

</codeblock>

**Question 1**     
Can you directly cast from a value of type `str` to a value of type `int`?    
Try it out in the cell above!

<choice id="1" >
<opt text="You can">

Did you try it? 

</opt>

<opt text="You cannot"  correct="true">

Python won't let you cast directly from a value of type `str` to a value `int`. 

</opt>

</choice> 


</exercise>

<exercise id="5" title="Python Data Structures: Lists, Tuples and Sets" type="slides">

<slides source="module4/module4_05">

</slides>

</exercise>

<exercise id="6" title="Name that Data Structure">

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


<exercise id="7" title="Data Structure True and False">

Is the following statement true or false?      




<choice>
<opt text="True">

Did you read this section? 

</opt>

<opt text= "False" correct="true">

Good job! Of course it depends on the statistical question!

</opt>

</choice> 

</exercise>


<exercise id="8" title="The Data Structure Basics">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**







Tasks:




<codeblock id="04_10">


</codeblock>


</exercise>


<exercise id="9" title="Making a Dataframe from Lists">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**







Tasks:




<codeblock id="04_09">


</codeblock>


</exercise>


<exercise id="10" title="Python Data Structures: Dictionaries" type="slides">

<slides source="module3/module3_08">

</slides>

</exercise>

<exercise id="11" title="Dictionary Questions">

**Question 1**          



<choice id="1" >
<opt text="True" >



</opt>

<opt text="False" correct="true">

Great work!

</opt>

</choice> 

       
**Question 2**          


<choice id="2" >
<opt text="<code></code>">

You may want to look over this before moving forward.

</opt>

<opt text="<code></code>" correct="true">

Nice work!

</opt>

</choice> 

</exercise>


<exercise id="12" title="Dictionary Basics">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**







Tasks:




<codeblock id="04_12">


</codeblock>


</exercise>



<exercise id="13" title="Building a Dataframe from a Dictionary">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**







Tasks:




<codeblock id="04_13">


</codeblock>


</exercise>



<exercise id="30" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_30" start="0:165" end="3:01">>
</slides>
</exercise>

