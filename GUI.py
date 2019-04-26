from tkinter import *
from tkinter.ttk import *
from NetworkController import NetworkController
from AttackAgent import AttackAgent
import time
import threading


class GUI:

    threads = []
    scanCounter = 0;

    def __init__(window, networkController):
        self.window = window
        self.networkController = networkController


    def configure_window():
        self.window.title("free-whify | Wifi Deauther and Cracker")
        self.window.geometry('500x500')
        startScanning = Button(self.window, text="Start Scanning", command= lambda: (startStopScanning(True)))
        stopScanning = Button(self.window, text="Stop Scanning", command= lambda: (startStopScanning(False)))

        startScanning.grid(column=0, row=0)
        stopScanning.grid(column=3, row=0)
        self.window.mainloop()

    def startStopScanning(scan):
        if(scan and scanCounter == 0):
            scanCounter++
            scanThread = threading.thread(target = self.networkController.channel_hopper, ())
            threads.append(scanThread)
            scanThread.start()
        else if(!scan and scanCounter == 1):
            scanCounter--
            threads[0].join()
        else:
            #There is no scan to stop or one is already started
