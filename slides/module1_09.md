---
type: slides
---

# Slicing with Pandas

Notes: Script here.
<html>
<audio controls >
  <source src="placeholder_audio.mp3" />
</audio></html>

---

## Unordered Indexing

Next Let's talk about if we want to select columns and rows too that don't fall consecutively.

Let's say we wanted only the rows named "Wheaties", "Trix" and "Clusters" in that ordered.
How would we obtain them now?

We need to specify each column and row name now between square brackets.


``` Python
df.loc[["Wheaties", "Trix", "Clusters"], ['type', 'rating', 'sugars']]
```


```out


```

<img src=''>



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
  <source src="572_placeholder_audio.mp3" />
</audio></html>
