from pathlib import Path


class Importer():
  def __init__(self, path: str):
    self.path = Path(path)

  def import_from_path(self):
    for file in Path.iterdir(self.path):
      print('Reading from', file.name)
      with open(file, 'r') as f:
        for line in f:
          print(line.split(','))