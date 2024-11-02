import socket

recieverIP = "10.0.0.2"
recieverPort   = 20002
bufferSize  = 1024 #Message Buffer Size

socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket_udp.bind((recieverIP, recieverPort))
print("UDP socket created successfully....." )

with open("StopWaitFile.jpg","wb") as file:
	seq = 0
	while True:
		packet, senderAddress = socket_udp.recvfrom(bufferSize)
		seq_num = int.from_bytes(packet[0:2], byteorder = "big")
		eof = packet[2]
		chunk = packet[3:]

		if seq_num == seq:
			file.write(chunk)
			#print("received packet with sequence {}".format(seq_num))
			seq += 1
			ACK = seq_num.to_bytes(2,byteorder = "big")
			socket_udp.sendto(ACK,senderAddress)
		else:
			ACK = (seq-1).to_bytes(2,byteorder = "big")
			socket_udp.sendto(ACK,senderAddress)
			#print("unexpected sequence{}".format(seq_num))
		if eof == 1:
			print("file is succesfully received.")
			break

socket_udp.close()