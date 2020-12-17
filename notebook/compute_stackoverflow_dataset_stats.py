# %% imports 

import pandas as pd
import numpy as np
import datetime

# %% Load StackOverflow data

so = pd.read_csv('../data/raw/so_questions.csv')

# %% Parse creation date

so['CreationTimestamp'] = so.CreationDate.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

so['FavoriteCount'] = so['FavoriteCount'].replace(r'^\s+$', np.nan, regex=True)

# %% divide by framework

# el tags ['nedb', 'electron', 'electron-packager', 'spectron', 'electron-builder', 'electron-forge']
el = so[so['Tags'].str.contains('<nedb>|<electron>|<electron-packager>|<spectron>|<electron-builder>|<electron-forge>')]

# nw tags ['node-webkit', 'nw.js', 'nedb', 'nwjs']
nw = so[so['Tags'].str.contains('<node-webkit>|<nw.js>|<nedb>|<nwjs>')]

# %% Print oldest-youngest creation date

print('\n--------- CREATION DATE ---------') 
print('\n##### NW ####### ') 
print('Oldest Q: {} \nNewest Q: {}'.format(np.min(nw.CreationDate), np.max(nw.CreationDate)))

print('\n##### EL ####### ') 
print('Oldest Q: {} \nNewest Q: {}'.format(np.min(el.CreationDate), np.max(el.CreationDate)))

# %% Print Descriptive stats

stats = ['Score', 'ViewCount', 'AnswerCount', 'CommentCount', 'FavoriteCount']

for s in stats:
    print('\n--------- {} ---------'.format(s))
    print('\n##### NW ####### ') 
    print('Min {} Max {} Median {} Mean {} SD {} IQR {}'.format(np.min(nw[s]), np.max(nw[s]), np.nanmedian(nw[s]), np.nanmean(nw[s]), np.std(nw[s]), np.nanquantile(nw[s], 0.75) - np.nanquantile(nw[s], 0.25)))

    print('\n##### EL ####### ') 
    print('Min {} Max {} Median {} Mean {} SD {} IQR {}'.format(np.min(el[s]), np.max(el[s]), np.nanmedian(el[s]), np.nanmean(el[s]), np.std(el[s]), np.nanquantile(el[s], 0.75) - np.nanquantile(el[s], 0.25)))

# %%
