---
title: 'Module 6: Functions Fundamentals and Best Practices'
description:
  'In this module, you will expand your knowledge on the concept of functions that were introduced in Module 5. This module covers how to develop good habits when writing functions like including docstrings, defensive programming, test-driven development and how to compose useful functions. '
prev: /module5
next: /module7
type: chapter
id: 6
---


<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module6/module6_00" shot = "0" start="0:165" end="3:01">
</slides>

</exercise> 

<exercise id="1" title="DRY Revisited and Function Fundamentals" type="slides, video">

<slides source="module6/module6_01" shot = "1" start="0:165" end="3:01">
</slides>

</exercise>

<exercise id="2" title="Questions on Scoping">

**Question 1**      

Given the code below, what is the output?

```python

toy = "ball"

def playtime():
    toy = "truck"
    return toy 

toy
```

<choice id="1" >
<opt text="<code>ball</code>" correct="true">

Well done!

</opt>

<opt text="<code>truck</code>">

Since `toy` is being called in the global environment, the output of `toy` is the value of the global variable value of  `toy`.

</opt>

<opt text="<code>Error</code>">

This will still run without an error!

</opt>

</choice> 

**Question 2**          

Given the code below, what is the output? 

```python

toy = "ball"

def playtime():
    toy = "truck"
    return toy 

playtime()
```

<choice id="2" >
<opt text="<code>ball</code>" >

`toy` is equal to `"truck"` in the local environment so it will return the local variable value of `toy`. 

</opt>

<opt text="<code>truck</code>"  correct="true">

Nice job!

</opt>

<opt text="<code>Error</code>">

This will still run without an error!

</opt>

</choice>  

**Question 3**          

Given the code below what is the output?

```python
def playtime():
    toy = "truck"
    return toy 

toy
```

<choice id="3" >
<opt text="<code>None</code>" >

`toy` is a local variable, will it be recognized in a global environment?

</opt>

<opt text="<code>truck</code>">

`toy` is a local variable, will it be recognized in a global environment?

</opt>

<opt text="<code>Error</code>" correct="true">

Great! `toy` is a local variable, and will not be recognized in the global environment. 

</choice> 

</exercise>

<exercise id="3" title="Side Effects">

**Question 1**      

***True or False***        
Side effects make your code easier to debug.



<choice id="1" >
<opt text="True" >

Ahh! Please go back and read over the slides. Side effects are generally avoided.

</opt>

<opt text="False" correct="true">

Well done. This is an important one to get right! 

</opt>

</choice> 

**Question 2**          

Which of the following functions produce a side effect? 

A) 
```python

toy = "ball"

def playtime():
    toy = "truck"
    print(toy) 

playtime()
```

B) 

```python

toy = "ball"

def playtime():
    toy = "truck"
    return toy 

playtime()
```

<choice id="2" >
<opt text="A"  >

Nice job!

</opt>

<opt text="B" correct="true">

printing `toy` is considered a function side effect! 

</opt>

<opt text="A and B"  >

having a function `return` something is not considered necessarily a side effect. 

</opt>


<opt text="Neither A or B"  >

printing `toy` is considered a function side effect! 

</opt>

</choice>  

**Question 3** 

***True of False***      
If a function modifies a variable in the function's local environment, that is considered a side effect.

<choice id="3" >
<opt text="True">

This is not considered a side effect if a variable created within a function is modified within the same function. 

</opt>

<opt text="False"  correct="true">

 Perfect!

</opt>

</choice> 

</exercise>


<exercise id="4" title= "Writing Functions Without Side Effects">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

The function `kg_to_lb()` is used to convert a list of elements with kg units into a list of elements with lbs units. Unfortunate this function includes a side effect that edits one of the global variables. 


Tasks:
- Write a new function named `better_kg_to_lb` that no longer contains a side effect.
- Test your new function on the `weight_kg` list and save the results in an object named `weight_lb_again`.



<codeblock id="06_04">

- Are you putting `weight_lb` inside the function now? 
- Are you returning `weight_lb`? 

</codeblock>

</exercise>

<exercise id="5" title="Default Arguments" type="slides, video">

<slides source="module6/module6_05" shot = "1" start="0:165" end="3:01">
</slides>

</exercise>

<exercise id="6" title="Will it Output?">

Given the following function, which of the function calls will result in an error? 

```python
def name_initials(first_name, last_name, year_of_birth = None):
    if year_of_birth is not None: 
        initials = first_name[0].upper() + middle_name[0].upper() + str(year_of_birth)
    else:
        initials = first_name[0].upper() + last_name[0].upper()
    return initials
```


