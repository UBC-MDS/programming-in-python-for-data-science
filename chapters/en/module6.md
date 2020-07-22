---
title: 'Module 6: A Slice of Numpy (Numpy Arrays)'
description:
  'In this module you will learn about ...'
prev: /module5
next: /module7
type: chapter
id: 6
---

<exercise id="23" title="Function Docstrings" type="slides">

<slides source="module5/module5_22">

</slides>

</exercise>


<exercise id="24" title="Docstring Questions">

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



<exercise id="25" title= "Writing a Docstring ">

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