from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import pandas as pd
import sys
reload(sys)  
# sys.setdefaultencoding('Cp1252')

#depict the files' paths
result = []
for month_ in range(1,13):
	for day_ in range(1,32):
		month_cach = ''
		day_cach = ''

		if month_ < 10:
			month_cach = '0' + str(month_)
		else:
			month_cach = str(month_)
		if day_ < 10:
			day_cach = '0' + str(day_)
		else:
			day_cach = str(day_)
		path = '2014/2014-' + month_cach + '-' + day_cach + '.txt'
		print path
		try:
			f = open(path)
		except Exception,e:
			print Exception,";",e
			continue
		raw = []
		for line in f:
			raw.append(line)

		for item in raw:
			try:
				item = item.decode('Cp1252','ignore')
				result.extend(sent_tokenize(item))
			except Exception,e:
				print Exception,";",e
				continue
file = open('output.txt','w')
for item in result:
	try:
		item = item.decode('Cp1252','ignore')
		file.write("%s\n" % item)
	except:
		continue
	

