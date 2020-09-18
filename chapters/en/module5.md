---
title: 'Module 5: Making Choices and Repeating Iterations'
description:
  'In this module, you will learn how to write conditionals statements and learn the fundamentals of how to create code that efficiently repeats the same operations by following the DRY principle.'
prev: /module4
next: /module6
type: chapter
id: 5
---

<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module5/module5_00" shot = "9" start="0:006" end="0:50">
</slides>

</exercise> 

<exercise id="1" title="Making Choices with Conditional Statements" type="slides, video">

<slides source="module5/module5_01" shot = "2" start="0:06" end="10:195">
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
time = 150

if time  < 120:
    speed = 'Fast'
elif time < 180:
    speed = 'Average'
else:
    speed = 'Slow'
speed
```

<choice id="2" >
<opt text="<code>Fast</code>" >

150 is not less than 120 so we would need to proceed to the next condition

</opt>

<opt text="<code>Average</code>" correct="true">

Well done.  

</opt>

<opt text="<code>Slow</code>">

150 is not greater than 180, so it would not enter the body of the `else` condition. 

</opt>

</choice>  

**Question 3**          

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

<choice id="3" >
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

<exercise id="6" title="Repeated Iterations (Loops)" type="slides, video">

<slides source="module5/module5_06" shot = "2" start="10:26" end="15:37">

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

Which of the following code result in an output? 


A) 

```python
sentence = ['Once', 'upon', 'a', 'time']
word_length = list()
for name in sentence: 
word_length.append(len(name))
```


B) 

```python
sentence = ['Once', 'upon', 'a', 'time']
word_length = list()
name in sentence: 
  word_length.append(len(name))
```


C) 

```python
sentence = ['Once', 'upon', 'a', 'time']
word_length = list()
for name in sentence: 
    word_length.append(len(name))
```

D) 

```python
sentence = ['Once', 'upon', 'a', 'time']
word_length = list()
for name in sentence
    word_length.append(len(name))
```

<choice id="2" >
<opt text="A">

This code seems to be missing colons the loop body indentation

</opt>

<opt text="B" >

This is missing the important keywork `for`!

</opt>

<opt text="C" correct="true">

Great work. 

</opt>

<opt text="D">

This is missing the colon in the first line of the loop. 

</opt>

</choice> 

</exercise>


<exercise id="8" title= "Practice Iterating Over a Collection">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've learned about iterating , now it's time to apply this! 
We have a list that contains all elements of type `float`.  We want to create a new list that casts each element to type `int`. 

Tasks:
- Create a new empty list named `integer_list`.
- Iterate over all the items in `float_list`. Cast the element to data type `int` and append it to `integer_list`. 
- Display the value of `integer_list`.



<codeblock id="05_08">

- Are you starting your loop with `for` and using a `colon` for the first line?
- Are you indenting each line of code in the loop?
- Are you appending the int value to the new list with `integer_list.append(int('variable-name-chose'))`

</codeblock>

</exercise>


<exercise id="9" title="Range, Dictionaries and Comprehensions" type="slides, video">

<slides source="module5/module5_09" shot = "2" start="15:43" end="19:11">

</slides>

</exercise>


<exercise id="10" title=" Range  Questions">


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


<exercise id="12" title= "Applying Range with Dataframes">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Let's read in multiple dataframes together and concatenate them vertically to one large dataframe using a loop and the `range()` function.

Tasks:
- There are 4 dataframes named `pkm1.csv` to `pkm4.csv`. that we wish to load in and vertically concatenate together.
- Fill in the blanks so the code reads in each dataframe according to their differing file name and concatenates them together. 
- Display the final dataframe. 

<codeblock id="05_12">

- Are you using `rpd.concat()`? 
- Are you adding `.csv` to the `string` object?
- Are you using `pd.read_csv()`?
- Are you indenting each line of code in the loop?

</codeblock>

</exercise>


<exercise id="13" title="Nested Loops" type="slides, video">

<slides source="module5/module5_13" shot = "2" start="19:17" end="24:01">

</slides>

</exercise>


<exercise id="14" title="Nested Loop Questions">

**Question 1**      

Given the code below, how many times does the line `print('Hurray')` get executed? 

```python
for i in range(0, 49, 10):
    print('Hurray')
    for j in range(0,8,2):
        print("This is fun!")
