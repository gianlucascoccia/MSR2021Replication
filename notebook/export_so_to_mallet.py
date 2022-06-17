import pandas as pd
import nltk
import os
from output_folder import get_output_file, get_output_folder

STEMMING = False
LEMMING =  True

OUTPUT_PATH = os.getenv('OUTPUT_PATH')
OUT_FOLDER = get_output_folder('so_data/')
PROCESSED_CSV = get_output_file('processed/so_questions.csv')

# Utility functions
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

def export_to_mallet():
  # load stack overflow questions
  so = pd.read_csv(PROCESSED_CSV)

  # output one question per file as mallet requires (title only)
  for index, row in so.iterrows():
    df_to_file(index, row, 'Title')

  # output comments one question per file as mallet requires (body only)
  for index, row in so.iterrows():
    df_to_file(index, row, 'Body')

if __name__ == '__main__':
  export_to_mallet()
