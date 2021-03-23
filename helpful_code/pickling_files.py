import pickle

def pickled(filename, data):
	outfile = open(f'folder/{filename}', 'wb')
	pickle.dump(data,outfile)
	outfile.close()