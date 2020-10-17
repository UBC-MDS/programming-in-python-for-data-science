# Course Syllabus and Learning Outcome 

## Course Learning Outcomes 

1. Define tidy data and explain why it is an optimal format for data analysis.
1. Transform data into the tidy data format using pandas.
1. Demonstrate fundamental programming concepts such as loops and conditionals.
1. Understand the key data structures in Python.
1. Read data into Python data from vanilla (e.g., .csv) and non-standard plain text files, as well as common spreadsheet file types (e.g., .xls).
1. Construct simple plots using pandas.
1. Manipulate a single data table by:   
    7.1 Filtering rows based on a criterion or combination of criteria.   
    7.2 Selecting variables.   
    7.3 Creating new variables and modifying pre-existing ones.   
    7.4 Rearranging the observations or variables by sorting.   
1. Manage and manipulate data with dates and times, missing values and categorical variables as well as renaming dataframe columns.
1. Use the split-apply-combine approach to iterate over and summarize data by groups.
1. Produce human-readable code that incorporates best practices of programming and coding style.


## Modules 

### Module 1: Python & Pandas - an unexpected friendship!

#### Topics 

- Understanding Dataframes 
- Reading in packages, libraries/modules
- Simple table manipulations (selecting) using Pandas
- Saving Dataframes as variables
- Indexing a dataframe using `.iloc[]` and `.loc[]`
- pandas plotting to make a scatter plot
- Obtain simple summary statistics of a dataframe 
- Writing data and saving plots 
- _(In the assignment introduce Jupyter notebooks)_

#### Learning Outcomes 

By the end of the module, students are expected to:

- Describe the components of a Dataframe.
- Read a standard `.csv` file using Pandas [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).
- Load the `pandas` library into Python.
- Demonstrate indexing and slicing with `.loc[]` and `.iloc[]`.
- Demonstrate Selecting columns of a dataframe using `df[]` notation.
- Obtain values from a dataframe using `.loc[]`.
- Sort a dataframe using [`.sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html).
- Create simple summary statistics using [`.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html).
- Construct simple visualizations using [Altair](https://altair-viz.github.io/).
- Create a `.csv` file from a dataframe using [`.to_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html).


### Module 2: Not So Scary Wrangling (Table Manipulation and Chaining)

#### Topics 

- Read different  files using Pandas `pd.read_csv()` and other functions
- Simple dataframe manipulations and operations
- filtering using `df[]`
- Chaining 
- `df.grouby()` and `df.agg()` 
- Modify values in a dataframe using `df.apply()` and `df.applymap()`



#### Learning Outcomes 

By the end of the module, students are expected to:

- Demonstrate how to rename columns of a dataframe using [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html).
- Create new or columns in a dataframe using [`.assign()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html) notation.
- Drop columns in a dataframe using [`.drop()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
- Use `df[]` notation to filter rows of a dataframe.
- Calculate summary statistics on grouped objects using [`.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [`.agg()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html).
- Explain when chaining is appropriate.
- Demonstrate chaining over multiple lines and verbs.


### Module 3: It's Tidy up Time! (Tidy Data)

#### Topics 

- Tidy data - what is it?
- Manipulating data using `df.melt()` and `df.pivot()`
- Dataframe stacking and unstacking 
- Combining dataframes 


#### Learning Outcomes 

By the end of the module, students are expected to:

- Explain what tidy data is.
- Use [`.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) and [`.pivot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html) to reshape dataframes, specifically to make tidy data.
- Learn how to reset a dataframe's index.
- Combine dataframes using [`.merge()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) and [`.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) and know when to use these different methods.
- Understand the different joining methods.


### Module 4: Python without the "eek": Basic Python 

#### Topics 

- Basic datatypes - within a dataframe? 
- Lists and tuples
- String methods
- Dictionaries how to convert them to a dataframe? 

#### Learning Outcomes 

By the end of the module, students are expected to:

- Compare and contrast Python's key data types.
- Compare and contrast Python's key data structures. 
- Use Python to determine the type and structure of an object.
- Demonstrate how to create data structures and convert them to another.
- Identify which operations can be applied to different data types and columns dtypes. 


### Module 5: Loops and Conditions 

#### Topics 

- Dry
- Loops 
- Loops to read in data 
- Nested loops 
- Conditions in loops 
- Intro to functions 


#### Learning Outcomes 

By the end of the module, students are expected to:

- Explain the DRY principle and how it can be useful.
- Write conditional statements with `if`, `elif` and `else` to run different code, depending on the input.
- Write `for` loops to repeatedly run code.
- Describe the expected outcome of code with nested loops.
- Define and use a function that accepts parameters and returns values.


### Module 6:  Functions

#### Topics

- Functions example in plotting, add data to a dataframe?
- Keyword arguments (default)
- Docstrings 
- Unit testing 

#### Learning Outcomes 

By the end of the module, students are expected to:

- Evaluate the readability, complexity and performance of a function.
- Write docstrings for functions following the NumPy/SciPy format.
- Write comments within a function to improve readability.
- Write and design functions with default arguments.
- Explain the importance of scoping and environments in Python as they relate to functions.
- Formulate test cases to prove a function design specification.
- Use `assert` statements to formulate a test case to prove a function design specification.
- Use test-driven development principles to define a function that accepts parameters, returns values and passes all tests.
- Handle errors gracefully via exception handling.


### Module 7: Importing Files and the Coding Style Guide

#### Topics 
- Importing your created functions from a different file
- `pytest`
- Style guides and coding style - black
- Python debugger (PDB) (video in notebook instead with MC question) 

#### Learning Outcomes 

By the end of the module, students are expected to:

- Describe what Python libraries are, as well as explain when and why they are useful.
- Identify where code can be improved concerning variable names, magic numbers, comments and whitespace.
- Write code that is human readable and follows the black style guide.
- Import files from other directories.
- Use [`pytest`](https://docs.pytest.org/en/stable/) to check a function's tests.
- When running [`pytest`](https://docs.pytest.org/en/stable/), explain how pytest finds the associated test functions.
- Explain how the Python debugger can help rectify your code.



### Module 8: Numpy, and Advanced Data Wrangling 

#### Topics 

- (Perhaps - - NumPy arrays, pandas relationship explained from old Module 6) 
- Working with DateTime format 
- Working with strings in dataframes?
- Identifying and handling missing/erroneous values 
- Pandas profiling 


#### Learning Outcomes 

By the end of the module, students are expected to:

- Use [NumPy](https://numpy.org/) to create ndarrays with `np.array()` and from functions such as `np.arrange()`, `np.linspace()` and `np.ones()`.
- Describe the shape, dimension and size of an array.
- Identify null values in a dataframe and manage them by removing them using [`.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) or replacing them using [`.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html).
- Manipulate non-standard date/time formats into standard Pandas datetime using [`pd.to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html).
- Find, and replace text from a dataframe using verbs such as [`.replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html) and [`.contains()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html).  

