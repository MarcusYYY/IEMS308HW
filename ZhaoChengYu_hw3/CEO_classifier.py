import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn import linear_model,datasets
import numpy as np


def NameRegonition(name):
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




#Attribution Construction
pos_tag = []
length = []
FirstUpperLetter = []
FirstLowLetter = []
SecondUpperLetter = []
SecpndLowLetter = []
Class = []
#TrainData Establishment

path_train = 'IEMS_308/all/ceo.csv'

# data =  pd.read_csv(path_train,encoding='cp1252',header = None)
data_ceo = open(path_train)
cach_ceo = []

for row in data_ceo:
	cach_ceo = row.split('\r')

count = 0
for item in cach_ceo:
	item = item.replace(',',' ')
	leng = len(item)-1
	fu,fl,su,sl = NameRegonition(item)
	tag = 'NNP'

# append attributes to the list
	FirstUpperLetter.append(fu)
	FirstLowLetter.append(fl)
	SecondUpperLetter.append(su)
	SecpndLowLetter.append(sl)
	pos_tag.append(tag)
	length.append(leng)
	Class.append(1)

attribute = pd.DataFrame.from_items([('POS_tag',pos_tag),('Length',length),('FirstUpperLetter',FirstUpperLetter),('FirstLowLetter',FirstLowLetter),('SecondUpperLetter',SecondUpperLetter),('SecpndLowLetter',SecpndLowLetter),('Class',Class)])
print attribute