<choice id="1" >
<opt text="<code>name_initials('Cameron', 'Grant')</code>" >

This one will run since `year_of_birth` is optional and will default to `None`. The output is `CG`. 

</opt>

<opt text="<code>name_initials(last_name = 'Grant', year_of_birth = 1987, first_name = 'Cameron')</code>">

Since we are defining our arguments with their names and values, this one will result in an output of `CG1987`.

</opt>

<opt text="<code>name_initials('Cameron', 1987, 'Grant')</code>"  correct="true">

This will result in an error since the argument values are not in the defined order and they are not defined with the argument names. 

</opt>

<opt text="<code>name_initials('Cameron', 'Grant', 1987)</code>">

This function calls the arguments in the same order they were defined in. The output is `CG1987`. 

</opt>

</choice> 

</exercise>

<exercise id="7" title="Default Arguments">

**Question 1**    

Given the function below: 
```python
def employee_wage(employee_id, position, experience = 3):
    if position == "doctor": 
        wage = 150000
    elif position == "teacher":
        wage = 60000
    elif position == "lawyer":
        wage = 100000
    elif position == "server":
        wage = 50000
    else: 
        wage = 70000
    return wage * (1 + (0.1 * experience)) 
```
What is the approximate wage of employee `765` who is a lawyer? 


<choice id="1" >
<opt text="<code>100000</code>" >

Are you taking a close look at the argument `experience` which has a default value?

</opt>

<opt text="<code>110000</code>">

Take a closer look at the default value of the `experience` argument. 

</opt>

<opt text="<code>130000</code>"  correct="true">

Nice Job!

</opt>

<opt text="<code>150000</code>" >

Are you looking at the right position?

</opt>

</choice>  

**Question 2**  

If I make a function call using the following code, and I know that that parameter `spice_level` is an argument that has a default value, which other arguments **MUST** also have set default values? 

```
menu_item_id = 42
menu_item_name = "Green Curry"
spice_level = "Medium"
meat = "Tofu"
rice = True

thai_food(menu_item_id, menu_item_name, spice_level, meat, rice)
```

<choice id="2" >

<opt text="<code>menu_item_id</code> and <code>menu_item_name</code>" >

These two arguments can be either required or default arguments.

</opt>

<opt text="<code>meat</code>">

This is partially right but not entirely.

</opt>

<opt text="<code>rice</code>">

This is partially right but not entirely.

</opt>

<opt text="<code>meat</code> and <code>rice</code>"  correct="true">

Nice job! arguments that are required for the function must come *before* defining default arguments.

</opt>

</choice>  

</exercise>


<exercise id="8" title= "Default Argument Practice">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

**Weight** and **mass** are 2 very different measurements althought they do get used interchangeably in everyday conversations. 
**Mass** is defined by  <a href="https://www.nasa.gov/pdf/591747main_MVW_Intro.pdf" target="_blank">NASA</a> as the amount of matter in an object, whereas, **weight** is defined as the vertical force exerted by a mass as a result of gravity (with units of Newtons). 
The function `earth_weight()` converts an object's mass to weight by multiplying it by the gravitational force acting on it. On Earth, the gravitational force is measured as 9.8 m/s^2.  


We want to make a more versatile function by having the ability to calculate the weight of any object on any particular planet and not just Earth. Redefine the function `earth_weight()` so that it takes an argument with a default gravitational force of 9.8. 


Tasks:
- Create a new function named `mass_to_weight` and give it an additional argument named  `g` which has a default value of 9.8.
- Test your new function by converting the mass of 76 kg to weight on Earth and save the results in an object named `earth_weight`.
- Test your function again but this time calculate the weight of the 76 kg object on the moon using a gravitational force of 1.62 m/s^2 and save your function call to an object named `moon_weight`.




<codeblock id="06_08">

- Are you putting `g=9.8` inside the function named `mass_to_weight`? 
- Are you calling `mass_to_weight(76)` and saving it in an object named `earth_weight`? 
- Are you calling `mass_to_weight(76, 1.62)` and saving it in an object named `moon_weight`? 

</codeblock>

</exercise>


<exercise id="9" title="Function Docstrings" type="slides, video">

<slides source="module6/module6_09" shot = "1" start="0:165" end="3:01">

</slides>

</exercise>




<exercise id="10" title="Docstring Questions">

**Question 1**      

What data type is returned from the following function? 


