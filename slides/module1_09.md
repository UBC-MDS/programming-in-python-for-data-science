---
type: slides
---

# Selecting using df.loc[]

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

## Unordered Indexing

We have our trusty `cereal.csv` data again with the cereal names as the index labels.

<img src='module1/cereal15.png' width="60%">

What would we do if we want to select columns and rows too that don't fall consecutively or if we want rearrange them.


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---
Let's say we wanted only the rows labeled "Clusters", "Trix" and "Wheaties" and the columns "type", "sugars" and "rating"
How would we obtain them now?

We need to specify each column and row label that we want between square brackets `[]`, separated with commas.


``` Python
df.loc[ ["Clusters", "Trix", "Wheaties"] , ["type", "sugars", "rating"] ]
```


```out


```

<img src='module1/selecting-cereal.png' width="30%">

We can also reorder it too to change the column and row order.


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

What if we wanted the rows to be in the order  "Wheaties", "Trix" and "Clusters" and columns in the order "type", "rating" and "sugars"
How would we obtain that?

we would just rearrange them in the square brackets!

``` Python
df.loc[ ["Wheaties", "Trix", "Clusters"] , ["type", "rating", "sugars"] ]
```


```out


```

<img src='module1/selecting-cereal-o.png' width="30%">


Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

Let's try it to get the same selection of rows and columns but with indices numbers as labels.    
Bring in the adjusted dataframe.

<img src='module1/cereal15.png' width="60%">

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>


---

We would just substitute the index label number without quotes as we did before.

``` Python
df.loc[ [75, 73, 13] , ["type", "rating", "sugars"] ]
```


```out


```

<img src='module1/number-select.png' width="40%">



Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

You can see that the last code didn't include the name of the cereal so we would need to specify `name` in the column brackets of the code if we want to include it in the dataframe.

``` Python
df.loc[ [75, 73, 13] , [ "name", "type", "rating", "sugars"] ]
```


```out


```

<img src='module1/name-num-select.png' width="40%">


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
