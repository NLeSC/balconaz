# input: two column csv file
# output: randomized two column csv file
# bad: all hardcoded filenames

import csv
import random

with open("../data/ground_truth-test.csv") as f:
    row = csv.reader(f)
    header, l = next(row), list(row)

# randomize first column
entryA = [x[1] for x in l]
random.shuffle(entryA)

# randomize another column
entryB = [x[2] for x in l]
random.shuffle(entryB)

# writeout keeping all but timestamp column
with open("../data/randomized_data-test.csv", "w") as f:
    csv.writer(f).writerows([header[1:]] + zip(entryA, entryB))

print("Randomization done.")
