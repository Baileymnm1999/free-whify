from tkinter import *
from tkinter.ttk import *
from NetworkController import NetworkController
from AttackAgent import AttackAgent
import time
import _thread


class GUI:

    def __init__(window, networkController):
        self.window = window
        self.networkController = networkController


    def configure_window():
        self.window.title("free-whify | Wifi Deauther and Cracker")
        self.window.geometry('500x500')
        startScanning = Button(self.window, text="Start Scanning", command= lambda: (start()))
        stopScanning = Button(self.window, text="Stop Scanning", command= lambda: (stop()))

        startScanning.grid(column=0, row=0)
        stopScanning.grid(column=3, row=0)
        self.window.mainloop()

    def start():
        _thread.start_new_thread(self.networkController.channel_hopper, ())

    def stop():
        nc.stop_scanning()
