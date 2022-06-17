# %% imports 

import glob
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os

# %% params

OUTPUT_PATH = os.getenv('OUTPUT_PATH')
IN_FOLDER =  os.path.join(OUTPUT_PATH, '/so_results/')
OUT_FILE = os.path.join(OUTPUT_PATH, 'so_results/topics_report_so.txt')

# %% List files in folder

in_files = glob.glob(IN_FOLDER + "*.xml")
in_files.sort()

# %% iterate on files and extract metrics

metrics_list = []

for _file in in_files:
    soup = BeautifulSoup(open(_file, 'r'))

    metrics = {
      'tokens' : [],
      'document_entropy': [], 
      'word-length': [], 
      'coherence': [], 
      'uniform_dist': [], 
      'corpus_dist': [], 
      'eff_num_words': [], 
      'token-doc-diff': [], 
      'rank_1_docs': [], 
      'allocation_ratio': [], 
      'allocation_count': [], 
      'exclusivity': [] 
    }

    topics = soup.model.find_all('topic')
    for t in topics:
        for m in metrics.keys():
            metrics[m].append(float(t.get(m)))

    for m in metrics.keys():
        data =  metrics[m]
        metrics[m] = {
            'mean' : np.mean(data).round(5),
            'sd' : np.std(data).round(5),
            'median' : np.median(data).round(5),
    }

    metrics_list.append((_file,metrics))

# %% print results to output file

padding_width = 234

with open(OUT_FILE, 'w') as output:

    metrics = ['mean', 'sd', 'median']

    for m in metrics:

        # Print metric name
        output.write("\n {s:{c}^{n}} \n".format(s=m, c='-', n=padding_width - 2))

        # Print header
        output.write('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18} \n'.format(*['num_topics'] + [i for i in list(metrics_list[1][1].keys())]))
        output.write("-" * padding_width + "\n")


        # Print body
        for item in metrics_list:     
                
            # Extract num_topics
            num_topics = item[0][36:-4]
            
            output.write('{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18}{:^18} \n'.format(*[num_topics] + [i[m] for i in list(item[1].values())]))

        output.write('\n')
    # %%
