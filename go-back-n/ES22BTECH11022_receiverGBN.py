import socket

recieverIP = "10.0.0.2"
recieverPort = 20002
bufferSize = 1024

socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket_udp.bind((recieverIP, recieverPort))
print("UDP socket created successfully....." )

with open("GBN.jpg", "wb") as file:
    expected_seq = 0
    while True:
        packet, senderAddress = socket_udp.recvfrom(bufferSize)

        sequence_num = int.from_bytes(packet[0:2], byteorder="big")
        eof = packet[2]
        chunk = packet[3:]

        if sequence_num == expected_seq:
            file.write(chunk)
            expected_seq += 1

        # Send cumulative ACK
        ACK = (expected_seq - 1).to_bytes(2, byteorder="big")
        socket_udp.sendto(ACK, senderAddress)

        if eof == 1:
            print("File transfer completed.")
            break
socket_udp.close()