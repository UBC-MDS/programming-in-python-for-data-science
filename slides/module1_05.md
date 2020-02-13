---
type: slides
---

# Tabular Data and Terminology

Notes: Script to be added
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

- For ML we typically work with "tabular data"
- Rows are examples
- Columns are features (the last column is typically the target)

```python
df = pd.read_csv('data/cities_USA.csv', index_col=0).sample(6, random_state=100)
df
```

```out

            lon 	     lat	   vote
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

  

```out

            lon 	     lat	   vote
249	-124.027305	40.822381	blue
319	-110.941976	42.712829	red
174	-84.569611	 39.032378	red
286	-95.340293	 41.827063	blue
185	-77.316731	 39.210042	blue
236	-100.310773	40.578560	red

```
<br>    
- This dataset contains longtitude and latitude data for 400 cities in the US
- Each city is labelled as `red` or `blue` depending on how they voted in the 2012 election.
- The cities data was sampled from (http://simplemaps.com/static/demos/resources/us-cities/cities.csv). The election information was collected from Wikipedia.

Notes: Script here
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

### Terminology


- You will see a lot of variable terminology in machine learning and statistics
- See the MDS terminology resource [here](https://ubc-mds.github.io/resources_pages/terminology/).

Of particular:
- **Examples** = rows = samples = records = instances (usually denoted by **n**)
- **Features** = inputs = predictors = explanatory variables = regressors = independent variables = covariates (usually denoted by **d**)
- **Targets** = outputs = outcomes = response variable = dependent variable = labels (if categorical).
- **Training** = learning = fitting

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

            lon 	     lat	   vote
249	-124.027305	40.822381	blue
319	-110.941976	42.712829	red
174	-84.569611	 39.032378	red
286	-95.340293	 41.827063	blue
185	-77.316731	 39.210042	blue
236	-100.310773	40.578560	red

```

```python
df.shape
```

```out
(6, 3)
```

In this data set we have 6 examples of 3 variables (2 features, 1 target).

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

