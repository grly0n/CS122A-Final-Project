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
    insert_agent.add_argument(arg)

  # addCustomizedModel [mid:int] [bmid:int]
  add_custom_model = subparser.add_parser('addCustomizedModel', help='Add new customized model to tables')
  add_custom_model.add_argument('mid')
  add_custom_model.add_argument('bmid')

  # deleteBaseModel [bmid:int]
  delete_base_model = subparser.add_parser('deleteBaseModel', help='Delete base model from tables')
  delete_base_model.add_argument('bmid')

  #  listInternetService [bmid:int]
  list_internet_service = subparser.add_parser('listInternetService', help='List internet services used by base model')
  list_internet_service.add_argument('bmid')

  # countCustomizedModel [bmid:int]
  count_customized_model = subparser.add_parser('countCustomizedModel', help='Count customized models built from base model')
  count_customized_model.add_argument('bmid', nargs='+')

  # topNDurationConfig [uid:int] [N:int]
  top_n_duration_config = subparser.add_parser('topNDurationConfig', help='List longest duration configurations managed by agent client')
  top_n_duration_config.add_argument('uid')
  top_n_duration_config.add_argument('N')

  # listBaseModelKeyWord [keyword:str]
  keyword_search = subparser.add_parser(
    'listBaseModelKeyWord',
    help='List models using LLM services containing keyword'
  )
  keyword_search.add_argument('keyword', type=str)

  # nl2sql (later...)
  nl2sql = subparser.add_parser(
    'printNL2SQLresult',
    help='Print NL2SQL experiment results from CSV'
)
  return parser
