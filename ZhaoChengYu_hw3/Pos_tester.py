import nltk



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


path_ceo = 'IEMS_308/all/ceo.csv'
path_companey = 'IEMS_308/all/companies.csv'
path_percentage = 'IEMS_308/all/percentage.csv'
f_ceo = open(path_ceo)
f_com = open(path_companey)
f_per = open(path_percentage)

count = 0
for row in f_ceo:
	cach_ceo = row.split('\r')
for row in f_com:
	cach_com = row.split('\r')
for row in f_per:
	cach_per = row.split('\r')



tag_ceo = []
tag_com = []
tag_per = []

for item in nltk.pos_tag(cach_ceo):
	tag_ceo.append(item[1])
for item in nltk.pos_tag(cach_com):
	tag_com.append(item[1])
for item in nltk.pos_tag(cach_per):
	tag_per.append(item[1])

print "These are tags of ceo"
print CategoryDetection(tag_ceo)

print "These are tags of companeies"
print CategoryDetection(tag_com)

print "These are tags of percentage"
print CategoryDetection(tag_per)




