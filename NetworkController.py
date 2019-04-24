import os, subprocess
from multiprocessing import Process
from scapy.all import *
from AccessPoint import AccessPoint


class NetworkController:

    def __init__(self):
        self.access_points = {}
        self.interface = "wlp2s0"

    def start_scanning(self):
        # Start the channel hopper
        p = Process(target=self.channel_hopper)
        p.start()
        sniff(iface=self.interface, prn=self.handle_packet)

    def stop_scanning(self):
        pass

    def capture_handshake(self, access_point):
        pass

    def channel_hopper(self):
        chans = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '36', '40',
                 '44', '48', '52', '56', '60', '64', '100', '104', '108', '112', '116', '120',
                 '124', '128', '132', '136', '140', '144', '149', '153', '161', '165', '169']
        while True:
            try:
                for chan in chans:
                    subprocess.call(['iwconfig', self.interface, 'chan', chan], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    time.sleep(0.5)
            except KeyboardInterrupt:
                break

    def handle_packet(self, packet):
        if packet.type == 0 and packet.subtype == 8:
            ssid = packet.getlayer(Dot11Beacon)[1].info
            ssid = ssid.decode('ASCII')
            channel = int.from_bytes(packet.getlayer(Dot11Beacon)[3].info, byteorder='little')
            bssid = packet.addr2

            if bssid not in self.access_points:
                self.access_points[bssid] = AccessPoint(bssid, ssid, channel)


