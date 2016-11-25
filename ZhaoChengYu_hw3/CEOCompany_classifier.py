import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn import linear_model,datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation,metrics
from sklearn import svm
import re
from sklearn.neural_network import MLPClassifier


def NameRecgonition(name):
	NameSlot = name.split(' ')
	if len(NameSlot) == 2:
		SecondName = NameSlot[1]
	else:
		SecondName = ''
	FirstName = NameSlot[0]

	First_tail = len(FirstName) - 1
	if First_tail > 0:
		if FirstName[0] <= 'Z' and FirstName[0] >= 'A':
			firstupperletter = 1
		else:
			firstupperletter = 0

		if FirstName[First_tail] <= 'z' and FirstName[First_tail] >= 'a':
			firstlowletter = 1
		else:
			firstlowletter = 0
	else:
		firstlowletter = 0
		firstupperletter = 0

	Second_tail = len(SecondName) - 1
	if Second_tail > 0:
		if SecondName[0] <= 'Z' and SecondName[0] >= 'A':
			secondupperletter = 1
		else:
			secondupperletter = 0

		if SecondName[Second_tail] <= 'z' and SecondName[Second_tail] >= 'a':
			secondlowletter = 1
		else:
			secondlowletter = 0
	else:
		secondlowletter = 0
		secondupperletter = 0
	return firstupperletter,firstlowletter,secondupperletter,secondlowletter

def FakeTrainingSet(data,num,dic):

	count = 0
	Class = []
	pos_tag = []
	length = []
	FirstUpperLetter = []
	FirstLowLetter = []
	SecondUpperLetter = []
	SecondLowLetter = []
	wholename = []
	currentname = []
	for item in data:
		if count > num - 2:
			break
		try:
			current_text = item.split('__')[0]
			current_tag = item.split('__')[1]
			next_text = data[count+1].split('__')[0]
			next_tag = data[count+1].split('__')[1]
			fu = current_text[0]
			su = next_text[0]
			fl = current_text[len(current_text)-1]
			sl = next_text[len(next_text)-1]
			leng = len(current_text) + len(next_text)
			length.append(leng)
		except:
			count = count + 1
			continue

		if fu <= 'Z' and fu >= 'A':
			FirstUpperLetter.append(1)
		else:
			FirstUpperLetter.append(0)
		if su <= 'Z' and su >= 'A':
			SecondUpperLetter.append(1)
		else:
			SecondUpperLetter.append(0)

		if fl <= 'z' and fl >= 'a':
			FirstLowLetter.append(1)
		else:
			FirstLowLetter.append(0)

		if sl <= 'z' and sl >= 'a':
			SecondLowLetter.append(1)
		else:
			SecondLowLetter.append(0)

		if current_tag == 'NNP' and next_tag == 'NNP':
			pos_tag.append(1)
		elif current_tag == 'NNP':
			pos_tag.append(1)
		else:
			pos_tag.append(0)

		whole_name = current_text + ' ' + next_text
		wholename.append(whole_name)
		currentname.append(current_text)
		if dic.has_key(whole_name):
			Class.append(1)
		else:
			Class.append(0)
		count = count + 1
	return length,FirstUpperLetter,FirstLowLetter,SecondUpperLetter,SecondLowLetter,Class,wholename,currentname
	
def BuildNameDic(cach_ceo):
	Cach = {}
	data = []
	for item in cach_ceo:
		item = item.strip()
		item = item.replace(',',' ')
		wholename = item.split(' ')
		FirstName = wholename[0]
		if len(wholename) > 1:
			SecondName = wholename[1]
			data.append(SecondName)
			if len(wholename) > 2:
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

def Build_traning_set(path_ceo,path_company,path_bad):
	pos_tag = []
	length = []
	FirstUpperLetter = []
	FirstLowLetter = []
	SecondUpperLetter = []
	SecpndLowLetter = []
	Class = []
	wholename = []
	currentname = []
	data_ceo = open(path_ceo)
	data_company = open(path_company)
	cach_ceo = []
	cach_company = []
	for row in data_ceo:
		cach_ceo = row.split('\r')
	dic = BuildNameDic(cach_ceo)

	for row in data_company:
		cach_ceo = row.split('\r')
	dic_ = BuildNameDic(cach_company)
	file_ = open(path_bad)
	for row in file_:
		cach_bad_example = row.split(' ')

	final_result = []
	for item in cach_bad_example:
		try:
			tag = item.split('__')[1]
			if tag == 'NNP':
				final_result.append(item)
		except:
			continue
	length,FirstUpperLetter,FirstLowLetter,SecondUpperLetter,SecpndLowLetter,Class,wholename,currentname =  FakeTrainingSet(final_result,len(final_result)/10,dic)
	for item in cach_ceo:
		item = item.replace(',',' ')
		leng = len(item)-1
		fu,fl,su,sl = NameRecgonition(item)
