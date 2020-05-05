import csv

#def file_load(filename):

content = []
facility_dict = {}
with open('CTMS_LaborPool_Extract_202005010002.csv') as csvfile:
    linereader = csv.reader(csvfile, delimiter = ',')
    for row in linereader:
        content.append(row)

for lhead in content[:1]:
    header = lhead

for line in content[1:]:
    fac_code = line[7]
    if fac_code in facility_dict:
        facility_dict[fac_code].append(line)
    else:
        facility_dict[fac_code] = []
        facility_dict[fac_code].append(line)

for key in facility_dict:
        with open('Department_{}.csv'.format(key), 'w') as csvwrite:
            filewriter = csv.writer(csvwrite, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(header)
            for line in facility_dict[key]:
                filewriter.writerow(line)

