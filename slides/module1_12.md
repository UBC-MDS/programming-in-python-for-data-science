---
type: slides
---

# Decision Tree Splitting Rules 

Notes: Script to be added
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

### Definitions

**Decision	Trees**	are	simple	programs	consisting	of:  
- Decision	trees	allow	sequences	of	splits based	on	multiple	features. 
– A	nested	sequence	of	“if-else”	decisions	based	on	the	features (splitting	rules).
– A	class	label	as	a	return	value	at	the	end	of	each	sequence.  
– Very	general	class	of	models:	can	get	very	high	accuracy.
– However,	it’s	computationally	infeasible	to	find	the	best	decision	tree.

**Decision	Stumps** are simple	decision	tree	with	1	splitting	rule	based	on	thresholding	1	feature.

<img src="module1/tree1.jpg" alt="This image is in /static" width="50%"> 

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

 ### How do we decide how to split the data? 

- Basic idea is to pick a criterion (see [here](https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation)) and then maximize it across possible splits.
- Common one is Gini impurity

<img src="module1/gini.png" alt="This image is in /static" width="60%"> 

- **C** is number of classes in target variable
- **p** is proportion of class **i** in a group

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

```python
def gini2(c1, c2):
    """
    Calculates the gini impurity for binary class data.

    Parameters
    ----------
    c1 : int
        Number of examples of class 1
    c2 : int
        Number of examples of class 2

    Returns
    -------
    float
        The gini impurity
    """
    n = c1 + c2  # total examples
    p1 = c1 / n  # proportion of instance that are class 1
    p2 = c2 / n  # proportion of instance that are class 2
    return p1*(1-p1) + p2*(1-p2)  # calculate gini impurity
    
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

<img src="module1/lat_long.png" alt="This image is in /static" width="50%">

- Let's first calculate the Gini impurity of the full dataset

```python 
gini2(3, 3)
```

```out 
0.5
``` 

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

- Let's calculate the Gini impurity of the shown split on lon = -97.5
- We now have 2 groups (on either side of red line) so calculate impurity for each group
- We add the results together but weight it by the proportion of observations

```python 
gini2(1, 2)*(3/6) + gini2(2, 1)*(3/6)
```

```out 
0.4444444444444445
```

```python 
gini2(0, 1)*(1/6) + gini2(3, 2)*(5/6)
```

```out 
0.4
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

# Let's practice!

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

