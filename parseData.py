import csv
from pathlib import Path
import json
import glob
import os

with open("bio_data.json", "r") as json_file:
	json_object = json.load(json_file)

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
			for header in short_headers:
				json_object[header] = []
			first_file = True
		else: # skip headers
			next(csv_file)                  
		csv_reader = csv.reader(csv_file, delimiter=',')
		for frame in csv_reader:
			i = 1+1

	csv_file.close()

with open("bio_data.json", "w") as json_file:
	json.dump(json_object, json_file)


