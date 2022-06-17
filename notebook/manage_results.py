from parse_topics_composition import parse_topics
from unite_topics_in_one_file import unite_questions_documents_by_topic

if __name__ == '__main__':
  print('Parsing topics...')
  parse_topics()
  print('\nUniting questions by topic...')
  unite_questions_documents_by_topic()
