# %% Imports

import pandas as pd
import numpy as np
import re

# %% Load questions 

so_questions = pd.read_csv('../data/raw/so_questions.csv')

# %% Remove code from body 

so_questions.Body = so_questions.Body.apply(lambda x: re.sub('\<code(.*)code>', '', x))

# %% Remove HTML Tags from body 

so_questions.Body = so_questions.Body.apply(lambda x: re.sub('<[^<]+?>', '', x))
so_questions.Body = so_questions.Body.apply(lambda x: re.sub('&#xA;', '', x))

# %% Store cleaned and processed data

# Questions
so_questions.to_csv('../data/processed/so_questions.csv')

# %%
