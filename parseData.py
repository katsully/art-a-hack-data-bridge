import csv
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "../Art_A_Hack_Data_Bridge/data/08-05-2020-hussein-floormap_withFrame.csv").resolve()

with open(file_path) as csv_file:
	# skip headers
        next(csv_file)                  
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx,frame in enumerate(csv_reader):
        	print(frame[0])

csv_file.close()