```python
def factor_of_10(number):
    """
    Takes a number and determines if it is a factor of 10 
    Parameters
    ----------
    number : int
        the value to check
      
    Returns
    -------
    bool
        Returns True if numbers are a multiple of 10 and False otherwise
      
    Examples
    --------
    >>> factor_of_10(72)
    False
    """

    if number % 10 == 0: 
        factor = True
    else:
        factor = False
        
    return factor
    

```

<choice id="1" >
<opt text="<code>str</code>">

Maybe look at the `Returns` heading in the docstring. 

</opt>

<opt text="<code>bool</code>" correct="true">

Nice work!

</opt>

<opt text="<code>float</code>" >

Maybe look at the `Returns` heading in the docstring. 

</opt>

<opt text="<code>list</code>" >

Maybe look at the `Returns` heading in the docstring.  

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

</choice> 

</exercise>




<exercise id="11" title="Which Docstring is Most Appropriate?">


Given the function below, which docstring follows the NumPy format? 

```python

def acronym_it(sentence):
    words = sentence.split()
    first_letters = [word[0].upper() for word in words]
    acronym =  "".join(first_letters)
    return acronym
```



A)
```python
"""
A function that converts a string into an acronym of capital
letters

Input
------
str : sentence
   The string to obtain the first letters from
    
Output
-------
str
    A string of the first letters of each word in an uppercase format
    
Sample
-------
>>> acronym_it("Let's make this an acronym")
"LMTAA"
"""

````


B)

```python
"""
A function that converts a string into an acronym of capital
letters

Input 
------
some_words : str
   The string to obtain the first letters from
    
Output 
-------
list 
    A list of the first letters of each word from the input string

Example
-------
>>> acronym_it("Let's make this an acronym")
"LMTAA"
"""

````

C) 


```python
"""
A function that converts a string into an acronym of capital
letters

Parameters
----------
sentence : str
   The string to obtain the first letters from
    
Returns
-------
str
    a string of just first letters in an uppercase format

Example
-------
>>> acronym_it("Let's make this an acronym")
"LMTAA"
"""

````


D) 


```python
"""
A function that converts a string into an acronym of capital
letters


Returns
-------
list :
    A list of the first letters of each word from the input string
    
Parameters
----------
str : sentence
   The string to obtain the first letters from
    
Example
-------
>>> acronym_it("Let's make this an acronym")
"LMTAA"
"""

````


<choice id="1" >
<opt text="A"  >

Are these the correct headings?.  

</opt>

<opt text="B" >

Are the headings correct? Also pay attention to the name of the input arguments and what the function is returning. 

</opt>

<opt text="C"  correct="true">

Nice job!

</opt>

<opt text="D">

Is the order of the description headings correct? 

</opt>

</choice> 

</exercise>


<exercise id="12" title= "Practice Writing a Docstring">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

In module 5, we wrote a function that returns the BMI given a person's weight and height. Let's write a docstring for it now!    
   

```python
def bmi_calculator(height, weight):
    return (weight / (height ** 2)) * 702

```

Tasks:
- Write a NumPy style docstring for the function provided. 
- For this question, we want you to write your docstring between 3 single quotations `'''` instead of the normal double quotations `"""`. This will allow us to test the solution provided.
- Make sure to include a brief description, parameters, return, and example sections. 
- View the documentation of the function.



<codeblock id="06_12">

- Are you using `'''` to contain your docstring?
- Are you including all the sections? 
- Are you getting the documentation of the docstring using `bmi_calculator?`

</codeblock>

</exercise>


<exercise id="13" title="Defensive Programming using Exceptions" type="slides, video">

<slides source="module6/module6_13" shot = "1" start="0:165" end="3:01">

</slides>

</exercise>



<exercise id="14" title="Exceptions">

**Question 1**      

Which of the following exceptions is most appropriate for when an operation or function receives an argument that has the right type but an inappropriate value?     

*Hint: Did you look over the resource we provided you in the slides?*

<choice id="1" >
<opt text="<code>TypeError</code>">

This is raised when an operation or function is applied to an object of inappropriate type.

</opt>

<opt text="<code>NameError</code>">

This is raised when a local or global name is not found. 

</opt>

<opt text="<code>AttributeError</code>"  >

This is raised when an attribute reference or assignment fails. 

</opt>

<opt text="<code>ValueError</code>" correct="true">

Great! 

</opt>

</choice> 

**Question 2**          

Why would we want to write code that raises an exception? 

<choice id="2" >

<opt text="To make the cause of the error much clearer to the caller of the function">

This is correct, but did you read the other options? 

</opt>

<opt text="To force code to fail sooner rather than later">

This is correct, but did you read the other options? 

</opt>

<opt text="To make your functions more usable"  >

