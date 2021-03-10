from socket import *
import time
import random

HOST = '127.0.0.1'
PORT = '3000'

# Create a UDP socket
# We should use SOCK_DGRAM for UDP packets
socket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
socket.bind((HOST, int(PORT)))
while True:
	try:
		# Receive the client packet along with the address it is coming from
		message, address = socket.recvfrom(1024)
		t_end = time.time() + random.uniform(0.0, 2.0)

		while time.time() < t_end:
			pass

		# Server response
		socket.sendto(message, address)
	except:
		print("Timed out")
