import os

OUTPUT_PATH = os.getenv('OUTPUT_PATH')

def get_output_folder(folder_name):
  subfolder = os.path.join(OUTPUT_PATH, folder_name)

  if not os.path.exists(subfolder):
    os.makedirs(subfolder)
    print('Folder {} created!'.format(subfolder))

  return subfolder

def get_output_file(file_name):
  return os.path.join(OUTPUT_PATH, file_name)
