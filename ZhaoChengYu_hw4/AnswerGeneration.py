import nltk
import Query_generation as Qg
import QuestionClassifier as QC
from nltk.tokenize import sent_tokenize
from nltk.chunk import *
import operator


Document_set = Qg.Document_subset(Qg.ans,4)


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
				continue

	print 'This is the back_up answer.----------------------------------------------------'
	print  len(Ans_Back_up)
	print 'This is the final_ans without score.-----------------------------------------------'
	print  len(final_ans)



Query_term = dict.fromkeys(QG.queryterms.keys(),0)
Ans_type = Rule_Based_AnswerSystem(question)
filterAnsByLabel(Document_set,Ans_type)


