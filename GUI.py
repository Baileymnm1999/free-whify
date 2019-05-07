from tkinter import *
import tkinter.ttk as ttk
from NetworkController import NetworkController
from Devices import *
import AttackAgent
import time
import threading
import sys


class GUI:

    def __init__(self, window, networkController):
        self.window = window
        self.networkController = networkController
        self.thread = None
        self.scanning = False;


    def configure_window(self):

        # create window
        self.window.title("free-whify | Wifi Deauther and Cracker")
        self.window.geometry("1000x800")
        self.window.config(bg="#f5f5f5")

        # create and attach scan btn
        self.scan_btn = Button(self.window, text="Scan", width=10, command=self.on_scan_btn)
        self.scan_btn.config(bg="#fff", activebackground="#0f0")
        self.scan_btn.grid(column=0, row=1, sticky="NSWE", padx=2, pady=2)
        
        # create and attach output text window
        self.text_box = Text(self.window, wrap="word", height = 50, width=80)
        self.text_box.config(state=DISABLED)
        self.text_box.grid(column=0, row=0, sticky="NSWE", padx=1, pady=1)

        # create notebook to hold tabs
        self.notebook = ttk.Notebook(self.window)

        # create deauth tab to hold deauth attack
        self.deauth_tab = Frame(self.notebook)
        self.deauth_tab.config(bg="#f5f5f5", padx=5, pady=5)

        # create and attach deauth btn to deauth tab
        self.deauth_btn = Button(self.deauth_tab, text="Deauth", width=10, command=self.on_deauth_btn)
        self.deauth_btn.config(bg="#fff", activebackground="#800000")
        self.deauth_btn.grid(column=0, row=0)

        # create and attach deauth target entry widget
        self.target = Entry(self.deauth_tab)
        self.target.grid(column=0, row=1)

        # attach tabs to notebook        
        self.notebook.add(self.deauth_tab, text="Deauth")
        self.notebook.grid(column=1 ,row=0, rowspan=2, sticky="NSWE")

        self.window.mainloop()


    def on_scan_btn(self):
        self.scan_btn.config(text="Stop Scan", bg="#0f0", activebackground="#f00", command=self.on_stop_scan_btn)
        threading.Thread(target=self.scan).start()
        threading.Thread(target=self.print_aps).start()


    def on_stop_scan_btn(self):
        self.scan_btn.config(text="Scan", bg="#fff", activebackground="#0f0", command=self.on_scan_btn)
        self.networkController.sniffing = False
        self.scanning = False


    def on_deauth_btn(self):
        trgt = self.target.get()
        ap = self.networkController.stations[trgt].access_point
        threading.Thread(target=AttackAgent.deauth, args=(trgt, ap, self.networkController.access_points[ap].channel, )).start()


    # scan for 'timeout' seconds
    def scan(self):
        if(not self.scanning):
            self.scanning = True
            self.networkController.start_scanning()
            self.scanning = False


    # print data for 'timeout' seconds
    def print_aps(self):
        while True:

            if not self.scanning or not self.networkController.sniffing:
                self.scanning = self.networkController.sniffing = False
                break
            
            aps = self.networkController.access_points
            stations = self.networkController.stations
            self.text_box.config(state=NORMAL)
            self.text_box.delete("1.0", END)
            self.text_box.insert("1.0", "-"*80 + "\n")
            self.text_box.insert("2.0", "BSSID" + " "*25)
            self.text_box.insert("2.30", "SSID" + " "*36)
            self.text_box.insert("2.70", "Channel\n")
            self.text_box.insert("3.0", "-"*80 + "\n")
            line = 4
            for key in aps:
                self.text_box.insert(str(line) + ".0", aps[key].bssid + " "*13)
                self.text_box.insert(str(line) + ".30", aps[key].ssid + " "*(40-len(aps[key].ssid)))
                self.text_box.insert(str(line) + ".70", str(aps[key].channel) + "\n")
                line += 1
            
            self.text_box.insert(str(line) + ".0", "-"*80 + "\n")
            line += 1
            self.text_box.insert(str(line) + ".0", "BSSID" + " "*25)
            self.text_box.insert(str(line) + ".30", "Client MAC" + " "*30)
            self.text_box.insert(str(line) + ".70", "Probes\n")
            line += 1
            self.text_box.insert(str(line) + ".0", "-"*80 + "\n")
            line += 1

            for key in stations:
                self.text_box.insert(str(line) + ".0", stations[key].access_point + " "*13)
                self.text_box.insert(str(line) + ".30", stations[key].mac + " "*(40-len(stations[key].mac)))
                self.text_box.insert(str(line) + ".70", str(stations[key].probes) + "\n")
                line += 1

            self.text_box.config(state=DISABLED)
            time.sleep(1)

