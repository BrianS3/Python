# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:29:25 2020

@author: SekoB
"""

from redcap import Project
import sqlite3
from datetime import datetime

api_url =
api_key_pg =
project_pg = Project(api_url, api_key_pg)

api_key_lf =
project_lf = Project(api_url, api_key_lf)

json_data1 = project_pg.export_records() #original project design
json_data2 = project_lf.export_records() #updated project design

db = sqlite3.connect('')

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

json_2_db(json_data1, db, '')
json_2_db(json_data2, db, '')
