
# main.py

import argparse
import csv

import mysql.connector
from mysql.connector import errorcode

parser = argparse.ArgumentParser()

parser.add_argument("--filename", help="enter the csv filename, file should be in the same directory as the script")

args = parser.parse_args()




def read_file(filename, delimiter=','):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                columns = row

                line_count += 1
            else:
                # print(row)
                line_count += 1

            if line_count == 10:
                break

    return columns


# first query will be to create a table in the database with the same name(minus the extension)
# and structure as the csv file if the table doesn't already exists.

DB = 'first_db'

cnx = mysql.connector.connect(user='jon', password='password')
cursor = cnx.cursor()


def createTable(tablename, columns):
    column_query = ""

    for col in columns:
        column_query += col + " VARCHAR(20), "

    column_query = column_query[:-2]
    create_table = f"CREATE TABLE {tablename} ({column_query});"

    print("Query")
    print(column_query)
    try:
        print(f"Creating table: {tablename}")
        cursor.execute(create_table)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"Table '{tablename}' already exists.")

        else:
            print(err.msg)


if __name__ == "__main__":

    columns = read_file(args.filename)

    print(args.filename, args.filename[:-4])
    print(columns)

    cursor.execute(f"USE {DB}")
    createTable(args.filename[:-4], columns)





