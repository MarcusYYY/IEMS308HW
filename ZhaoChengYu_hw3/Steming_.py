from nltk.stem.porter import PorterStemmer
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')


path = 'output_stopwords.txt'
f = open(path,)
result = []
idx = 0
cach = []
result = []
#to put each word as a single element on a slot 
for row in f:
	cach = row.split(' ')
	
for item in cach:
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



		