import re
import nltk
from sklearn import preprocessing
import numpy as np
from sklearn import svm,cross_validation,metrics
from sklearn.neural_network import MLPClassifier
import math
sentence = 'Every year, Facebook CEO Mark Zuckerberg will accept one challenge.'
token = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(token)
result_ = nltk.ne_chunk(pos_tags,binary = False)


dic_wh = {'Who':1,"When":2,"Where":3,"How":4,"What":5,"Which":6,"Whose":7,"Other":8}
dic_firstword = {'VBD':1,'NN':2,'VBZ':3,'MD':4,'VBP':5,'JJ':6,'CD':7,'VB':8,'VBG':9,'NNS':10,'PRP':11,'WDT':12,'NNP':13,'RB':14}
dic_label = {'ABBR':'de','DESC':1,'ENTY':2,'HUM':3,'LOC':4,'NUM':5,'Other':6}


ans = 643/608
print ans
print math.log(643/608)