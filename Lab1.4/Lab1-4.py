#
#
#
from ipaddress import IPv4Network
import random
from typing import List


class IPv4RandomNetwork(IPv4Network):
    def __init__(self, n_start=0, n_stop=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),random.randint(n_start, n_stop), False),strict=False)
    def regulars(self):
        return self.is_global and not (self.is_loopback or self.is_link_local or self.is_multicast or self.is_private or self.is_reserved or self.is_unspecified)
    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)
random.seed()

randlist: List[IPv4RandomNetwork] = []

while len(randlist) < 50:
    random_network = IPv4RandomNetwork(8, 24)
    if random_network not in randlist or random_network.regulars():
        randlist.append(random_network)


for x in sorted(sorted(randlist), key=IPv4RandomNetwork.key_value):
    print(x)

