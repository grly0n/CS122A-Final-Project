from src.arguments import initialize_arguments
from src.importer import Importer

def handle_function(args) -> None:
  if args.function_name == 'import':
    print('Importing data from', args.folderName)
    importer = Importer(args.folderName)
    importer.import_from_path()


def main():
  parser = initialize_arguments()
  args = parser.parse_args()  
  handle_function(args)

if __name__ == '__main__':
  main()