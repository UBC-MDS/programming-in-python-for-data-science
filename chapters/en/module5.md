---
title: 'Module 5: Making Choices and Repeating Iterations'
description:
  'In this module, you will learn how to write conditionals and learn the fundamentals of how to create code that efficiently repeats the same operations following the DRY principle.'
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

Every conditional decision **MUST** have which of the following:

<choice id="1" >
<opt text="<code>if</code>" correct="true">

Well done!

</opt>

<opt text="<code>elif</code>">

When we tell python to make a decision based on conditionals, an `elif` statement is optional. 

</opt>

<opt text="<code>else</code>">

We can still write functioning code without an `else` condition. 

</opt>


</choice> 

**Question 2**          

Given the code below, what is the value of the object `expensive`? 

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

Remember what happens when the first condition is met?  It gets removed from the stream. 

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

<choice id="1" >
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
- Start with an object named `exercise`.  Give it a string value of `burpees`.
- Make `if`, `elif`, and `else` statements for the following conditions:
    - if the exercise value is `lunges`, set an object value named `reps` to 20.
    - if the exercise value is `squats`, set `reps` to 25
    - if the exercise value is `burpees`, set `reps` to 15
    - If the exercise value is anything else, set `reps` to 10.
- Display the value of `reps`.



<codeblock id="05_04">
- Are you using double equal signs  (`==`) to make a conditional statement?
- Are you using a single `if` statement and 2 `elif` statements? 


</codeblock>

**Question**         
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

This is the default for all other values of  `exercise` that are not `lunges`, `squats` or `burpees`. 
</opt>


</choice> 


</exercise>

<exercise id="5" title="Creating an Inline if/else Statement">


**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's try to make inline conditional statements using `if` and `else`. 
the variable `cups_of_tea` is the number of cups of tea Ben drank last week. 

Tasks:

- Make an inline if/else statement that satisfies the following conditions:
    - if the data type of `cups_of_tea` is of type `list`, then set and object named `tea_amount` to the sum of the elements.
    - if the data type is anything else, set `tea_amount` to the string `'cannot sum'`. 
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

 the ***DRY*** principle aims to avoid what?

<choice id="1" >
<opt text="Multiple elements that are the same value">

Sometimes we may need to have objects that contain the same values.

</opt>

<opt text="Repeated code"  correct="true">

Great!

</opt>

<opt text="Object of type <code>None</code>">

`NoneType` can be very useful.  Why would we want to avoid them?

</opt>


</choice> 

**Question 2**          

Which of the following is another syntax for the code below?

```python
supply = supply - 1  
```

<choice id="2" >
<opt text="<code>supply =- 1 </code>" >

Double-check the order of the operators.

</opt>

<opt text="<code>supply - 1  = supply </code>">

The left side of the equal sign is reserved for object assignment!

</opt>

<opt text="<code>supply -= 1</code>" correct="true">

Great!

</opt>

</choice> 

</exercise>


<exercise id="8" title= "Practice Iterating Over a Collection">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've learned about iterating now it's time to apply this! 
We have a list that contains all elements of type `float`.  We want to create a new list that contains the `int` values of the elements. 

Tasks:
- Create a new empty list named `integer_list`.
- Iterate over all the items in the list and append the `int` value of each element in `float_list`. 
- Display the value of `integer_list`.



<codeblock id="05_08">

- Are you starting your loop with `for` and using a `colon` for the first line?
- Are you indenting each line of code in the loop?
- Are you appending the int value to the new list with `integer_list.append(int('variable-name-chose'))`

</codeblock>

</exercise>


<exercise id="9" title="Range and Comprehension" type="slides">

<slides source="module5/module5_09">

</slides>

</exercise>


<exercise id="10" title="Repeated Iterations Questions">


What is the output of the following code?

```python
numericals = []
for j in range(30,60,5):
    numericals.append(j)
numericals
```

<choice id="1" >
<opt text="<code>[30, 35, 40, 45, 50, 55, 60]</code>" >

Remember how `iloc[]` worked?  The starting number was inclusive and the ending number was exclusive. 

</opt>

<opt text="<code>[30, 35, 40, 45, 50, 55]</code>" correct="true">

Well done. 

</opt>

<opt text="<code>[60, 55, 50, 45, 40, 35, 30]</code>">

To have a list going backward, the skip rate step would be negative. 

</opt>

<opt text="<code>[30, 40, 50, 60]</code>">

The skip rate is 5, not 10
.  
</opt>

</choice> 

</exercise>



<exercise id="11" title= "Practice Iterating using Range">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's make a loop again but this time let's practice using the `range()` verb. 

Tasks:
- Iterate over a range from 50 to 10, stepping down 4 integers at a time. 
- Print the square of each number for each iteration.


<codeblock id="05_11">

- Are you using `range(50,10,-4)`? 
- Are you starting your loop with `for` and using a `colon` for the first line?
- Are you indenting each line of code in the loop?

</codeblock>


**Question 1**         
How many numbers does the code above print out? 

<choice id="1" >
<opt text="8" >

Are you sure you used the right values in `range()`?  

</opt>

