---
title: 'Module 4: Python Without the "Eek" (Basic Python)'
description:
  'In this module, you will learn about basic Python data types and structures. You will explore what data types and structures are used to create a Pandas dataframe and how understanding column dtypes is important to data analysis.'
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

Yes, this can only have the value `None`. 

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
- Use some of the string verbs you learned in the lecture to count all the times "let it be" (all upper and lower case versions) appears in the string `lyrics`. 
- Save it in an object named `letitbe_count`.

  

<codeblock id="04_03">

- Are you converting `lyrics` to lowercase using `.lower()`?
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

This data structure fits the first two statements but a string contains characters of all type `str`. 

</opt>

<opt text="<code>list</code>" >

This data structure can add elements using `.append()` 

</opt>

<opt text="<code>tuple</code>" correct="true">

Yes, this can only have the value `None`. 

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

This is, in fact, the opposite! 

</opt>

</choice> 


_Sets can only contain numerical data types._

<choice id="2">
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


_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Let's explore how to add to a list, slice it and convert it into a tuple. 


Tasks:


- Using the list provided, add a `pen`, a `scrap paper`, a `7.3` and a `True` element.
- Find the length of the list after adding the element and save the value in an object named `drawer_length`.
- Slice the list from element 4 to `scrap paper`  and save this in an object named `cleaned_junk_drawer`.
- Finally,  convert it into a set and name it `junk_set`.


