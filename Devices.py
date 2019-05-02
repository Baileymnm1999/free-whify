class AccessPoint:

    def __init__(self, bssid, ssid, channel):
        self.bssid = bssid
        self.ssid = ssid
        self.channel = channel


class Station:

    def __init__(self, access_point, mac):
        self.access_point = access_point
        self.mac = mac
        self.probes = 1


