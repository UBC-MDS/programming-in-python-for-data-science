---
title: "Module 7: Importing Files and the Coding Style Guide"
description:
   'In this module, you will learn about how to import files and libraries from other directories and stylize your code for optimal readability.'
prev: /module6
next: /module8
type: chapter
id: 7
---


<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module7/module7_00" shot = "11" start="0:001" end="0:48">
</slides>

</exercise> 

<exercise id="1" title="Importing Python Libraries" type="slides, video">

<slides source="module7/module7_01" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="2" title="Importing packages ">

**Question 1**      


How would you import a package named `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately, this would not import `numpy`.

</opt>


<opt text="<code>from numpy import numpy</code>">

Are you sure you read the slides properly?

</opt>


</choice> 

**Question 2**          

How would you import `numpy` if you wanted to refer to it as `np`? 


<choice id="2" >
<opt text="<code>as np import numpy </code>">

This would actually result in an error! 

</opt>

<opt text="<code>Import numpy As np</code>">

Be careful with capitals. In this case, when you use capitalization, neither `Import` nor `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is not the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>

<exercise id="3" title="Importing a Package Function">

How would you import the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try ordering this differently?

</opt>

<opt text="<code>from numpy import sqrt</code>"  correct="true">

Great!

</opt>


<opt text="<code>from sqrt import numpy</code>">

We are importing only the `sqrt` function from the `numpy` package.

</opt>


<opt text="<code>import numpy from sqrt</code>"  >

`sqrt` is a single function that we want to import from `numpy`.

</opt>

</choice> 

</exercise>


<exercise id="4" title= "Importing Packages... Again">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Ok, so we've seen this `numpy` package, let's actually load in one of the functions and use it! If you are wondering what this package does, don't worry, you'll learn more of this in the next module. `numpy` has a function called `power()`.

Tasks:
- Import the `power()` function from the `numpy` package. 
- Use the `power()` function to find  7 to the power of 5 - you may want to use `?power` to see what arguments the function requires.
- Display your results.



<codeblock id="07_04">

- Are you using `power(7, 5)`? 
- Are you importing using `from`?

</codeblock>

</exercise>

<exercise id="5" title="Working with Other Files" type="slides, video">

<slides source="module7/module7_05" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="6" title="Importing Your Own Functions Questions">

**Question 1**      

Where do you save your files so you can import them into new Jupyter notebooks? 


<choice id="1" >
<opt text="<code>.python</code>">

Not quite but you are on the right track. 

</opt>

<opt text="<code>.py</code>" correct="true">

Nice! 

</opt>


<opt text="<code>.ipynb</code>">

This is a Jupyter notebook file, not a file to import a function from. 

</opt>


</choice> 

**Question 2**          

Is the following statement True or False? 

*You can import files containing functions in a similar way to how you import Python libraries*


<choice id="2" >
<opt text="True" correct="true">

That's right! This makes things easy for us.

</opt>

<opt text="False">

Note quite, Python uses a similar importing style for libraries and saved scripts. 

</opt>



</choice>  

</exercise>

<exercise id="7" title="More Importing Your Own Functions Questions">

If I have a file named `baking.py` containing functions like `cake()` and `scones()` and I want to import it into a Jupyter notebook using the alias `bake`, which of the following would be required? 


<choice id="1" >
<opt text="<code>import cake from baking</code>"  >

`cake` is the function name, not the library. 

</opt>

<opt text="<code>from baking import bake</code>" >

this isn't quite right. `bake` is an alias, not a package. 

</opt>


<opt text="<code>import baking as bake</code>"  correct="true">

This is right!

</opt>


<opt text="<code>import bake as scone</code>"  >

The alias we want to call `baking` is `bake`, not `scone`.

</opt>

</choice> 

</exercise>

<exercise id="8" title="Testing Your Own Functions with Pytest" type="slides, video">

<slides source="module7/module7_08" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="9" title="Using Pytest Questions">

**Question 1**      


When you make a function from a unit test, what naming guideline does your function have to follow for `pytest` to work? 


<choice id="1" >
<opt text="The function must end with <code>test</code>">

It should not end with `test`, but the word "test" should be included in the name. 

</opt>

<opt text="The function must begin with <code>test</code>" correct="true">

Great! 

</opt>

<opt text="The function must end with <code>pytest</code>">

`pytest` does not need to be used in the function name. 

</opt>

<opt text="The function must begin with <code>pytest</code>">

`pytest` does not need to be used in the function name. 

</opt>


</choice> 

**Question 2**          

Where are your unit test functions saved?

<choice id="2" >
<opt text="In the same Jupyter notebook">

This would defy the DRY principle if wanted to test our function in multiple different notebooks. 

</opt>

<opt text="In the same file as the function you are testing">

Not if we want to use `pytest`!

</opt>

<opt text="In a seperate <code>.py</code> file"  correct="true">

Great!

</opt>

<opt text="In a seperate Jupyter notebook">

`pytest` would not be able to check the tests in a separate Jupyter notebook. 

</opt>

</choice>  

</exercise>

<exercise id="10" title="More Questions on Using Pytest">

I have a function named `travel_location()` stored in a file named `travelling.py` and unit tests that checked this function stored in a file named `test_travelling.py`, how would I check my function using `pytest` in a Jupyter notebook?


<choice id="1" >
<opt text="<code>!pytest travel_location</code>"  >

You do not need to use your function name.

</opt>

<opt text="<code>!pytest travelling</code>" >

The unit tests are not stored in the `travelling.py` script.

</opt>


<opt text="<code>!pytest tests</code>">

You need to specify a file!

</opt>


<opt text="<code>!pytest test_travelling</code>" correct="true" >

Nice!

</opt>

