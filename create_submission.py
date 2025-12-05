import zipfile

files = [
  'arguments.py',
  'database.py',
  'importer.py',
  'operations.py',
  'project.py',
  'project.sql'
]

with zipfile.ZipFile('submission.zip', 'w') as zip:
  for file in files:
    zip.write(file)