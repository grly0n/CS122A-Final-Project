from arguments import initialize_arguments

def main():
  parser = initialize_arguments()
  args = parser.parse_args()
  print(args)

if __name__ == '__main__':
  main()