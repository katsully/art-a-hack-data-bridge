from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
import json

avg_idx = 0

def normalize_data(*params):
	global avg_idx
	val_name = params[0].split('/')[-1:]
	master_list[val_name[0]].append(params[1])						
	avg_idx += 1
	if avg_idx == 160:
		for val_list in master_list:
			if len(master_list[val_list]) > 0:
				value = sum(master_list[val_list]) / len(master_list[val_list])
				normalized_value = (value - normal_object[val_list]['min']) / (normal_object[val_list]['max'] - normal_object[val_list]['min'])
				osc_address = '/' + val_list
				msg = osc_message_builder.OscMessageBuilder(address=osc_address)
				msg.add_arg(normalized_value)
				msg = msg.build()
				client.send(msg)
				client_sandro.send(msg)
				master_list[val_list].clear()
		avg_idx = 0


if __name__ == "__main__":
	master_list = dict()
	with open("normal_data.json", "r") as normal_file:
		normal_object = json.load(normal_file)
	normal_file.close()

	for header_name in normal_object:
	    master_list[header_name] = []

	client = udp_client.UDPClient('127.0.0.1', 9002)
	client_sandro = udp_client.UDPClient('127.0.0.1', 10001)

	dispatcher = dispatcher.Dispatcher()
	# need dispatcher map here
	dispatcher.map("/EmotiBit/0/*", normalize_data)

	server = osc_server.ThreadingOSCUDPServer(('localhost', 8000), dispatcher)
	server.serve_forever()