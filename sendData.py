from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
import json

avg_idx = 0

addresses = ['/ppgRed', '/ppgIR', '/ppgGreen', '/eda', '/humidity', '/accX', '/accY', '/accZ', '/gyroX', '/gyroY', '/gyroZ', '/magX', '/magY', '/magZ', '/therm', '/temp']
json_headers = ["PPG:RED", "PPG:IR", "PPG:GRN", "EDA", "HUMIDITY", "ACC:X", "ACC:Y", "ACC:Z", "GYRO:X", "GYRO:Y", "GYRO:Z",  "MAG:X", "MAG:Y", "MAG:Z",  "TEMP", "THERM"]

def normalize_data(*params):
	global avg_idx
	global master_list
	val_name = params[0].split('/')[-1:]
	if 'PPG:RED' in val_name:
		master_list[0].append(params[1])
	elif 'PPG:IR' in val_name:
		master_list[1].append(params[1])
	elif 'PPG:GRN' in val_name:
		master_list[2].append(params[1])
	elif 'EDA' in val_name:
		master_list[3].append(params[1])
	elif 'HUMIDITY' in val_name:
		master_list[4].append(params[1])
	elif 'ACC:X' in val_name:
		master_list[5].append(params[1])
	elif 'ACC:Y' in val_name:
		master_list[6].append(params[1])
	elif 'ACC:Z' in val_name:
		master_list[7].append(params[1])
	elif 'GYRO:X' in val_name:
		master_list[8].append(params[1])
	elif 'GYRO:Y' in val_name:
		master_list[9].append(params[1])
	elif 'GYRO:Z' in val_name:
		master_list[10].append(params[1])
	elif 'MAG:X' in val_name:
		master_list[11].append(params[1])
	elif 'MAG:Y' in val_name:
		master_list[12].append(params[1])
	elif 'MAG:Z' in val_name:
		master_list[13].append(params[1])	
	elif 'THERM' in val_name:
		master_list[14].append(params[1])
	elif 'TEMP' in val_name:
		master_list[15].append(params[1])							
	avg_idx += 1
	if avg_idx == 160:
		for idx,val_list in enumerate(master_list):
			if len(val_list) > 0:
				avg_total = 0
				for x in val_list:
					avg_total += x
				value = avg_total / len(val_list)
				normalized_value = (value - normal_object[json_headers[idx]]['min']) / (normal_object[json_headers[idx]]['max'] - normal_object[json_headers[idx]]['min'])
				msg = osc_message_builder.OscMessageBuilder(address=addresses[idx])
				msg.add_arg(normalized_value)
				msg = msg.build()
				client.send(msg)
				client_sandro.send(msg)
				val_list.clear()
		avg_idx = 0


if __name__ == "__main__":
	global master_list 
	master_list = []
	for x in range(16):
		master_list.append([])
	with open("normal_data.json", "r") as normal_file:
		normal_object = json.load(normal_file)
	normal_file.close()


	client = udp_client.UDPClient('127.0.0.1', 9002)
	client_sandro = udp_client.UDPClient('127.0.0.1', 10001)

	dispatcher = dispatcher.Dispatcher()
	# need dispatcher map here
	dispatcher.map("/EmotiBit/0/*", normalize_data)

	server = osc_server.ThreadingOSCUDPServer(('localhost', 8000), dispatcher)
	server.serve_forever()