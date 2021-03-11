# %% imports 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import MultipleLocator

# %% params

IN_FILE = '../data/processed/so_questions.csv'
OUT_FILE = '../../paper/figures/so_evolution.pdf'

# %% load data

so = pd.read_csv(IN_FILE)

# %% parse dates

so['Year'] = so.CreationDate.apply(lambda x : x[0:4])
so['Month'] = so.CreationDate.apply(lambda x : x[5:7])

# %% divide by framework

# el tags ['nedb', 'electron', 'electron-packager', 'spectron', 'electron-builder', 'electron-forge']
el = so[so['Tags'].str.contains('<nedb>|<electron>|<electron-packager>|<spectron>|<electron-builder>|<electron-forge>')]

# nw tags ['node-webkit', 'nw.js', 'nedb', 'nwjs']
nw = so[so['Tags'].str.contains('<node-webkit>|<nw.js>|<nedb>|<nwjs>')]

# %% group by date
el = el.groupby(['Year', 'Month']).size().reset_index(name='counts').sort_values(['Year', 'Month'])

nw = nw.groupby(['Year', 'Month']).size().reset_index(name='counts').sort_values(['Year', 'Month'])

el['Date'] =  el.Month + '-' + el.Year 
nw['Date'] =  nw.Month + '-' + nw.Year 

# %% remove last month since it has partial data

el.drop(el.tail(1).index,inplace=True)
nw.drop(nw.tail(1).index,inplace=True)

# %% make plot

el_padded = ([0] * 18)
el_padded.extend(el.counts)

plt.plot(nw.Date, nw.counts, label='NW.js')
plt.plot(el.Date, el.counts, label='Electron')
plt.plot(nw.Date, nw.counts + el_padded, label='Combined')
plt.xticks(np.arange(2, len(nw.Date)+1, 12.0), labels=nw.Year[2::12])
plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
plt.xlabel('Year', fontsize=12)
plt.ylabel('# Monthly questions', fontsize=12)
plt.grid(which='both')
plt.grid(which='minor', alpha=0.2)
plt.legend()
plt.tight_layout()
plt.savefig(OUT_FILE)

# %%
