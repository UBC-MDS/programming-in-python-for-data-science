---
type: slides
---

# Introduction to Machine Learning and Decision Trees

Notes: In this module you will be introduced to different machine learning branches and Decision Trees.


---

# Module Learning Outcomes 

<html>
<video style="display:block; margin: 0 auto;" width="100%" height="auto" controls >
  <source src="sample_video.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></html>

Notes: 
1. Describe the difference between supervised and unsupervised learning  
2. Distinguish machine learning terminology such as features, targets, training, error, etc.
3. Broadly describe how the decision tree algorithm works
4. Develop a decision tree model using scikit-learn and the fit/predict paradigm
5. Describe the difference between parameters and hyperparameters in machine learning models

---

# Supervised Learning 

- In supervised learning, we have a set of observations (__*X*__) with an associated response (__*y*__)
- We wish to find a model function that relates __*X*__ to __*y*__
- Then use that model function to predict future observations

<img src='module1/sup_learning.png' width="700">

Notes: Script here. 
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>

---

Goal	of	supervised	learning:	
– Use	data	to	find	a	model	that	outputs	the	right	label	based	on	the	features.

See the magic in practice...

```python
import pandas as pd
import numpy as np
from PIL import Image
import sys
sys.path.append('code/')
from toy_classifier import classify_image

img = Image.open("alpaca.jpg")
img
```

```out

       
```
<img src="module1/alpaca.jpg" alt="This image is in /static" width="20%">


Notes: Script here. 
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

<img src="module1/alpaca.jpg" alt="This image is in /static" width="20%">

```python
classify_image(img, 5)
```


```out

Class, Probability
llama, 0.68
Eskimo dog, husky, 0.07
Norwich terrier, 0.05
wallaby, brush kangaroo, 0.04
timber wolf, grey wolf, gray wolf, Canis lupus, 0.03
```

Notes: Script here. 
<html>
<audio controls >
  <source src="572_placeholder_audio.mp3" />
</audio></html>


---

## Unsupervised learning
- We have data, but no associated response
- We will not be covering unsupervised learning in this course and instead put our main focus on supervised

<img src='module1/unsup_learning.png' width="65%">

Notes: Script here. 
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

