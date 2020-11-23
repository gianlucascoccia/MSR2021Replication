# <codecell> %% Imports

import csv # for csv files
import re # for regular expressions
import pickle # for saving and loading lists to and from files

# <codecell> %% Process csv

with open("../data/raw/Posts.csv", "r", encoding="utf8") as csv_file: # open csv file with utf8 encoding (will give error without utf8)
    csv_reader = csv.reader(csv_file, delimiter=',') # parse csv per , character
    next(csv_reader) # skip first line
    tag_set_raw = '' # will contain all tags with ><

    for lines in csv_reader: # for all lines
        tag_set_raw = tag_set_raw + lines[16] # create a single list with all the strings

    tag_set = re.split("><", tag_set_raw) # will contain all the tags without ><, we have to clean first from  < and last from >
    tag_set[0] = tag_set[0][1:] # remove < from first
    tag_set[-1] = tag_set[-1][:-1] # remove > from last
    tag_set_single = list(dict.fromkeys(tag_set)) # remove duplicates

    print('complete tag set: ')
    print(tag_set) # print the whole tag set
    print('\n')
    print('single occurence tag set: ')
    print(tag_set) # print the single occurrence tag set
    print('\n')

    with open("../data/processed/alltags.dmp", "wb") as fp:  # open file for complete tag set dump
        pickle.dump(tag_set, fp) # dump complete tag set to file
    with open("../data/processed/singletags.dmp", "wb") as fp:  # open file for single occurrence tag set dump
        pickle.dump(tag_set_single, fp) # dump single occurrence tag set to file

# %%
