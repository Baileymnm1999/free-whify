from NetworkController import NetworkController
from GUI import *

nc = NetworkController()

window = Tk()

gui = GUI(window, nc)

gui.configure_window()

