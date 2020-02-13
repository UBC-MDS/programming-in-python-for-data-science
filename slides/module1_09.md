---
type: slides
---

# Training a Model using Scikit-learn

Notes: Script to be added
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

```python
conda install scikit-learn
```

```out  
Collecting package metadata (current_repodata.json): done
Solving environment: done
```

```python
from sklearn.tree import DecisionTreeClassifier, export_graphviz
```

```out    
DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',
                       max_depth=1, max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, presort='deprecated',
                       random_state=None, splitter='best')
```

```python
model.predict(X)
```

```out   
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-15-43a58eb494e8> in <module>
----> 1 model.predict(X)

NameError: name 'X' is not defined
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

 ```python
df
```

```out
        lon	       lat   	   vote
249	-124.027305	40.822381	blue
319	-110.941976	42.712829	red
174	-84.569611	 39.032378	red
286	-95.340293	 41.827063	blue
185	-77.316731	 39.210042	blue
236	-100.310773	40.578560	red
```

```python
model.fit(df)
```

```out    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-4b544d73ba2e> in <module>
----> 1 model.fit(df)

TypeError: fit() missing 1 required positional argument: 'y'
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

```python
X = df.drop(columns=['vote'])
y = df[['vote']]
X
```

```out   
	      lon	       lat
249	-124.027305	40.822381
319	-110.941976	42.712829
174	-84.569611     39.032378
286	-95.340293	 41.827063
185	-77.316731	 39.210042
236	-100.310773	40.578560
```

```python
y
```

```out   
	   vote
249	blue
319	red
174	red
286	blue
185	blue
236	red
```
- *An aside*: it is common to use uppercase letters for matrices (e.g., __*X*__) and lowercase for vectors (response vector __*y*__)

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

```python
model.fit(X, y)
```

```out
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=1,
                       max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, presort=False,
                       random_state=None, splitter='best')
```

```python
df
```

```out
        lon	       lat   	   vote
249	-124.027305	40.822381	blue
319	-110.941976	42.712829	red
174	-84.569611	 39.032378	red
286	-95.340293	 41.827063	blue
185	-77.316731	 39.210042	blue
236	-100.310773	40.578560	red
```

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

```python
import graphviz
dot_data = export_graphviz(model)
graphviz.Source(export_graphviz(model,
                                out_file=None,
                                feature_names=X.columns,
                                class_names=["blue", "red"],
                                impurity=False))
```

```out
  
                    
```

<img src="module1/tree1.jpg" alt="This image is in /static" width="50%">


Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---


```python
X
```

```out    
	      lon	       lat
249	-124.027305	40.822381
319	-110.941976	42.712829
174	-84.569611     39.032378
286	-95.340293	 41.827063
185	-77.316731	 39.210042
236	-100.310773	40.578560
```

```python
model.predict(X)
```

```out  
array(['blue', 'blue', 'red', 'blue', 'blue', 'blue'], dtype=object)
````

```python
np.squeeze(y.to_numpy())
```

```out   
array(['blue', 'red', 'red', 'blue', 'blue', 'red'], dtype=object)
````


```python
model.score(X, y)
```

```out    
0.6666666666666666
````

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

- We can also predict a brand new (made up) point

```python
X
```

```out   
	      lon	       lat
249	-124.027305	40.822381
319	-110.941976	42.712829
174	-84.569611     39.032378
286	-95.340293	 41.827063
185	-77.316731	 39.210042
236	-100.310773	40.578560
````

```python
made_up_X = np.array([-85, 30])
model.predict(made_up_X[np.newaxis])
```

```out  
array(['red'], dtype=object)
```

```python
made_up_X[np.newaxis].shape
```

```out   
(1, 2)
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