<opt text="9" >

Are you sure you used the right values in `range()`?  

</opt>

<opt text="10" correct="true">

Great!

</opt>

<opt text="11">

Are you sure you used the right values in `range()`?   

</opt>

</choice> 


</exercise>


<exercise id="12" title="Nested Loops" type="slides">

<slides source="module5/module5_12">

</slides>

</exercise>


<exercise id="13" title="Nested Loop Questions">

**Question 1**      

Given the code below, how many times does the inner loop get executed in full? 

```python
count = 0 
for i in range(0, 49, 10):
    for j in range(0,8,2):
        count += 1
count
```

<choice id="1" >
<opt text="48">

Keep track of the step increment the values are increasing by. 

</opt>

<opt text="49">

Keep track of the step increment the values are increasing by. 

</opt>

<opt text="4">

Focus your attention on the outer loop and the number of times it executes the code in its body. 

</opt>


<opt text="5" correct="true">

Well done!  The outer loop calls the inner loop to start 5 times since the range is 0 to 49 going in increments of 10 (`i` takes on the values of 0,10,20,30,40)

</opt>


</choice> 

**Question 2**          

From the above code, what is the value of `count` after the code is finished running? 

<choice id="2" >
<opt text="48">

We know the outer loop iterates 5 times and the inner loop iterates 4 times (0,2,4,6). 

</opt>

<opt text="25">

We know the outer loop iterates 5 times and the inner loop iterates 4 times (0,2,4,6). 

</opt>

<opt text="20" correct="true">

We know the outer loop iterates 5 times and the inner loop iterates 4 times (0,2,4,6). We must multiply those numbers together and get 20. 

</opt>


<opt text="5" >

We know the outer loop iterates 5 times and the inner loop iterates 4 times (0,2,4,6). 

</opt>

</choice> 

</exercise>


<exercise id="14" title= "Making a Nested Loop">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's get nitty-gritty here. 
Given a list, let's create a new dictionary that assigns the element names as the dictionary key and the number of characters in the element as the dictionary's values. 

Given the list:

```python
synonyms = ['cash', 'capital', 'coin', 'dollars', 'money', 'funds']
```

The expected output is below:

```out
{'cash': 4, 'capital': 7, 'coin': 4, 'dollars': 7, 'money': 5, 'funds': 5, 'stacks': 6}
```

Tasks:

- Make an empty dictionary named `wallet`.
- Make a loop that iterates over each word of the list `synonyms`.
- Make an object to count and tally up the number of characters in each word (*Hint: This should be contained in the body of the outer loop*)
- Make an inner loop that adds 1 to the object for each letter it iterates through.
- Outside the inner loop but inside the outer loop assign the word from the `synonyms` list as your dictionary key and the count values as the dictionary's values. 
- Display the value of `wallet` outside both loops.


<codeblock id="05_14">

- Are you assigning an object like `count = 0` before entering the inner loop? 
- Are you assigning the dictionary key-values with something like `wallet[word] = count`? 
- Are you assigning the key-value pairs outside the inner loop but inside the outer one?

</codeblock>

</exercise>

<exercise id="15" title="Repeated Iterations with Conditions" type="slides">

<slides source="module5/module5_15">

</slides>

</exercise>


<exercise id="16" title="Conditional Loop Questions">

**Question 1**      

Given the code below, what is the expected output? 

```python
parking_lot = [ 20, 60, -12,  110, -20, 80, 12, -40, 37, 92]
parking_tickets = list()

for stall in parking_lot: 
    if stall <0:
        parking_tickets.append(True)
    else:
        parking_tickets.append(False)

sum(parking_tickets)
```

<choice id="1" >
<opt text="<code>3</code>" correct="true">

Well done!

</opt>

<opt text="<code>[False, True, False, True, False, False, True, False]</code>">

Did you miss that the code is taking the  `sum()` of the list?  

</opt>

<opt text="<code>7</code>">

this is the number of false values.

</opt>

</choice> 

**Question 2**          

Given the code below, what is the expected output? 

```python
parking_lot = [ 20, 60,-12,  110, -20, 80, 12, -40, 37, 92]
parking_tickets = []

for stall in parking_lot: 
    if stall <0:
        break
    else:
        parking_tickets.append(False)
sum(parking_tickets)

```

<choice id="2" >
<opt text="<code>3</code>" >

Did you review what `break` means? 

</opt>

<opt text="<code>error</code>">

Did you review what `break` means? 

</opt>

<opt text="<code>0</code>" correct="true">

Nice work! 

</opt>

</choice> 

</exercise>


<exercise id="17" title= "Practice Iterating Over a Collection">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

It's been a while since we talked about a dataframe so I think it's time they returned.  For the last few Modules, we have been playing with different dataframes.  In this question, we have stored them in a list named `dataframes`.  

Tasks:

- Make an object named `count` and assign it a value of 0.
- Loop through the dataframes and count how many of them have more than 1000 rows. 
- *Hint: you can use `.shape[0]` to access the number of rows in a dataframe.*
- `count` should increase by 1 if the dataframe has more than 1000 rows and 0 otherwise. 
- Display the value of `count`.


