import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn import linear_model,datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation,metrics
from sklearn import svm
import re
from sklearn.neural_network import MLPClassifier


def BuildNameDic(cach_ceo):
	Cach = {}
	data = []
	for item in cach_ceo:
		item = item.strip()
		# item = item.replace(',',' ')
		wholename = item.split(' ')
		FirstName = wholename[0]
		if len(wholename) > 1 and wholename[1] != 'Inc' and wholename[1] != 'Ltd' and wholename[1] != 'Corp' and wholename[1] != 'Group':
			SecondName = wholename[1]
			data.append(SecondName)
			if len(wholename) > 2 and wholename[2] != 'Inc' and wholename[2] != 'Ltd' and wholename[2] != 'Corp' and wholename[2] != 'Group':
				ThirdName = wholename[2]
				data.append(ThirdName)
		data.append(item)
		data.append(FirstName)
	for items in data:
		items = items.strip()
		if Cach.has_key(items):
			continue
		else:
			Cach[items] = 1
	return Cach


path_ceo = 'IEMS_308/all/ceo.csv'
path_company = 'IEMS_308/all/companies.csv'
path_bad = 'output_of_pos_1.txt'

file_ = open(path_bad)

cach_all = []
for row in file_:
	cach_all = row.split(' ')
NNP_words = []
for item in cach_all:
	try:
		tag = item.split('__')[1]
		if tag == 'NNP':
			NNP_words.append(item.split('__')[0])
	except:
		continue

file_ceo = open(path_ceo)
for row in file_ceo:
	cach_ceo = row.split('\r')
file_companey = open(path_company)
for row in file_companey:
	cach_company = row.split('\r')
ceo_dic = BuildNameDic(cach_ceo)
company_dic = BuildNameDic(cach_company)

result_ceo = {}
result_company = {}
for item in NNP_words:
	if not ceo_dic.has_key(item):
		result_ceo[item] = 1
	elif not company_dic.has_key(item):
		result_company[item] = 1

count = 0
for key,val in result_ceo.iteritems():
	count = count + 1
	print key,count

count = 0
for key,val in result_company.iteritems():
	count = count + 1
	print key,count


