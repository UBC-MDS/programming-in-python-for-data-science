---
title: "Module 7: Importing Files and the Coding Style Guide"
description:
   'In this module you will learn about how to import files and libraries from other directories and stylize your code for optimal readability.'
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


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

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

How would you import just the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try reording this?

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

Ok, so we've seen this `numpy` package, let's actually load in one of the functions and use it! If you are wondering what this package does, don't worry, you'll learn more of this in the next module. `numpy` has a function called `power()`

Tasks:
- Import the `power()` function from the `numpy` package. 
- Use the `power()` function to find  7 to the power of 5 - You may want to use `?power` to see what arguments the function requires.
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


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is neither the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>

<exercise id="7" title="More Importing Your Own Functions Questions">

How would you import just the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try reording this?

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

<exercise id="8" title="Testing Your Own Functions with Pytest" type="slides, video">

<slides source="module7/module7_08" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="9" title="Using Pytest Questions ">

**Question 1**      


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is neither the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>

<exercise id="10" title="More Questions on Using Pytest">

How would you import just the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try reording this?

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

<exercise id="11" title="Automatic Style Formatters" type="slides, video">

<slides source="module7/module7_11" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="12" title="Using Flake8">

**Question 1**      


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is neither the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>

<exercise id="13" title="Using Black">

How would you import just the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try reording this?

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

<exercise id="14" title="Formatting That Can't Be Fixed Automatically" type="slides, video">

<slides source="module7/module7_14" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="15" title="Choosing Good Variable Names">

**Question 1**      


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is neither the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>

<exercise id="16" title="Writing Informative Comments">

How would you import just the square root function `sqrt` from the `numpy` package? 


<choice id="1" >
<opt text="<code>import sqrt from numpy</code>"  >

Maybe try reording this?

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

<exercise id="17" title="Python Debugger" type="slides, video">

<slides source="module7/module7_17" shot="4" start="0:165" end="3:01">
</slides>

</exercise>


<exercise id="18" title="Using the Python Debugger">

**Question 1**      


How would you import a package name `numpy`? 


<choice id="1" >
<opt text="<code>import numpy </code>"  correct="true">

This is the basic way to import a Python package.

</opt>

<opt text="<code>as np import numpy </code>">

Unfortunately this would not import `numpy`.

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

Be careful with capitals in this case, when you use capitalization, neither `Import` or `As` are Python keywords. 

</opt>

<opt text="<code>import numpy as np </code>"  correct="true">

Nice work!

</opt>

<opt text="<code>As np Import numpy </code>">

This is not the correct way to import, and it uses capitalization on keywords which is incorrect. 

</opt>

</choice>  

</exercise>


<exercise id="19" title="What Did We Just Learn?" type="slides, video">
<slides source="module7/module7_end" shot="11" start="0:49" end="1:32">>
</slides>
</exercise>