# Append attributes to the list
		FirstUpperLetter.append(fu)
		FirstLowLetter.append(fl)
		SecondUpperLetter.append(su)
		SecpndLowLetter.append(sl)
		pos_tag.append(tag)
		length.append(leng)
		wholename.append(item)
		currentname.append(item.split(' ')[0])
		Class.append(1)

	for item in cach_company:
		item = item.replace(',',' ')
		leng = len(item)-1
		fu,fl,su,sl = NameRecgonition(item)
# Append attributes to the list
		FirstUpperLetter.append(fu)
		FirstLowLetter.append(fl)
		SecondUpperLetter.append(su)
		SecpndLowLetter.append(sl)
		pos_tag.append(tag)
		length.append(leng)
		wholename.append(item)
		currentname.append(item.split(' ')[0])
		Class.append(1)

	train_ = pd.DataFrame.from_items([('Length',length),('FirstUpperLetter',FirstUpperLetter),('FirstLowLetter',FirstLowLetter),('SecondUpperLetter',SecondUpperLetter),('SecondLowLetter',SecpndLowLetter),('Class',Class)])
	return train_,final_result

#Attribution Construction
print 'begin'
pos_tag = []
length = []
FirstUpperLetter = []
FirstLowLetter = []
SecondUpperLetter = []
SecpndLowLetter = []
Class = []
wholename = []
currentname = []
#TrainData Establishment

path_ceo = 'IEMS_308/all/ceo.csv'
path_company = 'IEMS_308/all/companies.csv'

# data =  pd.read_csv(path_train,encoding='cp1252',header = None)
data_ceo = open(path_ceo)
data_company = open(path_company)
cach_ceo = []
cach_company = []

for row in data_ceo:
	cach_ceo = row.split('\r')

for row in data_company:
	cach_company = row.split('\r')

# Set up a dictionary of CEO's name
dic = BuildNameDic(cach_ceo)
# Set up a dictionary of company
dic_com = BuildNameDic(cach_company)
path_bad = 'output_of_pos_1.txt'
file_ = open(path_bad)

for row in file_:
	cach_bad_example = row.split(' ')

train_,final_result = Build_traning_set(path_ceo,path_company,path_bad)
attr = train_[['Length','FirstUpperLetter','FirstLowLetter','SecondUpperLetter','SecondLowLetter']]
out = train_['Class']
print 'created training data'
# model = log_model.fit(attr,out)
# print model.predict(attr)
# X = np.random.randn(300,2)
# Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
# d = svm.NuSVC()
# d.fit(X,Y)
# print d.predict(X)
# clf = svm.SVC(kernel = 'rbf')
# clf.fit(attr,out)
# count = 0
# for items in clf.predict(attr):
# 	if items == 1:
# 		count = count + 1
# 	print count
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
# clf.fit(attr,out)

# print clf.predict(attr)
# predicted = clf.predict(attr)
# print metrics.accuracy_score(out, predicted)
	
# predicted = cross_validation.cross_val_predict(log_model,attr,out,cv = 10)
# count = 0
# for item in predicted:
# 	if item == 1:
# 		count = count + 1
# print count
# print predicted
# print metrics.accuracy_score(out, predicted)
# print metrics.classification_report(out,predicted)

pos_tag = []
length = []
FirstUpperLetter = []
FirstLowLetter = []
SecondUpperLetter = []
SecpndLowLetter = []
Class = []
wholename = []
currentname = []
length,FirstUpperLetter,FirstLowLetter,SecondUpperLetter,SecpndLowLetter,Class,wholename,currentname =  FakeTrainingSet(final_result,len(final_result),dic)
test_ = pd.DataFrame.from_items([('Length',length),('FirstUpperLetter',FirstUpperLetter),('FirstLowLetter',FirstLowLetter),('SecondUpperLetter',SecondUpperLetter),('SecondLowLetter',SecpndLowLetter),('Class',Class),('wholename',wholename),('currentname',currentname)])
X = test_[['Length','FirstUpperLetter','FirstLowLetter','SecondUpperLetter','SecondLowLetter']]
y = test_['Class']
print 'training'
clf = svm.SVC(kernel = 'rbf')
clf.fit(attr,out)
result = clf.predict(X)
print metrics.accuracy_score(y,result)
print metrics.classification_report(result,y)
count = 0
namelist = []


for idx in range(0,len(result)):
	if result[idx] == 1:
		namelist.append(test_.iloc[idx,7])

print "-------------------------------------"
print 'CEO names'		
result_ceo = {}
for item in namelist:
	if dic.has_key(item):
		result_ceo[item] = 1

file = open('output_of_ceo_1.txt','w')
for key in result_ceo:	
	file.write("%s"" " % key)
print "-------------------------------------"
print 'company names'
result_com = {}
for item in namelist:
	if dic_com.has_key(item):
		result_com[item] = 1

file = open('output_of_company.txt_1','w')
for key in result_com:	
	file.write("%s"" " % key)













