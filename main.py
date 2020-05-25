from time import time
from src.levenshtein import levenshtein, scoring

start = time()

ref = "protect"
inp = "produce"

print("===============================================================================")
print("Ref:", ref)
print("Input:", inp)
print("-------------------------------------------------------------------------------")

dist, re = levenshtein(ref, inp)

print("edit-distance:", re)
print("===============================================================================")

corr, acc, h, d, s, i, n = scoring(ref, inp, dist)
print("실행시간:", time() - start)