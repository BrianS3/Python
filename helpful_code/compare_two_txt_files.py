handle_1 = open('file1.txt', 'r')
handle_2 = open('file2.txt', 'r')
rhandle_1 = handle_1.readlines()
rhandle_2 = handle_2.readlines()

# for row in rhandle_1:
#     print(row)

def comparison(list1, list2):
    for row in (set(list1).difference(list2)):#values in list 1 that are not in list 2
        obj = row.strip().split('|')
        print('#:{};     Status:{};     Date/time:{}'.format(str(obj[0]).replace(' ', ''), str(obj[2]).replace(' ', ''),str(obj[3]).replace(' ', ''))         ,"""
         """)

print('Items in file 1, not in file 2:', comparison(rhandle_1, rhandle_2))
print('Items in file 2, not in file 1:', comparison(rhandle_2, rhandle_1))
