import os

def showPredResult(file_dir):       
	f = open(file_dir, 'r')
	data = f.read()
	f.close()
	return data

