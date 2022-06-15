# %% Imports

import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

DATASET_PATH = os.getenv('DATASET_PATH')
OUTPUT_PATH = os.getenv('OUTPUT_PATH')

#nltk.download('stopwords')

# %% Load questions

so_questions = pd.read_csv(DATASET_PATH)

print("Loaded CSV!")

# %% Remove code from body

so_questions.Body = so_questions.Body.apply(lambda x: re.sub('\<code(.*)code>', '', x))
print("Removed questions body!")

# %% Remove HTML Tags from body

so_questions.Body = so_questions.Body.apply(lambda x: re.sub('<[^<]+?>', '', x))
so_questions.Body = so_questions.Body.apply(lambda x: re.sub('&#xA;', '', x))
print("Removed HTML tags!")


# %% Remove stopwords from body

# TODO: The stop words aplication is not working properly. Need refector
so_questions.Body = so_questions.Body.apply(lambda x: ' '.join([w for w in word_tokenize(x) if not w in stopwords.words('english')]))
print("Removed stopwords!")

# %% Store cleaned and processed data
subfolder = os.path.join(OUTPUT_PATH, 'processed/')

if not os.path.exists(subfolder):
  os.makedirs(subfolder)
  print('Folder {} created!'.format(subfolder))

processed_csv = os.path.join(subfolder, 'so_questions.csv')

# Questions
so_questions.to_csv(processed_csv)

print("Saved new csv!")


# %%
