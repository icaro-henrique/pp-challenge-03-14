import socket

def connection(n):
    number = int(n)
    UDP_IP = "127.0.0.1"
    UDP_PORT = 9999
    if(number == 1):
        print("Digite suas mensagens")
        MESSAGE = " "
        while MESSAGE != "":
            MESSAGE = input("")
            if MESSAGE != "":
                print ("Eu: %s" % MESSAGE)
                send = MESSAGE.encode(encoding='UTF-8')
                sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                sock.sendto(send, (UDP_IP, UDP_PORT))
    elif(number == 2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))

        while True:
             data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
             read = data.decode(encoding='UTF-8')
             print ("Amigo: %s" % read)

print("Digite 1 para client: ")
print("Digite 2 para servidor: ")
n = input("")
connection(n)
