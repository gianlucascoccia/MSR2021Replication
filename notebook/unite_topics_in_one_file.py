import pandas as pd
import os

OUTPUT_PATH = os.getenv('OUTPUT_PATH')
TOPICS_NUM = os.getenv('TOPICS_NUM')

OUT_FOLDER =  os.path.join(OUTPUT_PATH, 'so_data/')


def df_to_file(row, topic):
  file_name = str(int(row['filename']))

  file_path = os.path.join(OUT_FOLDER, "{}.txt".format(file_name))
  text_file = open(file_path, "r")
  content = text_file.read()
  text_file.close()

  path = '../tcc_topics/' + topic + '.txt'

  with open(path, 'a+') as file:
    file.write(content + '\n\n')


if not os.path.exists(OUT_FOLDER):
  os.makedirs(OUT_FOLDER)
  print('Folder {} created!'.format(OUT_FOLDER))

print('Uniting documents...')

for i in range(1, TOPICS_NUM):
  topic = 'topic_{}'.format(i)
  print(topic)
  so = pd.read_csv('../tcc_data/processed/SO_T_output_Mallet/topics/{}.csv'.format(topic))
  for index, row in so.iterrows():
    df_to_file(row,  topic)

print('Done!')