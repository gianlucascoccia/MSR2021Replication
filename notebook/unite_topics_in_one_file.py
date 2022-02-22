import glob
import pandas as pd
import nltk
STEMMING = False
LEMMING =  True

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
stemmer = nltk.stem.snowball.SnowballStemmer("english")

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]

def stem_text(text):
    return [stemmer.stem(w) for w in w_tokenizer.tokenize(text)]

def df_to_file(_index, _row, topic):
    file_name = str(int(_row['filename']))

    text_file = open("../tcc_mallet/so_data/{}.txt".format(file_name), "r")
    content = text_file.read()
    text_file.close()

    path = '../tcc_topics/' + topic + '.txt'

    with open(path, 'a+') as file:
      file.write(content + '\n\n')

for i in range(1,15):
  topic = 'topic_{}'.format(i)
  print(topic)
  so = pd.read_csv('../tcc_data/processed/SO_T_output_Mallet/topics/{}.csv'.format(topic))
  for index, row in so.iterrows():
    df_to_file(index, row,  topic)