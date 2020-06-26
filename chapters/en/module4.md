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

How many times do the lyrics "Let it be" occur in the Beatles Hit song of the same title? 


Tasks:
- Use some of the string verbs you learn in lecture to count all the times "let it be" (all upper and lower case versions) appears in the string `lyrics`. 
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

How can we cast from a string to an integer value?

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
 _"I don't care about my elements order."_     
 Who am I? 

<choice id="1" >
<opt text="<code>str</code>">

Which data structure does not have a particular order? 

</opt>

<opt text="<code>list</code>" >

Which data structure does not have a particular order? 
</opt>

<opt text="<code>tuple</code>" >

Which data structure does not have a particular order? 

</opt>

<opt text="<code>set</code>" correct="true">

Well done.

</opt>

</choice> 


**Question 2**          
 _"I can't be changed, I don't accept new elements but I can contain multiple data types"_     
 Who am I? 
 
<choice id="2" >
<opt text="<code>str</code>">

The data structure in fits the first two statements but a string contain characters of all type `str`. 

</opt>

<opt text="<code>list</code>" >

This data structure can add elements using `.append()` 

</opt>

<opt text="<code>tuple</code>" correct="true">

Yes,this can only have the value `None`. 

</opt>

<opt text="<code>set</code>">

This data structure can add to it using `.add()`

</opt>

</choice> 

</exercise>


<exercise id="7" title="Data Structure True and False">


Are the following statements True or False?      


_Tuples are immutable._


<choice id="1">
<opt text="True" correct="true">

Yay! You got it!

</opt>

<opt text= "False" >

This is in fact the oposite! 

</opt>

</choice> 


_Sets can only contain numerical data types._

<choice id="1">
<opt text="True">

Sets can contain many different datatypes apart from numerical values. 

</opt>

<opt text= "False"  correct="true">

Yay! You got it!

</opt>

</choice> 

</exercise>


<exercise id="8" title="The Data Structure Basics">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's explore how to add to  a list, slice it and convert it into a tuple. 


Tasks:


- Using the list provided, add a `pen`, a `scrap paper`, a `7.3` and a `True` element.
- Find the length of the list after adding the element and save the value in an object named `drawer_length`.
- Slice the list from the element 4 to `scrap paper`  and save this in an object named `cleaned_junk_drawer`.
- Finally,  convert it into a set and name it `junk_set`.


