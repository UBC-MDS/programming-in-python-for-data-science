<exercise id="12" title="Hierarchical Indexing" type="slides">

<slides source="module3/module3_12">

</slides>

</exercise>


<exercise id="13" title="Hierarchical Indexing Questions">

**Question 1**          
Which of the following is used to sort values by a dataframe's index? 


<choice id="1" >
<opt text="<code>.sort_index()</code>"  correct="true" >

Great work! 

</opt>

<opt text="<code>.sort_values()</code>">

This is used to sort columns.  Index values are not recognized as a typical column. 

</opt>

<opt text="<code>.index_sort()</code>">

You are on the right track but I think you may have it reversed!

</opt>

<opt text="<code>.sort()</code>">

It may be a good idea to look over the last section again. 

</opt>

</choice> 


**Question 2**      
Is the following `fruit_salad` dataframe stacked or unstacked?

<center> <img src='/module3/hi_fruit.png'  alt="404 image" /></center>


<choice id="2" >
<opt text='Stacked' correct="true">

Nice!  The columns are stacked on top of each other.  

</opt>

<opt text= 'Unstacked'>

Do you notice anything interesting about the third column? 

</opt>

</choice> 

</exercise>
 
<exercise id="14" title="Hierarchical Indexing slicing">

It’s time for dessert!  Bring in the dataset `fruit_salad`. 

```out
                           location   seed   shape    sweetness   water-content  weight
        name      colour                    
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

It appears that there are 2 indexes this time around `name` ***and*** `colour`!  How would you select the `guava` row now? 

<choice id="1" >

<opt text= "<code>fruit_salad.loc[['guava, 'green']]</code>">

hmmm, something seems a little off with your parentheses.  Are you sure they are all the right type? 

</opt>

<opt text= "<code>fruit_salad.loc['guava]</code>">

Good job!  Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

<opt text= "<code>fruit_salad.loc[('guava, 'green')]</code>"  correct="true">

Nice work!  You definitely paid attention!

</opt>

<opt text= "<code>fruit_salad[('guava, 'green')]</code>">

I think you are missing a verb in your sentence!  

</opt>

</choice> 

</exercise>


<exercise id="15" title="Setting Multiple Indexes">
   

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's start simple.  Set multiple indexes for one of our Lego dataframes. 


Tasks:
- Create hierarchical indexes from the columns `set_num` and `name`.
- Name the new dataframe `lego_build`.


<codeblock id="03_15">
- Are you using the verb `.set_index()`?
- Are you wrapping the column days with square brackets?

</codeblock>

</exercise>

<exercise id="16" title="Applying Stacking">
      

      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

Let's find the minimum and the maximum number of pieces per set there are in each Lego theme. 

Tasks:
- From the `lego` dataframe, make groups from the `theme_name` columns.
- Find the max and min values for the `num_parts` column only using `.agg()`.
- Stack the max and min values using `.stack()`.
- Name the new dataframe `stacked_lego`.


<codeblock id="03_16">
- Are you using the verb `.groupby()` with the correct column named `theme_name`?
- Are you using `.arg()` where you can designate different statistics to different columns to obtain only the `num_parts` column?
- Are you remembering to `.stack()`?

</codeblock>

</exercise>