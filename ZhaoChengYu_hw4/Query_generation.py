import re
import nltk
from nltk.corpus import stopwords
import math as m
import operator
from fractions import Fraction

#Question term generator
def Question_term(question):
	stop = set(stopwords.words('English'))
	token = nltk.word_tokenize(question)
	cach = []
	for word in token:
		if word not in stop:
			cach.append(word)
	pos_tags = nltk.pos_tag(cach)
	query_term = {}
	for item in pos_tags:
		if item[1] == 'NNP' or item[1] == 'NN' or item[1] == 'JJ' or item[1] == 'NNS' or item[1] == 'VBD' and not query_term.has_key(item[0]):
			query_term[item[0]] = 1
		elif item[1] == 'NNP' or item[1] == 'NN' or item[1] == 'JJ' or item[1] == 'NNS' or item[1] == 'VBD' and query_term.has_key(item[0]):
			query_term[item[0]] = query_term[item[0]] + 1
	return query_term

#find the document which contains at least one of the keywords
def DocumentRetrieve(path,keywords):
	file = open(path)
	flag = False
	for row in file:

		row = row.replace('\n','')
		row = row.replace('\r','')
		row = row.split()
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
			TF = 0.5 + (0.5 * value/max_term)
			IDF = m.log(Fraction(totalNum,df[eachterm]))
			# IDF = m.log(float(totalNum/df[eachterm]))
			tf_idf = TF * IDF
			score = score + tf_idf
		if score != 0:
			TFIDF[key] = score

	return 	sorted(TFIDF.iteritems(), key=operator.itemgetter(1),reverse = True)

#compute the maximum term frequency of a specific document
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

# compute document_frequency
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

# compute Term_frequency
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

# find  Num Documents with high score 
def Document_subset(Document,Num):
	result = []
	for i in range(0,Num):
		result.append(Document[i][0])
	return result

# find all documents that contains at least one word
def All_Document(key_words):
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
	return All_relevant_Document

question = 'Who is the CEO of Facebook?'
queryterms = Question_term(question)
All_relevant_Document = All_Document(queryterms)
ans = TF_IDF(queryterms,All_relevant_Document,len(All_relevant_Document))
print Document_subset(ans,5)









