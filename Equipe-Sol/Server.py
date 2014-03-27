import sys
import datetime
from net_packet import Packet_Generator
i = datetime.datetime.now()
timeStart = str(i.day)+"-"+str(i.month)+"-"+str(i.year)+" "+str(i.hour)+":"+str(i.minute)+":"+str(i.second)
messageUDP = []
messageServer = []
file = open("Log.txt","w")
file.write("")

class Udp:

	def __init__(self,port,host,name):
		self.port = port
		self.host = host
		self.name = name

	def processPackage(self,package):
		#print("  Package Received:",package.pkt_type+"|"+package.src_ip+"|"+package.dest_ip+"|"+package.content+"|")
		messageUDP.append("  Message:"+package.src_ip+"|"+package.content)		

class Http:

	def __init__(self,port, host,name):
		self.port = port
		self.host = host
		self.name = name

	def processPackage(self,package):
		#print("  Package Received:",package.pkt_type+"|"+package.src_ip+"|"+package.dest_ip+"|"+package.content+"|")
		#print("  Message:",package.src_ip+"|"+package.content)
		writeToFile(package,self.name)

class Router:

	def __init__(self,udpServers,httpServers):
		self.udpServers = udpServers
		self.httpServers = httpServers

	def receivePackage(self,package):
		if(package.pkt_type == "udp"):
			self.choiceUdpServer(package)
		elif (package.pkt_type == "http"):
			self.choiceHttpServer(package)
		elif(package.pkt_type == "tcp"):
			messageServer.append("TCP Package denied!")		

	def choiceUdpServer(self,package):
		for el in range(0,len(udpServers)):
			if(udpServers[el][1] ==  0):
				messageServer.append("Package "+package.pkt_type+" sent to "+udpServers[el][0].name+":")
				self.udpServers[el][0].processPackage(package)
				udpServers[el][1] =  1
				break
			if(len(udpServers)-1 == el and udpServers[el][1] ==  1):
				messageServer.append("Package "+package.pkt_type+" sent to "+udpServers[0][0].name+":")
				self.udpServers[0][0].processPackage(package)
				udpServers[el][1] =  1
				for i in range(1,len(udpServers)):
					udpServers[i][1] = 0;
				break

	def choiceHttpServer(self,package):
		for el in range(0,len(httpServers)):
			if(httpServers[el][1] ==  0):
				messageServer.append("Package "+package.pkt_type+" sent to "+httpServers[el][0].name+":")
				httpServers[el][0].processPackage(package)				
				httpServers[el][1] =  1
				break
			if(len(httpServers)-1 == el and httpServers[el][1] ==  1):
				messageServer.append("Package "+package.pkt_type+" sent to "+httpServers[0][0].name+":")
				httpServers[0][0].processPackage(package)
				httpServers[el][1] =  1
				for i in range(1,len(httpServers)):
					httpServers[i][1] = 0;
				break

def generatePackages(size):
	listofPackages = []
	generator = Packet_Generator(size)
	while(generator.has_next()):
		listofPackages.append(generator.next())
	return listofPackages

def writeToFile(package,name):
	fileR = open("Log.txt","r")
	conteudo = fileR.read()
	fileR.close()
	file = open("Log.txt","w")	
	file.write(conteudo+"\n"+timeStart+" : "+package.src_ip+" - "+package.dest_ip+" - "+package.content+" - "+name)
	file.close()
	fileR.close()

packages = generatePackages(int(sys.argv[1]))

udpServers = [[Udp("80","123","UDP_1"),0],[Udp("80","123","UDP_2"),0]]
httpServers = [[Http("80","123","HTTP_1"),0],[Http("80","123","HTTP_2"),0]]
router = Router(udpServers,httpServers)

for el in range(0,len(packages)):	
	router.receivePackage(packages[el])
	
for el in range(0,len(messageUDP)):	
	print(messageUDP[el])
for el in range(0,len(messageServer)):	
	print(messageServer[el])
	