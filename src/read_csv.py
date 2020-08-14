import csv
import json


def read_csv(filename, delimiter=','):
    data = {}
    with open(filename, 'r') as f:
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


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    print(data)


# read_csv('src/disaster_train.csv')
read_json('data/station-information-9.json')
