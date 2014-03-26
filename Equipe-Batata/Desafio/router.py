from net_packet import Packet_Generator
from net_packet import Net_Packet
from packet import Packet
from datetime import datetime
import sys

try:
	packet_number = int(sys.argv[1])
except IndexError:
	print("Informe o numero de pacotes a serem gerados por parametro! \n")
	exit(0) 
generator = Packet_Generator(packet_number)
will_generate = True
packet_list = []
while will_generate:
    packet_string = str(generator.next())
    will_generate = generator.has_next()
    packet = Packet()
    src_ip = ""
    dest_ip = ""
    content = ""
    pkt_type = ""
    bullet_count = 0
    for c in packet_string:
        if(c == "|"):
            bullet_count += 1
        if(bullet_count == 1 and c != " " and c != "|"):
            pkt_type += c
        if(bullet_count == 2 and c != " " and c != "|"):
            src_ip += c
        if(bullet_count == 3 and c != " " and c != "|"):
            dest_ip += c
        if(bullet_count == 4 and c != " " and c != "|"):
            content += c
    packet.pkt_type = pkt_type
    packet.src_ip = src_ip
    packet.dest_ip = dest_ip
    packet.content = content
    packet.datetime = datetime.now()
    packet_list.append(packet)
log = ""
udp_flag = True
http_flag = True
f = open("Output.txt", "w")
for p in packet_list:
    if(p.pkt_type == "udp"):
        if udp_flag == True:
            p.server = "udp_1"
            udp_flag = False
        else:
            p.server = "udp_2"
            udp_flag = True
        print("Mensagem: " + p.src_ip + ": " + p.content + "\n")
        log += "Pacote UDP enviado para: " + p.server + "\n"
    elif(p.pkt_type == "tcp"):
        log += "Pacote TCP descartado\n"
    else:
        if http_flag == True:
            p.server = "http_1"
            http_flag = False
        else:
            p.server = "http_2"
            http_flag = True
        f.write(str(p.datetime.day) + "-" + str(p.datetime.month) + "-" + str(p.datetime.year) + " " + str(p.datetime.hour) + ":" + str(p.datetime.minute) + ":" + str(p.datetime.second) + " - " + p.src_ip + " - " + p.dest_ip + " - " + p.content + " - " + p.server + "\n")
        log += "Pacote HTTP enviado para: " + p.server + "\n"
f.close()
print(log)
