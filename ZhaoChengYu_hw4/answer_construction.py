import re
import nltk
import Query_generation as Qg
import AnswerGeneration as AG

question = Qg.question
token = nltk.word_tokenize(question)
pos_tags = nltk.pos_tag(token)
path_ceo = 'ceo.csv'
path_com = 'companies.csv'
ans = AG.ans_sub

file_ceo = open(path_ceo)
file_com = open(path_com)

CEO_dic = {}
COM_dic = {}

for row in file_ceo:
	row = row.replace(',',' ')
	dic = row.split('\r')
	for item in dic:
		if not CEO_dic.has_key(item):
			CEO_dic[item] = 1

for row in file_com:
	row = row.replace(',',' ')
	dic = row.split('\r')
	for item in dic:
		if not COM_dic.has_key(item):
			COM_dic[item] = 1

flag = ''
for item in pos_tags:
	if item[0] == 'CEO':
		flag = 'ceo'
		break
	elif item[0] == 'company':
		flag = 'company'
		break
final_ans = ''

if flag == 'ceo':
	for sentence in ans:
		token = nltk.word_tokenize(sentence)
		result_bigram = list(nltk.bigrams(token))
		for bigram in result_bigram:
			name = str(bigram[0]) + ' ' + str(bigram[1])
			if CEO_dic.has_key(name):
				final_ans = name

elif flag == 'company':
	final_ans = []
	for sentence in ans:
		pattern = r'[^A-Za-z0-9\s]+'
		sentence = re.sub(pattern,'', sentence) 
		token = nltk.word_tokenize(sentence)
		result_bigram = list(nltk.bigrams(token))
		result_trigram = list(nltk.ngrams(token,3))
		result_fourgram = list(nltk.ngrams(token,4))
		for item in token:
			if COM_dic.has_key(item):
				final_ans = item
		for bigram in result_bigram:
			name = str(bigram[0]) + ' ' + str(bigram[1])
			if COM_dic.has_key(name):
				final_ans = item
		for bigram in result_trigram:
			name = str(bigram[0]) + ' ' + str(bigram[1]) + ' ' + str(bigram[2])
			if COM_dic.has_key(name):
				final_ans = item
		for bigram in result_fourgram:
			name = str(bigram[0]) + ' ' + str(bigram[1]) + ' ' + str(bigram[2]) + ' ' + str(bigram[3])
			if COM_dic.has_key(name):
				final_ans = item

print question
print final_ans
