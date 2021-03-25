import cx_Oracle

dsn = cx_Oracle.makedsn("dbhost.example.com", 1521, service_name="orclpdb1")
connection = cx_Oracle.connect("hr", userpwd, dsn, encoding="UTF-8")
cur = connection.cursor()


import pyodbc

server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

import sqlite3

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()


import mariadb

conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"
    )
cur = conn.cursor()

#####Examples#####
dsn_1 = cx_Oracle.makedsn("dbhost.example_1.com", 1521, service_name="orclpdb1")
cnxn_oracle = cx_Oracle.connect("hr", userpwd, dsn, encoding="UTF-8")

server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn_mssql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


oracle_query = """
select employees, id, role, salary from eployees"""

mssql_query = """
select employee, id, start_date, end_date from empl_table """

set1 = pd.read_sql_query(oracle_query, cnxn_oracle)
set2 = pd.read_sql_query(mssql_query, cnxn_mssql)

cnxn_oracle.close()
cnxn_mssql.close()

merge_df = pd.merge(set1, set2, how="inner", left_on = "id", right_on="id")

import pickle

def pickled(filename, data):
	outfile = open(f'folder/{filename}', 'wb')
	pickle.dump(data,outfile)
	outfile.close()

pickled(merge_df.data, merge_df)

#############################################

dsn_1 = cx_Oracle.makedsn("dbhost.example_1.com", 1521, service_name="orclpdb1")
cnxn_oracle = cx_Oracle.connect("hr", userpwd, dsn, encoding="UTF-8")

server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn_mssql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

oracle_query = """
select employees, id, role, salary from eployees"""

or_df = pd.read_sql_query(oracle_query, cnxn_oracle)

def sql_output(df, column):
	lst = []
	for ind, row in df.iterrows():
		lst.append(row[column])

	count = len(lst)
	if count>1000:
		print('query cannot support parameters greater than 1000 objects')
		return None
	output = ''
	for y in lst:
		if count>1:
			output = output+"'"+str(y)+"'"+","+" "
		else:
			output = output+"'"+str(y)+"'"
		count+=1
	return output


sql_param = sql_output(or_df, "id")

mssql_query = f"""
select employee, id, start_date, end_date 
from empl_table 
where id in {sql_param}
"""
ms_df = pd.read_sql_query(mssql_query, cnxn_mssql)