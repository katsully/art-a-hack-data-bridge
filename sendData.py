from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
import json

avg_idx = 0
avg_total = 0

def normalize_data():
	global avg_idx
	global avg_total
	avg_idx += 1
	avg_total += 0
	if avg_idx == 10:
		value = avg_total / avg_idx
		avg_idx = 0


if __name__ == "__main__":
	with open("normal_data.json", "r") as normal_file:
		normal_object = json.load(normal_file)
	normal_file.close()


	client = udp_client.UDPClient('localhost', 9001)

	dispatcher = dispatcher.Dispatcher()
	# need dispatcher map here

	server = osc_server.ThreadingOSCUDPServer(('localhost', 8000), dispatcher)
	normalize_data()