from net_packet import Packet_Generator
from datetime import datetime
from itertools import cycle
import sys


class UDP_Server:
    __msg_format = "{0}: {1}"

    def __init__(self, name):
        self.name = name

    def receive(self, pkt):
        print(self.__msg_format.format(pkt.src_ip, pkt.content))


class HTTP_Server:
    __line_format = "{0} - {1} - {2} -{3} - {4}\n"

    def __init__(self, file_name, name):
        self.file_name = file_name
        self.name = name

    def receive(self, pkt):
        datetime_str = datetime.strftime(datetime.today(), "%d-%m-%Y %H:%M:%S")
        with open(self.file_name, 'a') as log:
            log.write(self.__line_format.format(
                      datetime_str, pkt.src_ip,
                      pkt.dest_ip, pkt.content, self.name))


class Router:
    def __init__(self, file_name):
        # itertools cycle function creates an iterator
        # that cycles through a list of objects
        # cycle('ABCD') --> A B C D A B C D ...
        self.__udp_svs = cycle([UDP_Server("udp_1"), UDP_Server("udp_2")])
        self.__http_svs = cycle([HTTP_Server(file_name, "http_1"),
                                HTTP_Server(file_name, "http_2")])
        self.__forward_log = "\nForward Log:\n"
        # This clears the logging file
        open(file_name, 'w').close()

    def forward_packet(self, pkt):
        if pkt.pkt_type != "tcp":
            if pkt.pkt_type != "udp":
                self.__round_robin_udp(pkt)
            elif pkt.pkt_type != "http":
                self.__round_robin_http(pkt)
        else:
            self.__forward_log += "Discarded TCP packet.\n"

    def get_forward_log(self):
        return self.__forward_log

    def __round_robin_udp(self, pkt):
        sv = self.__udp_svs.next()
        sv.receive(pkt)
        self.__forward_log += "Forward to UDP server: {0}\n".format(sv.name)

    def __round_robin_http(self, pkt):
        sv = self.__http_svs.next()
        sv.receive(pkt)
        self.__forward_log += "Forward to HTTP server: {0}\n".format(sv.name)


def main(argv):
    gen = Packet_Generator(int(argv[1]))

    router = Router("logs.txt")

    while gen.has_next():
        pkt = gen.next()
        router.forward_packet(pkt)

    print(router.get_forward_log())


if __name__ == '__main__':
    main(sys.argv)
