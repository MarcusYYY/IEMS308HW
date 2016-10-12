import string
import random
import numpy as np
import pandas as pd
import math 
from scipy 	import stats
import matplotlib.pyplot as plot
import matplotlib
import sklearn
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm


#detect the value of non-numeric attribute and count the frequence
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

#outlier removal,data standardization and normalization and organization deletion
def DataPreprocessing(DataFrame):
	#removing outliers
	clean_data = DataFrame[(np.abs(DataFrame.iloc[:,19:27].mean() - DataFrame.iloc[:,19:27])< 3*DataFrame.iloc[:,19:27].std()).all(axis=1)]
	#organization deletion
	# individual_data = clean_data[clean_data['Entity Type of the Provider'] == 'I']
	#filter nan
	# non_na = individual_data.dropna(subset = ['Credentials of the Provider'])
	#data normalization
	return clean_data

def DataExploration(DataFrame):
	data = DataFrame.iloc[:,19:26]
	print data.corr()
	print '-----------------------------------------------------------------'
	print data.cov()
	print '-----------------------------------------------------------------'
	print data.describe()
	print '-----------------------------------------------------------------'

def ScatterPlot(data_IL):
	ax1 = plot.figure().add_subplot(111)
	ax1.scatter(data_IL['Number of Medicare Beneficiaries'],data_IL['Total charge paid'],s = 10, c= 'r', marker="s")
	plot.xlabel('Number of Medicare Beneficiaries')
	plot.ylabel('Total charge paid')
	plot.legend(loc='upper right')
	ax1 = plot.figure().add_subplot(111)
	ax1.scatter(data_IL['Average Medicare Payment Amount'],data_IL['Number of Services'],s = 10, c = 'b', marker="s")
	plot.xlabel('Average Medicare Payment Amount')
	plot.ylabel('Number of Services')
	plot.legend(loc='upper right')
	ax1 = plot.figure().add_subplot(111)
	ax1.scatter(data_IL['Average Submitted Charge Amount'],data_IL['Number of Services'],s = 10, c = 'purple', marker="s")
	plot.xlabel('Average Submitted Charge Amount')
	plot.ylabel('Number of Services')
	plot.legend(loc='upper right')
	ax1 = plot.figure().add_subplot(111)
	ax1.scatter(data_IL['Average Submitted Charge Amount'],data_IL['Total charge paid'],s = 10, c = 'yellow', marker="s")
	plot.xlabel('Average Submitted Charge Amount')
	plot.ylabel('Total charge paid')
	plot.legend(loc='upper right')
	ax1 = plot.figure().add_subplot(111)
	ax1.scatter(data_IL['Total charge paid'],data_IL['Number of Medicare Beneficiaries'],s = 10, c = 'green', marker="s")
	plot.xlabel('Total charge paid')
	plot.ylabel('Number of Medicare Beneficiaries')
	plot.legend(loc='upper right')
	plot.show()


def K_means(data_IL):

	data_IL = data_IL.sample(frac = 0.1)

	X = data_IL[['Average Submitted Charge Amount','Number of Medicare Beneficiaries']]
	

	kmeans = KMeans(n_clusters = 2).fit(X)
	item = CategoryDetection(kmeans.labels_)
	print '-----------------------------------------------'
	print '--------------2 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg
	

	kmeans = KMeans(n_clusters = 3).fit(X)
	item = CategoryDetection(kmeans.labels_)
	print '-----------------------------------------------'
	print '--------------3 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg

	kmeans = KMeans(n_clusters = 4).fit(X)
	print '-----------------------------------------------'
	print '--------------4 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg


	kmeans = KMeans(n_clusters = 5).fit(X)
	item = CategoryDetection(kmeans.labels_)
	print '-----------------------------------------------'
	print '--------------5 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg


	kmeans = KMeans(n_clusters = 6).fit(X)
	item = CategoryDetection(kmeans.labels_)
	print '-----------------------------------------------'
	print '--------------6 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg

	kmeans = KMeans(n_clusters = 7).fit(X)
	item = CategoryDetection(kmeans.labels_)
	print '-----------------------------------------------'
	print '--------------7 clusters-----------------------'
	for key,val in item.iteritems():
		print key,val
	print kmeans.cluster_centers_
	avg =  sklearn.metrics.silhouette_score(X,kmeans.labels_,metric = 'euclidean')
	print avg

def DataNomarlization(DataFrame,attribute):
	min_ = DataFrame[attribute].min()
	max_ = DataFrame[attribute].max()
	DataFrame[attribute] = (DataFrame[attribute] - min_)/(max_ - min_)
	return DataFrame

data =  pd.read_csv('Medicare_Provider_Utilization_and_Payment_Data__Physician_and_Other_Supplier_PUF_CY2014.csv',encoding='utf-8')
data_1 = data
DataExploration(data_1)
# items = CategoryDetection(data_1['State Code of the Provider'])
# for key,val in items.iteritems():
# 	if key == 'NY':
#  		print key,val
#  	elif key == 'TX':
#  		print key,val
#  	elif key == 'IL':
#  		print key,val
data_1['Total charge paid'] = data_1['Number of Services'] * data_1['Average Submitted Charge Amount']
data_IL = data_1[data_1['State Code of the Provider'] == 'IL']
print len(data_IL)
data_IL = DataPreprocessing(data_IL)
data_IL.iloc[:,19:27] = (data_IL.iloc[:,19:27] - data_IL.iloc[:,19:27].mean())/data_IL.iloc[:,19:27].std()
data_IL = DataNomarlization(data_IL,'Number of Medicare Beneficiaries')
data_IL = DataNomarlization(data_IL,'Total charge paid')
data_IL = DataNomarlization(data_IL,'Number of Services')
data_IL = DataNomarlization(data_IL,'Number of Distinct Medicare Beneficiary/Per Day Services')
data_IL = DataNomarlization(data_IL,'Average Medicare Allowed Amount')
data_IL = DataNomarlization(data_IL,'Average Submitted Charge Amount')
data_IL = DataNomarlization(data_IL,'Average Medicare Payment Amount')
K_means(data_IL)
# X = data_IL[['Total charge paid','Number of Medicare Beneficiaries']]
# X.to_csv('tinydata.csv', encoding='utf-8', header=False, index=False, mode='a')
# ScatterPlot(data_IL)
# X = data_IL[['Average Submitted Charge Amount','Number of Medicare Beneficiaries']]
# print 1
# Z = linkage(X, 'ward')
# print 2
# c, coph_dists = cophenet(Z, pdist(X))
# print c



















