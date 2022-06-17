import pandas as pd
import os
from output_folder import get_output_file, get_output_folder


IN_FILE = get_output_file('so_composition.txt')
OUT_FILE = get_output_file('processed/SO_T_output_Mallet/so_topic_matrix.csv')
OUT_DOCS_FOLDER = get_output_folder('processed/SO_T_output_Mallet/topics')

THRESHOLD = 0.5
TOPICS_NUM = int(os.getenv('TOPICS_NUM'))

def parse_input_file(docs):
  with open(IN_FILE, 'r') as in_file:
    for line in in_file:
      parts = line.split('\t')

      document = {
        'filename' : parts[1].split("/")[-1][:-4]
      }
      for i in range(1, TOPICS_NUM + 1):

        document.update({
          'topic_' + str(i) : 1 if float(parts[1 + i]) > THRESHOLD else 0
        })

      docs.append(document)

def save_output_to_file(docs):
  o = pd.DataFrame()
  o = o.append(docs)
  o = o.sort_values(by=['filename'])
  o.to_csv(OUT_FILE)

  # Save documents that compose each topic in file
  for col in o.columns[1:]:
      t = o[ o[col] == 1 ]
      t.to_csv(OUT_DOCS_FOLDER + '/' + col + '.csv')

def parse_topics():
  docs = []
  parse_input_file(docs)
  save_output_to_file(docs)

if __name__ == '__main__':
  parse_topics()
