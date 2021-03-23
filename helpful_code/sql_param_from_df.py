def sql_output(df, column):
	lst = []
	for ind, row in df.iterrows():
		lst.append(row[column])

	count = len(lst)
	if count>1000:
		print('query cannot support parameters greating than 1000 objects')
		return None
	output = ''
	for y in lst:
		if count>1:
			output = output+"'"+str(y)+"'"+","+" "
		else:
			output = output+"'"+str(y)+"'"
		count+=1
	return output