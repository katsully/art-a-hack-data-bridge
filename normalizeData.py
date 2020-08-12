import json


with open("bio_data.json", "r") as json_file:
	json_object = json.load(json_file)
json_file.close()

with open("normal_data.json", "r") as normal_file:
	normal_object = json.load(normal_file)
normal_file.close()

normal_object = {}

#Normalized Data

for key in json_object:
	normal_object[key] = {}
	# get weighted/averaged min and max
	low_five = list(json_object[key].items())[:5]
	high_five = list(json_object[key].items())[-5:]
	sum_of_five = 0
	total = 0
	for k,v in low_five:
		print(k,v)
		sum_of_five += float(k) * v
		total += v
	key_min = sum_of_five / total
	normal_object[key]["min"] = key_min
	sum_of_five = 0
	total = 0
	for k,v in high_five:
		print(k,v)
		sum_of_five += float(k) * v
		total += v
	key_max = sum_of_five / total
	normal_object[key]["max"] = key_max


with open("normal_data.json", "w") as normal_file:
	json.dump(normal_object, normal_file, sort_keys=True)
normal_file.close()