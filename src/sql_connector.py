"""
    Goal of this script
    -------------------

    * Connect to an existing database
    * Add tables to the existing database
    * Create a new database
    * Add tables to this new database

"""


import mysql.connector
from mysql.connector import errorcode



# connect to an existing database
# cnx = mysql.connector.connect(user='jon', password='password',
#                              host='127.0.0.1', database='first_db')



DB_NAME = 'first_db'

TABLES = {}

TL = 'LIGHTYEAR'


TABLES[TL] = (
    f""CREATE TABLE `{TL}`" ("
    "`id` int(9) NOT NULL AUTO_INCREMENT,"
    "`founding_year` date NOT NULL,"
    "`category` varchar(40) NOT NULL,"
    "`market` varchar(20) NOT NULL,"
    "`total_funding` int(15) NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


TABLES['startups'] = (
    "CREATE TABLE `startups` ("
    "`id` int(9) NOT NULL AUTO_INCREMENT,"
    "`founding_year` date NOT NULL,"
    "`category` varchar(40) NOT NULL,"
    "`market` varchar(20) NOT NULL,"
    "`total_funding` int(15) NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


TABLES['funding'] = (
    "CREATE TABLE `funding` ("
    " `id` int(9) NOT NULL AUTO_INCREMENT,"
    " `seed` int(12) NOT NULL,"
    " `angel` int(12) NOT NULL,"
    " `series_A` int(12) NOT NULL,"
    " `series_B` int(12) NOT NULL,"
    " `series_C` int(12) NOT NULL,"
    " `series_D` int(12) NOT NULL,"
    " `series_E` int(12) NOT NULL,"
    " `series_F` int(12) NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='jon', password='password')
cursor = cnx.cursor()


# create a database
def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf-8'")

    except mysql.connector.Error as err:
        print(f"Failed creating databse: {DB_NAME}")
        exit(1)


# if database exists then use the existing database else create the new one
# if there is any error the application exits

try:
    cursor.execute(f"USE {DB_NAME}")

except mysql.connector.Error as err:
    print(f"Database {DB_NAME} doesn't exists.")
    if err.errno == errorcode.ERR_BAD_DB_ERROR:
        create_database(DB_NAME)
        print(f"Database {DB_NAME} created successfully.")
        cnx.database = DB_NAME

    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print(f"Creating table: {table_name}")
        cursor.execute(table_description)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists")
        else:
            print(err.msg)

    else:
        print("OK")


cursor.close()
cnx.close()














