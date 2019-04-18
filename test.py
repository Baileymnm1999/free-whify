from NetworkController import NetworkController
import time
import _thread

nc = NetworkController()

_thread.start_new_thread(nc.start_scanning, ())
print('here')

while True:
    aps = nc.access_points
    st = nc.stations
    print(aps)
    for key in aps:
        print('AP: ', aps[key].bssid, aps[key].ssid, aps[key].channel)
    for key in st:
        print('STATION: ', st[key].access_point, st[key].mac, st[key].probes)
    # time.sleep(0.5)


