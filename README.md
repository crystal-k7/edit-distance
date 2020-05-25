# edit-distance
edit distance

```
from src.levenshtein import levenshtein, scoring

ref = "protect"
inp = "produce"

dist, re = levenshtein(ref, inp)
corr, acc, h, d, s, i, n = scoring(ref, inp, dist)
```