This is correct, but did you read the other options? 

</opt>

<opt text="All of the above" correct="true">

Great! 

</opt>

</choice> 

</exercise>


<exercise id="15" title="Documenting Exceptions">


Which docstring correctly includes the documentation for exceptions? 


A) 

```python
def factor_of_10(number):
    """
    Takes a number and determines if it is a factor of 10 
    Parameters
    ----------
    number : int
        the value to check
      
    Returns
    -------
    bool
        Returns True if number is a multiple of 10 and False otherwise
        
    Raises
    ------
    TypeError
        If the input argument number is not of type int 
      
    Examples
    --------
    >>> factor_of_10(72)
    False
    """
    if not isinstance(number, int): 
        raise TypeError("the input value of number is not of type int")
        
    if number % 10 == 0: 
        factor = True
    else:
        factor = False
        
    return factor
```


B) 

```python
def factor_of_10(number):
    """
    Takes a number and determines if it is a factor of 10 
    Parameters
    ----------
    number : int
        the value to check
      
    Returns
    -------
    bool
        Returns True if number is a multiple of 10 and False otherwise
        
    Exceptions
    ------
    TypeError
        If the input argument number is not of type int 
      
    Examples
    --------
    >>> factor_of_10(72)
    False
    """
    if not isinstance(number, int): 
        raise TypeError("the input value of number is not of type int")
        
    if number % 10 == 0: 
        factor = True
    else:
        factor = False
        
    return factor
```

<choice id="1" >
<opt text="A" correct="true" >

That's right, `Raises` goes between the `Returns` and `Examples`.  

</opt>

<opt text="B"  >

To document what happens when an exception is raised, we use the title `Raises`.

</opt>

</choice> 

</exercise>


<exercise id="16" title= "Raising Exceptions">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build on the BMI function we made in module 5. This time we want to raise 2 exceptions.  
 

```python
def bmi_calculator(height, weight):
    return (weight / (height ** 2)) * 702

```

Tasks:
- Write an exception that checks if `height` is of type `float`.
- Write a second exception that raises an error if weight is 0 or less.
- Test your function with the values given in variable `tall` and `mass`.



<codeblock id="06_16">

- Are you using `TypeError` and `Exception` respectively for the exception messages?
- Are you checking the `height` type with `if not isinstance(height, float):`?
- Are you checking if weight is greater than 0 with `if weight <= 0:`?


</codeblock>

</exercise>


<exercise id="17" title="Unit tests and Corner Cases" type="slides, video">

<slides source="module6/module6_17" shot = "1" start="0:165" end="3:01">

</slides>

</exercise>


<exercise id="18" title="Assert Questions">

**Question 1**      

Which of the statements is correct?     


<choice id="1" >
<opt text="<code>assert</code> statements cause our program to fail if the condition is <code>True</code>.">

`Exceptions` are what causes an error if the conditional statement is `True`. 

</opt>

<opt text="<code>assert</code> statements cause our program to fail if the condition is <code>False</code>." correct="true">

Nice work!

</opt>

</choice> 

</exercise>


<exercise id="19" title="Unit Tests Questions">

**Question 1** 

```python
def acronym_it(sentence):
    words = sentence.split()
    first_letters = [word[0].upper() for word in words]
    acronym =  "".join(first_letters)
    return acronym
```

Given the function above, which would **not** result in an error? 


<choice id="1" >

<opt text="<code>assert acronym_it('Hard work pays off') == 'HWPO'</code>" correct="true">

Great!

</opt>

<opt text="<code>assert acronym_it('Hard work pays off') == 'Hwpo'</code>" >

It might be helpful to read the function code line by line. 

</opt>

<opt text="<code>assert acronym_it('Hard work pays off') == 'H'</code>"  >

It might be helpful to read the function code line by line. 

</opt>

<opt text="<code>assert acronym_it('Hard work pays off') == str<code>" >

It might be helpful to read the function code line by line. 

</opt>

</choice> 


**Question 2** 

```python
def acronym_it(sentence):
    words = sentence.split()
    first_letters = [word[0].upper() for word in words]
    acronym =  "".join(first_letters)
    return acronym
```

Given the function above, which test **would** fail?  

```python 
assert acronym_it("Hard work pays off") == ???
```

<choice id="2" >

<opt text="<code>assert acronym_it('If at first you do not succeed, try try again') == 'IAFYDNSTTA'</code>" >

Great!

</opt>

<opt text="<code>assert acronym_it('There are 30 bottles of beer on the wall!') == 'TA3BOBOTW'</code>" >

It might be helpful to read the function code line by line. 

