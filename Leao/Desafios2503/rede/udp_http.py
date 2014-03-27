import sys
import time

from datetime import datetime
from net_packet import Packet_Generator


date = datetime.now()

n = int(sys.argv[1])
i = 0

rr_udp = 0
rr_http = 0
log = open("log.txt", 'w')

Httplog = open("Httplog.txt", 'w')
toLog = []

# gera pacotes
generator = Packet_Generator(n)
for i in range(0, n):
    packet = generator.next()
    src_ip = packet.src_ip
    dest_ip = packet.dest_ip
    dest_ip = packet.dest_ip
    pkt_type = packet.pkt_type
    content = packet.content

    if pkt_type == "http":
        if rr_http == 0:

            rr_http = 1
            toLog = (str(date.day), '-', str(date.month), '-', str(date.year),
                     " ", str(date.hour), ':', str(date.minute),
                     ':', str(date.second), " - ", src_ip, " - ", dest_ip,
                     " - ", content, " - ", "http1\n")
            toLog = "".join(toLog)
            Httplog.write(toLog)
            log.write("Pacote HTTP enviado para http1\n")

        else:
            rr_http == 0
            toLog = (str(date.day), '-', str(date.month), '-', str(date.year),
                     " ", str(date.hour), ':', str(date.minute),
                     ':', str(date.second), " - ", src_ip, " - ", dest_ip,
                     " - ", content, " - ", "http2\n")
            toLog = "".join(toLog)
            Httplog.write(toLog)
            log.write("Pacote HTTP enviado para http2\n")

    elif pkt_type == "udp":
            if rr_udp == 0:
                rr_udp = 1
                log.write("Pacote UDP enviado para UDP1\n")
                print (packet.src_ip, " : ", packet.content)

            else:
                rr_udp = 0
                log.write("Pacote UDP enviado para UDP2\n")

    else:
        log.write("Pacote TCP descartado\n")

log.close()
Httplog.close()
