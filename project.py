from src.arguments import initialize_arguments
from src.importer import Importer
from src import operations


def handle_function(args) -> None:
  if args.function_name == 'import':
    print('Importing data from', args.folderName)
    importer = Importer(args.folderName)
    success = importer.import_from_path()
    print('Success' if success else 'Fail')

  elif args.function_name == 'insertAgentClient':
    operations.insert_agent_client(
      args.uid,
      args.username,
      args.email,
      args.card_number,
      args.card_holder,
      args.expiration_date,
      args.cvv,
      args.zip,
      args.interests,
    )

  elif args.function_name == 'addCustomizedModel':
    operations.add_customized_model(args.mid, args.bmid)

  elif args.function_name == 'deleteBaseModel':
    operations.delete_base_model(args.bmid)

  elif args.function_name == 'listInternetService':
    operations.list_internet_service(args.bmid)

  elif args.function_name == 'countCustomizedModel':
    operations.count_customized_model(str(args.bmid))

  elif args.function_name == 'topNDurationConfig':
    operations.top_n_duration_config(args.uid, args.N)

  elif args.function_name == 'listBaseModelKeyword':
    operations.list_base_model_keyword(args.keyword)

  elif args.function_name == 'printNL2SQLresult':
    operations.print_nl2sql_result()

def main():
  parser = initialize_arguments()
  args = parser.parse_args()  
  handle_function(args)

if __name__ == '__main__':
  main()