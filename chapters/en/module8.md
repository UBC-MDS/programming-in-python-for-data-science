---
title: 'Module 8: A Slice of NumPy and Advanced Data Wrangling'
description:
  'In this module, you will learn about NumPy arrays and more advanced wrangling techniques such as handling columns with dates and strings and identifying null values.'
prev: /module7
next: /module9
type: chapter
id: 8
---



<exercise id="0" title="Module Learning Outcomes" type="slides, video">

<slides source="module8/module8_00" shot='1' start="1:16" end="3:01">
</slides>

</exercise> 

<exercise id="1" title="NumPy and 1D Arrays" type="slides">

<slides source="module8/module8_01">
</slides>

</exercise>


<exercise id="2" title="NumPy and Array Questions">

**Question 1**      


Which of the following statements is correct? 


<choice id="1" >
<opt text="Pandas is built using NumPy"  correct="true">

Nice!

</opt>

<opt text="NumPy is built using pandas">

NumPy arrays are the building blocks of Pandas dataframes

</opt>

</choice> 

**Question 2**          

Which of the following statements is ***False*** ? 


<choice id="2" >
<opt text="NumPy arrays can be multi-dimensional">

This is very much true and a very helpful feature. 

</opt>

<opt text="NumPy contains constants and mathematical functions">

This is another benefit of NumPy as it contains multiple other functions and constants 

</opt>

<opt text="NumPy arrays can contain multiple data types"  correct="true">

NumPy arrays must have elements with a homogenous data type. 

</opt>

<opt text="<code>numpy.ndarray</code> is a data type">

We saw that `array` is a data type in the slides.  

</opt>

</choice>  


**Question 3**      


Which verbs would I use to make the following array? 

```python
array([ 0, 5, 10, 15, 20, 25, 30])
```


<choice id="3" >
<opt text="<code>np.linspace(0, 30, 5)</code>"  >
This would only produce 5 values (all equally spaced from 0 to 30)

</opt>

<opt text="<code>np.zeros(7)</code>" >
This gives an array with only `0` elements. 

</opt>


<opt text="<code>np.ones(7)</code>">

This gives an array with only `1` elements. 

</opt>


<opt text="<code>np.arange(0, 35, 5)</code>" correct="true" >

Great!

</opt>

</choice> 

</exercise>

<exercise id="3" title="More NumPy">

Look at the <a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy documentation</a> and identify  which of the following is **not** an existing NumPy function? 

<choice id="1" >
<opt text="<code>np.degrees()</code>"  >
Are you looking at the <a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy documentation</a>?

</opt>

<opt text="<code>np.cross()</code>" >
Are you looking at the <a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy documentation</a>?

</opt>


<opt text="<code>np.interp()</code>">

Are you looking at the <a href="https://numpy.org/doc/stable/reference/routines.math.html" target="_blank">NumPy documentation</a>?

</opt>


<opt text="<code>np.reticulate()</code>" correct="true" >

Great!

</opt>

</choice> 

</exercise>


<exercise id="4" title= "NumPy Practice">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's explore how Python compares lists and arrays. 

Tasks:
- Create 2 lists of the same length and save each as objects named  `a_list` and `b_list`.
- Using Boolean operators, what is outputted when you test to see if they are equal? 



<codeblock id="08_04a">

- Are you using `[]` or `list()` notation?
- Are you using `==` to check if the lists are equal?

</codeblock>


<choice id="1" >
<opt text="A single Boolean (Either <code> True</code> or <code>False</code>)"  correct="true" >

This is checking if the lists are equal. 

</opt>

<opt text="A list containing a Boolean value for each pair of elements" >

Use the cell above to help yourself out. 

</opt>

</choice> 


Now let's do the same exercises using arrays.

Tasks:
- - Create 2 lists of the same length and save each as objects named `a_array` and `b_array`. 
- Using Boolean operators, what is outputted when you test to see if they are equal? 



<codeblock id="08_04b">

