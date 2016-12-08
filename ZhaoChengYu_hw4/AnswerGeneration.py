import nltk
import Query_generation as Qg
import QuestionClassifier as QC
from nltk.tokenize import sent_tokenize
from nltk.chunk import *
import operator
from nltk.corpus import stopwords
import math as m
from fractions import Fraction
import re 

Document_set = Qg.Document_subset(Qg.ans,20)
stop = set(stopwords.words('english'))

def Rule_Based_AnswerSystem(Question):
	Question_class = QC.test_questions(Question)
	# rule = {'PERSON':'HUM','GPE':'LOC','NNP':['ENTY','DESC'],'NN':['ENTY','DESC'],'CD':'NUM','NNS':['ENTY','DESC']}
	rule = {'HUM':'PERSON','LOC':'GPE','ENTY':['NNP','NN','NNS'],'DESC':['NNP','NN','NNS'],'NUM':'CD','ABBR':['NNP','NN','NNS']}
	Ans_class = rule[Question_class]
	return Ans_class

def filterAnsByLabel(Document_set,Ans_class):
	Ans_Back_up = []
	for Document in Document_set:
		file = open(Document)
		for row in file:
			row = row.replace('\r','')
			row = row.replace('\n','')
			try:
				sentence = sent_tokenize(row)
			except:
				continue
			for singleSentence in sentence:
				flag = False
				words = singleSentence.split()
				for word in words:
					if Query_term.has_key(word) and flag == False:
						Ans_Back_up.append(singleSentence)
						flag = True

	final_ans = []
	for sentence in Ans_Back_up:
		flag = False
		token = nltk.word_tokenize(sentence)
		pos_tags = nltk.pos_tag(token)
		result_ = nltk.ne_chunk(pos_tags,binary = False)
		for item in result_:
			try:
				if item.label() == Ans_class and flag == False:
					final_ans.append(sentence)
					flag = True
			except:
				if flag == False:
					if len(Ans_class) == 3:
						inerflag = False
						for tag in pos_tags:
							if tag[1] == 'CD':
								inerflag = True
						if inerflag == False:
							final_ans.append(sentence)
							flag = True
					elif Ans_class == 'CD':
						if item[1] == 'CD':
							final_ans.append(sentence)
							flag = True
	return final_ans

def bigrams(sentence):
	stop = set(stopwords.words('english'))
	Q = nltk.word_tokenize(sentence)
	result = []
	result.extend([i for i in Q if i not in stop])
	result_bigram = list(nltk.bigrams(result))
	return result_bigram

def Answer_Score_System(Ans_set,question_):
	question = nltk.word_tokenize(question_)
	pattern = r'[^A-Za-z0-9\s]+'
	question = re.sub(pattern,'',question_)
	question_bigram = list(nltk.bigrams(question))
	Number_of_Same_word = 0 
	total_score = {}
	for sentence in Ans_set:
		label = sentence
		score = 0
		sentence = nltk.word_tokenize(sentence)
		sentence_bigram = list(nltk.bigrams(sentence))
		#score of bigram match
		for bigram in question_bigram:
			for item in sentence_bigram:
				if item == bigram:
					score = score + 2
		#score of unigram match
		for item in question:
			for word in sentence:
				if word == item:
					score = score + 1
		score = Fraction(score,len(sentence))
		total_score[label] = score
	answer = sorted(total_score.iteritems(), key = operator.itemgetter(1),reverse = True)
	# answer = total_score
	return answer

def TF_IDF(Ans_set,question_):
	total_Num = len(Qg.All_relevant_Document)
	question_term = Qg.Question_term(question_)
	df = Doucment_Frequency(question_term,Qg.All_relevant_Document)
	print df
	mark = []
	for key,val in df.iteritems():
		if val == 0:
			mark.append(key)
	TFIDF = {}
	for each_sentence in Ans_set:
		each_sentence = each_sentence.replace(',','')
		each_sentence = each_sentence.replace('|','')

		sentence_ = nltk.word_tokenize(each_sentence)
		sentence = []
		for word in sentence_:
			if word not in stop:
				sentence.append(word)
		
		tf = Term_frequency(question_term,sentence)
		mean = Average_len(Ans_set)
		Num = len(sentence)
		score = 0
		for eachterm,termval in tf.iteritems():
			if termval != 0:
				TF = 0.5 + 0.5 * termval/Num
				IDF = m.log(Fraction(total_Num,df[eachterm]))
				# score = score + TF * IDF
				score = score + TF * IDF
			else :
				TF = 0.5 + 0.5 * termval/Num
				IDF = m.log(Fraction(total_Num,df[eachterm]))
				# score = score - TF * IDF
				score = score - TF * IDF
		TFIDF[each_sentence] = score
	return sorted(TFIDF.iteritems(), key=operator.itemgetter(1),reverse = True)
	# return TFIDF

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
def question_Term(question):
	question = question.replace('?','')
	question_ = nltk.word_tokenize(question)
	pos_tags = nltk.pos_tag(question_)
	question = []
	for item in pos_tags:
		if item[0] != 'Which':
			if item[1] == 'NNP' or item[1] == 'NNS' or item[1] == 'NN' or item[1] == 'CD' or item[1] == 'JJ':
				question.append(item[0])
	question_term = {}
	#create question term
	for item in question:
		if not question_term.has_key(item):
			question_term[item] = 1
		else:
			question_term[item] = question_term[item] + 1
	return question_term 

def Term_frequency(queryterm,sentence):
	tf = dict.fromkeys(queryterm.keys(),0)
	for word in sentence:
		if queryterm.has_key(word):
			tf[word] = tf[word] + 1
	return tf		

def max_term(sentence):
	max_term = {}
	for word in sentence:
		if max_term.has_key(word):
			max_term[word] = max_term[word] + 1
		else:
			max_term[word] = 1
	return max(max_term.iteritems(), key = operator.itemgetter(1))[1]

def Document_subset(subset,Num):
	result = []
	for i in range(0,Num):
		result.append(subset[i][0])
	return result

def Average_len(Allset):
	Idx = 0
	length = 0
	pattern = r'[^A-Za-z0-9\s]+'
	for sentence in Allset:
		sentence = re.sub(pattern,'',sentence)
		result = []
		for word in sentence:
			if word not in stop:
				result.append(word)
		length = length + len(result)
		Idx = Idx + 1
	return Fraction(length,Idx)


Query_term = dict.fromkeys(Qg.queryterms.keys(),0)
Ans_type = Rule_Based_AnswerSystem(Qg.question)

ansset = filterAnsByLabel(Document_set,Ans_type)
# ansset = Document_set
# print Answer_Score_System(ansset,Qg.question)
ans = TF_IDF(ansset,Qg.question)
ans_sub = Document_subset(ans,20)

print ans_sub

