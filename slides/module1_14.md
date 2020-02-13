---
type: slides
---

# ML Model Parameters and Hyperparameters 

Notes: Script to be added
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

- When you call `fit`, a bunch of values get set, like the split variables and split thresholds. 
- These are called **parameters**
- But even before calling `fit` on a specific data set, we can set some "knobs" that control the learning.
- These are called **hyperparameters**

```python 
df = pd.read_csv('data/cities_USA.csv', index_col=0)
X = df.drop(columns=['vote'])
y = df[['vote']]
df
```

```out 
	      lon	          lat	   vote
1	  -80.162475	  25.692104	 blue
2	  -80.214360	  25.944083	 blue
3	  -80.094133	  26.234314	 blue
4	  -80.248086	  26.291902	 blue
5	  -81.789963	  26.348035	 blue
...	    ...	        ...   	 ...
396	-97.460476	  48.225094	 red
397	-96.551116	  48.591592	 blue
398	-166.519855	 53.887114	 red
399	-163.733617	 67.665859	 red
400	-145.423115	 68.077395	 red
400 rows × 3 columns
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

 In scikit-learn, hyperparameters are set in the constructor:

 ```python 
model = DecisionTreeClassifier(max_depth=3) # this is a "decision stump"
model.fit(X, y)
```

```out 
DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',
                       max_depth=3, max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, presort='deprecated',
                       random_state=None, splitter='best')
```

Here, `max_depth` is a hyperparameter. There are many, many more! See the output above and [here](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html).

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

```python
dot_data = export_graphviz(model)
graphviz.Source(export_graphviz(model,
                                out_file=None,
                                feature_names=X.columns,
                                class_names=["red", "blue"],
                                impurity=True))
```
```out 


``` 
<img src="module1/largetree.png" alt="This image is in /static" width="63%">


Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

```python 
model = DecisionTreeClassifier(max_depth=None).fit(X, y)
plot_tree(X, y, model)
```

```out 


``` 
<img src="module1/plot_votes.png" alt="This image is in /static" width="50%">

```python 
model.score(X, y)
```

```out 
1.0
``` 
Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

<br>   
<br>

<font size="6"> **Question to Ponder Before the Next Lecture**</font>     

<br>

<font size="5"> Why not just use a very deep decision tree for every supervised learning problem and get super high accuracy?</font> 


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

