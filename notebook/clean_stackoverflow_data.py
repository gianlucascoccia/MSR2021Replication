from output_folder import get_output_folder
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
from output_folder import get_output_folder


def load_questions():
  DATASET_PATH = os.getenv('DATASET_PATH')
  print(DATASET_PATH)
  so_questions = pd.read_csv(DATASET_PATH)
  print("Loaded CSV!")
  return so_questions


def remove_html_tags(questions):
  # Remove code from body
  questions.Body = questions.Body.apply(lambda x: re.sub('\<code(.*)code>', '', x))

  # Remove HTML Tags from body
  questions.Body = questions.Body.apply(lambda x: re.sub('<[^<]+?>', '', x))
  questions.Body = questions.Body.apply(lambda x: re.sub('&#xA;', '', x))
  print("Removed HTML tags!")

def remove_stopwords(questions):
  questions.Body = questions.Body.apply(lambda x: ' '.join([w for w in word_tokenize(x) if not w in stopwords.words('english')]))
  print("Removed stopwords!")

def save_processed_data(questions):
  # Store cleaned and processed data
  folder = get_output_folder('processed/')
  processed_csv = os.path.join(folder, 'so_questions.csv')

  questions.to_csv(processed_csv)
  print("Saved new csv!")

def clean_so_data():
  questions = load_questions()
  remove_html_tags(questions)
  remove_stopwords(questions)
  save_processed_data(questions)

if __name__ == '__main__':
  clean_so_data()