import json


with open("bio_data.json", "r") as json_file:
	json_object = json.load(json_file)
json_file.close()

with open("normal_data.json", "r") as normal_file:
	normal_object = json.load(normal_file)
normal_file.close()

normal_object = {}

#Normalized Data
normal_object = json_object

for key in normal_object:
	print(list(normal_object[key].items())[0])


#normalized = (x-min(x))/(max(x)-min(x))



with open("normal_data.json", "w") as normal_file:
	json.dump(normal_object, normal_file, sort_keys=True)
normal_file.close()