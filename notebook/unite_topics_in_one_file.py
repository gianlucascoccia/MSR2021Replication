import pandas as pd
import os
from output_folder import get_output_folder, get_output_file

TOPICS_NUM = int(os.getenv('TOPICS_NUM'))
OUT_FOLDER = get_output_folder('so_data/')

def df_to_file(row, topic):
  file_name = str(int(row['filename']))

  file_path = os.path.join(OUT_FOLDER, "{}.txt".format(file_name))
  text_file = open(file_path, "r")
  content = text_file.read()
  text_file.close()

  path = get_output_file(
    'topics/{}.txt'.format(topic)
  )

  with open(path, 'a+') as file:
    file.write(content + '\n\n')

def unite_questions_documents_by_topic():

  get_output_folder('topics')

  for i in range(1, TOPICS_NUM + 1):
    topic = 'topic_{}'.format(i)
    file = get_output_file(
        'processed/SO_T_output_Mallet/topics/{}.csv'.format(topic))
    so = pd.read_csv(file)
    for _, row in so.iterrows():
      df_to_file(row,  topic)

if __name__ == '__main__':
  unite_questions_documents_by_topic()