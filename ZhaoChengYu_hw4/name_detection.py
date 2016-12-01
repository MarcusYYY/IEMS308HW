import re
import os.path
import nltk

def catgoryDection(data):
	cach = {}
	for item in data:
		if not cach.has_key(item[1]):
			cach[item[1]] = 1
		else:
			cach[item[1]] = cach[item[1]] + 1
	return cach

fpath = 'output_of_ceo.txt'
file = open(fpath)
result = []
for row in file:
	result = row.split(' ')
result = result[0:len(result)-1]
things = nltk.pos_tag(result)
print things
print catgoryDection(things)