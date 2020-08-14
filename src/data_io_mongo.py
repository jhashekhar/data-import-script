"""
insert data in database

mongodb hierarchy
-----------------
database -> collections -> documents -> values
"""

import json
import csv

import os
import argparse
import pprint

from pymongo import MongoClient


parser = argparse.ArgumentParser()

parser.add_argument(
    "--folder", help='folder containing the data files')

parser.add_argument(
    "--database", help="Input the database that you want to insert data to")

args = parser.parse_args()


# read a single .csv file
def read_csv(root, filename, delimiter=','):
    data = {}
    with open(os.path.join(root, filename), 'r') as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        count = 0

        for row in csv_reader:
            if count == 0:
                for k in row:
                    data[k] = []
            else:
                for k, v in zip(list(data.keys()), row):
                    data[k].append(v)
            count += 1
    return data


# read a single .json file
def read_json(root, filename):
    with open(os.path.join(root, filename), 'r') as f:
        data = json.load(f)

    return data


# insert data into the database with appropritate structure
def insert_data(database=None, collection=None):
    return


# make connection with MongoClient
client = MongoClient('localhost', 27017)

# getting a database
db = client['first_db']


# getting a collection
def add_collection_to_db(db=None, collection=None, data=None):
    # get a list of collections from the db if there is none
    # then add this collection
    if collection in db.list_collection_names():
        print(f"Collection {collection} in database {db} exists")
    else:
        print(f"Creating collection {collection}...")
        add_document(db=db, collection=collection, data=data)


# getting a single document
def add_document(db, collection, data=None):
    posts = db.posts
    posts.insert_one(data)
    print("Inserting data is successful.")

# querying


"""
    TODO: Parse the json, csv data and insert them into the database
          and then run queries

Insertion
---------
Data parsed from .csv/.json -> insert as document in mongo database.

"""


if __name__ == "__main__":

    # connect with MongoClient()
    client = MongoClient()
    client = MongoClient('localhost', 27017)

    # get the database
    db = client[args.database]

    all_files = os.listdir(args.folder)
    print("Searching files done")
    files = [f for f in all_files if ('.json' or '.csv') in f]
    pprint.pprint(files)

    for f in files:
        # parse the files
        if '.json' in f:
            data = read_json(root='data/', filename=f)

            collection = add_collection_to_db(
                    db=db, collection=f[-5], data=data)

        else:
            data = read_csv(root='data/', filename=f, delimiter=',')

        # create a new document

        # insert the data parsed from the .csv/.json file into the collection
