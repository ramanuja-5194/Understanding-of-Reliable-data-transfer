import time
import socket
import os # to get the file size

senderIP = "10.0.0.1"
senderPort = 20001
receiverAddressPort = ("10.0.0.2",20002)
bufferSize = 1024
timeout = 0.02

socket_udp = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
socket_udp.settimeout(timeout)

count = 0
size = os.path.getsize("testFile.jpg")
start = time.time()
with open("testFile.jpg","rb") as file:
	seq_num = 0
	while True:
		chunk = file.read(bufferSize - 4)
		if not chunk:
			break
		eof = 1 if len(chunk) < (bufferSize - 4) else 0
		h = seq_num.to_bytes(2,byteorder = "big") + eof.to_bytes(1,byteorder = "big")
		packet = h + chunk
		while True:
			try:
				socket_udp.sendto(packet,receiverAddressPort) # sending packet and waiting for ACK
				#print("send packet with sequence {}".format(seq_num))
				ACK,temp = socket_udp.recvfrom(bufferSize)

				ACK_num = int.from_bytes(ACK,byteorder = "big")
				if ACK_num == seq_num:
					#print("received ACK for sequence{}".format(seq_num))
					seq_num += 1
					break
			except socket.timeout:
				count += 1
				print("Timeout, resending sequence{}.".format(seq_num)) # the loop will run again

end = time.time()
total = end - start
throughput = size / total / 1024

print("file successfully transfered.")
print("throughput = {}".format(throughput))
print("number of retransmissions = {}".format(count))
socket_udp.close()