---
title: 'Module 2: Not So Scary Wrangling (Table Manipulation and Chaining)'
description:
  'In this module you will learn how to import different types of files, perform more advanced table manipulations (modifying columns inplace with and without the apply function) as well ast method chaining conventions (style, including multi-line).'
prev: /module1
next: /module3
type: chapter
id: 2
---



<exercise id="0" title="Module Learning Outcomes" type="slides">

<slides source="module2_00">
</slides>

</exercise>


<exercise id="1" title="Reading in Different File Types" type="slides">

<slides source="module2_01">
</slides>

</exercise>

<exercise id="2" title="Delimiter">

**Question 1**          
What is a delimiter?


<choice id="1" >
<opt text="It defines how column values are separated." correct="true">

Good job!

</opt>

<opt text="It prevents a limitation on the data being read it.">

You may want to look over this before moving forward.

</opt>

<opt text="It is a manner of deleting values from a dataframe." >

You may want to look over this before moving forward.

</opt>

</choice> 


**Question 2**         
What argument is needed if we want to read in our data with from an Excel spreadsheet where there are multiple dataframes saved on different sheets?

<choice id="2" >
<opt text='<code>header</code>'>

This is not specifying a particular sheet. You want want to review this section. 

</opt>

<opt text= '<code>sheet_name</code>' correct="true">

Good job!

</opt>

<opt text='<code>sheet</code>' >

Note quite but you are on the right track. 

</opt>

</choice> 

</exercise>


<exercise id="3" title="Reading in a URL">

Let's try reading in some data from a URL using `pd.read_csv()`.      
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:

- Use `pd.read_csv()` to read in the data from [this url](https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv) and save it as `pokeman_df`.
- Use the Pokemon column name as the index.
- Display the first 10 rows.



<codeblock id="02_03">

- Are you sure you are saving your dataframe as `pokemon_df`?
- Are you using `pd.read_csv()`?

</codeblock>

</exercise>

<exercise id="4" title="Reading in a Text File">

Let's try reading in a `.txt` file.     
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:

- Read in the data from a text file name `pokemon-text.txt` located in the `data` folder and save it as `pokemon_df`.
- it's a good idea to see what the delimiter.
- Use the Pokemon column name as the index.
- Display the first 10 rows.

<codeblock id="02_04">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()`?
- Are you including the full path through the `data/` folder when calling the file name?
- Check that your delimiter argument is correct.   

</codeblock>

</exercise>

<exercise id="5" title="Reading in an Excel File">

Let's try reading in a Excel file.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:
- Read in the data from the text file name `pokemon.xlsx` located in the `data` folder and save it as `pokemon_df`.
- there is a sheet in the excel file named `pokemon` which is where the data is stored.
- Use the Pokemon column name as the index.
- Display the first 10 rows.

<codeblock id="02_05">


- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_excel()`?
- Check that you are using `sheet_name="pokemon"`. 
- Are you including the full path through the `data/` folder when calling the file name?

</codeblock>

</exercise>

<exercise id="6" title="Arguments for Reading Data" type="slides">

<slides source="module2_06">
</slides>

</exercise>

<exercise id="7" title="Name that Argument!">

**Question 1**          
Which argument will assign your index label when reading in your data with `pd.read_excel()`?


<choice id="1" >
<opt text='<code>header</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>ncols</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>index_col</code>' correct="true">

Good job!

</opt>

</choice> 


**Question 2**         
Which argument will select only specific columns of the data file  with `pd.read_csv()`?

<choice id="2" >
<opt text='<code>header</code>'>

Note quite but you are on the right track. 

</opt>

<opt text= '<code>nrows</code>' correct="true">

Note quite but you are on the right track. 

</opt>

<opt text='<code>usecols</code>'  correct="true">

Good job!

</opt>

</choice> 

</exercise>


<exercise id="8" title="Using Arguments when Reading in Files">

Load in the data using the most suitable arguments. 
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:
Read in the `pokemon.csv` file using the full pathway.
Save it as `pokemon_sample`.   
Only load in the first 100 rows and only load in columns  `name`, `total_bs`, `type`. 
Display the entire dataframe.


<codeblock id="02_08">

- Are you sure you are saving your dataframe as `pokeman_df`?
- Are you using `pd.read_csv()`?
- Are you including the full path through the `data/` folder when calling the file name?
- Do you have an argument `nrows=100`?
- Are you loading in the specified column index labels?
- Perhaps you are using `index_col=0` when it was not required?

</codeblock>

</exercise>

<exercise id="9" title="Using Arguments when Reading in Files">

