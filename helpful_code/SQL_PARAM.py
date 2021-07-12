def sql_output(df, column):
    lst = []
    for ind, row in df.iterrows():
        lst.append(row[column])

    count =len(lst)
    output = ''
    for y in lst:
        if count>1:
            output =  output+"'" + str(y) + "'" + ","+" "
            count-=1
        else:
            output = output+"'" + str(y) + "'"
    return output

