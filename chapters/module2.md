---
title: 'Module 2: Not So Scary Wrangling (Table Manipulation and Chaining)'
description:
  'In this module, you will learn how to import different types of files, perform more advanced table manipulations (modifying and creating new columns) as well as method chaining conventions (style, including multi-line).'
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
<opt text="It defines how column values are separated" correct="true">

Good job!

</opt>

<opt text="It prevents a limitation on the data being read it">

You may want to look over this before moving forward.

</opt>

<opt text="It is a manner of deleting values from a dataframe" >

You may want to look over this before moving forward.

</opt>

</choice> 


**Question 2**         
What argument is needed if we want to read in data from an Excel spreadsheet where there is data saved on different sheets?

<choice id="2" >
<opt text='<code>header</code>'>

This is not specifying a sheet.  You may want to review this section. 

</opt>

<opt text= '<code>sheet_name</code>' correct="true">

Good job!

</opt>

<opt text='<code>sheet</code>' >

Not quite but you are on the right track. 

</opt>

</choice> 

</exercise>


<exercise id="3" title="Reading in a URL">

Let's try reading in some data from a URL using `pd.read_csv()`.      
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Use `pd.read_csv()` to read in the data from [this url](https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv) using the Pokemon column name as the index.
- Save the resulting dataframe as `pokemon_df`.
- Use the Pokemon column name as the index.
- Display the first 10 rows of `pokemon_df`.



<codeblock id="02_03">

- Are you sure you are saving your dataframe as `pokemon_df`?
- Are you using `pd.read_csv()`?

</codeblock>

</exercise>

<exercise id="4" title="Reading in a Text File">

Let's try reading in a `.txt` file.     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Read in the data from a text file name `pokemon-text.txt` located in the `data` folder useing the Pokemon column name as the index.
- Save the resulting dataframe as `pokemon_df`.
- it's a good idea to see what the [delimiter](https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/blob/binder/data/pokemon-text.txt) is.
- Display the first 10 rows of `pokemon_df`.

<codeblock id="02_04">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()`?
- Are you including the full path through the `data/` folder when calling the file name?
- Check that your delimiter argument is correct.   

</codeblock>

</exercise>

<exercise id="5" title="Reading in an Excel File">

Let's try reading in an Excel file.    
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:
- Read in the data from the sheet named `pokemon` from the Excel file `pokemon.xlsx` located in the `data` folder using the Pokemon column name as the index. 
- Save the resulting dataframe as `pokemon_df`.
- Display the first 10 rows of `pokemon_df`.

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
Which argument will assign your row index labels when reading in your data with `pd.read_excel()`?


<choice id="1" >
<opt text='<code>header</code>'>

This labels your column names, not your row index labels. 

</opt>

<opt text='<code>ncols</code>'>

You may want to look over this before moving forward.

</opt>

<opt text='<code>index_col</code>' correct="true">

Good job!

</opt>

</choice> 


**Question 2**         
Which argument will select only specific columns of the data file with `pd.read_csv()`?

<choice id="2" >
<opt text='<code>header</code>'>

Not quite but you are on the right track. 

</opt>

<opt text= '<code>nrows</code>' correct="true">

Not quite but you are on the right track. 

</opt>

<opt text='<code>usecols</code>'  correct="true">

Good job!

</opt>

</choice> 

</exercise>


<exercise id="8" title="Using Arguments when Reading in Files">

Load in the data using the most suitable arguments.     
      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:
-  Read in the first 100 rows and columns name, total_bs and type from the file `pokemon.csv`, which is located in the data directory.
- Save the resulting dataframe as `pokemon_sample`. 
- Display `pokemon_sample`.


<codeblock id="02_08">

- Are you sure you are saving your dataframe as `pokeman_df`?
- Are you using `pd.read_csv()`?
- Are you including the full path through the `data/` folder when calling the file name?
- Do you the argument `nrows=100`?
- Are you loading in the specified column index labels?
- Perhaps you are using `index_col=0` when it was not required?

</codeblock>

</exercise>


<exercise id="9" title="Column Renaming and Dropping" type="slides">

<slides source="module2_09">
</slides>

</exercise>


<exercise id="10" title="Column Editing Questions">

**Question 1**          
If we do not assign an object name when renaming a column (`df.rename()`) what will happen?


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
If you want your dataframe to drop a column permanently using `df.drop()`, it is necessary to assign it to an object. 


<choice id="2" >
<opt text='True' correct="true">

Good job!


</opt>

<opt text='False' >

When using `df.drop()` we need to save the dataframe in an object for the changes to be permanent

</opt>

</choice> 

</exercise>


<exercise id="11" title="Renaming a Column Index">

Let's rename one of the columns in our `pokemon.csv` data.     
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Rename the column `sp_attack` to `special_a` and `sp_defense` to `special_d` using `df.rename()` only once.
- Save the new dataframe as `pokemon_special`.
- Display the first 5 rows of the dataframe.


<codeblock id="02_11">

- Are you using `pokemon.rename()`?
- Are you saving the new dataframe as the correct name?
- Are you using the argument `columns ={'sp_attack' : 'special_a', 'sp_defense' : 'special_d'}`?

</codeblock>

</exercise>

<exercise id="12" title="Droping Columns in a Dataframe">

Some of the columns in `pokemon.csv` we have deemed not useful. Let's get rid of them! 
    
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Tasks:

- Drop the columns `deck_no`, `capture_rt`, and `legendary`.
- Make sure to overwrite the new dataframe to object `pokemon`.
- Display the first 5 rows of the dataframe.

<codeblock id="02_12">

- Are you using `pokemon.drop()`?
- Are you overwriting the new dataframe to object `pokemon`?
- Are you using square brackets in the argument `columns`?

</codeblock>

</exercise>


<exercise id="13" title="Column Arithmetic and Creation" type="slides">

<slides source="module2_13">
</slides>

</exercise>

<exercise id="14" title=" Column Arithmetic Questions ">

What is the result if we multiply 2 columns together using the syntax 

```
df[['Column_A']] * df[['Column_B']]
```

<choice id="1" >
<opt text='A new column in our dataframe with each column value multiplied together per row.'>

Take care of the syntax being used. Are we using `.assign()` and the correct number of square brackets? 

</opt>

<opt text='A single column with each column value multiplied together per row.'>

You may want to look over this before moving forward.  Are we using the correct number of square brackets? 

</opt>

<opt text='A dataframe with 2 new columns with `NAN` values' correct="true">

Good job!

</opt>

</choice> 

</exercise>



</exercise>

<exercise id="15" title="Creating a New Column">

For this exercise, we are going to create and drop some columns from our dataframe. 
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Create a new column named `total_special` that is the sum of column `sp_attack` and `sp_defense`.
- Save it, overwriting the dataframe named `pokemon`
- Display the first 5 rows of the dataframe.


<codeblock id="02_13">

- Are you using `pokemon.assign()`?
- Are you saving the new dataframes as the correct names?
- For the new column does `total_special  = pokemon['sp_attack'] + pokemon['sp_defense']`?


</codeblock>

</exercise>


<exercise id="16" title="Data Filtering" type="slides">

<slides source="module2_14">
</slides>

</exercise>

<exercise id="17" title="Single Condition Filtering">

Starting the exercises with some straight forward single condition filtering.    
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Create a new dataframe named `fire_pokemon` containing only the rows of `type` "fire".


<codeblock id="02_15">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pokemon['type'] == 'fire'` as your condition?

