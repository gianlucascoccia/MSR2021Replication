# %% imports 

import pandas as pd

# %% params

IN_FILE = '../git_composition.txt'
OUT_FILE = 'git_topic_matrix.csv'
THRESHOLD = 0.5
NUM_TOPICS = 14

# %% parse input file

docs = []

with open(IN_FILE, 'r') as in_file:
    for line in in_file:
        parts = line.split('\t')
        
        document = {
            'filename' : parts[1].split("/")[-1][:-4]
        }
        for i in range(1, NUM_TOPICS - 1):
            
            document.update({
                'topic_' + str(i) : float(parts[1 + i]) > THRESHOLD
            })

        docs.append(document)


# %% Save output to file

o = pd.DataFrame()
o = o.append(docs)
o = o.sort_values(by=['filename'])
o.to_csv(OUT_FILE)

# %%
