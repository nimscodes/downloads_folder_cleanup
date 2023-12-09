import shutil
from pathlib import Path

def clean_downloads_folder():
  # Specify the path to the Downloads folder
  downloads_path = Path.home() / 'Downloads'

  #Create directories for organizations
  documents_path = downloads_path / 'Documents'
  images_path = downloads_path / 'Images'
  others_path = downloads_path / 'Others'

  # Ensures directories exist, create if not
  documents_path.mkdir(exist_ok=True)
  images_path.mkdir(exist_ok=True)
  others_path.mkdir(exist_ok=True)

  # Iterative over files in Downloads folder
  for file in downloads_path.iterdir():
    if file.is_file():
      # classify files into categories based on file extensions
      if file.suffix.lower() in ['.pdf', '.docx', '.txt']:
        destination_folder = documents_path
      elif file.suffix.lower() in ['.jpg', '.png', '.gif']:
        destination_folder = images_path
      else:
        destination_folder = others_path
      
      # Move the file to the appropriate folder
      shutil.move(file, destination_folder / file.name)

if __name__ == "__main__":
  clean_downloads_folder()
  print("Downloads folder cleaned up.")
