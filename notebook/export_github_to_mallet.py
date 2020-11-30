# %% imports 

import glob
import pandas as pd
import nltk

# %% params

OUT_FOLDER = '../mallet/git_data/'
STEMMING =  False
LEMMING =  True

# %%  load issues

el_iss = pd.read_csv('../data/processed/el_issues.csv')
nw_iss = pd.read_csv('../data/processed/nw_issues.csv')

# %%  load comments

el_comm = pd.read_csv('../data/processed/el_comments.csv')
nw_comm = pd.read_csv('../data/processed/nw_comments.csv')

# %% utility funcs

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
stemmer = nltk.stem.snowball.SnowballStemmer("english")

def lemmatize_text(text):
    return [stemmer.stem(w) for w in w_tokenizer.tokenize(text)]

def stem_text(text):
    return [stemmer.stem(w) for w in w_tokenizer.tokenize(text)]

def df_to_file(_index, _row):
    #issue_name = str(_row['commentId'])
    issue_name = str(_row['folderName']) + '_' + str(int(_row['id']))
    #issue_body = str(_row['body'])
    issue_body = str(_row['title'])
    if STEMMING:
        issue_body = ' '.join(stem_text(issue_body))
    if LEMMING:
        issue_body = ' '.join(lemmatize_text(issue_body))
    with open(OUT_FOLDER + issue_name + '.txt', 'a') as issue_file:
        issue_file.write(issue_body + '\n')


# %% output comments one issue per file as mallet requires 

#for index, row in nw_comm.iterrows():
 #   df_to_file(index, row)

#for index, row in el_comm.iterrows():
  #  df_to_file(index, row)


# %% output one issue per file as mallet requires (title only)

for index, row in nw_iss.iterrows():
    df_to_file(index, row)

for index, row in el_iss.iterrows():
    df_to_file(index, row)

# %%
