# %% imports

import glob
import pandas as pd
import nltk
import os

# %% params

STEMMING = False
LEMMING =  True

OUTPUT_PATH = os.getenv('OUTPUT_PATH')
OUT_FOLDER = os.path.join(OUTPUT_PATH, 'so_data/')
PROCESSED_CSV = os.path.join(OUTPUT_PATH, 'processed/so_questions.csv')

if not os.path.exists(OUT_FOLDER):
  os.makedirs(OUT_FOLDER)
  print('Folder {} created!'.format(OUT_FOLDER))


# %%  load stack overflow questions

so = pd.read_csv(PROCESSED_CSV)

# %% utility funcs

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
stemmer = nltk.stem.snowball.SnowballStemmer("english")

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]

def stem_text(text):
    return [stemmer.stem(w) for w in w_tokenizer.tokenize(text)]

def df_to_file(_index, _row, _fieldname):
    issue_name = str(int(_row['Id']))
    issue_body = str(_row[_fieldname])

    if STEMMING:
        issue_body = ' '.join(stem_text(issue_body))
    if LEMMING:
        issue_body = ' '.join(lemmatize_text(issue_body))
    with open(OUT_FOLDER + issue_name + '.txt', 'a+') as issue_file:
        issue_file.write(issue_body + '\n')

# %% output one question per file as mallet requires (title only)

for index, row in so.iterrows():
    df_to_file(index, row, 'Title')

# %% output comments one question per file as mallet requires (body only)

for index, row in so.iterrows():
   df_to_file(index, row, 'Body')