- Are you using `np.array()` with parentheses to make your arrays?
- Are you using `==` to check if the lists are equal?

</codeblock>


<choice id="2" >
<opt text="A single Boolean (Either <code> True</code> or <code>False</code>)"   >

Use the cell above to help yourself out. 

</opt>

<opt text="An array containing a Boolean value for each pair of elements" correct="true">

NumPy performs the operation element-wise and compares the elements that share the same index location. 

</opt>

</choice> 


This is an example of how useful arrays can be when doing numerical computation! To compare each element in a list would take more code and time for the same result. 

</exercise>


<exercise id="5" title="Multi-dimensional Arrays" type="slides">

<slides source="module8/module8_05">
</slides>

</exercise>


<exercise id="6" title="Make that Array">


**Question 1**  

Given this code, what array would be outputted? 

```python
np.ones((4, 3))
```


<choice id="1" >
<opt text="<code>array([[1., 1., 1.], <br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;  [1., 1., 1.], <br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1., 1.], <br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1., 1.]])</code>"  correct="true">

Nice work!

</opt>

<opt text="<code>array([[1., 1., 1., 1.],<br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1., 1., 1.],<br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1., 1., 1.]])</code>" >

Remember that the number of rows precedes the number of columns. 

</opt>


<opt text="<code>array([[1., 1.],<br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1.],<br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1.]])</code>">

When we make arrays, it's not like slicing where we exclude the last value. 

</opt>


<opt text="<code>array([[1., 1., 1.],<br>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; [1., 1., 1.]])</code>"  >

When we make arrays, it's not like slicing where we exclude the last value. 

</opt>


</choice> 


</exercise>


<exercise id="7" title="Shape, Size, and Dimension">

**Question 1**      


What is the shape of the following array?

```python
array([[ 0,  1,  2,  3,  4,  5,  6,  7],
       [ 8,  9, 10, 11, 12, 13, 14, 15]])

```

<choice id="1" >
<opt text="<code>(7, 2)</code>"  >

Are you getting your columns and rows mixed up?

</opt>

<opt text="<code>(2, 7)</code>" >

Are you counting the number of columns correctly?

</opt>


<opt text="<code>(8, 2)</code>">

Remember the number of rows precedes the number of columns. 

</opt>


<opt text="<code>(2, 8)</code>"  correct="true">

Great!

</opt>

</choice> 


**Question 2**         


```python
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9]],

       [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],

       [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]])
```

Given the above array, which code would result in the given output below?  

```out
30
```

<choice id="2" >
<opt text="<code>.size</code>" correct="true">


</opt>

<opt text="<code>.ndim</code>" >
This gives the dimension of the array, which would be 3, not 30. 

</opt>


<opt text="<code>.prod</code>">

This would result in an error.

</opt>


<opt text="<code>.size()" >

Since these are attributes, there is no need for the parentheses. 

</opt>

</choice> 


**Question 3**  

Give an array with `shape` of `(2,3,4,2)`, What is it's `.ndim`? 

<choice id="3" >
<opt text="2"  >

The values in the tuple do not answer this question.  

</opt>

<opt text="3" >

The values in the tuple do not answer this question.  

</opt>

<opt text="4" correct="true">

Bingo! You count the length of the tuple to find the dimension. 

</opt>


<opt text="5" >

What is the length of the tuple? 

</opt>


</choice> 

</exercise>

<exercise id="8" title="More Arrays Questions">

Use the following array named `hurray` to answer the next set of questions.
```python
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14],
       [15, 16, 17]])
```

**Question 1**  


Which code would I use to obtain the following output? 

```python
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```

<choice id="2" >
<opt text="<code>hurray[:3]</code>"  correct="true">

Nice!

</opt>

<opt text="<code>hurray[,:3])</code>" >

You are slicing columns when you should be slicing rows. 

</opt>


<opt text="<code>hurray[,:2])</code>">

You are slicing columns when you should be slicing rows.  

</opt>


<opt text="<code>hurray[:2])</code>">