```

<choice id="1" >
<opt text="48">

Keep track of the step increment the values are increasing by in the outer loop. 

</opt>

<opt text="49">

Keep track of the step increment the values are increasing by in the outer loop. 

</opt>

<opt text="4">

Focus your attention on the outer loop and the number of times it executes the code in its body. 

</opt>


<opt text="5" correct="true">

Well done!  The outer loop calls `print('Hurray')` 5 times.

</opt>


</choice> 

**Question 2**          

Given the code above, how many times does the line `print("This is fun!")` get executed?



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


<exercise id="15" title= "Making a Nested Loop">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's count how many letters are contained in the dishes of a menu! 
We have a list named `menu` that contains multiples lists. We want to calculate how many character are contain in the entire `menu`. 


Tasks:

- Make an object named `charater_count` and give it a value of 0.
- Make an outer loop that iterates over each list of the `menu` list.
- Make an inner loop that iterates over each element in the nested list and add the length of it to `charater_count`.

- Display the value of `charater_count` outside both loops.


<codeblock id="05_15">

Are you using 4 indentations for each loop?
Are you putting `character_count = character_count + len(dish)` in the inner loop?

</codeblock>

</exercise>

<exercise id="16" title="Repeated Iterations with Conditions" type="slides, video">

<slides source="module5/module5_16" shot = "2" start="24:085" end="27:472">

</slides>

</exercise>


<exercise id="17" title="Conditional Loop Questions">


**Question 1**          

Which of the following is another syntax for the code below?

```python
supply = supply - 1  
```

<choice id="1" >
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




**Question 2**      

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

<choice id="2" >
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

**Question 3**          

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

<choice id="3" >
<opt text="<code>3</code>" >

Did you review what `break` means? 

</opt>

<opt text="<code>Error</code>">

Did you review what `break` means? 

</opt>

<opt text="<code>0</code>" correct="true">

Nice work! 

</opt>

</choice> 

</exercise>


<exercise id="18" title= "Practice Iterating Over a Collection">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

For the last few Modules, we have been playing with different dataframes.  In this question, we have stored them in a list named `dataframes`.  
Let's count how many of these dataframes have more than 1000 rows.

Tasks:

- Make an object named `count` and assign it a value of 0.
- Loop through the dataframes and count how many of them have more than 1000 rows. 
- *Hint: you can use `.shape[0]` to access the number of rows in a dataframe.*
- `count` should increase by 1 if the dataframe has more than 1000 rows and 0 otherwise. 
- Display the value of `count`.


<codeblock id="05_18">

- Did you use `if data.shape[0] >1000:` as you if statement? 
- You don't necessarily need an else statement here. 


</codeblock>


**Question**         
Does the code above used to read in the dataframes adhere to the DRY principle?

<choice id="1" >
<opt text="Yes" >

It seems that we are repetitively using `pd.read_csv()`. Remember what we did in exercise 12?

</opt>

<opt text="No" correct="true">

We can read in all our data with a loop (In fact, you did this exercise 12!)

</opt>

<opt text="No but this can't be avoided" >

With repetitive code, there is generally always a manner to reduce redundant code. 

</opt>

</choice> 

</exercise>


<exercise id="19" title="Functions" type="slides, video">

<slides source="module5/module5_19" shot = "2" start="27:54" end="33:20">

</slides>

</exercise>


<exercise id="20" title="Function Questions">

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
<opt text="<code>None</code>" correct="true">

Well done. 

</opt>

<opt text="A string surrounded by stars">

Does it really return anything?

</opt>

<opt text="<code>Error</code>">

Are you seeing an error that we aren't? 

</opt>

</choice> 

</exercise>


<exercise id="21" title= "Making a Function from Existing Code">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice converting existing code into a function so that it complies with the DRY principle. 


Tasks:
- Using the code provided, transform it into a function named `uppercase_count`
- The function should take in one argument and return the number of uppercases in the string
- Test it on the string `I hope you've Been Learning ALOT!`


<codeblock id="05_21">

- Are you defining your function with `def uppercase_count(string):`?
- Are you returning the object `uppercase_num`?

</codeblock>

</exercise>



<exercise id="22" title= "Making a Function">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice making a function that returns the BMI (Body Mass Index) given a person's weight and height.

Tasks:
- Define a function and give it the name `BMI_calculator`.
- It should take 2 arguments which can be called `height`, and `weight`.
- BMI can be calculated as: 

<center><img src='/module5/CodeCogsEqn.gif'  alt="404 image"/></center>
<br>

- Make sure the function returns the calculated BMI.
- Once you have created your function, use it to calculate the BMI of a person with a height of 62 inches and a weight of 105 lbs.   
- Save this in an object name `bmi_calc`.



<codeblock id="05_22">

- Are you defining your function with `def bmi_calculator(height, weight):`
- Are you returning `(weight/(height**2)) * 702`?
- To use it, are you running `bmi_calculator(62, 105)`?

</codeblock>

</exercise>


<exercise id="23" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" shot = "9" start="0:51" end="1:35">>
</slides>
</exercise>
