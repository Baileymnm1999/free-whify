import os, subprocess
from scapy.all import *
from AccessPoint import *


class NetworkController:

    def __init__(self):
        self.access_points = {}
        self.stations = {}

    def start_scanning(self):
        sniff(iface="wlp2s0", prn=self.handle_packet)

    def stop_scanning(self):
        pass

    def capture_handshake(self, access_point):
        pass

    def handle_packet(self, packet):

        print('here')
        if packet.type == 0 and packet.subtype == 8:
            ssid = packet.getlayer(Dot11Beacon)[1].info
            ssid = ssid.decode('ASCII')
            channel = int.from_bytes(packet.getlayer(Dot11Beacon)[3].info, byteorder='little')
            bssid = packet.addr2

            if bssid not in self.access_points:
                self.access_points[bssid] = AccessPoint(bssid, ssid, channel, 1)
        #     else:
        #         self.access_points[bssid].beacons += 1
        #
        # if packet.type == 0 and packet.subtype == 4:
        #     # ssid = packet.getlayer(Dot11Beacon)[1].info
        #     # ssid = ssid.decode('ASCII')
        #     mac = packet.addr2
        #
        #     if mac not in self.stations:
        #         self.access_points[mac] = Station(None, mac, [])
        #


