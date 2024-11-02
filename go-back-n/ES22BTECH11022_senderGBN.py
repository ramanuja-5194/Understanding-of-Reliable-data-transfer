import socket
import time
from threading import Timer
import os

senderIP = "10.0.0.1"
senderPort = 20001
receiverAddressPort = ("10.0.0.2", 20002)
bufferSize = 1024
window_size = 2
timeout = 1.8

socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket_udp.settimeout(timeout)

size = os.path.getsize("testFile.jpg")
start = time.time()
with open("testFile.jpg", "rb") as file:
    base = 0
    next_seq = 0
    packets = []

    while True:
        chunk = file.read(bufferSize - 4)
        if not chunk:
            break
        eof = 1 if len(chunk) < (bufferSize - 4) else 0
        header = next_seq.to_bytes(2, byteorder="big") + eof.to_bytes(1, byteorder="big")
        packets.append(header + chunk)
        next_seq += 1

    next_seq = 0
    while base < len(packets):
        while next_seq < base + window_size and next_seq < len(packets):
            socket_udp.sendto(packets[next_seq], receiverAddressPort)
            next_seq += 1

        try:
            ACK, temp = socket_udp.recvfrom(bufferSize)
            ack_num = int.from_bytes(ACK, byteorder="big")
            base = ack_num + 1
        except socket.timeout:
            next_seq = base

end = time.time()
total = end - start
throughput = size / total / 1024
print("File transfer completed.")
print("throughput = {}".format(throughput))
socket_udp.close()