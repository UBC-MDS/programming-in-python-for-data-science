---
type: slides
---

# Summary Statistics!

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

Now we've learned about how to get our dataframe how we want it, let's try and get some fun out of it!

We have our data, now what? 

We usually like to learn from it. We want to find out about maybe some summary statistics about the features of the data. 

Let's load in our cereal dataset again. 

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

``` Python
df = pd.read_csv('cereal.csv',)
df.head(15)
```


```out


```

<img src='module1/cereal15.1.png' width = "90%">


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>


---

## Pandas describe()

Pandas has a lot up it's sleeve but one of the most useful functions is called describe and it does exactly that. it _describes_ your data let's try it out. 

``` Python
df.describe()
```


```out


```

<img src='module1/pandas_describe.png'>


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

```out


```

<img src='module1/pandas_describe.png'>

This table will tell you about:
- `count`: The number of non-NA/null observations.
- `mean`: The mean of  column 
- `std` : The standard deviation of a column
- `min`: The min value for a column
- `max`: The max value for a column 
- By default the 25, 50 and 75 percentile of the observations

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

You can make change to either limit how much you show or extend it too with additional arguments:

```python
df.describe(include = "all")

```

```out


```

<img src='module1/include_all.png'>


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

```out


```

<img src='module1/include_all.png' width="90%">

Adding `include = "all"` withinh the brackets adds some additional statistics about categorical columns.

- `unique`: how many observations are unique
- `top`: which observation value is most occuring
- `freq`: what is the frequency of the most occuring observation 

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>


---

you can also get single statistics of each column using:
either `df.mean()`,`df.std()`, `df.count()`, `df.median()`, `df.sum()`. Some of these might produce some wild results especially if the column is a qualitative observation.  

```python
df.sum()

```

```out
mfr         NQKKRGKGRPQGGGGRKKGKNKGRKKKPKPPGPPPQGPKKGQGARR...
type        ColdColdColdColdColdColdColdColdColdColdColdCo...
calories                                                 8230
protein                                                   196
fat                                                        78
sodium                                                  12295
fiber                                                   165.7
carbo                                                    1124
sugars                                                    533
potass                                                   7398
vitamins                                                 2175
shelf                                                     170
weight                                                  79.28
cups                                                    63.22
rating                                                3285.26
```

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
## `pd.value_counts`

If you want to get a frequency table of categorical columns `pd.value_counts` is very useful. 
In the previous slides we talked about getting a single column from a dataframe using double brackets like `df[['column-name']]`.  That's great but to  use pd.value_counts we need to use a different structure which you'll learn in the next module. Instead of getting a single column with double brackets we only use single brackets like so:

```python
manufacturer_column = df["mfr"]
manufacturer_column

```

```out
name
100% Bran                    N
100% Natural Bran            Q
All-Bran                     K
All-Bran with Extra Fiber    K
Almond Delight               R
                            ..
Triples                      G
Trix                         G
Wheat Chex                   R
Wheaties                     G
Wheaties Honey Gold          G
Name: mfr, Length: 77, dtype: object

```

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

We saved the object in a variable called `manufacturer_column` in the same way as we have other dataframes before.  
Next we cant use `pd.value_counts()` referencing that the column we saved as `manufacturer_column` within the brackets.  

```python
manufacturer_freq = manufacturer_column.value_counts()
manufacturer_freq

```

```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64

```

We can then see the frequency of each qualitative value.   
_We can also use the argument `sort = True` withing the brackets if we want to sort the categories in frequency order_ 


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
   
```out
K    23
G    22
P     9
R     8
Q     8
N     6
A     1
Name: mfr, dtype: int64
```

This looks a bit funny though doesn't it? That's because this output isn't our usual dataframe type so we need to make it so. We can make it prettier with `pd.DataFrame` and saving it as a new variable:

```python
manufacturer_freq_df = pd.DataFrame(manufacturer_freq)
manufacturer_freq_df
```

Notes: Script here.

<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

```out
  
   
```

<img src='module1/dataframe_counts.png'>

Ah! That's what we are used to. The column name is specifying the counts of the manufacturers, but maybe we should rename that column to something that makes more sense. 

let's rename that column to `freq`. But how?    

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
    
We use something called `rename` of course! When we rename things it's especially important that we don't forget to assign it to a variable or the column name won't stick! Let's assign it to `freq_mfr_df`.

```python
freq_mfr_df = manufacturer_freq_df.rename(columns = {"mfr": "freq"})
freq_mfr_df

```

```out

          
```

<img src='module1/renamed.png' >

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
     
     
    
```python
freq_mfr_df = manufacturer_freq_df.rename(columns = {"mfr": "freq"})
```

This code  uses something we've never seen before, `{}` curley brackets!   
These have a special meaning but for now you need to know that this `columns` argument need to be set equal to  `"old column name" : "new-column-name"` in curley brackets for us to rename the column.

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

# let’s apply what we learned!

Notes: Script here
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>