<codeblock id="04_10">
- The verbs `.append()` and `len()` may be handy.
- You can convert you list to a tuple with `tuple(). 
- Have you sliced keeping in mind the end of the slice is excluded? 

</codeblock>


</exercise>


<exercise id="9" title="Making a Dataframe from Lists">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's use lists and convert them into a pandas dataframe. 


Tasks:

- Use the lists given in the cell below toto make a dataframe.
- Name the dataframe `family`.


<codeblock id="04_09">
- Are you using `pd.DataFrame()`?
- Are you using the arguments `data` and `columns`?

</codeblock>


</exercise>


<exercise id="10" title="Python Data Structures: Dictionaries" type="slides">

<slides source="module4/module4_10">

</slides>

</exercise>

<exercise id="11" title="Dictionary Questions">

**Question 1**          


Is the following statement True or False?      


_Dictionaries and sets use the same type of brackets to create them._


<choice id="1" >
<opt text="True" correct="true" >

That's right. They both use curly brackets.


</opt>

<opt text="False" >

What kind of brackets do the both use? 

</opt>

</choice> 

       
**Question 2**          

Which verb transforms dictionariesinto dataframes? 

<choice id="2" >
<opt text="<code>.from_dict()</code>">

You seem to be missing something at the begining. 

</opt>

<opt text="<code>pd.dataframe.from_dict()</code>">

Careful with capitalizations. You are extremely close. 

</opt>

<opt text="<code>pd.DataFrame.from_dictionary()</code>">

Maybe it's not quite this long. 

</opt>

<opt text="<code>pd.DataFrame.from_dict()</code>" correct="true">

Nice work!

</opt>

</choice> 

</exercise>


<exercise id="12" title="Dictionary Basics">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Recently Jeremy bought a new Ikea shoe rack.  The packaging included quite a few parts and he is finding it hard to keep track! 


Tasks:
Make a dictionary that includes the quantity of each part included in the Ikea set. 

The shoe rack contained the following parts: 

- 8 `Long Screw`
- 8 `Flat Top Metric Screw`
- 8 `Wood Dowel`
- 2 `Short Screw`
- 1 `Allen Key`
- 1 `Connector Plate` 

- Construct the dictionary so that the part names are the keys and the quantities of the the parts, are the values for the dictionary.
- Name the dictionary `ikea_shoe_rack`.

<codeblock id="04_12">
- Are you naming your dictionary properly? 
- Are all your parts spelt correctly?

</codeblock>


</exercise>



<exercise id="13" title="Building a Dataframe from a Dictionary">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


With no surprise the shoe rack was not the only thing Jeremy bought. below is a table of all his purchases. 

|    | item_name       | collection   |   price |
|---:|:----------------|:-------------|--------:|
|  0 | Bistro Set      | APPLARO      |  216.98 |
|  1 | Reclining Chair | APPLARO      |   80.00 |
|  2 | Shelf Unit      | HYLLIS       |   11.99 |
|  3 | Seat Pad        | KUDDARNA     |   29.99 |
|  4 | Shoe Rack       | TJUSIG       |   29.99 |




Tasks:

- Create the table above from a dictionary using `pd.DataFrame.from_dict()`.
- Name your new dataframe ikea_df




<codeblock id="04_13">
- Are you using lists as the values in your dictionary? 
- Are you making sure to use floats for price?
- are all your items and collections spelts correctly?

</codeblock>


</exercise>

<exercise id="14" title="Dataframes, Series and Column dtypes" type="slides">

<slides source="module4/module4_14">

</slides>

</exercise>

<exercise id="15" title="Name That dtype">

**Question 1**         
 _"I don't care about my elements order."_     
 Who am I? 

<choice id="1" >
<opt text="<code>str</code>">

Which data structure does not have a particular order? 

</opt>

<opt text="<code>list</code>" >

Which data structure does not have a particular order? 
</opt>

<opt text="<code>tuple</code>" >

Which data structure does not have a particular order? 

</opt>

<opt text="<code>set</code>" correct="true">

Well done.

</opt>

</choice> 


**Question 2**          
 _"I can't be changed, I don't accept new elements but I can contain multiple data types"_     
 Who am I? 
 
<choice id="2" >
<opt text="<code>str</code>">

The data structure in fits the first two statements but a string contain characters of all type `str`. 

</opt>

<opt text="<code>list</code>" >

This data structure can add elements using `.append()` 

</opt>

<opt text="<code>tuple</code>" correct="true">

Yes,this can only have the value `None`. 

</opt>

<opt text="<code>set</code>">

This data structure can add to it using `.add()`

</opt>

</choice> 

</exercise>


<exercise id="16" title="Data Structure True and False">


Are the following statements True or False?      


_Tuples are immutable._


<choice id="1">
<opt text="True" correct="true">

Yay! You got it!

</opt>

<opt text= "False" >

This is in fact the oposite! 

</opt>

</choice> 


_Sets can only contain numerical data types._

<choice id="1">
<opt text="True">

Sets can contain many different datatypes apart from numerical values. 

</opt>

<opt text= "False"  correct="true">

Yay! You got it!

</opt>

</choice> 

</exercise>


<exercise id="17" title="The Data Structure Basics">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's explore how to add to  a list, slice it and convert it into a tuple. 


Tasks:


- Using the list provided, add a `pen`, a `scrap paper`, a `7.3` and a `True` element.
- Find the length of the list after adding the element and save the value in an object named `drawer_length`.
- Slice the list from the element 4 to `scrap paper`  and save this in an object named `cleaned_junk_drawer`.
- Finally,  convert it into a set and name it `junk_set`.


<codeblock id="04_17">
- The verbs `.append()` and `len()` may be handy.
- You can convert you list to a tuple with `tuple(). 
- Have you sliced keeping in mind the end of the slice is excluded? 

</codeblock>


</exercise>


<exercise id="18" title="Making a Dataframe from Lists">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**



Tasks:




<codeblock id="04_18">
- Are you using `pd.DataFrame()`?
- Are you using the arguments `data` and `columns`?

</codeblock>


</exercise>



<exercise id="30" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_30" start="0:165" end="3:01">>
</slides>
</exercise>

