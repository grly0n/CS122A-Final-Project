import mysql.connector

mydb = mysql.connector.connect(
  user='root',
  database='final_project'
)

cursor = mydb.cursor()

print('DESCRIBE Test')
cursor.execute('DESCRIBE Test')

result = cursor.fetchall()

for x in result:
  print(x)