<codeblock id="05_17">

- Did you use `if data.shape[0] >1000:` as you if statement? 
- You don't necessarily need an else statement here. 


</codeblock>


**Question**         
Does the code above used to read in the dataframes adhere to the DRY principle?

<choice id="1" >
<opt text="Yes" >

It seems that we are repetitively using `pd.read_csv()`. .

</opt>

<opt text="No" correct="true">

We can read in all our data with a loop (In fact, you will do this in the assignment)!

</opt>

<opt text="No but this can't be avoided" >

With repetitive code, there is generally always a manner to reduce redundant code. 

</opt>

</choice> 

</exercise>


<exercise id="18" title="Functions" type="slides">

<slides source="module5/module5_18">

</slides>

</exercise>


<exercise id="19" title="Function Questions">

**Question 1**      

What Python keyword is needed to begin the construction of a function?

<choice id="1" >
<opt text="<code>fun</code>">

Unfortunately, `fun` is not a python keyword, but it would have been `fun` if it was!

</opt>

<opt text="<code>funct</code>">

Maybe look back at the material again

</opt>

<opt text="<code>def </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>define </code>">

We are defining a function but python doesn't have `define` as a keyword.

</opt>


</choice> 

**Question 2**          

What does the function below return? 

```python
def add_stars(name):
    name = "**" + name + "**"
    return
```

<choice id="2" >
<opt text="Nothing" correct="true">

Well done. 

</opt>

<opt text="A string surrounded by stars">

Does it really return anything?

</opt>

<opt text="Error">

Are you seeing an error that we aren't? 

</opt>

</choice> 

</exercise>


<exercise id="20" title= "Making a Function from Existing Code">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice converting existing code into a function. 


Tasks:
- Using the code provided, transform it into a function named `uppercase_count`
- The function should take in one argument and return the number of uppercases in the string
- Test it on the string `I hope you've Been Learning ALOT!`
- Save the result as `string2`


<codeblock id="05_20">

- Are you defining your function with `def uppercase_count(string):`?
- Are you returning the object `uppercase_num`?

</codeblock>

</exercise>



<exercise id="21" title= "Making a Function">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice making a function that returns the BMI (Body Mass Index) given a person's weight and height.
(*Disclaimer: Much more than these two measurements are needed to determine if someone is healthy*)

Tasks:
- Define a function and give it the name `BMI_calculator`.
- It should take 2 arguments which can be called `height`, and `weight`.
- BMI can be calculated as: 

<center><img src='/module5/CodeCogsEqn.gif'  alt="404 image"/></center>
<br>

- Make sure the function returns the calculated BMI.
- Once you have created your function, use it to calculate the BMI of a person with a height of 62 inches and a weight of 105 lbs.   
- Save this in an object name `bmi_calc`.



<codeblock id="05_21">
- Are you defining your function with `def bmi_calculator(height, weight):`
- Are you returning `(weight/(height**2)) * 702`?
- To use it, are you running `bmi_calculator(62, 105)`?

</codeblock>

</exercise>



<exercise id="22" title="Function Docstrings" type="slides">

<slides source="module5/module5_22">

</slides>

</exercise>


<exercise id="23" title="Docstring Questions">

**Question 1**      

Which docstring style requires the explanation of ***Arguments***?

<choice id="1" >
<opt text="Single line">

This only uses 1 line!  How can we fit all arguments on one line?

</opt>

<opt text="PEP-8" correct="true">

Nice work!

</opt>

<opt text="SciPy" >

This style elaborates with parameters, returns and examples. 

</opt>

</choice> 

**Question 2**          

How do you obtain the documentation for the function below?

```python
def add_stars(name):
  """
  This will return your input string between a pair of stars. 
  Parameters
    ----------
    name: str
        a sentence or word
        
    Returns
    -------
    str
        The initial string beginning and ending with a pair of stars 
        
    Examples
    --------
    >>> add_stars('Good Job')
    'Good Job'
    """

    name = '**' + name + '**'
    return
```

<choice id="2" >
<opt text="<code>documentation?</code>">

The `documentation` for which function though?

</opt>

<opt text="<code>?docstring(add_stars)</code>">

Maybe look back at the material again.

</opt>

<opt text="<code>add_stars()?</code>"  >

You are so close! 

</opt>

<opt text="<code>add_stars?</code>" correct="true">

Great! 

</opt>

</exercise>



<exercise id="24" title= "Writing a Docstring ">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Remember the function we wrote that returns the BMI given a person's weight and height?  We must write a docstring for it now!
(*Disclaimer: Much more than these two measurements are needed to determine if someone is healthy*)

Tasks:
- Write a Scipy style docstring for the function provided. 
- Make sure to include a brief description, parameters, return, and example sections. 
- View the documentation of the function.



<codeblock id="05_24">

- Are you using `'''` or `""""` to contain your docstring?
- Are you including all the sections? 
- Are you getting the documentation of the docstring using `bmi_calculator?`

</codeblock>

</exercise>

<exercise id="25" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" start="0:165" end="3:01">>
</slides>
</exercise>
