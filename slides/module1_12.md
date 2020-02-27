---
type: slides
---

# Slicing and Selecting using df.iloc[]

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
## Slicing Dataframe

Up to this point we have been manipulating our dataframe with column and row _**names**_ using `df. loc`.     
`df.iloc` is very similar, however the "i" in `iloc` refers to index **position**.     

Let's return to our cereal dataset and take a look at the first 15 rows. 


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

``` Python
df = pd.read_csv('cereal.csv', index_col = 0)
df.head(15)
```


```out


```

<img src='module1/slide12_1.png' width="40%">

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

Let's say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` but we want to slice based on their position.      
Using Python's counting method of starting at zero, we conclude `All-Bran` to be at position to 2. We get `Apple Cinnamon Cheerios` position to be 5 in the same way. Using the same coding structure we learned with `df.loc`, but using the position instead of labels would look like this. 

``` Python
df.iloc[2:5]
```


```out


```

<img src='module1/slide12_2.png' width="30%">




Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

But why doesn't "Apple Cinnamon Cheerios" appear in the dataframe? That's because when we use slicing by index position, it will take all the indices including the lower bound but _EXCLUDING_ the upper bound. So if we wanted to include "Apple Cinnamon Cheerios" we would have to go 1 index position further. 

``` Python
df.iloc[2:6]
```


```out


```

<img src='module1/slide12_3.png' width="30%">


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

Ah, that's better.  
The same concepts woucand apply to the columns of the dataframe.   
Let's say we want all the rows but we only want the columns starting at `protein` and ending (including) at column `sugars`.     
Using the logic we learned in the last set of slides we would use the following code  

``` Python
df.iloc[ : , 3:9 ]
```


```out


```

<img src='module1/slide12_4.png' width="30%">

we would need to specify all rows using ` : ` as we did using `df.loc[]`. The column `protein` is at index position 3 and `sugars` is at index position 8, but since we want to include the 8th column we need to use the 9th position to make sure we get all the columns _BEFORE_ the upper bound. 



Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>


---

The same would apply if we only wanted certain rows with certain columns so now we want the rows  `All-Bran` to `Apple Cinnamon Cheerios` and `protein` to `sugars`.     
**Rows**    
`All-Bran` being at position 2.     
`Apple Cinnamon Cheerios` being at position 5.     
**Columns**   
`protein` being at position 3.     
`sugar` being at position 8. 


``` Python
df.iloc[2:6, 3:9]
```


```out


```

<img src='module1/slide12_5' width="40%">


Both of our upper bound have now been compensated with + 1 to make sure it they are included. 


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
## Selecting with `df.iloc[]` 

Selecting using `iloc` is done identically to `loc` however the items withing each set of square brackets **MUST** be numeric.   

Lets say we want the rows `Cheerios`, `Basic 4` and `Apple Jacks`  with the columns `rating`, `fat` and `type` _in that order_. 

**Rows**    
`Cheerios` being at position 2.     
`Basic 4` being at position 5.    
`Apple Jacks` being at position 3.

**Columns**   
`rating` being at position 14.  
`fat` being at position 4.  
`type` being at position 1.   

Now let's put those position into square backing within `df.iloc[]`

``` Python
df.iloc[[11, 7, 6], [14, 4, 1]]
```


```out


```

<img src='module1/slide12_6.png' width="40%">


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>


---

# Super! Nice work! Let’s apply what we learned!

Notes: Script here
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>
