import re
import nltk
from nltk.chunk import *

path = 'output_Of_CEOname.txt'
file = open(path)
result = []
for row in file:
	row = row.replace('\n','')
	result.append(row)

path_Ceo = 'ceo.csv'
file_ = open(path_Ceo)
ceo_name = {}
cach = []

for row in file_:
	cach = row.split('\r')
count = 0

for item in cach:
	item = item.replace(',',' ')
	item = item.strip()
	firstName = item.split(' ')[0]
	try:
		secondName = item.split(' ')[1]
	except:
		secondName = ''
	if not ceo_name.has_key(firstName):
		ceo_name[firstName] = 1
	if secondName != '':
		if not ceo_name.has_key(secondName):
			ceo_name[secondName] = 1

finalresult = []
for item in result:
	if ceo_name.has_key(item):
		finalresult.append(item)
output = open('True_ceoName.txt','w')
for item in finalresult:
	output.write("%s " % item)
