import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
MESSAGE = ""
if sys.argv[1] == 'client':
    while True:
        MESSAGE = input("Eu: ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE, 'UTF-8'), (UDP_IP, UDP_PORT))
        if MESSAGE == "":
            break
elif sys.argv[1] == 'server':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        receivedMessage = str(data)[2:-1]
        print("Amigo:", receivedMessage)
        if receivedMessage == "":
            break
