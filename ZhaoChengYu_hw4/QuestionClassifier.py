import re
import nltk
from nltk.chunk import *
from sklearn import preprocessing
import numpy as np
from sklearn import svm,cross_validation,metrics
from sklearn.neural_network import MLPClassifier
from sklearn import tree

def test_questions():
	sentence = 'Who is the CEO of FaceBook?'
	token = nltk.word_tokenize(sentence)
	pos_tags = nltk.pos_tag(token)
	sub = []
	#w_word
	if dic_wh.has_key(pos_tags[0][0]):
		sub.append(dic_wh[pos_tags[0][0]])
	else:
		sub.append(8)

	#length of NNP	
	count = 0
	for item in pos_tags:
		if item[1] == 'NNP':
			count = count + 1
	sub.append(count)
	#first_non wh word POS label
	if dic_firstword.has_key(pos_tags[1][1]):
		sub.append(dic_firstword[pos_tags[1][1]])
	else:
		sub.append(15)

	#second_word POS label
	if dic_secondword.has_key(pos_tags[2][1]):
		sub.append(dic_secondword[pos_tags[2][1]])
	else:
		sub.append(26)

	experiment = np.asarray(sub)
	X = experiment

	result = clf.predict(X)
	print sentence
	print '-------------------final_result-----------------------'
	for key,val in dic_label.iteritems():
		if val == result:
			print key
#create question training set
path = 'train_5500.label.txt'
file = open(path)
enc = preprocessing.OneHotEncoder(categorical_features = [0,2,3])

#features
label = []
w_word = []
first_word = []
secd_word = []
lengthof_NNP = []
question = []

dic_wh = {'Who':1,"When":2,"Where":3,"How":4,"What":5,"Which":6,"Whose":7,"Other":8}
dic_firstword = {'VBD':1,'NN':2,'VBZ':3,'MD':4,'VBP':5,'JJ':6,'CD':7,'VB':8,'VBG':9,'NNS':10,'PRP':11,'WDT':12,'NNP':13,'RB':14}
dic_label = {'ABBR':0,'DESC':1,'ENTY':2,'HUM':3,'LOC':4,'NUM':5,'Other':6}
dic_secondword = {'PRP$':1,'VBG':2,'VBD':3,'VBP':4,'WDT':5,'JJ':6,'VBZ':7,'DT':8,'NN':9,'POS':10,'.':11,'PRP':12,'RB':13,':':14,'NNS':15,'NNP':16,'VB':17,'CC':18,'VBN':19,'IN':20,'CD':21,'MD':22,'NNPS':23,'JJS':24,'JJR':25}
final_train = []

for row in file:
	token = nltk.word_tokenize(row.split(' ',1)[1].replace('\n',''))
	pos_tags = nltk.pos_tag(token)
	label = row.split(':',1)[0]
	sub = []
	#w_word
	if dic_wh.has_key(pos_tags[0][0]):
		sub.append(dic_wh[pos_tags[0][0]])
	else:
		sub.append(8)

	#length of NNP	
	count = 0
	for item in pos_tags:
		if item[1] == 'NNP':
			count = count + 1
	sub.append(count)

	#first_non wh word POS label
	if dic_firstword.has_key(pos_tags[1][1]):
		sub.append(dic_firstword[pos_tags[1][1]])
	else:
		sub.append(15)

	#second_word POS label
	if dic_secondword.has_key(pos_tags[2][1]):
		sub.append(dic_secondword[pos_tags[2][1]])
	else:
		sub.append(26)

	#classLabel
	if dic_label.has_key(label):
		sub.append(dic_label[label])
	else:
		sub.append(6)



	final_train.append(sub)

final_train = np.asarray(final_train)
# path = 'question.csv'
# file = open(path,'w')
# for row in final_train:
# 	for num in row:
# 		file.write("%s""," % num)
# 	file.write('\n')
# final_train = enc.fit_transform(final_train).toarray()

clf = tree.DecisionTreeClassifier()
X = final_train[:,0:4]
y = final_train[:,4]
clf.fit(X,y)
result = clf.predict(X)
print 'accruacy'
print metrics.accuracy_score(y,result)
print 'report'
print metrics.classification_report(result,y)
test_questions()


# clf_ = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10,10), random_state=1)
# clf_.fit(X, y)
# result = clf_.predict(X)
# print 'accruacy'
# print metrics.accuracy_score(y,result)
# print 'report'
# print metrics.classification_report(result,y)