Remember the last index is excluded. 

</opt>

</choice> 



**Question 2**          

Which code would result in the following output? 

```python
array([[10, 11],
       [13, 14]])
```


<choice id="3" >
<opt text="<code>hurray[3:4, 1:]</code>"  >

Remember that the last element is excluded from the selection. 

</opt>

<opt text="<code>hurray[2:4, 1:]</code>" >

Remember the first index value is included and the last value is excluded. 

</opt>


<opt text="<code>hurray[1:, 3:5]</code>">

Remember the number of rows precedes the number of columns. 

</opt>


<opt text="<code>hurray[3:5, 1:]</code>"  correct="true">

Great!

</opt>

</choice> 


**Question 3**      


Which code would I use to obtain the following output? 

```python
array([[ 0,  3,  6,  9, 12, 15],
       [ 1,  4,  7, 10, 13, 16],
       [ 2,  5,  8, 11, 14, 17]])
```

<choice id="3" >
<opt text="<code>hurray.t</code>"  >

Uppercase and lowercase characters are not considered equal in Python.

</opt>

<opt text="<code>hurray.T</code>" correct="true">

Nice work!

</opt>


<opt text="<code>np.T(hurray)</code>">

`np.T` is not a valid function.

</opt>


<opt text="<code>hurray.T()</code>"  >

Transposing does not require any parentheses. 

</opt>

</choice> 

</exercise>


<exercise id="9" title= "Making an Array">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's make an array and find its size and dimension. 

Tasks:
- Create an array named `arr1` that contains only elements with values 1 and a shape of (3,5).
- Save the dimension and size of `arr1` in objects named `arr1_dim` and `arr1_size` respectively. 



<codeblock id="08_09">

- Are you using `.ones((3,5))`?
- Are you using `.ndim` and `.size`?
- Are you saving your objects as the correct names?

</codeblock>

</exercise>



<exercise id="10" title= "Array Practice ">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's make a new array and transform it by slicing and transposing.

