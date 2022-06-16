import pandas as pd
import os
from output_folder import get_output_folder

TOPICS_NUM = os.getenv('TOPICS_NUM')
OUT_FOLDER = get_output_folder('so_data/')

def df_to_file(row, topic):
  file_name = str(int(row['filename']))

  file_path = os.path.join(OUT_FOLDER, "{}.txt".format(file_name))
  text_file = open(file_path, "r")
  content = text_file.read()
  text_file.close()

  path = '../tcc_topics/' + topic + '.txt'

  with open(path, 'a+') as file:
    file.write(content + '\n\n')

def unite_questions_documents_by_topic():
  print('Uniting documents...')

  for i in range(1, TOPICS_NUM):
    topic = 'topic_{}'.format(i)
    print(topic)
    so = pd.read_csv(
        '../tcc_data/processed/SO_T_output_Mallet/topics/{}.csv'.format(topic))
    for _, row in so.iterrows():
      df_to_file(row,  topic)

    print('Done!')

if __name__ == '__main__':
  unite_questions_documents_by_topic()