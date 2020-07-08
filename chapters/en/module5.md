---
title: 'Module 5: Loops and Functions'
description:
  'In this module you will learn about how to write conditionals and learn the fundamentals of how to create code that repeats the same operations.'
prev: /module4
next: /module6
type: chapter
id: 5
---

<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module5/module5_00" start="0:165" end="3:01">
</slides>

</exercise> 

<exercise id="1" title="Making Choices with Conditional Statements" type="slides">

<slides source="module5/module5_01">
</slides>

</exercise>

<exercise id="2" title="Quick Questions with Conditionals">


**Question 1**      

Every conditionial decision **MUST** have which of the following:

<choice id="1" >
<opt text="<code>if</code>" correct="true">

Well done

</opt>

<opt text="<code>elif</code>">

When we tell python to make a decision based on conditionals, an `elif` statement is optional. 

</opt>

<opt text="<code>else</code>">

We can still write functioning code without an `else` condition. 

</opt>


</choice> 

**Question 2**          

Given the code below what is the value of the object `expensive`. 

```python
price = 150

if price > 50:
    expensive = 'moderately'
elif price > 100:
    expensive = 'valuable'
else:
    expensive = 'affordable'
expensive
```

<choice id="2" >
<opt text="<code>moderately</code>" correct="true">

Well done. 

</opt>

<opt text="<code>valuable</code>">

Proceeding to the body of this condition isn't possible since the first condition was met. 

</opt>

<opt text="<code>affordable</code>">

Remember what happens when the first condition is met? It gets removed from the stream. 

</opt>

</choice> 

</exercise>


<exercise id="3" title="Will it Run with Conditionals">
       
Which of the following code wouldn't result in an error? 

A) 

```python
if price > 100
    expensive = 'valuable'
else
    expensive = 'affordable'
expensive
```


B) 

```python
if price > 50:
expensive = 'moderately'
elif price > 100:
expensive = 'valuable'
else:
expensive = 'affordable'
expensive
```


C) 

```python
if price > 50:
  expensive = 'moderately'
expensive
```

<choice id="3" >
<opt text="A">

This code seems to be missing colons in the statement. 

</opt>

<opt text="B" >

Are you sure the structure is correct?

</opt>

<opt text="C" correct="true">

Great work. 

</opt>

</choice> 

</exercise>

<exercise id="4" title="Creating Conditional Statements">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice making decisions with conditional statements. 
We are going to the gym and our exercise plan takes different amounts of reps. let's make conditional statements that depend on the name of the exercises.

Tasks:
- Start with an object named `exercise`. Give it a value of `burpees`.
- Make `if`, `elif`, and `else` statements for the following conditions:
    - if the exercise value is `lunges`, set an object value named `reps` to 20.
    - if the exercise value is `squats`, set `reps` to 25
    - if the exercise values is `burpees`, set `reps` to 15
    - If the exercise value is anything else, set `reps` to 10.
- Display the value of `reps`.



<codeblock id="05_04">
- Are you using double equal signs  (`==`) to make a conditional statement?
- Are you using a single `if` statement and 2 `elif` statements? 


</codeblock>

**Question 1**         
What is the output of the code above? 

<choice id="1" >
<opt text="<code>20</code>" >

This is the value if `exercise` is  `lunges`.

</opt>

<opt text="<code>25</code>">

This is the value if `exercise` is  `squats`.

</opt>

<opt text="<code>15</code>" correct="true">

Great!

</opt>

<opt text="<code>10</code>">

This is the  default for all other values of  `exercise` that are not `lunges`, `squats` or `burpees`. 
</opt>


</choice> 


</exercise>

<exercise id="5" title="Creating an Inline if/else Statement">


**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's try to make inline conditional statements using `if` and `else`. 
the variable `cups_of_tea` is the amount of cups of tea Ben drank last week. 

Tasks:

