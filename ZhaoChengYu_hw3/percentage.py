import re

pattern = r'[^"()\']+\w+[^.,?:"()\']'
pattern_ = r'([0-9]*.?[0-9]*%)|([0-9]+.?[0-9]*(percent)|(((third)|(quarter)|(half)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten))( percent))|(((third)|(quarter)|(half)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten))(%)))'
path = 'output_of_pos_1.txt'

file = open(path)
raw_data = []
for row in file:
	# raw_data = row.split(' ')
	raw_data = re.findall(pattern_,row)
finalresult = []
for item in raw_data:
	for tup in item:
		if tup != '':
			finalresult.append(tup)

file = open('output_of_percent.txt','w')

for item in finalresult:	
	file.write("%s"" " % item)
# for item in raw_data:
# 	print item
# text = []
# for item in raw_data:
# 	try:
# 		text.append(item.split('__')[0])
# 	except:
# 		continue