</codeblock>

Add to the coding cell above code to answer the following question:    
**How many fire Pokemon are there?**
*Hint: Think about how we obtain dataframe row and column size from the previous module*

<choice id="1" >
<opt text='11'>

You can answer this question using <code>fire_pokemon.shape</code>

</opt>

<opt text='52' correct="true">

That's great!  Did you use <code>fire_pokemon.shape</code>?

</opt>

<opt text='776' >

You can answer this question using <code>fire_pokemon.shape</code>

</opt>

</choice> 

</exercise>

<exercise id="18" title='Filtering using "and" or "or"'>

Let's find all the pokemon that meet multiple requirements.  
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Filter the dataframe for the pokemon that have `attack` and `defense` values both greater than 100. 
- Save this dataframe as an object named `mighty_pokemon`.


<codeblock id="02_16">

- Are you sure you are saving your dataframe as the correct object names?
- Are you separating your conditions with brackets?
- Are you using the symbol` & ` to get the intersect?
- Are you using `pokemon['defense'] > 100` and  `pokemon['attack'] > 100` as your conditions?

</codeblock>


Add to the coding cell above code to answer the following question: 
**which `type` has the most Pokemon with attack and defense scores greater than 100?**     
*Hint: Think about how we counted the frequency of categorical columns in module 1*

<choice id="1">
<opt text='Rock and Bug' correct="true">

Well done!

</opt>

<opt text='Water and Rock'>

You can use `mighty_pokemon['type'].value_counts()` to find out.

</opt>

<opt text='Bug and Water' >

You can use `mighty_pokemon['type'].value_counts()` to find out.

</opt>

</choice> 

</exercise>


<exercise id="19" title="Conditional Value Replacement" type="slides">

<slides source="module2_16">
</slides>

</exercise>


<exercise id="20" title='Practice Replacing Values'>

Our pokemon dataset may need some conditional changes. 
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:


<codeblock id="02_17">


</codeblock>

</exercise>


<exercise id="21" title="Function vs. Attributes">

**Question 1**          
Is the following statements is true or false: 
_Chaining removes the need for intermediate objects_


<choice id="1" >
<opt text='True' correct="true>

Good job!

</opt>

<opt text='False'>

You may want to look over this before moving forward.

</opt>
</choice> 


**Question 2**         
Which of the following statements is true?

<choice id="2" >
<opt text='Functions are associated with an object'>

