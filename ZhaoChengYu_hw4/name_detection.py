import re
import nltk
from nltk.chunk import *


def catgoryDection(data):
	cach = {}
	for item in data:
		if not cach.has_key(item[1]):
			cach[item[1]] = 1
		else:
			cach[item[1]] = cach[item[1]] + 1
	return cach

path = 'output.txt'
path_Ceo = 'ceo.csv'
file_ = open(path_Ceo)
ceo_name = {}
count = 0 
for row in file_:
	if not ceo_name.has_key(row):
		ceo_name[row] = 1
	else:
		ceo_name[row] = ceo_name[row] + 1

file = open(path)
sentence = ''
token = []

for row in file:
	count = count + 1
	if count > 1000:
		break
	try:
		tokens = nltk.word_tokenize(row)
		token.extend(tokens)
	except Exception,e:
		continue
pos_tags = nltk.pos_tag(token)
# pattern = "DT:{<NP>?<JJ>*<NN>}"
# NPChunker = nltk.RegexpParser(pattern)
# result = NPChunker.parse(pos_tags)
result_ = nltk.ne_chunk(pos_tags)
names = {}
print '-----------------------------------'
for item in result_:
	try:
		if len(item) < 2:
			if item.label() == 'PERSON':
				if not names.has_key(item[0][0]):
					names[item[0][0]] = 1
				else:
					names[item[0][0]] = names[item[0][0]] + 1
	except:
		continue
finalresult = {}

for key in names:
	if not ceo_name.has_key(key):
		finalresult[key] = 1
	else:
		finalresult[key] = finalresult[key] + 1
output = open('output_Of_CEOname.txt','w')

for key in finalresult:
	try:
		item = key.decode('cp1252','ignore')
		output.write("%s\n" % item)
	except:
		continue


# st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
# print st.tag('What is the airspeed of an unladen swallow ?'.split())
