import os, subprocess
from multiprocessing import Process
from scapy.all import *
from Devices import *


class SniffError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NetworkController:

    def __init__(self, interface=""):
        self.access_points = {}
        self.stations = {}
        self.interface = interface
        self.sniffing = False


    def start_scanning(self):
        # Start the channel 
        self.sniffing = True
        p = Process(target=self.channel_hopper)
        p.start()
        try:
            sniff(iface=self.interface, prn=self.handle_packet, stop_filter=lambda p: not self.sniffing)
        except SniffError:
            print("sniff done")
        p.terminate()


    def stop_scanning(self):
        self.sniffing = False


    def capture_handshake(self, access_point):
        pass


    def channel_hopper(self):
        chans = ['1', '6', '7', '11', '36', '40', '44', '48', '52', '56', '60', '64', '100', '104', '108', 
            '112', '116', '120', '124', '128', '132', '136', '140', '144', '149', '153', '161', '165']
        while True:
            try:
                for chan in chans:
                    subprocess.call(['iwconfig', self.interface, 'chan', chan], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    time.sleep(0.25)
            except KeyboardInterrupt:
                break


    def handle_packet(self, packet):
        if not self.sniffing:
            raise SniffError("Sniffing execution stopped")

        if packet.type == 0 and packet.subtype == 8:
            ssid = packet.getlayer(Dot11Beacon)[1].info
            ssid = ssid.decode('ASCII')
            channel = int.from_bytes(packet.getlayer(Dot11Beacon)[3].info, byteorder='little')
            bssid = packet.addr2

            if bssid not in self.access_points:
                self.access_points[bssid] = AccessPoint(bssid, ssid, channel)

        if packet.type == 2:
            bssid = packet.addr1
            mac = packet.addr2

            if mac not in self.stations:
                self.stations[mac] = Station(bssid, mac)
            else:
                self.stations[mac].probes += 1



