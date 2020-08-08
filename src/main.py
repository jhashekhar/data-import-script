# main.py

import argparse
import csv

import mysql.connector
from mysql.connector import errorcode


parser = argparse.ArgumentParser()

parser.add_argument(
    "--filename", 
    help="enter the csv filename, file should be in the same directory as the script")

args = parser.parse_args()


# read the files and create table
def readFile(filename, delimiter=','):
    """
    reads the csv file and returns the column head of the csv file
    """
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        count = 0
        tablename = filename[:-4]
        data = []

        for row in csv_reader:
            if count == 0:
                columns = row
                # first row - headers/feature names
                createTable(tablename, columns)
                count += 1
            else:
                data.append(tuple(row))        
                count += 1

    return columns, data


def createTable(tablename, columns):
    column_query = ""

    for col in columns:
        column_query += col + " VARCHAR(200), "   # how to make this VARCHAR() length flexible

    column_query = column_query[:-2]    # remove the space and comma
    create_table = f"CREATE TABLE {tablename} ({column_query});"
    
    try:
        print(f"Creating table: {tablename}")
        cursor.execute(create_table)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"Table '{tablename}' already exists.")

        else:
            print(err.msg)


if __name__ == "__main__":

    DB = 'first_db'  # local database -- already existing

    cnx = mysql.connector.connect(user='jon', password='password')
    cursor = cnx.cursor()
    cursor.execute(f"USE {DB}")

    print(f"Using local database: {DB}")
    print("-"*30)

    # feature/column header, data(rest of the values)
    columns, data = readFile(args.filename)

    # INSERT INTO filename (c1, c2, ...) VALUES (%s, %s, ...)
    query = f"INSERT INTO {args.filename[:-4]} ({', '.join(columns)}) VALUES ({', '.join(str('%s '*len(columns)).split())})"

    print("Inserting data...")
    
    cursor.executemany(query, data)
    cnx.commit()
    
    print(f"{cursor.rowcount} rows were inserted in the table: {args.filename[:-4]}")
    print('Done!')