Functions are not associated with any object.

</opt>

<opt text= 'Method are associated with an object' correct="true">

Nice work!

</opt>

<opt text='Functions are a type of method'  correct="true">

The reverse is true; methods are a type of function. 

</opt>

</choice> 

</exercise>


<exercise id="22" title="Practice Chaining">

 Make a plot using our Pokemon dataset and chaining.     
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:

- Chain the following methods in the order specified.
- First, rename the column `capture_rt` to `capture_rate`.
- Create a new column named `AD_total` by adding the `attack` and `defense` columns from the pokemon dataset
- Finally use `.plot.scatter()` to plot `AD_total` on the x-axis and `capture_rate` on the y-axis
- Name the full chain `pokemon_plot`
- Use a new line for each method

<codeblock id="02_20">

- Are you sure you are saving your dataframe as the correct object names?
- Are you using `pd.read_csv()` and `pd.read_excel()` in the correct locations?

</codeblock>

</exercise>

<exercise id="23" title="Grouping and Aggregating" type="slides">

<slides source="module2_21">
</slides>

</exercise>


<exercise id="24" title="Fruit Salad Grouping and Aggregating">

Remember the fruit salad dataframe named `fruit_salad`?  Refer to it for the next two questions.

```out
                 colour    location   seed   shape    sweetness   water-content  weight
        name                        
       apple        red     canada    True   round       True          84         100
      banana     yellow     mexico   False    long       True          75         120
  cantaloupe     orange      spain    True   round       True          90        1360
dragon-fruit    magenta      china    True   round      False          96         600
  elderberry     purple    austria   False   round       True          80           5
         fig     purple     turkey   False    oval      False          78          40
       guava      green     mexico    True    oval       True          83         450
 huckleberry       blue     canada    True   round       True          73           5
        kiwi      brown      china    True   round       True          80          76
       lemon     yellow     mexico   False    oval      False          83          65
```

**Question 1**          
Which code would create a grouby object for the column `shape`? 

<choice id="1" >
<opt text="<code>fruit_salad.get_groups(by='shape')</code>">

Not quite but you are on the right track. 

</opt>

<opt text="<code>fruit_salad.groupby(by='shape')</code>" correct="true">

Great work!

</opt>

<opt text="<code>fruit_salad.group(by='shape')</code>" >

Not quite but you are on the right track. 

</opt>

</choice> 

**Question 2**         
Consider this output made from the `fruit_salad` dataframe:


<center> <img src='module2/question22output.png'  alt="404 image" /></center>

Which of the following code returns the dataframe above. 

<choice id="2" >
<opt text="<code>fruit_salad.groupby(by ='shape').get_group('oval')</code>" correct="true">

Good job!

</opt>

<opt text= "<code>fruit_salad.groupby(by ='shape').get_group['oval']</code>">

Take care of which type of brackets are needed. 

</opt>

<opt text="<code>fruit_salad.get_group(by ='shape').group['oval']</code>">

Are you using the correct verbs?

</opt>

</choice> 

</exercise>

<exercise id="25" title="Practice Grouping">

Find the mean of some Pokemon "types" using `.mean()` and `.groupby()`.

      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_ 

Tasks:

- Make a groupby object on the column `type` and name it `pokemon_type`.
- Make a new dataframe named `type_means` using `.mean()` containing the mean values of each pokemon type.
- Using `.loc[]`, obtain from the `type_means` dataframe, the mean `speed` of the following pokemon types: 
    - `fire` and save it in an object named `fire_mean`
    - `ice` and save it in an object named `ice_mean`
    - `water` and save it in an object named `water_mean`


<codeblock id="02_26">

- Are you grouping by `type`? 
- Are you using `.mean()` on the `pokemon_type` dataframe?
- Are you naming the mean speed objects correctly?
- Are you obtaining the mean values using `.loc[]`?

</codeblock>

</exercise>

<exercise id="27" title="Practice Aggregating">

Let's practice using `.agg()`  
      
**Instructions:**    
Running a coding exercise for the first time, could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Tasks:
- Make a groupby object on the column `legendary` and name it pokemon_type.
- Make a new dataframe named `legendary_stats` using `.agg()` containing the `max` and `min` values of legendary groups.
- Using `.loc[],` obtain from the `legendary_stats` dataframe, the following values:
    - The capture rates (`capture_rt`) for non-legendary (`=0`) pokemon and save them as object `capture_0` 
    - The total base scores (`total_bs`)for legendary (`=1`) pokemon and save them as object `total_1`


<codeblock id="02_24">

- Are selecting the dataframe with `pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]`? 
- Are you grouping by `legendary`? 
- Are you using `.agg()` on the `legendary_stats` dataframe?
- Are you naming the objects correctly?
- Are you obtaining the stats using `.loc[]`?

</codeblock>

</exercise>


<exercise id="28" title="What Did We Just Learn?" type="slides">
<slides source="module2_25">
</slides>
</exercise>
