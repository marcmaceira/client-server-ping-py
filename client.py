from socket import *
from time import time, ctime

HOST = '127.0.0.1'
PORT = '3000'

# AF_INET is the Internet address family for IPv4
# SOCK_DGRAM is a UDP datagram-based protocol
socket = socket(AF_INET, SOCK_DGRAM)
socket.settimeout(1)

packetsReceived = 0
packetsLost = 0
# Send and receive 10 requests.
for i in range(10):
    # Retrieve the current time
    currentTime = time()
    message = "PING " + ctime(currentTime)
    try:
        # Sending the message and waiting for the answer
        socket.sendto(message.encode(), (HOST, int(PORT)))
        receivedMessage, serverAddress = socket.recvfrom(1024)
        packetsReceived += 1
        endTime = time()

    except:
        packetsLost += 1
        print("PING Request timed out\n")
        continue

    # Calculate the round trip time
    RTT = (endTime - currentTime)

    # Modified message is decoded.
    print(receivedMessage.decode())

    # Prints the RTT
    print("Round Trip Time: %.2f\n" % RTT)

print("Packets received: %d" % packetsReceived)
print("Packets lost: %d" % packetsLost)

socket.close()
