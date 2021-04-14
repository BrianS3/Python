def listToString(s):
    str1= " "
    return(str1.join(s))

def extract_string(dataframe, column, regex, new_column=None):
    if new_column == None:
        dataframe[column] = dataframe[column].apply(lambda x: re.findall(regex, x))
        dataframe[column] = dataframe[column].apply(lambda x: listToString(x))
        dataframe[column] = dataframe[column].apply(lambda x: x.lstrip())
        return dataframe[column]
    else:
        dataframe[new_column] = dataframe[column].apply(lambda x: re.findall(regex, x))
        dataframe[new_column] = dataframe[new_column].apply(lambda x: listToString(x))
        dataframe[new_column] = dataframe[new_column].apply(lambda x: x.lstrip())
        return dataframe[new_column]
