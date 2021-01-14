# input: two column csv file
# output: randomized two column csv file


import csv
import random

with open("data/links.csv") as f:
    row = csv.reader(f)
    header, l = next(row), list(row)

entryA = [[x[0]] for x in l]
random.shuffle(entryA)

entryB = [x[1] for x in l]
random.shuffle(entryB)

with open("data/random.csv", "w") as f:
    csv.writer(f).writerows([header] + zip(entryA, entryB))
