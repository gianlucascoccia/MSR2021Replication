# %% Imports

import pickle # for saving and loading lists to and from files
from collections import Counter # to fast count occurrences
import untangle # to convert XML to python objects

# %% number of posts with tag t in P

with open("../data/processed/alltags.dmp", "rb") as fp:   # pen file for alltags.dmp load
    tag_set = pickle.load(fp) # list from file

tag_in_P = Counter(tag_set) # create "tag : occurrence" for P

# %%  number of posts with tag t in S

input_file = "../data/raw/Tags.xml" # input XML file
obj = untangle.parse(input_file) # untangle XML file

tag_in_S = {} # create "tag : occurrence" for S

for i in range(0, len(obj.tags.row)): # for each row entry of XML (for each TagName)
    tag_name = obj.tags.row[i]['TagName'] # extract TagName
    tag_count = obj.tags.row[i]['Count'] # extract Count
    tag_entry = {tag_name:tag_count} # create dictionary entry
    tag_in_S.update(tag_entry) # append dictionary entry

# %% calculate alpha

alpha_tags = []
for key in tag_in_P.keys():
    numerator = int(tag_in_P[key])
    if key in tag_in_S:
        denominator = int(tag_in_S[key])
    alpha = numerator / denominator
    if alpha >= 0.1:
        alpha_tags.append(key)

# %% write alpha tag list

with open('../data/processed/alphatags.txt', 'w') as f:
    for item in alpha_tags:
        f.write("%s\n" % item)

# %% calculate beta

beta_tags = []
for key in tag_in_P.keys():
    numerator = int(tag_in_P[key])
    denominator = len(tag_in_P)
    beta = numerator / denominator
    if beta >= 0.01:
        beta_tags.append(key)

# %% write beta tag list

with open('../data/processed/betatags.txt', 'w') as f:
    for item in beta_tags:
        f.write("%s\n" % item)

# %% create T

T = []
for member in alpha_tags:
    if member in beta_tags:
        T.append(member)

# %% write T tag list

with open('../data/processed/T.txt', 'w') as f:
    for item in T:
        f.write("%s\n" % item)

print(T)
# %%
