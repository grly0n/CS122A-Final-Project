import argparse


def initialize_arguments() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser('project.py')
  subparser = parser.add_subparsers(dest='function_name', required=True)
  
  # import [folderName:str]
  import_data = subparser.add_parser('import', help='Import new database from .csv file')
  import_data.add_argument('folderName', type=str, help='Path to .csv file containing database information')

  # insertAgentClient [uid:int] [username:str] [email:str] [card_number:int] [card_holder:str] [expiration_date:date] [cvv:int] [zip:int] [interests:str]
  insert_agent = subparser.add_parser('insertAgentClient', help='Insert new agent client to tables')
  arguments = {'uid': int, 'username': str, 'email': str, 'card_number': int, 'card_holder': str, 'expiration_date': str, 'cvv': int, 'zip': int, 'interests': str}
  for arg, arg_type in arguments.items():
    insert_agent.add_argument(arg, type=arg_type)

  # addCustomizedModel [mid:int] [bmid:int]
  add_custom_model = subparser.add_parser('addCustomizedModel', help='Add new customized model to tables')
  add_custom_model.add_argument('mid', type=int)
  add_custom_model.add_argument('bmid', type=int)

  # deleteBaseModel [bmid:int]
  delete_base_model = subparser.add_parser('deleteBaseModel', help='Delete base model from tables')
  delete_base_model.add_argument('bmid', type=int)

  #  listInternetService [bmid:int]
  list_internet_service = subparser.add_parser('listInternetService', help='List internet services used by base model')
  list_internet_service.add_argument('bmid', type=int)

  # countCustomizedModel [bmid:int]
  count_customized_model = subparser.add_parser('countCustomizedModel', help='Count customized models built from base model')
  count_customized_model.add_argument('bmid', type=int)

  # topNDurationConfig [uid:int] [N:int]
  top_n_duration_config = subparser.add_parser('topNDurationConfig', help='List longest duration configurations managed by agent client')
  top_n_duration_config.add_argument('uid', type=int)
  top_n_duration_config.add_argument('N', type=int)

  # listBaseModelKeyWord [keyword:str]
  keyword_search = subparser.add_parser('listBaseModelKeyword', help='List models using LLM services containing keyword')
  keyword_search.add_argument('keyword', type=str)

  # nl2sql (later...)

  return parser


def main():
  parser = initialize_arguments()
  args = parser.parse_args()
  print(args)

if __name__ == '__main__':
  main()