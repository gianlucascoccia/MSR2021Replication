import pandas as pd

def df_to_file(row, topic):
    file_name = str(int(row['filename']))

    text_file = open("../tcc_mallet/so_data/{}.txt".format(file_name), "r")
    content = text_file.read()
    text_file.close()

    path = '../tcc_topics/' + topic + '.txt'

    with open(path, 'a+') as file:
      file.write(content + '\n\n')

print('Uniting documents...')

for i in range(1,15):
  topic = 'topic_{}'.format(i)
  print(topic)
  so = pd.read_csv('../tcc_data/processed/SO_T_output_Mallet/topics/{}.csv'.format(topic))
  for index, row in so.iterrows():
    df_to_file(row,  topic)

print('Done!')