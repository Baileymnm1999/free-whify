from NetworkController import NetworkController
import time
import _thread

nc = NetworkController()

_thread.start_new_thread(nc.start_scanning, ())
print('here')

while True:
    aps = nc.access_points
    for key in aps:
        print(aps[key].bssid, aps[key].ssid, aps[key].channel)
    time.sleep(0.5)


