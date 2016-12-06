import re
import nltk
from nltk.corpus import stopwords
import math as m
import operator

#find the document which contains at least one of the keywords
def DocumentRetrieve(path,keywords):
	file = open(path)
	flag = False
	for row in file:
		for word in row:
			if keywords.has_key(word):
				flag = True
				break
	if flag:
		return path
	else:
		return ''

# score the file that contains keywords
def TF_IDF(keywords,All_relevant_Document,totalNum):
	
	qtf = keywords

	df = Doucment_Frequency(keywords,All_relevant_Document)
	total_tf = {}
	for document in All_relevant_Document:
		tf = Term_Frequencey(keywords,document)
		if tf != {}:
			total_tf[document] = tf
	TFIDF = {}
	for key,val in total_tf.iteritems():
		max_term = maximumTerm(key)
		term = val
		score = 0
		for eachterm,value in term.iteritems():
			TF = 0.5 + 0.5 * value/max_term
			IDF = m.log(totalNum/df[eachterm])
			tf_idf = TF * IDF
			score = score + tf_idf
		TFIDF[key] = score
	return 	max(TFIDF.iteritems(), key=operator.itemgetter(1))

def maximumTerm(Document):
	file = open(Document)
	Maximum_term = {}
	stop = set(stopwords.words('English'))
	for row in file:
		row = row.replace('\n','')
		words = row.split(' ')
		for word in words:
			if word not in stop and word != 'The' and word != 'I' and word != 'Would' and word != 'would':
				if not Maximum_term.has_key(word):
					Maximum_term[word] = 1
				else:
					Maximum_term[word] = Maximum_term[word] + 1
	return max(Maximum_term.iteritems(), key=operator.itemgetter(1))[1]



def Doucment_Frequency(queryterms,All_relevant_Document):
	df = dict.fromkeys(queryterms.keys(),0)
	for term in df:
		for document in All_relevant_Document:
			flag = False
			file = open(document)
			for row in file:
				row = row.replace('\n','')
				words = row.split(' ')
				for word in words:
					if word == term:
						df[term] = df[term] + 1
						flag = True
						break
				if flag == True:
					break
	return df

def Term_Frequencey(queryterms,Document):
	tf = {}
	file = open(Document)
	for row in file:
		row = row.replace('\n','')
		words = row.split(' ')
		for word in words:
			if queryterms.has_key(word) and not tf.has_key(word):
				tf[word] = 1
			elif queryterms.has_key(word) and tf.has_key(word):
				tf[word] = tf[word] + 1
	return tf

path = 'train_1000.label.txt'
stop = set(stopwords.words('english'))
file = open(path)
cach = []
question = []
key_words = {}

for row in file:
	sentence = row.split(' ',1)[1].replace('\n','')
	question.append(sentence)
	token = nltk.word_tokenize(sentence)
	pos_tags = nltk.pos_tag(token)
	cach.extend([i for i in sentence.split() if i not in stop])
	for item in pos_tags:
		try:
			if item[1] == 'NNP' or item[1] == 'NN' or item[1] == 'NNS' or item[1] == 'JJ' and not key_words.haskey(item[0]):
				key_words[item[0]] = 1
			elif item[1] == 'NNP' or item[1] == 'NN' or item[1] == 'NNS' or item[1] == 'JJ' and key_words.haskey(item[0]):
				key_words[item[0]] = key_words[item[0]] + 1
		except:
			continue

#define the document list 
All_relevant_Document = []

for year in range(3,5):
	for month in range(1,13):
		for day in range(1,32):

			if month < 10 and day < 10:
				file_path ='201' + str(year) + '/' + '201' + str(year) + '-0' + str(month) + '-0' + str(day) + '.txt'
			elif month < 10 and day >= 10:
				file_path ='201' + str(year) + '/' + '201' + str(year) + '-0' + str(month) + '-' + str(day) + '.txt'
			elif month > 10 and day < 10:
				file_path ='201' + str(year) + '/' + '201' + str(year) + '-' + str(month) + '-0' + str(day) + '.txt'
			else:
				file_path ='201' + str(year) + '/' + '201' + str(year) + '-' + str(month) + '-' + str(day) + '.txt'
			document = ''
			try:
				document = DocumentRetrieve(file_path,key_words)
			except Exception,e:
				continue
			if document != '':
				All_relevant_Document.append(document)

queryterms = {'Apple':1,'Tim':1}
print TF_IDF(queryterms,All_relevant_Document,730)





