from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":
	print("hi")

	client = udp_client.UDPClient('localhost', 9001)

	dispatcher = dispatcher.Dispatcher()
	# need dispatcher map here

	server = osc_server.ThreadingOSCUDPServer(('localhost', 8000), dispatcher)
