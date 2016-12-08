import re
import nltk
from sklearn import preprocessing
import numpy as np
from sklearn import svm,cross_validation,metrics
from sklearn.neural_network import MLPClassifier
import math as m
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from fractions import Fraction
import re
sentence = 'Who What Which When Why Where How Whose Whom.'
sentence = 'Targets included SnapChat, Bitcoin, and in-flight smartphone use'
token = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(token)
print pos_tags
result_ = nltk.ne_chunk(pos_tags,binary = False)
print result_

dic_wh = {'Who':1,"When":2,"Where":3,"How":4,"What":5,"Which":6,"Whose":7,"Other":8}
dic_firstword = {'VBD':1,'NN':2,'VBZ':3,'MD':4,'VBP':5,'JJ':6,'CD':7,'VB':8,'VBG':9,'NNS':10,'PRP':11,'WDT':12,'NNP':13,'RB':14}
dic_label = {'ABBR':'de','DESC':1,'ENTY':2,'HUM':3,'LOC':4,'NUM':5,'Other':6}

# for item in result_:
# 	try:
# 		print item.label()
# 	except:
# 		pass
# 	print item[1]

# ans = nltk.bigrams(['more','is','said','than','down'])
# for item in ans:
# 	print item

# stemmer = PorterStemmer()
# print stemmer.stem('Facebook\'s')

# try:
# 	item = item.decode('Cp1252','ignore')
# 	result.append(stemmer.stem(item))
# except:
# 	pass

# wordnet_lemmatizer = WordNetLemmatizer()
# wordnet_lemmatizer.lemmatize('Facebook\'s')
