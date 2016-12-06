import re
import nltk
from nltk.chunk import *
from sklearn import preprocessing
from sklearn import svm
import numpy as np

# -*- coding:utf-8 -*-
sentence = 'who when where how what which whose Other ?'
token = nltk.word_tokenize(sentence)
print token
pos_tags = nltk.pos_tag(token)
print 'pos_tags------------------------------',pos_tags
result_ = nltk.ne_chunk(pos_tags,binary = False)
print 'NER chunk-----------------------------',result_
feature = 'wh-word ,numbers of NNP , first word tag after wh-word'

#create question training set
path = 'train_1000.label.txt'
file = open(path)
label = []
w_word = []
first_word = []
lengthof_NNP = []
question = []
# pattern = "WH:{(<WP>|<WRB>|<WDT>|<WP$>)+(<VBD>|<NN>|<VBZ>|<MD>|<VBP>|<JJ>|<CD>|<VB>|<VBG>)}"
pattern = "NP:{<DT>?<JJ>*<NN>}"
NPChunker = nltk.RegexpParser(pattern)
result = NPChunker.parse(pos_tags)
dic_wh = {'Who':1,"When":2,"Where":3,"How":4,"What":5,"Which":6,"Whose":7,"Other":8}
dic_firstword = {'VBD':1,'NN':2,'VBZ':3,'MD':4,'VBP':5,'JJ':6,'CD':7,'VB':8,'VBG':9,'NNS':10,'PRP':11,'WDT':12,'NNP':13,'RB':14}
dic_label = {'ABBR':0,'DESC':1,'ENTY':2,'HUM':3,'LOC':4,'NUM':5,'Other':6}
final_train = []
dic_second = {}

le = preprocessing.LabelEncoder()
for row in file:
	label = row.split(':',1)[0]
	question.append(row.split(' ',1)[1].replace('\n',''))
	token = nltk.word_tokenize(row.split(' ',1)[1].replace('\n',''))
	pos_tags = nltk.pos_tag(token)
	w_word.append(pos_tags[0][0])
	first_word.append(pos_tags[1][1])
	count = 0
	if not dic_second.has_key(pos_tags[2][1]):
		dic_second[pos_tags[2][1]] = 1
	for item in pos_tags:
		if item[1] == 'NNP':
			count = count + 1
	lengthof_NNP.append(count)
	sub = []
	#w_word:
	if dic_wh.has_key(pos_tags[0][0]):
		sub.append(dic_wh[pos_tags[0][0]])
	else:
		sub.append(8)
	#len of NNP
	sub.append(count)
	#first_non wh word POS label
	if dic_firstword.has_key(pos_tags[1][1]):
		sub.append(dic_firstword[pos_tags[1][1]])
	else:
		sub.append(15)

	#classLabel
	if dic_label.has_key(label):
		sub.append(dic_label[label])
	else:
		sub.append(6)
	#throw all rows into final_result
	final_train.append(sub)
	# result = NPChunker.parse(pos_tags)
	# try:
	# 	print'---------------------result'
	# 	print result
	# except Exception,e:
	# 	print e
	# 	continue
result = []
for key in dic_second:
	result.append(key)
print result





