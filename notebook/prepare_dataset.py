from clean_stackoverflow_data import clean_so_data
from export_so_to_mallet import export_to_mallet

if __name__ == '__main__':
    print('Cleaning dataset...')
    clean_so_data()
    print('Exporting documents to Mallet...')
    export_to_mallet()
    print('Done!')
