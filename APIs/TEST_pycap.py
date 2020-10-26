#%%
from redcap import Project
import pprint as pp
from operator import itemgetter
import re
import json
from datetime import datetime

#%%
api_url_pg =
api_key_pg =
project_pg = Project(api_url_pg, api_key_pg)

records_pg = project_pg.export_records()

with open('records_pg_json.txt', 'w') as outfile:
    json.dump(records_pg, outfile, indent=4, sort_keys=False)

#%%
pp.pprint(records_pg[1], sort_dicts=False)

#%%
meta = project.export_metadata()

#%%
for key,value in records[0].items():
    #if key == 'mutation___1':
#    if re.findall('^[a-zA-Z]+', key) in data2:
    print(key, value)

#%%
print(re.findall('^[a-zA-Z]+', "mutation___1"))

#%%
for x in meta:
        for y in x.values():
            if y == 'mutation': print('success')

#%%
print('mutation' in meta.values())

#%%
ti = [{'record_id': '99-999', 'dept_num':'test-999
project.import_records(ti, overwrite = 'overwrite')


#%%
api_url_lf =
api_key_lf = 
project_lf = Project(api_url_lf, api_key_lf)

records_lf = project_lf.export_records()

with open('records_lf_json.txt', 'w') as outfile:
    json.dump(records_lf, outfile, indent=4, sort_keys=False)


#%%
conn = sqlite3.connect('test.db')

#%%
c = conn.cursor()
c.execute("CREATE TABLE records_pg (id varchar(3), data json)")

#%%
for record in records_pg:
    c.execute("insert into records_pg values (?, ?)",[record['record_id'], json.dumps(records_pg)])
    conn.commit()
