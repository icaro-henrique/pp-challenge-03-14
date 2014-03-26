"""
Como usar:
Em seu script, adicionar a linha a seguir no topo:
    from net_packet import Packet_Generator
Quando for usar o gerador de pacotes, inicie-o da seguinte maneira:
    generator = Packet_Generator(N)
Sendo N a quantidade de pacotes a serem gerados. Para gerar um pacote, use:
    packet = generator.next()
Isto retorna um pacote se a quantidade informada na inicializacao
nao foi alcancada, caso contrario, None eh retornado.
Use a funcao abaixo para verificar se ainda eh possivel gerar pacotes:
    will_generate = generator.has_next()
Acesse os atributos do pacote da seguinte maneira:
    src_ip = packet.src_ip
    dest_ip = packet.dest_ip
    dest_ip = packet.dest_ip
    pkt_type = packet.pkt_type
    content = packet.content
"""
from random import randrange
from random import randint
from random import choice
from string import ascii_uppercase
from string import ascii_lowercase
from string import digits


PACKET_TYPES = {1: "tcp", 2: "udp", 3: "http"}


class Net_Packet:
    """
    Net_Packet object has the following structure:
    |               |               |                   |               |
    |   PKT_TYPE    |   SOURCE_IP   |   DESTINATION_IP  |   CONTENT     |
    |               |               |                   |               |
    """
    def __init__(self, pkt_type, src_ip, dest_ip, content):
        self.pkt_type = pkt_type
        self.src_ip = src_ip
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.content = content

    def __str__(self):
        """
        Pretty print the packet properties.
        """
        return "| " + self.pkt_type + " | " +\
            self.src_ip + " | " + self.dest_ip + " | " + self.content + " |"


class Packet_Generator:
    """
    Generator for Net_Packet objects. In the constructor, pass the number
    of packets you want to be generated.
    e.g.
        generator = Packet_Generator(100)
    """
    def __init__(self, quantity):
        self.quantity = quantity
        self.count = 0

    def has_next(self):
        """
        Checks if the quantity set in the constructor has been reached.
        """
        return self.count < self.quantity

    def next(self):
        """
        Generates a new packet while the quantity set in the constructor
        hasn't been reached, returns None after that
        """
        if self.count < self.quantity:
            self.count += 1
            return Net_Packet(self.__randomize_type(),
                              self.__generate_ip(), self.__generate_ip(),
                              self.__generate_alphanumeric_string(16))

        return None

    def __randomize_type(self):
        """
        Randomize a packet type based in the "PACKET_TYPES" dictionary.
        """
        type_ = randint(1, 3)

        return PACKET_TYPES[type_]

    def __generate_ip(self):
        """
        Generate a valid ip address, including the exclusion of
        invalid ranges.
        """
        not_valid = [10, 127, 169, 172, 192]

        first = randrange(1, 256)
        while first in not_valid:
            first = randrange(1, 256)

        ip = ".".join([str(first), str(randrange(1, 256)),
                      str(randrange(1, 256)), str(randrange(1, 256))])

        return ip

    def __generate_alphanumeric_string(self, char_count):
        """
        Randomize a choice "char_count" quantity of any a-z, A-Z
        or 0-9 characters.
        """
        return ''.join(choice(ascii_uppercase + ascii_lowercase + digits)
                       for n in range(char_count))
