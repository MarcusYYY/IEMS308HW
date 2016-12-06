import re
import nltk
from nltk.corpus import stopwords
path = 'train_1000.label.txt'
#define the subset of stop words
stop = set(stopwords.words('english'))

file = open(path)
cach = []
question = []
key_words = []

for row in file:
	sentence = row.split(' ',1)[1].replace('\n','')
	question.append(sentence)
	token = nltk.word_tokenize(sentence)
	pos_tags = nltk.pos_tag(token)
	cach.extend([i for i in sentence.split() if i not in stop])
	key_word = []
	for item in pos_tags:
		try:
			if item[1] == 'NNP' or item[1] == 'NN' or item[1] == 'NNS' or item[1] == 'JJ':
				key_word.append(item[0])
		except:
			continue
	key_words.append(key_word)
print key_words