- Make an inline if/else statement that satisfies the following conditions:
    - if the data type of `cups_of_tea` is of type `list`, then set and object named `tea_amount` to the sum of the elements.
    - if the data type is anything else, set `tea_amount` to  the string `'cannot sum'`. 
- Display the result of `tea_amount`.

<codeblock id="05_05">
- To check the data type of `cups_of_tea`, you can use `type(cups_of_tea) == list`.
- Are you using `sum()` to sum up the elements in a list? 

</codeblock>

**Question 1**         
What is the output of the code above? 

<choice id="1" >
<opt text="<code>18</code>" >

Did you add an extra element to `cups_of_tea`? 

</opt>

<opt text="<code>16</code>" correct="true">

Great!

</opt>

<opt text="<code>cannot sum</code>" >

`cups_of_tea` is a list and should be able to sum up the elements.  

</opt>

<opt text="<code>Error</code>">

The code you made above should not result in an error message.
</opt>

</choice> 

</exercise>

<exercise id="6" title="Repeated Iterations (Loops)" type="slides">

<slides source="module5/module5_06">

</slides>

</exercise>


<exercise id="7" title="Repeated Iterations Questions">

**Question 1**      

Every conditionial decision **MUST** have which of the following:

<choice id="1" >
<opt text="<code>if</code>" correct="true">

Well done

</opt>

<opt text="<code>elif</code>">

When we tell python to make a decision based on conditionals, an `elif` statement is optional. 

</opt>

<opt text="<code>else</code>">

We can still write functioning code without an `else` condition. 

</opt>


</choice> 

**Question 2**          

Given the code below what is the value of the object `expensive`. 

```python
price = 150

if price > 50:
    expensive = 'moderately'
elif price > 100:
    expensive = 'valuable'
else:
    expensive = 'affordable'
expensive
```

<choice id="2" >
<opt text="<code>moderately</code>" correct="true">

Well done. 

</opt>

<opt text="<code>valuable</code>">

Proceeding to the body of this condition isn't possible since the first condition was met. 

</opt>

<opt text="<code>affordable</code>">

Remember what happens when the first condition is met? It gets removed from the stream. 

</opt>

</choice> 

</exercise>


<exercise id="8" title= "Practice Interating Over a Collection">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice making decisions with conditional statements. 
We are going to the gym and our exercise plan takes different amounts of reps. let's make conditional statements that depend on the name of the exercises.

Tasks:
- Start with an object named `exercise`. Give it a value of `burpees`.
- Make `if`, `elif`, and `else` statements for the following conditions:
    - if the exercise value is `lunges`, set an object value named `reps` to 20.
    - if the exercise value is `squats`, set `reps` to 25
    - if the exercise values is `burpees`, set `reps` to 15
    - If the exercise value is anything else, set `reps` to 10.
- Display the value of `reps`.



<codeblock id="05_08">

- Are you using double equal signs  (`==`) to make a conditional statement?
- Are you using a single `if` statement and 2 `elif` statements? 

</codeblock>

</exercise>


<exercise id="9" title= "Practice Interating using Range">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice making decisions with conditional statements. 
We are going to the gym and our exercise plan takes different amounts of reps. let's make conditional statements that depend on the name of the exercises.

Tasks:
- Start with an object named `exercise`. Give it a value of `burpees`.
- Make `if`, `elif`, and `else` statements for the following conditions:
    - if the exercise value is `lunges`, set an object value named `reps` to 20.
    - if the exercise value is `squats`, set `reps` to 25
    - if the exercise values is `burpees`, set `reps` to 15
    - If the exercise value is anything else, set `reps` to 10.
- Display the value of `reps`.



<codeblock id="05_09">

- Are you using double equal signs  (`==`) to make a conditional statement?
- Are you using a single `if` statement and 2 `elif` statements? 

</codeblock>

</exercise>


<exercise id="10" title="Nested Loops" type="slides">

<slides source="module5/module5_10">

</slides>

</exercise>


<exercise id="20" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" start="0:165" end="3:01">>
</slides>
</exercise>