</opt>

<opt text="<code>assert acronym_it('Build me up, buttercup') == 'BMUB'</code>"  >

It might be helpful to read the function code line by line. 

</opt>

<opt text="<code>assert acronym_it('10 times 5 is 50') == '10T5I50'<code>" correct="true">

Good work! 

</opt>

</choice> 

</exercise>


<exercise id="20" title="Unit Tests and Test-Driven Development Questions">


**Question 1**

When do we ideally like to write our unit tests for our functions? 



<choice id="1" >
<opt text="Before writing our function code" correct="true" >

You got it!

</opt>

<opt text="After writing our function's code" >

This is not ideal.

</opt>

<opt text="While writing our function's code"  >

Although this happens sometimes, it's better to write your tests before your function's code.

</opt>

</choice> 


**Question 2**


When can we be confident in our code? 


<choice id="2" >
<opt text="When all our tests pass."  >

You got it!

</opt>

<opt text="After writing edge cases and they also pass." >

This is not ideal.

</opt>

<opt text="When our function does what we want without even writing test."  >

Although this happens sometimes, it's better to write your tests before your function's code.

</opt>

<opt text="It's good to err on the side of caution when it comes to being confident in our code (bad things can happen to good coders)."  correct="true">

</choice> 

**Question 3**


The first step in a systematic approach to program design is: 


<choice id="3" >
<opt text="Write unit tests."  >

But we don't know our input arguments or the output type that we are expecting yet?

</opt>

<opt text="Write a docstring." >

This is the last step!

</opt>

<opt text="Write a function stub." correct="true" >

Nailed it!

</opt>

<opt text="Write your pseudo-code."  >

This should come after writing tests and defining your function!

</choice> 



</exercise>


<exercise id="21" title= "Writing Tests">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Given our BMI function from the previous few questions, let's write some unit tests.

Tasks:
- Write 4 unit tests and check that at least 2 of them are testing edge cases. 


<codeblock id="06_21">

- Are you using `Assert` statements?
- Are you checking that they equal a correct value?



</codeblock>

</exercise>

<exercise id="22" title="Good Function Design Choices" type="slides, video">

<slides source="module6/module6_22" shot = "1" start="0:165" end="3:01">

</slides>

</exercise>


<exercise id="23" title="Function Design Questions">

What's wrong with the function below? 

```python
def give_me_facts(myinfo):
    max_val = max(myinfo)
    min_val = min(myinfo)
    range_val = max_val - min_val
    return max_val, min_val, range_val
```


<choice id="1" >
<opt text="It is doing too many calculations" >

Calculations are fine if we need them and here it looks like we need them to calculate the range.

</opt>

<opt text="It is using a global variable inside the function" >

There are no global variables in the function.

</opt>

<opt text="It's returning too many objects" correct="true">

Perfect! This is too many!

</opt>

<opt text="It's hard coding values in the function"  >

We are lucky that there are no hardcoded values in this function!

</opt>

</choice> 


</exercise>


<exercise id="24" title="Improve it!">

How can we improve this function?

```python

def count_the_sevens(mylist): 
    number_of_occurances  = mylist.count(7)
    return number_of_occurances
```


<choice id="1" >
<opt text="Avoid using a list as an input arguments" >

Lists are completely fine to use as input arguments. 

</opt>

<opt text="Simplify the operations" >

This function is only 3 lines! Do we need it simpler?

</opt>

<opt text="Use fewer global variables" >

Luckily no global variables are being used in this function.

</opt>

<opt text="Remove the hard-coded value"  correct="true">

Perfect! Let's make the count variable (in this case the `7`) an input argument. 

</opt>

</choice> 


</exercise>


<exercise id="25" title= "Function Design">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Given the function below, improve it so that it follows good function design principles. 


Tasks:
- Given the function above, improve it using to the new function `new_wage()`. We have provided you with the function stub and the docstring to guide you.   
- Make sure it follows good function design practices by not looping over a function, avoiding hard-coding and not returning multiple values.
- Test your new function on a person with a salary of $84000 and an expected raise of 12%.
- Save this in an object named `person1_new_wage`.


<codeblock id="06_25">

- Are you removing the hardcoded values in the function?
- Are removing the return of 2 variables? 
- Are you removing the loop from inside the function? 
- Are you multiplying the `salary` by `(1 + (0.01 * percent_raise)` ? 

</codeblock>

</exercise>

<exercise id="26" title="What Did We Just Learn?" type="slides, video">
<slides source="module6/module6_end" shot = "0" start="0:165" end="3:01">>
</slides>
</exercise>
