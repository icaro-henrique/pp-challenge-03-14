from net_packet import Packet_Generator
from time import gmtime, strftime
import sys
import itertools
 
udpList = ["UDP1","UDP2"]
httpList = ["HTTP1","HTTP2"]
cycleUdp = itertools.cycle(udpList)
cycleHttp = itertools.cycle(httpList)


def roundRobin(packetType):
    if packetType == "udp":
        return next(cycleUdp)
    if packetType == "http":
        return next(cycleHttp)
    
def routerPrint(packetType, variable):
    if packetType == "udp":
        return ("Packet %s sent to: %s" % (packetType,variable))
    if packetType == "http":
        return ("Packet %s sent to: %s" % (packetType,variable))
    if packetType == "tcp":
        return ("Packet %s discarded" % packetType)

generator = Packet_Generator(int(sys.argv[1]))
listUDP = []
listHTTP = []
listRouter = []

# Save the current stream
save_out = sys.stdout

# Define the log file
f = "router_log.log"
# Append to existing log file. 
# Change 'a' to 'w' to recreate the log file each time.
fsock = open(f, 'w')

# Set stream to file
sys.stdout = fsock

while generator.has_next():
    packet = generator.next()
    variable = roundRobin(packet.pkt_type)
    if packet.pkt_type == "udp":
        listUDP.append("MESSAGE: %s: %s" % (packet.src_ip, packet.content))
    if packet.pkt_type == "http":       
        listHTTP.append("MESSAGE: %s - %s - %s - %s - %s" % (strftime("%d-%m-%Y %H:%M:%S", gmtime()), packet.src_ip, packet.dest_ip, packet.content, variable))
    listRouter.append(routerPrint(packet.pkt_type, variable))

for i in range(0,len(listHTTP)-1):
    print (listHTTP[i])

print("\n")



sys.stdout = save_out
fsock.close()    

print ("UDP MESSAGES")

for k in range(0,len(listUDP)-1):
    print (listUDP[k])

print ("\n")
print ("\nREADING THE LOG")
a = open("router_log.log", "r")
print (a.read())

print("\n")

for j in range(0,len(listRouter)-1):
    print (listRouter[j])
