import psycopg2
from psycopg2 import sql

#establishing the connection

try:
	conn = psycopg2.connect(database="cctest", user='postgres', password='321321', host='127.0.0.1', port= '5432')
except:
	print("Cannot Connect")	

conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = '''CREATE database mydb''';

cursor.execute(sql)

#cursor.execute(sql.SQL('CREATE DATABASE {};').format(
 #   sql.Identifier('cctest')))

sql ='''CREATE TABLE Amir(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)



#crusor.execute(sql.SQL('CREATE TABLE rolan (
#try:
 #       cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#except:
#        print("I can't drop our test database!")

conn.close()
cursor.close()
#print("Table created successfully........")



#Closing the connection
#conn.close()
