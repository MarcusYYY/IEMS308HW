import sys
from nltk.corpus import stopwords
reload(sys)  
sys.setdefaultencoding('Cp1252')
# nltk.download('stopword')
path = 'output.txt'
f = open(path)
result = []

#define the subset of stop words
stop = set(stopwords.words('english'))

for row in f:
	cach = []
	cach.extend([i for i in row.lower().split() if i not in stop])
	result.extend(cach)

file = open('output_stopwords.txt','w')
for item in result:
	# item = item.encode('Cp1252',)
	file.write("%s"" " % item)	



