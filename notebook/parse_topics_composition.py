# %% imports

import pandas as pd

# %% params

IN_FILE = '../tcc_mallet/so_composition.txt'
OUT_FILE = '../tcc_data/processed/SO_T_output_Mallet/so_topic_matrix.csv'
OUT_DOCS_FOLDER = '../tcc_data/processed/SO_T_output_Mallet/topics'
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
        for i in range(1, NUM_TOPICS + 1):

            document.update({
                'topic_' + str(i) : 1 if float(parts[1 + i]) > THRESHOLD else 0
            })

        docs.append(document)


# %% Save output to file

o = pd.DataFrame()
o = o.append(docs)
o = o.sort_values(by=['filename'])
o.to_csv(OUT_FILE)


# %% Save documents that compose each topic in file

for col in o.columns[1:]:
    t = o[ o[col] == 1 ]
    t.to_csv(OUT_DOCS_FOLDER + '/' + col + '.csv')

# %%
