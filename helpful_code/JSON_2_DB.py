import sqlite3
from datetime import datetime
import json

def read_json(file):
    with open(file) as f:
        json_data = json.load(f)
    return json_data

file1 = 'meta.txt'
file2 = 'records.txt'

json_meta = read_json(file1)
json_records = read_json(file2)

db = sqlite3.connect('.db')

def json_2_db(json_data, database, table):
    columns = []
    column = []
    for data in json_data:
        column = list(data.keys())
        for col in column:
            if col not in columns:
                columns.append(col)

    value = []
    values = []
    for data in json_data:
        for i in columns:
            value.append(str(dict(data).get(i)))
        values.append(list(value))
        value.clear()


    create_query = "create table if not exists {0} ({1})".format(table," text,".join(columns))
    insert_query = "insert into {0} ({1}) values (?{2})".format(table,",".join(columns), ",?" * (len(columns)-1))
    print("insert has started at " + str(datetime.now()))
    c = db.cursor()
    c.execute(create_query)
    c.executemany(insert_query , values)
    values.clear()
    db.commit()
    c.close()
    print("insert has completed at " + str(datetime.now()))
