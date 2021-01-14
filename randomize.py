# input: single column csv file
# output: randomized single column csv file

import csv
import random

with open("data/links.csv") as f:
    row = csv.reader(f)
    header, l = next(row), list(row)


entry = [[x[0]] for x in l]
random.shuffle(entry)

with open("data/random.csv", "w") as f:
    csv.writer(f).writerow(header)
    csv.writer(f).writerows(entry)