</choice> 

</exercise>


<exercise id="11" title= "Making test function">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Remember the BMI function and unit tests we made back in the last module? Well, let's do the first step in testing it with `pytest` by converting them into an appropriate function. 

Tasks:
- Take these unit tests we wrote and compile them together in a function to test the function `bmi_calculator()`.
- Don't forget to give it a name compliant with `pytest`'s needs. 


<codeblock id="07_11">

- Are you naming it something starting with `test`? 
- Are you remembering these functions do not need to return anything?
- These functions do not take any arguments.

</codeblock>

</exercise>


<exercise id="12" title="Automatic Style Formatters" type="slides, video">

<slides source="module7/module7_12" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="13" title="Using Flake8 and Black">

**Question 1**      

Which of the following tools will modify your code? 


<choice id="1" >
<opt text="<code>PEP8</code>"  >

This is a style guide, not a library to modify your code. 

</opt>

<opt text="<code>flake8</code>">

This tool will suggest changes but will not change your code. 

</opt>

<opt text="<code>blue</code>" >

This is not a style guide nor is it a formatter, in fact, we are not sure what this is either!

</opt>

<opt text="<code>black</code>" correct="true">

Great work. 

</opt>


</choice> 

**Question 2**          

Which of the following formatting would Black **NOT** fix?


<choice id="2" >
<opt text="Trailing white space">

Black will remove unnecessary white space!

</opt>

<opt text="Adding white space where necessary">

Black will add white space where appropriate.

</opt>

<opt text="Fixing grammar in comments"  correct="true">

Nice work!

</opt>

<opt text="Indentations">

Black fixes indentations thankfully!

</opt>

</choice>  

</exercise>

<exercise id="14" title="Using Black">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take the function named `cleanup()` which drops duplicate rows and columns. Rewrite the function code (not the docstring) so that it's written with necessary spaces and indentations.

Tasks:
- Amend the function `cleanup()` so that it adopts an approach that has spaces where necessary and blank space is removed. Make sure that you have indentations and empty lines where necessary.


<codeblock id="07_14">

- Are you adding spaces between operators? 
- Are you removing spaces where appropriate?
- Did you fix the indentation error?
- How about removing the blank lines before the return statement?

</codeblock>

</exercise>


<exercise id="15" title="Formatting That Can't Be Fixed Automatically" type="slides, video">

<slides source="module7/module7_15" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="16" title="Writing Useful Comments">

Given the code here: 


```python
candy = pd.read_csv('candybars.csv')
chocolate = pd.read_csv('chocolate_types.csv')


dessert = candy.merge(chocolate,  how='inner').dropna()
```


<choice id="1" >
<opt text="<code># Combine dataframes and drops NaN values</code>"  correct="true">

Great!

</opt>

<opt text="<code># Merge dataframes</code>"  >

This could be a bit more useful, what about the `.dropna()`?

</opt>


<opt text="<code># Combines the candy and chocolate dataframes and only keeps rows that both dataframes have in common, then removes any rows with missing values</code>">

This is a bit excessive. 

</opt>


<opt text="No comment is needed here"  >

A comment here could be useful since we are chaining verbs here. 

</opt>

</choice> 


</exercise>

<exercise id="17" title="Choosing Good Variable Names">


**Question 1**      


Which of the following is an acceptable variable name?


<choice id="1" >
<opt text="<code>bool</code>"  >

This is a Python keyword and is not an acceptable object name. 

</opt>

<opt text="<code>AppleTrees</code>" >

It's not good styling to have capitalizations in your variable names. 

</opt>


<opt text="<code>Hotel_Df</code>">

It's not good styling to have capitalizations in your variable names. 

</opt>

<opt text="<code>paper_sales</code>" correct="true">

Nice!

</opt>


</choice> 

**Question 2**          

I have a dataframe that contains different flowers, their seasonality, and where they are found in the world. 

Which of the following is the most suitable name for this dataframe? 


<choice id="2" >
<opt text="<code>flowers_seasonality_location</code>">

We find this a bit long-winded. Is it necessary to add the columns to the object name?

</opt>

<opt text="<code>FLOWERS</code>">

Please don't use all capitals for your object names. 

</opt>

<opt text="<code>flowers_df</code>"  correct="true">

Nice work!

</opt>

<opt text="<code>flw</code>">

I think we should try and make this a more readable object name. 

</opt>

</choice>  


</exercise>

<exercise id="18" title="The Python Debugger" type="slides, video">

<slides source="module7/module7_18" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="19" title="Using the Python Debugger">

**Question 1**      


How is the Python debugger helpful?


<choice id="1" >
<opt text="It can help explain where your code is failing"  correct="true">

This is exactly why the Python debugger is useful!

</opt>

<opt text="It tells us where our code could be more efficient">

The Python debugger can't improve code that works. 

</opt>


<opt text="It removes any of the code that is not following the DRY principle">

The Python debugger helps with *debugging* and not with adhering to the DRY principle. 

</opt>


</choice> 

**Question 2**          

Which of the following can we use from the Python Debugger to examine our code and inspect our variables?



<choice id="2" >
<opt text="<code>break()</code>">

Almost but not quite. 

</opt>

<opt text="<code>tracepoint()</code>">

This is not the function but the ending sure sounds familiar...

</opt>

<opt text="<code>traceback()</code>">

This does seem plausible, doesn't it? Unfortunately, this isn't correct. 

</opt>

<opt text="<code>breakpoint()</code>" correct="true">

You got it!

</opt>

</choice>  

</exercise>


<exercise id="20" title="What Did We Just Learn?" type="slides, video">
<slides source="module7/module7_end" shot="11" start="0:49" end="1:32">>
</slides>
</exercise>