Let's read in a new pokemon data file using `pd.read_csv()` and the most suitable arguments to satisfie the task requirements.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**


Tasks:
- Read in the data from a csv file name `pokemon2.csv` using the full pathway
- Save it as `pokemon_df2`.
- It may be a good idea to look at the data via [this link](https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/blob/binder/data/pokemon2.csv) first. 
- Use the Pokemon column name as the index.
- Change the values in column `legendary` from `yes` to `True` the values `no` to `False`. 
- Only load in the column named `attack`,	`defense`, `speed`, `type` and `lengendary`.
- Display the dataframe. 

<codeblock id="02_09">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` ?
- Are you including the full path through the `data/` folder when calling the file name?
- Did you use `header=4`?
- Did you make sure to use square brackets with `usecols`?
- Did you use both `true_values` `false_values`?


</codeblock>

</exercise>


<exercise id="10" title="Column Renaming and Creation" type="slides">

<slides source="module2_07">
</slides>

</exercise>


<exercise id="11" title="Column Edit Questions">

**Question 1**          
If we do not assign an object name when renaming a column (`df = df.rename()`)  or creating a new dataframe column  (`df = df.assign()`) what will happen?


<choice id="1" >
<opt text='The code will not run'>

You may want to look over this before moving forward.

</opt>

<opt text='The dataframe will not be displayed'>

You may want to look over this before moving forward.

</opt>

<opt text='The new column or column name will not be saved' correct="true">

Good job!

</opt>

</choice> 


**Question 2**   
If you want your dataframe to drop a column for good using `df.drop()`, it is necessary to assign it to an object. 


<choice id="2" >
<opt text='<code>True</code>'>
When using `df.drop()` we need to save the dataframe in a object for the changes to be permanent

</opt>

<opt text='False'  correct="true">

Good job!

</opt>

</choice> 

</exercise>


<exercise id="11" title="Renaming a Column Index">

Let's rename one of the columns in our `pokemon.csv` data.     
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:

- Load in the data 


<codeblock id="02_11">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` ?
- Did you use `header=4`?
- Did you make sure to use square brackets with `usecols`?
- Did you use both `true_values` `false_values`?

</codeblock>

</exercise>

<exercise id="12" title="Creating a New Column">

Load in the `pokemon.csv file only taking the first 500 values of the dataset. 
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_12">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>


<exercise id="13" title="Data Filtering" type="slides">

<slides source="module2_10">
</slides>

</exercise>

<exercise id="14" title="Single Condition Filtering">

Let's  read in some our hockey_players file using `pd.read_csv()` using different arguments to satisfy certain requiresments.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_11">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="15" title='Filtering using "and" or "or"'>

Let's  read in some our hockey_players file using `pd.read_csv()` using different arguments to satisfy certain requiresments.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_12">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="16" title='Filtering using "and" and "or"'>

Let's  read in some our hockey_players file using `pd.read_csv()` using different arguments to satisfy certain requiresments.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_13">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="17" title="Chaining and Method Chaining" type="slides">

<slides source="module2_14">
</slides>

</exercise>

<exercise id="18" title="Function vs. Attributes">

**Question 1**          


<choice id="1" >
<opt text='<code>header</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>ncols</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>index_col</code>' correct="true">

Good job!

</opt>

</choice> 


**Question 2**         


<choice id="2" >
<opt text='<code>header</code>'>

Note quite but you are on the right track. 

</opt>

<opt text= '<code>nrows</code>' correct="true">

Note quite but you are on the right track. 

</opt>

<opt text='<code>usecols</code>'  correct="true">

Good job!

</opt>

</choice> 

</exercise>


<exercise id="19" title="Practice Chaining">

  
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_16">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="20" title="Grouping and Aggregating" type="slides">

<slides source="module2_17">
</slides>

</exercise>


<exercise id="21" title="Grouping and Aggregating Quick Questions">

**Question 1**          


<choice id="1" >
<opt text='<code>header</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>ncols</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>index_col</code>' correct="true">

Good job!

</opt>

</choice> 


**Question 2**         


<choice id="2" >
<opt text='<code>header</code>'>

Note quite but you are on the right track. 

</opt>

<opt text= '<code>nrows</code>' correct="true">

Note quite but you are on the right track. 

</opt>

<opt text='<code>usecols</code>'  correct="true">

Good job!

</opt>

</choice> 

</exercise>

<exercise id="22" title="Practice Chaining">

  
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_19">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="23" title="Practice Chaining">

  
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run it and see if you obtain the desired output. Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_20">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

