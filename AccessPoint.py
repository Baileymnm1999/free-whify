

class AccessPoint:

    def __init__(self, bssid, ssid, channel, beacons):
        self.bssid = bssid
        self.ssid = ssid
        self.channel = channel
        self.beacons = beacons


class Station:

    def __init__(self, access_point, mac, probes):
        self.access_point = access_point
        self.mac = mac
        self.probes = probes


