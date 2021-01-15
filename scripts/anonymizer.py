# input: multiple csv files
import csv
import random

def readCSV(filename):
    # read csv file
    # return header and rows
    with open(filename) as f:
        row = csv.reader(f)
        header, l = next(row), list(row)
        return header, l

def create_alias(orig_list, str_name, ):
    # randomize and create aliases
    random.shuffle(orig_list)
    alias = []
    i = 0
    for _ in orig_list:
        i += 1
        alias.append(str_name + str(i))
    return alias

# read original csv file
header_origin, l_origin = readCSV("../data/ground_truth-test.csv") # first file provides the entries for vocabulary keys

# prepare keys for the anonymization dictionary
names = [x[1] for x in l_origin]
urls = [x[2] for x in l_origin]

#creating values
players = create_alias(names, "Player")
links = create_alias(urls, "URL")

# create dictionary for anonymization
d_names = dict(zip(names,players))
d_links = dict(zip(urls,links))

# read the guesses file
header_guess, l_guess = readCSV("../data/guesses.csv")

#replacing values with anonymized entries
url_g = [d_links.get(x[1]) for x in l_guess] #change 2nd column
names_g = [d_names.get(x[2]) for x in l_guess] #change 3rd column
guess_g = [d_names.get(x[3]) for x in l_guess] #change 4th column
timestamp_g = [x[0] for x in l_guess]

# writeout anonymized values from this vocabulary
with open("../data/randomized_data-test.csv", "w") as f:
    csv.writer(f).writerows([header_guess])
    csv.writer(f).writerows(zip(timestamp_g,url_g, names_g, guess_g))