<codeblock id="04_08">
- The verbs `.append()` and `len()` may be handy.
- You can convert your list to a tuple with `tuple(). 
- Have you sliced keeping in mind the end of the slice is excluded? 

</codeblock>


</exercise>


<exercise id="9" title="Making a Dataframe from Lists">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's use lists and convert them into a pandas dataframe. 


Tasks:

- Use the lists given in the cell below to make a dataframe.
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

What kind of brackets do they both use? 

</opt>

</choice> 

       
**Question 2**          

Which verb transforms dictionaries into dataframes? 

<choice id="2" >
<opt text="<code>.from_dict()</code>">

You seem to be missing something at the beginning. 

</opt>

<opt text="<code>pd.dataframe.from_dict()</code>">

Careful with capitalization. You are extremely close. 

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
- 8 `Wood Dowel`
- 2 `Short Screw`
- 1 `Allen Key`

- Construct the dictionary so that the part names are the keys and the quantities of the parts, are the values for the dictionary.
- Name the dictionary `ikea_shoe_rack`.

<codeblock id="04_12">
- Are you naming your dictionary properly? 
- Are all your parts spelled correctly?

</codeblock>


</exercise>



<exercise id="13" title="Building a Dataframe from a Dictionary">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


The shoe rack was not the only thing Jeremy bought. below is a table of all his purchases. 

|    | item_name       | collection   |   price |
|---:|:----------------|:-------------|--------:|
|  0 | Bistro Set      | APPLARO      |  216.98 |
|  1 | Shelf Unit      | HYLLIS       |   11.99 |
|  3 | Shoe Rack       | TJUSIG       |   29.99 |




Tasks:

- Create the table above from a dictionary using `pd.DataFrame.from_dict()`.
- Name your new dataframe ikea_df




<codeblock id="04_13">
- Are you using lists as the values in your dictionary? 
- Are you making sure to use floats for the price?
- are all your items and collections spelled correctly?

</codeblock>


</exercise>

<exercise id="14" title="Dataframes, Series and Column dtypes" type="slides">

<slides source="module4/module4_14">

</slides>

</exercise>

<exercise id="15" title="Name That type/dtype">



**Question 1**         
What is the data type of a Pandas dataframe?  


<choice id="1" >
<opt text="<code>pandas.core.frame.DataFrame</code>" correct="true">

Yes, this is the data type!

</opt>

<opt text="Multiple series" >

This is what makes up a dataframe but it's not the data type. 
</opt>

<opt text="<code>object</code>" >

This is a dtype, not a type. 

</opt>

<opt text="<code>str</code>">

This is a type, but not the dataframe type. 

</opt>

</choice> 


**Question 2**          
What is the data type of a column in a dataframe?
 
<choice id="2" >
<opt text="<code>pd.DataFrame</code>">

This is the whole dataframe type. 

</opt>

<opt text="<code>pd.Series</code>" correct="true">

That's right! A column has a type of pd.Series. 

</opt>

<opt text="<code>object</code>">

This is a dtype and not a data type. 

</opt>

<opt text="<code>str</code>">

Although you are guessing a data type, this is the incorrect one. 

</opt>

</choice> 

</exercise>


<exercise id="16" title="Dataframe and Series True and False">


Are the following statements True or False?      


_Dataframes are a made up of a tuple of Series._


<choice id="1">
<opt text="True">

It is made up of Series but not a tuple data structure. 

</opt>

<opt text= "False" correct="true">

A Dataframe is made up of a dictionary of Series

</opt>

</choice> 


_Pandas will assign a dtype of `obj` when it's having difficulty recognizing the column dtype._

<choice id="2">
<opt text="True" correct="true">

When it's unclear what the dtype is, Pandas will assign it a dtype `object`. 

</opt>

<opt text= "False">

You may want to review this section. 

</opt>

</choice> 

</exercise>


<exercise id="17" title="Dtype Practice">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Remember our `canucks` dataframe? Let's take a closer look at the labels of the columns.

| Player   | No.   | Age   | Height   | Weight   | Country   | Position   | Experience   | Birth Date   | Salary   |
|----------|-------|-------|----------|----------|-----------|------------|--------------|--------------|----------|



**Question 1 (a)**     

What dtype is would be an appropriate guess for the `Salary` column?

<choice id="1" >
<opt text="<code>float64</code>" correct="true">

Nice! `float64` and `int64` are both appropriate dtype guesses for the `Salary` column.    

</opt>

<opt text="<code>int64</code>" correct="true">

Nice! `float64` and `int64` are both appropriate dtype guesses for the `Salary` column.   

</opt>

<opt text="<code>str</code>">

 This is not a dtype, this is one of Python's data types. 

</opt>

<opt text="<code>bool</code>" >

`float64` and `int64` would be more appropriate dtype guesses for the `Salary` column. 

</opt>

</choice> 


**Question 1 (b)**  

Use the coding cell below to check the dtype for the `Salary` column. 


<codeblock id="04_17">

- Are you using the attribute `dtypes`?

</codeblock>


**Question 1 (c)**   

What is the actual dtype of the `Salary` column?

<choice id="1" >
<opt text="<code>float64</code>" correct="true">

Nice!

</opt>

<opt text="<code>int64</code>">

This time is was not of dtype `int64`.

</opt>

<opt text="<code>object</code>">

Are you looking at the output from above? 

</opt>

<opt text="<code>bool</code>" >

Are you looking at the output from above? 

</opt>

</choice> 


<br>


**Question 2 (a)**  

What dtype is would be an appropriate guess for the `Weight` column?

<choice id="1" >
<opt text="<code>float64</code>" correct="true">

Nice! `float64` and `int64` are both appropriate dtype guesses for the `Weight` column.    

</opt>

<opt text="<code>int64</code>" correct="true">

Nice! `float64` and `int64` are both appropriate dtype guesses for the `Weight` column.   

</opt>

<opt text="<code>str</code>">

 This is not a dtype, this is one of Python's data types. 

</opt>

<opt text="<code>bool</code>" >

`float64` and `int64` would be more appropriate dtype guesses for the `Weight` column. 

</opt>

</choice> 


**Question 2 (b)**  

Use the coding cell below to check the dtype for the `Weight` column. 


<codeblock id="04_17">

- Are you using the attribute `dtypes`?

</codeblock>


**Question 1 (c)**     

What is the actual dtype of the `Weight` column?

<choice id="1" >
<opt text="<code>float64</code>" >

This time is was not of dtype `float64`.

</opt>

<opt text="<code>int64</code>" correct="true">

 Nice! 

</opt>

<opt text="<code>object</code>">

Are you looking at the output from above? 

</opt>

<opt text="<code>bool</code>" >

Are you looking at the output from above? 

</opt>

</choice> 


</exercise>


<exercise id="18" title="Operations with  Data Types" type="slides">

<slides source="module4/module4_18">

</slides>

</exercise>

<exercise id="19" title="Output or Error with Operations">

Will the following operations result with an output or an error?

**Question 1**          

```python
['One', 'Two', 3] + (4, 'five', 6)
```

<choice id="1" >

<opt text="Runs successfully" >

Take special care to the brackets being used. dictionary1 + dictionary2


</opt>

<opt text="Error"  correct="true" >

Both elements must be of the same data structure to add together. 

</opt>

</choice> 

       
**Question 2**          

```python
tuple(['One', 'Two', 3]) + (4, 'five', 6)
```

<choice id="2" >

<opt text="Output" correct="true" >

That's right. the output would be `('One', 'Two', 3, 4, 'five', 6)`. 

</opt>

<opt text="<code>Error</code>" >

Are they both the same data structure?

</opt>

</choice> 


**Question 3**          

```python
dictionary1 = {1: 'one', 2: 'two'}
dictionary2 = {3: 'three', 4: 'four'}