Tasks:
- Create an array named `arr2` using `np.linspace()` with 6 equally spaced values from 1 to 16 and a shape of (2,3).  (you'll need `.reshape()` for this!)
- Transpose the array and name it `arr2t`.
- Finally, slice it so it only includes the values 7 and 16. Save this as an object named `sliced_arr2t`.



<codeblock id="08_10">

- Are you using `.reshape()` to change the dimension of np.linspace()?
- Are you using `.T`?
- Are you slicing with `[:,1]`?

</codeblock>

</exercise>


<exercise id="11" title="Working with Null Values" type="slides">

<slides source="module8/module8_11">
</slides>

</exercise>


<exercise id="12" title="Finding and Dropping Null Values Questions">

**Question 1**    

You run `.info()` on the `fruit_salad` dataframe and get the following output.

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 8 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   name           10 non-null     object 
 1   colour         10 non-null     object 
 2   location       10 non-null     object 
 3   seed           10 non-null     bool   
 4   shape          9 non-null      object 
 5   sweetness      10 non-null     bool   
 6   water_content  8 non-null      float64
 7   weight         10 non-null     int64  
dtypes: bool(2), float64(1), int64(1), object(4)
memory usage: 628.0+ bytes
```



Which of the columns contain null values?
*Hint: There could be more than one.*



<choice id="1" >
<opt text="<code>name</code>"  >

This column has all of its 10 rows with non-null values. 

</opt>

<opt text="<code>location</code>" >

This column has all of its 10 rows with non-null values. 

</opt>


<opt text="<code>shape</code>" correct="true">

Of the 10 rows (entries) only 9 have non-null values meaning this column contains a null value. Are there any others?

</opt>


<opt text="<code>water_content</code>" correct="true">

Of the 10 rows (entries) only 8 have non-null values meaning this column contains a null value. Are there any others?

</opt>

<opt text="<code>weight</code>">

This column has all of its 10 rows with non-null values. 

</opt>


</choice> 

**Question 2**   


```out
     name  height  diameter   age flowering
0  Cherry    15.0         2  12.0      True
1     Fir    20.0         4   4.0     False
2  Willow    25.0         3   2.0      True
3     Oak     NaN         2   NaN     False
4     Oak    10.0         5   6.0       NaN
```

Given the dataframe named `forest`, what code would you use to remove only the rows missing from the `age` column?  


<choice id="2" >
<opt text="<code>forest.drop(columns=['age'])</code>"  >

This is just dropping the entire `age` column!

</opt>

<opt text="<code>pd.dropna(forest['age'])</code>" >

`.dropna()` is not called in this manner. 

</opt>


<opt text="<code>pd.dropna(columns=['age'])</code>">

Are you using the correct argument?

</opt>


<opt text="<code>forest.dropna(subset=['age'])</code>" correct="true">

Nice!

</opt>

</choice>  

</exercise>

<exercise id="13" title="Filling Methods">

Use the `forest` dataframe below to answer the next 2 questions: 

```out
     name  height  diameter   age flowering
0  Cherry    15.0         2  12.0      True
1     Fir    20.0         4   4.0     False
2  Willow    25.0         3   2.0      True
3     Oak     NaN         2   3.0     False
4     Oak    10.0         5   6.0     False
```


**Question 1**      


Which code will replace the `NaN` value in the `height` column so the new dataframe looks like the one below?


```out
     name  height  diameter  age  flowering
0  Cherry    15.0         2   12       True
1     Fir    20.0         4    4      False
2  Willow    25.0         3    2       True
3     Oak    17.5         2    3      False
4     Oak    10.0         5    6      False
```


<choice id="1" >
<opt text="<code>forest.fillna(value = forest['height'].mean())</code>"  correct="true">

Great!

</opt>

<opt text="<code>forest.fillna(value = forest['height'].max())</code>" >

The max value in the `height` column is `25`, not `17.5`. 

</opt>


<opt text="<code>forest.fillna(method = 'bfill')</code>">

This value isn't an option in the dataframe and would not be possible with `bfill`. 

</opt>


<opt text="<code>forest.fillna(method = 'ffill')</code>" >

This value isn't an option in the dataframe and would not be possible with `ffill`. 

</opt>

</choice>  

**Question 2**          

Which code will replace the `NaN` value in the `height` column so the new dataframe looks like the one below?

```out
     name  height  diameter  age  flowering
0  Cherry    15.0         2   12       True
1     Fir    20.0         4    4      False
2  Willow    25.0         3    2       True
3     Oak    10.0         2    3      False
4     Oak    10.0         5    6      False
```


<choice id="2" >
<opt text="<code>forest.fillna(value = 13)">

The `NaN` value is being filled with a value of 10, not 13. 

</opt>

<opt text="<code>forest.fillna(value = forest['height'].max())</code>" >

The max value in the `height` column is `25`, not `10`. 

</opt>


<opt text="<code>forest.fillna(method = 'bfill')</code>" correct="true">

Perfect! 

</opt>

<opt text="<code>forest.fillna(method = 'ffill')</code>" >

`ffill` has the `NaN` value adopt the same value and the row that precedes it. 

</opt>

</choice>  

</exercise>


<exercise id="14" title= "Practice Filling Null Values">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's replace the values missing in the `canucks` dataframe with the salary mean.

Tasks:
- Replace the `NaN` values in the dataframe with the mean salary value. 
- Save this as a new dataframe named `canucks_altered`.
- Display the `canucks_altered` dataframe.

<codeblock id="08_14">

- Are you using `.fillna()`?
- Are you using the argument `value=canucks['Salary].mean()`?

</codeblock>

</exercise>


<exercise id="15" title= "Practice Identifying Null Values">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's practice using `.isnull()` in our data processing using the `canucks` dataset from earlier in this course.

Tasks:
- Identify any columns with null values in the `canucks` dataframe with `.info()` and save this as `canucks_info`.
- Create a new column in the dataframe named `Wealth` where all the values equal `"comfortable"`. 
- Name the new dataframe `canucks_comf`.
- Do conditional value replacement, where if the value in the `Salary` column is null, we replace `"comfortable"` with `"unknown"`.
- Display the new `canucks_comf` dataframe.

<codeblock id="08_15">

- Are you using `canucks.info()`?
- Are you creating `canucks_comf` with `canucks.assign(Wealth = "comfortable")`?
- Are you using `.loc[]` to replace the values in the `Wealth` column?
- Are you using `canucks_comf['Salary'].isnull()` as your condition in `.loc[]`?

</codeblock>

</exercise>


<exercise id="16" title="Working with Dates and Time" type="slides">

<slides source="module8/module8_16">
</slides>

</exercise>


<exercise id="17" title="Datetime Questions">

**Question 1**      

Which of the following dtypes measures an interval of time? 


<choice id="1" >
<opt text="Timestamp"  >

This is a snapshot in time. 

</opt>

<opt text="timedelta" correct="true">

Great work!

</opt>


<opt text="datetime">

This is a dtype not a measurement

</opt>


</choice> 

**Question 2**          

What code would you use to create a column with the name of the month from a datetime column?


<choice id="2" >
<opt text="<code>ts.month</code>" >

This will produce a numerical value, not the month name. 

</opt>

<opt text="<code>.month</code>">

This will produce a numerical value for a single Timestamp instead of a column. 

</opt>

<opt text="<code>ts.month_name()</code>" correct="true">

You got it!

</opt>

<opt text="<code>ts.month_name</code>">

So close, but in this case, we need parentheses. 

</opt>

</choice>  


**Question 3**      


Which verb do we use to find the time interval between rows?


<choice id="3" >
<opt text="<code>.diff()</code>" correct="true">

Way to go!

</opt>

<opt text="<code>.difference()</code>">

Not quite. 

</opt>

<opt text="<code>differ()</code>" >

This isn't the function we are looking for. 

</opt>

<opt text="<code>.differ</code>">

Maybe, review the notes a bit more before proceeding. 


</opt>

</choice> 

</exercise>



<exercise id="18" title= "Practice Processing Dates">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Use the output of the following code chunk to help answer the next question.

<codeblock id="hockey_players">

</codeblock>


Let's read in data and parse a datetime column as well as calculate the hockey team's oldest and youngest player. 

Tasks:
- Read in the `canucks.csv` file from the data folder and parse the `Birth Date` column. Save this as an object named `canucks`.
- Find the oldest player (going by their date of birth) and save the Timestamp as `oldest`. 
- Find the youngest player (going by their date of birth) and save the Timestamp as `youngest`.
- Find the age difference between the two players in years to 2 decimal places. Save this as an object name `age_range`. 
- Display `age_range`.


<codeblock id="08_18">

- Are you using the argument `parse_dates` while reading in the data?
- The oldest player has the `min()` date of birth.
- The youngest player has the `max()` date of birth.
- Are you subtracting the min value from the max value?
- Are you rounding to 2 decimal places? 

</codeblock>

</exercise>

<exercise id="19" title="Introduction to Working with Strings" type="slides">

<slides source="module8/module8_19">
</slides>

</exercise>


<exercise id="20" title="String Questions">

**Question 1**      

What must we add to our string functions when processing columns of dtype `object`? 


<choice id="1" >
<opt text="<code>.ts</code>"  >

We use this for functions that work with time stamps

</opt>

<opt text="<code>.str</code>" correct="true">

Great work!

</opt>


<opt text="<code>.st</code>">

this is not quite right

</opt>


</choice> 

**Question 2**          

Which function will remove leading or trailing characters from a string? 


<choice id="2" >
<opt text="<code>.split()</code>" >

This will produce a numerical value, not the month name. 

</opt>

<opt text="<code>.strip()</code>" correct="true">

Nice!

</opt>

<opt text="<code>.string()</code>">

This isn't a possible method.

</opt>

<opt text="<code>.rstrip()</code>">

This function removes the trailing character specified in the argument.  

</opt>

</choice>  

</exercise>

<exercise id="21" title="Identify the String Code">  


```out
           name   colour location   seed  shape  sweetness  water_content  weight
0         apple      red   canada   True  round       True             84     100
1        banana   yellow   mexico  False   long       True             75     120
2    cantaloupe   orange    spain   True  round       True             90    1360
3  dragon-fruit  magenta    china   True  round      False             96     600
4    elderberry   purple  austria  False  round       True             80       5
5           fig   purple   turkey  False   oval      False             78      40
6         guava    green   mexico   True   oval       True             83     450
7   huckleberry     blue   canada   True  round       True             73       5
8          kiwi    brown    china   True  round       True             80      76
9         lemon   yellow   mexico  False   oval      False             83      65

```


Given the dataframe above named `fruit_salad`,  which code would produce the following output?     
*Hint: Look at the `location` column*


<center><img src='/module8/output.png' width="80%"></center>

<br>

<choice id="1" >
<opt text="<code>fruit_salad.assign(location=fruit_salad['location'].str.capitalize())</code>" correct="true">

Way to go!

</opt>

<opt text="<code>fruit_salad.assign(location=fruit_salad['location'].capitalize())</code>">

This would result in an error. 

</opt>

<opt text="<code>fruit_salad.assign(location=fruit_salad['shape'].str.upper())</code>" >

The `shape` column doesn't look uppercase to me. 

</opt>

<opt text="<code>fruit_salad.assign(location=fruit_salad['shape'].upper()</code>">

You seem to be missing an important part of you code. 


</opt>

</choice> 

</exercise>



<exercise id="22" title= "Practice Handling Strings">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Use the output of the following code chunk to help answer the next question.

<codeblock id="hockey_players">

</codeblock>


Let's transform some of the columns in your canucks dataset. Let's also see how many of the players have multiple `T`'s in their name. 

Tasks:
- Convert the `Position` and `Country` columns into uppercase and save this in a dataframe named `canucks_upper`.
- Create a new column in the `canucks_upper` dataframe named `number_ts` where you count the total number of times the letter T (lowercase or uppercase) appears in their name.
- Save this dataframe named as `canucks_upper_ts`.
- How many players have multiple T's in their name? 


<codeblock id="08_22">

- Are you using `.assign` and `.upper()`?
- You will have to convert the lower to `.lower()` first and then `.count('t')`
- The number of players with `number_ts` greater than two can be calculated by filtering on that column and getting the `.shape` of the dataframe.

</codeblock>


How many players have the letter "T" in their name more than once?

<choice id="1" >

<opt text="3"   >

There are more than that! Are you using `.shape[0]`? 

</opt>

<opt text="5" >

This is not right. Maybe check that you are counting both upper and lower cases of "T".

</opt>

<opt text="6" correct="True">

Great!

</opt>

<opt text="7" >

Are you filtering the dataset correctly?

</opt>

</choice> 

</exercise>


<exercise id="23" title="More Advanced String Processing" type="slides">

<slides source="module8/module8_23">
</slides>

</exercise>


<exercise id="24" title="Advanced String Questions">

**Question 1**      

Which of the following would you use to replace string patterns with another string within a dataframe column?

<choice id="1" >
<opt text="<code>.replace()</code>" >

Way to go!

</opt>

<opt text="<code>str.replace()</code>" correct="true">

This would result in an error. 

</opt>

<opt text="<code>.contains()</code>" >

This checks if a substring is contained in a larger string.

</opt>

<opt text="<code>.str.contains()</code>">

Unfortunately this is not the right verb in this case. 


</opt>

</choice> 

**Question 2**          

Is the following statement True or False?

*The `.contains()` verb will output a new dataframe that matches any values in a specific column and replaces it with your desired value.* 


<choice id="2" >

<opt text="True" >

`.contains()` actually will output a Boolean Series based on whether a given pattern is contained within a string of a Series.

</opt>

<opt text="False" correct="true">

Great! You knew that it outputs a Boolean Series! The value replacement is using `.loc[]`. 

</opt>

</choice>  

</exercise>


<exercise id="25" title="Strings">


```out
           name   colour location   seed  shape  sweetness  water_content  weight
0         apple      red   canada   True  round       True             84     100
1        banana   yellow   mexico  False   long       True             75     120
2    cantaloupe   orange    spain   True  round       True             90    1360
3  dragon-fruit  magenta    china   True  round      False             96     600
4    elderberry   purple  austria  False  round       True             80       5
5           fig   purple   turkey  False   oval      False             78      40
6         guava    green   mexico   True   oval       True             83     450
7   huckleberry     blue   canada   True  round       True             73       5
8          kiwi    brown    china   True  round       True             80      76
9         lemon   yellow   mexico  False   oval      False             83      65

```


Given the dataframe above named `fruit_salad`,  which code would produce the following dataframe with the new column `berry`?  

```out
           name   colour location   seed  shape  sweetness  water_content  weight   berry
0         apple      red   canada   True  round       True             84     100   False
1        banana   yellow   mexico  False   long       True             75     120   False
2    cantaloupe   orange    spain   True  round       True             90    1360   False 
3  dragon-fruit  magenta    china   True  round      False             96     600   False
4    elderberry   purple  austria  False  round       True             80       5    True
5           fig   purple   turkey  False   oval      False             78      40   False
6         guava    green   mexico   True   oval       True             83     450   False 
7   huckleberry     blue   canada   True  round       True             73       5    True
8          kiwi    brown    china   True  round       True             80      76   False
9         lemon   yellow   mexico  False   oval      False             83      65   False

```

<choice id="1" >
<opt text="<code>fruit_salad.assign(name = fruit_salad['name'].contains('berry'))</code>">

This doesn't contain the necessary `str.` and it appears to edit the `name` column.


</opt>

<opt text="<code>fruit_salad.assign(name = fruit_salad['name'].str.contains('berry').replace(True))</code>">

Not the correct way of making a new column. 

</opt>

<opt text="<code>fruit_salad.assign(berry = fruit_salad['name'].str.replace('berry', True))</code>" >

This is not the correct syntax for this output. 

</opt>

<opt text="<code>fruit_salad.assign(berry = fruit_salad['name'].str.contains('berry'))</code>"  correct="true">

Nice work. 


</opt>

</choice> 

</exercise>


<exercise id="26" title= "Processing Strings in a Dataframe">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load. Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Use the `lego` dataframe to help answer the next question.

<codeblock id="lego_sets">

</codeblock>


Let's practice using the verbs we learned from the lesson to process a string column in our Lego dataset. 

Tasks:
- Convert the `name` column in the `lego` dataset to lowercase and overwrite the dataframe by saving it as an object named `lego`.
- Filter the dataset to find all the Lego sets that contain `"weetabix"` in the `name` column.
- Save this as an object named `lego_weetabix`.
- Replace the word` "weetabix`" in the `name` column of the `lego_wetabix` dataframe with the string `"cereal-brand"`.
- Save this in an object called `lego_cereal`.
- If the row contains the word `"promotional"` in the `name` column, change the entire value to `"cereal-brand freebie"`.
- Display `lego_cereal`.


<codeblock id="08_26">

- Are you using `.assign()` and `.lower()` to convert the name column to lowercase?
- Are you using `str.contains('weetabix')` to filter all the rows? 
- You should be using `assign()` with `str.replace('weetabix', 'cereal-brand')` to replace "weetabix".
- You should be using  `.loc[]` and `str.contains('promotional')` (and a single `=`) to assign new row values. 

</codeblock>

</exercise>

<exercise id="27" title="What Did We Just Learn?" type="slides, video">
<slides source="module8/module8_end" start="0:165" end="3:01">>
</slides>
</exercise>
