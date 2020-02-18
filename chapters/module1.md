---
title: 'Module 1: Python & Pandas - an Unexpected Friendship!'
description:
  'In this module you will be introduced to dataframes and the pandas python package.'
prev: module0
next: /module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes" type="slides">

<slides source="module1_00">
</slides>

</exercise>


<exercise id="1" title="Introduction to Dataframes and Pandas" type="slides">

<slides source="module1_01">
</slides>

</exercise>

<exercise id="2" title="Describing a Dataframe">

**What are data frames comparable to?**


<choice id="1" >
<opt text="Text Documents">

Is this an easy way to organize data?

</opt>

<opt text="Excel Sheets" correct="true">

Good job! 

</opt>

<opt text="Picture Frames" >

Are we storing pictures in a data frame?

</opt>

</choice>

**What is Pandas?**    


<choice id="2">
<opt text="A Python package needed for extra tools" correct="true">

Nice work! Pandas is a package we import so we can use additional features.

</opt>

<opt text="A programming language">

Are you sure you know the difference between Python and Pandas? 

</opt>

<opt text=" Fluffy animals that eat bamboo">

Although that isn't wrong, we are studying Python and coding and in this course, the context is not quite right. 

</opt>

</choice >

</exercise>

<exercise id="3" title="Title here">

Let's try importing pandas and loading in our own dataset. 

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load. 

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**


- Import `pandas` as `pd`. 
- Load in a dataset named `.csv`.
- Save the dataframe as ``.
- display the dataframe

<codeblock id="01_03a">

- Are you sure you are saving `candybar_feat` and `candybar_names` as lists?
- Did you import the csv with the correct manner?

</codeblock>

- Let's display the column names 
- Let's find our the dataframes dimension 
- How many rows does the dataframe have? 

<codeblock id="01_03b">

- Are you sure you are saving `candybar_feat` and `candybar_names` as lists?
- Did you import the csv with the correct manner?

</codeblock>

**Question:**  
How many features does the data have?

<choice  id="1">
<opt text="9">

This is the total number of columns, not the number of features

</opt>

<opt text="8" correct="true">

Yes! Good job!

</opt>

<opt text="25">

This is not the number of features.

</opt>

<opt text="6">

This is not the number of features.

</opt>
</choice>

**Question:**   
 How many examples does the data have?

<choice  id="2">

<opt text="9">

This is the total number of columns, not the number of examples.

</opt>

<opt text="8" >

This is the not the number of examples.

</opt>

<opt text="25" correct="true">

Well done!

</opt>

<opt text="26">
This is not the number of examples.

</opt>
</choice>

**Question:**   
Would this be considered classification or regression?

<choice  id="3">
<opt text="Classification" correct="true">

Great job!

</opt>

<opt text="Regression" >

What would we be predicting, a numerical value or categorical?

</opt>
</choice>
</exercise>

<exercise id="5" title="More Pandas, Less Fur" type="slides">

<slides source="module1_05">
</slides>

</exercise>


<exercise id="9" title="Title here" type="slides">
<slides source="module1_09">
</slides>
</exercise>

<exercise id="10" title="Title here">

**Do the following statements correspond to the `fit` or the `predict` function:**  

**Statement:**   
_Is called first (before the other one)._

<choice id="1">
<opt text="Fit" correct="true">

Great job! Training on training data must be done before predicting on new data. 

</opt>

<opt text="Predict" >

How can the model predict without education first?

</opt>
</choice>

**Statement:**  
_At least for decision trees, this is where most of the hard work is done._

<choice id="2">
<opt text="Fit" correct="true">

Great job! Training is more intensive then predicting for decision trees. 

</opt>

<opt text="Predict" >

Where do we teach the model? 

</opt>
</choice>

**Statement:**   
_Only takes `X` as an argument._

<choice id="3">
<opt text="Fit">

We need to make sure we give the model the correct labels so it can _learn_. 

</opt>

<opt text="Predict" correct="true">

Great job!

</opt>
</choice>

**Statement:**  
_In scikit-learn, we can ignore its output._

<choice id="4">
<opt text="Fit" correct="true">
 
Great job!

</opt>

<opt text="Predict">

You may want to look at the slides and see what each function delivers as an output. 

</opt>
</choice>
</exercise>

<exercise id="11" title="Title here">

Let's try training and prediction our own model. 

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load. 

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**

<codeblock id="01_11">

- Make sure you are using the correct functions 
- Are you using the model named `model`?

</codeblock>
</exercise>

<exercise id="12" title="Title here" type="slides">
<slides source="module1_12">
</slides>
</exercise>

<exercise id="13" title="Title here">

Let's try calculating the Gini impurity  on our candybar dataset using the same `gini2` function from the module slides. The function has been imported for you. 

Let's make the split on the feature `peanuts` where anything greater than 0.5 is classified as `American`. Remember that you now have 2 groups and you need to calculate the impurity for both groups.  

* Don't forget to take into consideration the porportion of observations in each group!

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load. 

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**

The packages you need will be loaded for you. 
Save your Gini impurity as object `peanut_gini_impurity`

<codeblock id="01_13">

- Are you taking into consideration there are 2 gini calculations ( you will have to call `gini2 ` twice)?
- There are 6 observations of the 16 that have `peanuts` >= 0.5. Of those, 5 are of class `America` and 1 is of class `Canada`. 
- There are 10 observations of the 16 that have `peanuts` < 0.5. Of, those 3 are of class `America` and 7 is of class `Canada`.


</codeblock>
</exercise>

<exercise id="14" title="Title here" type="slides">
<slides source="module1_14">
</slides>
</exercise>


<exercise id="15" title= "Title here">

**Question:**   
What type of tree are Decision Trees?

<choice id="1">
<opt text= "General Tree" >
 
How are the features split ?  

</opt>

<opt text="Binary Trees (2 children per node)." correct="true">

Nice work!

</opt>

<opt text="AVL Tree (self-balancing binary search tree).">

Does the tree need to be balanced? 

</opt>

</choice>

</exercise>

<exercise id="16" title= "Title here">

Who choses the features that are split on at each node?

<choice id="1">
<opt text= "Data Scientist" >
 
Where would we input this information?  

</opt>

<opt text="Model" correct="true">

Great!

</opt>

</choice>

</exercise>

<exercise id="17" title= "Title here">

**Question:**   
What is the depth of a decision stump? 

<choice id="1">
<opt text= "1" correct="true">
 
You have been paying attention! Nice work! 

</opt>

<opt text="5" >

This is the default max depth of the decision tree classifier not the depth of a decision stump.

</opt>

<opt text="Whatever you set it as" >

Decision stumps are what make up a decision tree, stumps are not a hyperparameter

</opt>
</choice>
</exercise>

<exercise id="18" title= "Title here">

**Are the following Statements True or False**:

**Statement**    
_The standard decision tree algorithm finds the optimal tree given a data set._

<choice id="1">
<opt text= "True" >
 
For each node the model finds the optimal feature to split on but the nodes are chosen sequentially and it cannot choose the overall optimal tree. 

</opt>

<opt text="False" correct="true">

Great! Just because the model chooses the best feature to split on each node does not mean the total tree is the optimal one! 

</opt>

</choice>

**Statement:**     
_The same feature can be split on multiple times in a tree with depth > 1._

<choice id="2">
<opt text= "True" correct="true">
 
Super! There can be multiple threshold splits used for the same feature. 

</opt>

<opt text="False" >

There can be multiple threshold splits used for the same feature. 

</opt>

</choice>
</exercise>

<exercise id="19" title="What Did We Just Learn?" type="slides">
<slides source="module1_19">
</slides>
</exercise>