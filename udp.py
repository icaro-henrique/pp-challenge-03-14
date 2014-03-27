import socket
import threading
import sys


# IP = "192.168.100.78"
# Local
IP = "127.0.0.1"
PORT = 3545


def main(argv):
    if len(argv) > 1:
        opt = int(argv[1])

        if opt == 1:
            thread_server = threading.Thread(target=server)
            thread_server.start()
            thread_server.join()

        if opt == 2:
            thread_client = threading.Thread(target=client)
            thread_client.start()
            thread_client.join()
    else:
        print("Parametros de entrada:\
              \n1 para iniciar como servidor\
              \n2 para iniciar como cliente")


def client():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Digite suas mensagens")

    message = None
    while message != "":
        message = raw_input("Voce: ")
        sender.sendto(message.encode(encoding='UTF-8'), (IP, PORT))

    sender.close()


def server():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind((IP, PORT))

    print("Esperando mensagens")

    message = None
    while message != "":
        message, addr = receiver.recvfrom(1024)
        message = message.decode(encoding='UTF-8')
        print("Amigo: " + message)

    receiver.close()

if __name__ == '__main__':
    main(sys.argv)
