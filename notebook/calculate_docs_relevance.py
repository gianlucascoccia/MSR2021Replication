# %% imports 

import pandas as pd
import numpy as np
import datetime
import scipy.stats as stats
import matplotlib.pyplot as plt 
import scikit_posthocs as sp

# %% Params

SO_NUM_TOPICS = 14
GH_NUM_TOPICS = 13

# %% Load data

so_data = pd.read_csv('../data/raw/so_questions.csv')

so_answers = pd.read_csv('../data/raw/so_accepted_answers.csv')

so_comp = '../data/processed/SO_T_output_Mallet/so_composition.txt' 

el_data = pd.read_csv('../data/processed/el_issues.csv')
nw_data = pd.read_csv('../data/processed/nw_issues.csv')

gh_data = pd.concat([el_data, nw_data])

gh_comp = '../data/processed/GH_T_output_Mallet/git_composition.txt' 

# %% filter only questions with accepted answers

so_data = so_data.dropna(subset=['AcceptedAnswerId'])

so_data = so_data.merge(so_answers[['CreationDate', 'Id']], left_on='AcceptedAnswerId', right_on='Id')

so_data = so_data.rename(columns={"CreationDate_x": "CreationDate", "CreationDate_y": "AcceptedDate", "Id_x": "Id"})
so_data = so_data.drop(columns="Id_y")

# %% filter only issues that are closed 

gh_data = gh_data[gh_data['status'] == 'closed']

# %% calculate alive time for SO

so_data['CreationTimestamp'] = so_data.CreationDate.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

so_data['AcceptedTimestamp'] = so_data.AcceptedDate.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))

so_data['AliveTime'] = so_data.AcceptedTimestamp - so_data.CreationTimestamp

so_data['AliveTime'] = so_data.AliveTime.apply(lambda x: x.total_seconds())

# %% parse SO topic composition

docs = []
with open(so_comp, 'r') as in_file:
    for line in in_file:
        parts = line.split('\t')
        document = {
            'filename' : str(parts[1].split("/")[-1][:-4])
        }
        for i in range(1, SO_NUM_TOPICS + 1):
            
            document.update({
                'topic_' + str(i) : (parts[1 + i]) 
            })
        docs.append(document)

# %% merge SO topic composition and other SO data

comp_data = pd.DataFrame()
comp_data = comp_data.append(docs).sort_values(by=['filename'])

so_data['Id']= so_data['Id'].astype(str)

so_data = so_data.merge(comp_data, left_on = 'Id', right_on = 'filename')

# %% Merge probabilities of topics that were manually merged (topics 1 & 7)

so_data['topic_1'] = so_data['topic_1'].astype(np.float64) + so_data['topic_7'].astype(np.float64)

so_data = so_data.drop('topic_7', axis=1)

# %% Remove probabilities < 0.05 in SO --- CURRENTLY NOT USED 

#cols = [1,2,3,4,5,6,8,9,10,11,12,13,14]

#for c in cols:
#    so_data['topic_' + str(c)] = so_data['topic_' + str(c)].astype(np.float64).apply(lambda x: x if x > 0.05 else np.nan)

# %% multiplicate probs for the time

so_data['time_topic_1'] = so_data['topic_1'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_2'] = so_data['topic_2'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_3'] = so_data['topic_3'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_4'] = so_data['topic_4'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_5'] = so_data['topic_5'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_6'] = so_data['topic_6'].astype(np.float64) * so_data['AliveTime'] 
#so_data['time_topic_7'] = so_data['topic_7'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_8'] = so_data['topic_8'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_9'] = so_data['topic_9'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_10'] = so_data['topic_10'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_11'] = so_data['topic_11'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_12'] = so_data['topic_12'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_13'] = so_data['topic_13'].astype(np.float64) * so_data['AliveTime'] 
so_data['time_topic_14'] = so_data['topic_14'].astype(np.float64) * so_data['AliveTime'] 

# %% parse GH topic composition

docs = []
with open(gh_comp, 'r') as in_file:
    for line in in_file:
        parts = line.split('\t')
        document = {
            'filename' : str(parts[1].split("/")[-1][:-4])
        }
        for i in range(1, GH_NUM_TOPICS + 1):
            
            document.update({
                'topic_' + str(i) : (parts[1 + i]) 
            })
        docs.append(document)

# %% merge GH topic composition and other GH data

comp_data = pd.DataFrame()
comp_data = comp_data.append(docs).sort_values(by=['filename'])

gh_data['filename']= gh_data['folderName'] + '_' + gh_data['id'].astype(int).astype(str)

gh_data = gh_data.merge(comp_data, left_on = 'filename', right_on = 'filename')

# %% Remove probabilities < 0.05 in GH --- CURRENTLY NOT USED 

#cols = [1,2,3,4,5,6,7,9,10,11,12,13]

#for c in cols:
#    gh_data['topic_' + str(c)] = gh_data['topic_' + str(c)].astype(np.float64).apply(lambda x: x if x > 0.05 else np.nan)

# %% Merge probabilities of topics that were manually merged (topics 7 & 8)

gh_data['topic_7'] = gh_data['topic_7'].astype(np.float64) + gh_data['topic_8'].astype(np.float64)

gh_data = gh_data.drop('topic_8', axis=1)


# %% multiplicate probs for the time

gh_data['time_topic_1'] = gh_data['topic_1'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_2'] = gh_data['topic_2'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_3'] = gh_data['topic_3'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_4'] = gh_data['topic_4'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_5'] = gh_data['topic_5'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_6'] = gh_data['topic_6'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_7'] = gh_data['topic_7'].astype(np.float64) * gh_data['aliveTIme'] 
#gh_data['time_topic_8'] = gh_data['topic_8'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_9'] = gh_data['topic_9'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_10'] = gh_data['topic_10'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_11'] = gh_data['topic_11'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_12'] = gh_data['topic_12'].astype(np.float64) * gh_data['aliveTIme'] 
gh_data['time_topic_13'] = gh_data['topic_13'].astype(np.float64) * gh_data['aliveTIme'] 

# %% Extract accepted answers ID

# Needed to collect the answers, no need to run it again
#with open('../data/raw/accepted_answers_id.txt','a') as ID_FILE:
#    np.savetxt(ID_FILE, so_data.AcceptedAnswerId, fmt='OR ID = %d')

# %% Export data

so_data.to_csv('so_test_data.csv')
gh_data.to_csv('gh_test_data.csv')