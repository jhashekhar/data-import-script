
import mysql.connector
from mysql.connector import errorcode


table_name = 'gameofthrones'
create_table = f"CREATE TABLE {table_name} (name VARCHAR(20), power VARCHAR(20), sex CHAR(10));"


cnx = mysql.connector.connect(user='jon', password='password')
cursor = cnx.cursor()



cursor.execute("USE first_db")
cursor.execute(create_table)


cursor.close()
