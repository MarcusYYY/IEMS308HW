from nltk.stem.porter import PorterStemmer
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')
import re

path = 'output_stopwords.txt'
f = open(path,)
result = []
idx = 0
cach = []
result = []
#to put each word as a single element on a slot 
for row in f:
	cach = row.split(' ')

pattern = r'[^"()\']+\w+[^.,?:"()\']'
cach_ = []
for item in cach:
	# if item[len(item)-1] == '?' or item[len(item)-1] == '.' or item[len(item)-1] == ',' or item[len(item)-1] == ':':
	# 	item = item[0:len(item)-1]
	# if item[0] == '"':
	# 	item = item[1:len(item)]
	try:
		item = re.findall(pattern,item)[0]
		cach_.append(item)
	except Exception,e:
		# print Exception,";",e,item
		continue

for item in cach_:
	idx = idx + 1

	# if idx > 10000:
	# 	break
	# print item
	stemmer = PorterStemmer()
	try:
		item = item.decode('Cp1252','ignore')
		result.append(stemmer.stem(item))
	except Exception,e:
		print Exception,";",e
		continue

file = open('output_of_stem.txt','w')
for item in result:	
	file.write("%s"" " % item)



		