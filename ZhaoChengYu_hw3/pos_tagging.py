import nltk
import re
# nltk.download('maxent_treebank_pos_tagger')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger') 
# from nltk.tag.perceptron import PerceptronTagger

# tagger = PerceptronTagger
# path = 'output_of_stem.txt'
# f = open(path)

# cach = []
# for row in f:
# 	cach = row.split(' ')

# result_ = []
# for idx in range(0,len(cach)-2):
# 	result_.append(cach[idx])

# result = nltk.pos_tag(result_)
# file = open('output_of_pos.txt','w')

# for item in result:	
# 	file.write("%s__%s"" " % item)
result = []
result.append('Avishai')
result.append('John')
result.append('Skiddy')
print nltk.pos_tag(result)
