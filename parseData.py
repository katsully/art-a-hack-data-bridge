import csv
from pathlib import Path
import json
import glob
import os

# json_file = open("bio_data.json", "r")
# json_object = json.load(json_file)
# json_file.close()


base_path = Path(__file__).parent
file_path = (base_path / "../Art_A_Hack_Data_Bridge/data").resolve()
for filename in glob.glob(os.path.join(file_path, '*.csv')):
	with open(os.path.join(os.curdir, filename), 'r') as csv_file: # open in readonly mode
		# skip headers
		next(csv_file)                  
		csv_reader = csv.reader(csv_file, delimiter=',')
		for idx,frame in enumerate(csv_reader):
			
			
	csv_file.close()

# json_file = open("bio_data.json", "w")
# json.dump(json_object, json_file)
# json_file.close()


