import json
from pprint import pprint
with open ('allItems.json') as data_file:
	data = json.load(data_file)

ls = []
for each in data:
	for i in each['url']:
		ls.append(i)

def retriveLS():
	return ls