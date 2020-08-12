import csv
from pathlib import Path
import json
import glob
import os

json_file = open("bio_data.json", "r")
json_object = json.load(json_file)
json_file.close()

first_file = False


base_path = Path(__file__).parent
file_path = (base_path / "../Art_A_Hack_Data_Bridge/data").resolve()
for filename in glob.glob(os.path.join(file_path, '*.csv')):
	with open(os.path.join(os.curdir, filename), 'r') as csv_file: # open in readonly mode
		if not first_file:
			headers = next(csv_file).split(",")
			# remove newline from last element
			headers[-1] = headers[-1].strip()
			short_headers = [x.split("/EmotiBit/0/", 1)[1] if "/EmotiBit/0/" in x else x[1:] for x in headers]
			first_file = True
		else: # skip headers
			next(csv_file)                  
		csv_reader = csv.reader(csv_file, delimiter=',')
		for frame in csv_reader:
			i = 1+1

	csv_file.close()

json_file = open("bio_data.json", "w")
json.dump(json_object, json_file)
json_file.close()


