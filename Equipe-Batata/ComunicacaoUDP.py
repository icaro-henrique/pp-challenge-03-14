import sys
import socket

try:
    if int(sys.argv[1]) == 1:
        port = 5000
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", port))
        print("Server esperando mensagens...\n")
        while 1:
            d = s.recvfrom(1024)
            data = str(d[0])
            addr = d[1]
            if len(data) == 3:
                break
            print(data[2:(len(data) - 1)] + "\n")
    elif int(sys.argv[1]) == 2:
        UDP_IP = "127.0.0.1"
        UDP_PORT = 5000
        while 1:
            MESSAGE = input("Informe a mensagem a ser enviada: ")          
            sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            sock.sendto(bytes(MESSAGE, "UTF-8"), (UDP_IP, UDP_PORT))
            if MESSAGE == "":
                break
except IndexError:
    print("Para iniciar como Server use parametro 1")
    print("Para iniciar como Cliente use parametro 2")
