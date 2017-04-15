import json
from pprint import pprint
with open ('../ItemID.json') as data_file:
	data = json.load(data_file)

ls = []
for each in data:
	for i in each['url']:
		if i not in ls:
			ls.append(i)

def retriveLS():
	return ls