dictionary1 + dictionary2
```

<choice id="3" >

<opt text="Output" >

Dictionaries cannot be concatenated together. We would have to combine them adding the individual keys-value pairs separately. 

</opt>

<opt text="<code>Error</code>" correct="true" >

That's right!

</opt>

</choice> 


**Question 4**          

```python
sum(['nine', 'ten', 'eleven', 'twelve'])
```

<choice id="4" >

<opt text="Output"  >

We cannot sum `str` elements in a list. 

</opt>

<opt text="<code>Error</code>"  correct="true">

Right!

</opt>

</choice> 

**Question 5**          

```python
'The monster under my bed' + [1, 2.0, 3, 4.5]
```

<choice id="2" >

<opt text="Output">


</opt>

<opt text="<code>Error</code>"  correct="true" >

That's right. We cannot concatenate together `lists` and `str` data types 


</opt>

</choice> 

</exercise>


<exercise id="20" title="True or False with Boolean Operators ">

Given the statement above, would the following result in a `True` of `False` value. 

**Question 1**          

```python
'hotels' != 'homes' and 50< 5000
```


<choice id="1" >

<opt text="True" correct="true" >

Both statements are true so the output is True. 


</opt>

<opt text="False" >

`and` checks if all statements are True`. 

</opt>

</choice> 

       
**Question 2**          

```python
not ('hotels' != 'homes') 
```

<choice id="2" >

<opt text="True"  >

The statement is True and `not` checks if the statement is False. 

</opt>

<opt text="False" correct="true">

That's right. The statement is not false so the output is False. 

</opt>

</choice> 


**Question 3**          

```python
not not ('hotels' != 'homes')
```

<choice id="3" >

<opt text="True" correct="true" >

The right! 

</opt>

<opt text="False" >

The statement `not 'hotels' != 'homes' ` is false so checking if that statement is False results in a True output. 

</opt>

</choice> 

</exercise>


<exercise id="20" title="More Practice with Data Types">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's explore Python's operators. 

Tasks:

- Concatenate together `string1` and `numerical1`    
- Save the result in an object named `together`
- Use `condition1` and `condition2` to answer the multiple-choice question below. 

<codeblock id="04_21">
- Maybe use the verb `str()` to help you.

</codeblock>


What is the value of the following equations? 

**Question 1**          

```python
3*(condition1 or condition2) + (condition1)
```


<choice id="1" >

<opt text="0">

The first set of brackets equals True. `3 * 1 + 0`.

</opt>

<opt text="3" >

The first set of brackets equals True. `3 * 1 + 0`.

</opt>

<opt text="4"  correct="true" >

Well done!

</opt>


<opt text="<code>Error</code>" >

The first set of brackets equals True. `3 * 1 + 0`.

</opt>

</choice> 

       
**Question 2**          

```python
(not condition2) * (not condition1)
```

<choice id="2" >


<opt text="0">

Well done!

</opt>

<opt text="3" >

The statement is True and `not` checks if the statement is False. Since the statement is not false the output is equal to 0. 

