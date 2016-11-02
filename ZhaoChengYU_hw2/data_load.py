import numpy as np
import pandas as pd
import csv
from apyori import apriori
import re
import matplotlib.pyplot as plt

def CategoryDetection(DataFrame):
	Cach = {}
	for items in DataFrame:
		if items:
			if Cach.has_key(items):
				count = Cach.get(items) + 1
			else:
				count = 1
			Cach[items] = count
	return Cach

def DataExploration(DataFrame):
	data = DataFrame.iloc[:,8:11]
	print data.corr()
	print '-----------------------------------------------------------------'
	print data.cov()
	print '-----------------------------------------------------------------'
	print data.describe()
	print '-----------------------------------------------------------------'

def CategoryCount(items ,num):
	for key,val in items.iteritems():
		if val > num:
			print key,val

def putItemsInBasket(data):
	Cach = {}
	for index in range(0,len(data)):
		keys = (data.iloc[index,1],data.iloc[index,2],data.iloc[index,3])
		if Cach.has_key(keys):
			Cach.get(keys).append(data.iloc[index,0])
		else:
			basket = []
			basket.append(data.iloc[index,0])
			Cach[keys] = basket
	result = []
	count = 0
	for key,value in Cach.iteritems():
		if len(value) > count:
			count = len(value)
		result.append(value)
	return result,count

def write_to_csv(result):
	resultFile = open('output_LA.csv','wb')
	wr = csv.writer(resultFile,dialect = 'excel')
	for items in result:
		wr.writerow(items)

def count_Maxmium_line(data):
	count = 0
	for item in data:
		print item	
	return count

def count_min_support():
	count = 0



data =  pd.read_csv('strinfo.csv',encoding='utf-8')
data.columns =['STR','lOCATION','STATE','CODE','ZERO']
data = data[(data['STATE'] == 'LA')]
# data.columns = ['SKU','STORE','REGISTER','TRANNUM','SALEDATE','SEQ','STYPE','QUANTITY','PRICE_1','PRICE_2','PRICE_3','InnerID','IMC','ZERO']
# data_1 = data.iloc[:,0:8]
# data_2 = data_1[data_1['STYPE'] == 'P']
# data_2.to_csv('filted.csv', encoding='utf-8', header=False, index=False, mode='a')

#detect the value of non-numeric attribute and count the frequence	
items = CategoryDetection(data.iloc[:,0])
# plt.bar(range(len(items)),items.values(),align='center')
# plt.xticks(range(len(items)),items.keys())
# plt.show()
for key,val in items.iteritems():
	print key,val

data_large = pd.read_csv('trnsact.csv',encoding='utf-8')
data_large.columns = ['SKU','STORE','REGISTER','TRANNUM','SALEDATE','SEQ','STYPE','QUANTITY','PRICE_1','PRICE_2','PRICE_3','InterID','MIC','ZERO']
data_LA = data_large[(data_large['STORE'] == 3204)|(data_large['STORE'] == 8202)|(data_large['STORE'] == 3604)|(data_large['STORE'] == 9112)|(data_large['STORE'] == 8602)|(data_large['STORE'] == 8102)|(data_large['STORE'] == 9512)|(data_large['STORE'] == 9002)|(data_large['STORE'] == 3504)|(data_large['STORE'] == 9402)|(data_large['STORE'] == 8512)|(data_large['STORE'] == 8002)|(data_large['STORE'] == 1100)|(data_large['STORE'] == 3404)|(data_large['STORE'] == 8402)|(data_large['STORE'] == 9812)|(data_large['STORE'] == 9302)|(data_large['STORE'] == 8802)|(data_large['STORE'] == 3304)|(data_large['STORE'] == 9708)|(data_large['STORE'] == 8302)|(data_large['STORE'] == 8702)]
data_LA = data_LA[data_LA['STYPE'] == 'P']
# data_IL = data_large[(data_large['STORE'] == 600)|(data_large['STORE'] == 2600)|(data_large['STORE'] == 3000)|(data_large['STORE'] == 3600)|(data_large['STORE'] == 6009)|(data_large['STORE'] == 6109)|(data_large['STORE'] == 6209)|(data_large['STORE'] == 9106)]
data_LA.to_csv('filted_LA.csv', encoding='utf-8', header=False, index=False, mode='a')
# new_data = pd.read_csv('filted_CA.csv',encoding='utf-8')
# new_data.columns = ['SKU','STORE','REGISTER','TRANNUM','SALEDATE','SEQ','STYPE','QUANTITY','PRICE_1','PRICE_2','PRICE_3','InnerID','IMC','ZERO']
# newdata = new_data[new_data['STYPE'] == 'P']
# newdata.to_csv('filted_new_CA.csv', encoding='utf-8', header=False, index=False, mode='a')
data_related = pd.read_csv('filted_LA.csv',encoding='utf-8')
data_related.columns = ['SKU','STORE','REGISTER','TRANNUM','SEQ','SALEDATE','STYPE','QUANTITY','PRICE_1','PRICE_2','PRICE_3','InterID','MIC','ZERO']
# data_of603 = data_related[data_related['STORE'] == 603]
# data_of1003 = data_related[data_related['STORE'] == 1003]
# del data_of603['PRICE_3']
# del data_of1003['PRICE_3']

# items = CategoryDetection(data_of603.iloc[:,5])
# for key,val in items.iteritems():
# 	print key,val
# print len(items)

data_used = data_related[['SKU','REGISTER','TRANNUM','SALEDATE']]
# data_used = data_whole
result_related ,num = putItemsInBasket(data_used)

# print num
# data_used = data_of1003[['SKU','REGISTER','TRANNUM','SALEDATE']]
# result_1003 = putItemsInBasket(data_used)
# data__ = [[1,2],[2,3],[3,4],[4,3,2]]
# results = apriori(result_603)
# print results
 
write_to_csv(result_related)



