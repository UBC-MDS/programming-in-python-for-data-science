# Course Syllabus and Learning Outcome 

## Course Learning Outcomes 

1. Define tidy data and explain why it is an optimal format for data analysis.
1. Transform data into the tidy data format using pandas.
1. Demonstrate fundamental programming concepts such as loops and conditionals.
1. Understand the key data structures in Python.
1. Read data into Python data from vanilla (e.g., .csv) and non-standard plain text files, as well as common spreadsheet file types (e.g., .xls).
1. Construct simple plots using pandas
1. Manipulate a single data table by:
    6.1 Filtering rows based on a criterion or combination of criteria
    6.2 Selecting variables
    6.3 Creating new variables and modifying pre-existing ones
    6.4 Rearranging the observations or variables by sorting.
1. Manage and manipulate data with dates and times, missing values and categorical variables as well as renaming dataframe columns.
1. Use the split-apply-combine approach to iterate over and summarize data by groups.
1. Produce human-readable code that incorporates best practices of programming and coding style.


## Modules 

### Module 1: Python & Pandas - an unexpected friendship!

#### Topics 

- Understanding Dataframes 
- Reading in packages, libraries/modules
- Simple table manipulations (selecting, filtering) using Pandas.
- Saving Dataframes as variables
- pandas plotting to make a scatter plot
- Obtain simple summary statistics of a dataframe. 
- _(In the assignment introduce Jupyter notebooks)_

#### Learning Outcomes 
By the end of the module, students are expected to:
- Describe the components of a Dataframe.
- Read a standard .csv file using Pandas `pd.read_csv()`.
- Explain modules and import libraries.
- Demonstrate indexing and slicing with `df.loc[]` and `df.iloc[]`.
- Demonstrate Selecting and filtering columns of a dataframe using `df[]` notation.
- Create simple summary statistics using `pd.describe()` and `pd.summary()`.
- construct simple visualizations using pandas.


### Module 2: Python without the "eek": Basic Python 
_Note: This module can be pushed to the end of the wrangling material but I wanted to discuss why I think we should introduce datatypes earlier_

#### Topics 

- Basic datatypes - within a dataframe? 
- Lists and tuples
- String methods
- Dictionaries how to convert them to a dataframe? 
- Conditionals also how this can be mapped to apply? 

#### Learning Outcomes 

- Compare and contrast python's key data types.
- Compare and contrast python's key data structures. 
- Use python to determine the type and structure of an object 
- Write conditional statements with `if`, `elif` and `else` to run different code depending on the input
- Demonstrate how to create data structures and convert them to another.
- Describe what python packages/libraries are, as well as explain when and why they are useful


### Module 3: Not So Scary Wrangling (Table Manipulation and Chaining)

#### Topics 

- Read different `.csv` files using Pandas `pd.read_csv()`
- Review wrangling, practice creation of plots
- Indexing a dataframe using `[]`, `[[]]`, `.iloc[]`, `.loc[]`.
- Simple dataframe manipulations and operations
- filtering recap using `df[]` and introduce `df.query()` notation
- Dataframe reshaping
- Modify values in a dataframe using `df.apply()` and `df.applymap()`
- Chaining 
- Writing data and saving plots 

#### Learning Outcomes 

By the end of the module, students are expected to:
- Demonstrate how to rename columns of a dataframe using df.rename().
- Sort a dataframe using df.sort_values()`.
- Use different methods of indexting dataframes and predict the datatypes that will result. 
- Use `df[]` and `df.query()` notation to filter rows of a dataframe.
- Create new rows or columns in a dataframe using `df[]` notation.
- Use pandas to modify values in a dataframe using `df.apply()` and `df.applymap()`.
- Demonstrate chaining over multiple lines.
- create a `.csv` file from a dataframe using `df.to_csv()`.


### Module 4: It's Tidy up time! (Time and Tidy Data)

#### Topics 

- `df.grouby()` and `df.agg()` 
- Tidy data - what is it?
- Manipulating data using `df.melt()` and `df.pivot()`
- Working with datetime format 
- Pandas profiling 

#### Learning Outcomes 

- Perform aggregating methods on grouped or ungrouped objects such as finding the minimum, maximum and sum of values in a dataframe using df.agg().
- Explain what tidy data is
- Use `df.melt() `and `df.pivot() `to reshape dataframes, specifically to make tidy data
- Manipulate non-standard date/time formats into standard Pandas datetime using `pd.to_datetime()`.

### Module 5: Marriage & the Whole Package: (Missing Values and joining Dataframes)

#### Topics 

 -Identifying and handling missing/erroneous values 
- Working with strings in dataframes 
- Dataframe stacking and unstacking 
- Combining dataframes 

#### Learning Outcomes 

- Identify missing and erroneous values in a dataframe and manage them by removing (using `df.dropna()`) or replacing (`df.fillna()`).
- Find, replace and extract text from a Series or dataframe using methods such as `df.replace()` with regular expressions.
- Use stacking and unstacking operations to reshape a dataframe.
- Combine dataframes using `df.merge()` and `pd.concat()` and know when to use these different methods.

### Module 6:  Fruit Loops and Function: Loops & Functions 

#### Topics 

- Loops 
- Functions example in plotting, add data to a dataframe ?
- DRY principle 
- Keyword arguments 
- Docstrings 
- Unit tests, corner cases
- Multiple return values 

#### Learning Outcomes 

- Write for loops to repeatedly run code
- Evaluate the readability, complexity and performance of a function
- Explain what the DRY principle is
- Define and use a named function that accepts parameters and returns values
- Use `assert` statements to formulate a test case to prove a function design specification
- Use test-driven development principles to define a function that accepts parameters, returns values and passes all tests
- Handle errors gracefully via exception handling
- Write Docstrings for functions following the NumPy/SciPy format
- Write comments within a function to improve readability
- Source and use functions stored as python code in another file, as well as those in


### Module 7: A Slice of Numpy (Numpy Arrays)

#### Topics 

- Numpy arrays 
- Numpy array dimensions  
- Numpy indexing and slicing 
- Explain broadcasting 
- Compare arrays with pandas series and dataframes

#### Learning Outcomes 

- Explain what broadcasting is and how to use it  (Mikes L3+ Tom's L1)
- Use NumPy to create ndarrays from existing data with `np.array()` and from functions such as `np.arange()`, `np.linspace()` and `np.full()`
- Describe resulting array shapes from operations  
- Access values from a numpy ndarray by indexing and slicing.
- Compare and contrast np.ndarray, pd.Series and pd.DataFrame objects in Python.
- Convert between a NumPy ndarray, Pandas Series, & Pandas DataFrame.

### Module 8: Vogue Code the Style Guide (Readable code and libraries)

_Things to add here? Definitely my weekest module!_ 

#### Topics 

- Python import
- Importing your own functions
- Style guides and coding style 
- Python debugger (pdb)

#### Learning Outcomes 

- Demonstrate how to import classes and functions for different python libraries
- Source and use functions stored as python code in another file
- Describe what python libraries are, as well as explain when and why they are useful
- Identify where code can be improved concerning variable names, magic numbers, comments and whitespace
- Write code that is human readable and follows the pep8 style guide.
- Explain how the python debugger can help rectify your code. 