</opt>

<opt text="4" >

The statement is True and `not` checks if the statement is False. Since the statement is not false the output is equal to 0. 

</opt>


<opt text="<code>Error</code>" >

The statement is True and `not` checks if the statement is False. Since the statement is not false the output is equal to 0. 


</choice> 


</exercise>


<exercise id="21" title="Operations with Columns" type="slides">

<slides source="module4/module4_21">

</slides>

</exercise>

<exercise id="22" title="What's That Output? With Column Operations">



Here is my dataframe named `fruit_salad`:    

|    | name         | colour   | location   | seed   | shape   | sweetness   |   water-content |   weight |
|---:|:-------------|:---------|:-----------|:-------|:--------|:------------|----------------:|---------:|
|  0 | apple        | red      | canada     | True   | round   | True        |              84 |      100 |
|  1 | banana       | yellow   | mexico     | False  | long    | True        |              75 |      120 |
|  2 | cantaloupe   | orange   | spain      | True   | round   | True        |              90 |     1360 |
|  3 | dragon-fruit | megenta  | china      | True   | round   | False       |              96 |      600 |
|  4 | elderberry   | purple   | austria    | False  | round   | True        |              80 |        5 |
|  5 | fig          | purple   | turkey     | False  | oval    | False       |              78 |       40 |
|  6 | guava        | green    | mexico     | True   | oval    | True        |              83 |      450 |
|  7 | huckleberry  | blue     | canada     | True   | round   | True        |              73 |        5 |
|  8 | kiwi         | brown    | china      | True   | round   | True        |              80 |       76 |
|  9 | lemon        | yellow   | mexico     | False  | oval    | False       |              83 |       65 |

**Question 1**          

What would be the output of 

```python
df['seed'].sum()
```
<choice id="1" >
<opt text="<code>0</code>" >

Can we sum up a column of dtype `bool`? What values does it sum up? 


</opt>

<opt text="<code>1</code>" >

Can we sum up a column of dtype `bool`? What values does it sum up? 

</opt>

<opt text="<code>6</code>" correct="true">

Great!

</opt>


<opt text="<code>Error</code>" >

Can we sum up a column of dtype `bool`? What values does it sum up? 

</opt>

</choice> 

       
**Question 2**          

```python
df.loc[:,['seed', 'sweetness']].sum(axis=1)
```


<choice id="2" >
<opt text="A single value" >

`axis=1` means we can sum up row-wise.


</opt>

<opt text="2 values, one for each column">

`axis=1` means we can sum up row-wise.


</opt>


<opt text="A value for each row" correct="true" >

Well done!


</opt>

<opt text="<code>Error</code>" >

`axis=1` means we can sum up row-wise. We are calculating the number of `True` values total for `Seed` and `Sweetness`.

</opt>


</choice> 



**Question 3**          

```python
df['shape'].mean()
```


<choice id="3" >
<opt text="<code>round</code>" >

`axis=1` means we can sum up row-wise.


</opt>

<opt text="<code>13.4</code>">

`axis=1` means we can sum up row-wise.


</opt>


<opt text="All the values concatenated together">

Well done!


</opt>

<opt text="<code>Error</code>" correct="true" >

We cannot take the mean of a column of dtype `object`. 

</opt>

</choice> 

</exercise>


<exercise id="23" title="Splitting a Column" type="slides">

<slides source="module4/module4_23">

</slides>

</exercise>



<exercise id="24" title="Practice Operations with Dataframe columns">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's split up a column of dtype `object`. 

Tasks:

- Split up the column `Birth Date` into 3 separate columns named `Birth_Day`, `Birth_Month` and `Birth_Year`. 
- Name this new dataframe `birthdate_df`.
- Save these as columns in the `canucks` dataframe as dtype `int`.


<codeblock id="04_24">

- Are you using `str.split('-', expand='True')`?    
- Are you saving the columns from the `birthdate_df` back to the `canucks` dataframe?   

</codeblock>


</exercise>


<exercise id="25" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_25" start="0:165" end="3:01">>
</slides>
</exercise>

