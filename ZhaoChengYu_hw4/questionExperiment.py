import re
import nltk

sentence = 'What is your name ?'
token = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(token)
print pos_tags