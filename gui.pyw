import os
import threading
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog

import pythoncom
import wmi

import dvrlog_parse
import TD5GTools
from threading import Thread

import opFormat
import processes

version = '1.1.0'
windows = []
diagOutput = []
stop_event = threading.Event()
dvr_thread = Thread
network_thread = Thread
server_thread = Thread
td5g_thread = Thread
options_thread = Thread

proc_list = ["TDMonitor.exe", "TDService.exe", "EventsService.exe", "GPSLogConvertor.exe", "httpd.exe",
             "mysqld.exe", "javaw.exe", "relay266.exe", "QTLogToDB.exe", "mss.exe", "MSSUploadServer.exe",
             "TeamViewer.exe", "airControl2Server.exe", "extsvr.exe", "tdavlservice2.exe"]


# functions
def manual():
    messagebox.showinfo(f"TDII Auto-Diag v{version} User Manual \n",
                        f"<placeholder>")


def parse_log():
    outputText.insert(END, "Please Select DVRLog File" + '\n')
    file = filedialog.askopenfilename(initialdir=os.path.join(os.path.join(os.environ['USERPROFILE']),
                                                              'Desktop', 'TD5G Diagnostics'))
    outputText.insert(END, f"File Selected: {file}" + '\n')
    outputText.insert(END, f"Reading {file} and formatting for Parse")
    lines = dvrlog_parse.read_log(file)
    dvrLogFilters = [dvrlog_parse.parseMCUVersion(lines), dvrlog_parse.parseDVRFirmware(lines),
                     dvrlog_parse.parseRecMode(lines), dvrlog_parse.parseExitRecMode(lines),
                     dvrlog_parse.parseKillSignal(lines), dvrlog_parse.parseQuitDVR(lines),
                     dvrlog_parse.parseFlashFormat(lines), dvrlog_parse.parseFileBackup(lines)]
    outputText.insert(END, f"{file} read and formatted. Parsing. . . . .")
    for dvrLogFilter in dvrLogFilters:
        outputText.insert(END, f"{dvrLogFilter}" + '\n')


def auto_log_parse():
    try:
        outputText.insert(END, f"Beginning System Scan for DVRLogs" + '\n')
        files = dvrlog_parse.find_dvrlogs()
        for file in files:
            lines = dvrlog_parse.read_log(file)
            dvrLogFilters = ['\n', dvrlog_parse.parseMCUVersion(lines), dvrlog_parse.parseDVRFirmware(lines),
                             dvrlog_parse.parseRecMode(lines), dvrlog_parse.parseExitRecMode(lines),
                             dvrlog_parse.parseKillSignal(lines), dvrlog_parse.parseQuitDVR(lines),
                             dvrlog_parse.parseFlashFormat(lines), dvrlog_parse.parseFileBackup(lines), '\n']
            outputText.insert(END, f"Parsing: {file}" + '\n')
            for dvrLogFilter in dvrLogFilters:
                outputText.insert(END, f"{dvrLogFilter}" + '\n')
    except UnicodeDecodeError as e:
        print(e)


def placeholder():
    outputText.insert(END, "This function is still under development" + '\n')
    outputText.insert(END, "Contact: MarkL@surveillance-247.com for assistance / feedback." + '\n')
    outputText.insert(END, "Thank you." + '\n')


def terminate_services():
    names = ["apache",
             "mysql",
             "java",
             "TD monitor",
             "server",
             "qtlogtodb",
             "gps",
             "mss",
             "tdservice",
             "eventservice",
             "relay266",
             "tdval"]
    services = [TD5GTools.apache_off,
                TD5GTools.mysql_off,
                TD5GTools.java_off,
                TD5GTools.monitor_off,
                TD5GTools.server_off,
                TD5GTools.qtlogtodb_off,
                TD5GTools.gps_off,
                TD5GTools.mss_off,
                TD5GTools.tdservice_off,
                TD5GTools.eventsservice_off,
                TD5GTools.relay266_off,
                TD5GTools.tdval_off]
    for service in services:
        for name in names:
            if str(service).__contains__(name):
                outputText.insert(END, f"Terminating: {name}" + '\n')
                service()


def activate_services():
    names = ["apache",
             "mysql",
             "java",
             "TD monitor",
             "server",
             "qtlogtodb",
             "gps",
             "mss",
             "tdservice",
             "eventservice",
             "relay266",
             "tdval"]
    services = [TD5GTools.apache_off,
                TD5GTools.mysql_off,
                TD5GTools.java_off,
                TD5GTools.monitor_off,
                TD5GTools.server_off,
                TD5GTools.qtlogtodb_off,
                TD5GTools.gps_off,
                TD5GTools.mss_off,
                TD5GTools.tdservice_off,
                TD5GTools.eventsservice_off,
                TD5GTools.relay266_off,
                TD5GTools.tdval_off]
    for service in services:
        for name in names:
            if str(service).__contains__(name):
                outputText.insert(END, f"Activating: {name}" + '\n')
                service()


def reboot_services():
    terminate_services()
    activate_services()


def td5gServices():
    running_services = []
    pythoncom.CoInitialize()
    f = wmi.WMI()
    header1 = opFormat.center("PROCESS", 20)
    header2 = opFormat.center("ID", 6)
    header3 = opFormat.center("STATE", 7)
    outputText.insert(END, "| {:<19} | {:<4} | {:<7} |\n".format(header1, header2, header3))
    for process in f.win32_Process():
        running_services.append(process)
    for var in proc_list:
        state = 0
        for process in running_services:
            print(f"Checking {var} against {process.Name}\n")
            if var == process.Name:
                state = 1
                break
            else:
                state = 0
        if state == 1:
            print(state)
            data1 = opFormat.center(var, 20)
            data2 = opFormat.center(str(process.processId), 6)
            data3 = opFormat.center("RUNNING", 7)
            outputText.insert(END, "| {:<19} | {:<4} | {:<7} |\n".format(data1, data2, data3))
        elif state == 0:
            print(state)
            data1 = opFormat.center(var, 20)
            data2 = opFormat.center(str("NAN"), 6)
            data3 = opFormat.center("STOPPED", 7)
            outputText.insert(END, "| {:<19} | {:<4} | {:<7} |\n".format(data1, data2, data3))


if __name__ == '__main__':
    global outputText
    threads = []
    root = Tk()
    root.geometry("800x700")
    root.configure(bg='ghost white')
    root.resizable(False, False)
    root.title(f'TD5G Diagnostic Tools v{version}')
    # root.iconbitmap('s247ico.ico')
    rows = 0
    while rows < 50:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1
    # root.overrideredirect(True)
    # DVR TOOLS INTERFACE
    dvrFrame = LabelFrame(root, text="DVR Tools", padx=5, pady=5)
    dvrFrame.configure(bg='ghost white')
    dvrBtn1 = Button(dvrFrame, text="Parse Single DVRLog File", width=22,
                     command=lambda: [dvr_thread(target=parse_log).start()])
    dvrBtn2 = Button(dvrFrame, text="Parse Multiple DVRLog Files", width=22,
                     command=lambda: [dvr_thread(target=auto_log_parse).start()])
    dvrBtn3 = Button(dvrFrame, text="Auto Parse", width=22,
                     command=lambda: [dvr_thread(target=auto_log_parse).start()])
    dvrBtn4 = Button(dvrFrame, text="Telnet Diagnostic", command=placeholder, width=22)
    # NETWORK TOOLS INTERFACE
    networkFrame = LabelFrame(root, text="Network Tools", padx=5, pady=5)
    networkFrame.configure(bg='ghost white')
    networkBtn1 = Button(networkFrame, text="DVR Scan", command=placeholder, width=22)
    networkBtn2 = Button(networkFrame, text="Bridge Scan", command=placeholder, width=22)
    networkBtn3 = Button(networkFrame, text="Access Point Scan", command=placeholder, width=22)
    networkBtn4 = Button(networkFrame, text="Comprehensive Scan", command=placeholder, width=22)
    # SERVER TOOLS INTERFACE
    serverFrame = LabelFrame(root, text="Server Tools", padx=5, pady=5)
    serverFrame.configure(bg='ghost white')
    serverBtn1 = Button(serverFrame, text="System Info", command=placeholder, width=22)
    serverBtn2 = Button(serverFrame, text="NIC Info", command=placeholder, width=22)
    serverBtn3 = Button(serverFrame, text="Storage Info", command=placeholder, width=22)
    serverBtn4 = Button(serverFrame, text="A/V Info", command=placeholder, width=22)
    serverBtn5 = Button(serverFrame, text="Firewall Info", command=placeholder, width=22)
    # TD SERVICES INTERFACE
    tdServicesFrame = LabelFrame(root, text="TD5G Tools", padx=5, pady=5)
    tdServicesFrame.configure(bg='ghost white')
    tdServiceBtn1 = Button(tdServicesFrame, text="Reboot TD5G Services",
                           command=lambda: [dvr_thread(target=reboot_services).start()], width=22)
    tdServiceBtn2 = Button(tdServicesFrame, text="Turn Off TD5G Services",
                           command=lambda: [dvr_thread(target=terminate_services).start()], width=22)
    tdServiceBtn3 = Button(tdServicesFrame, text="Turn On TD5G Services",
                           command=lambda: [dvr_thread(target=activate_services).start()], width=22)
    tdServiceBtn4 = Button(tdServicesFrame, text="Check Running Services",
                           command=lambda: [dvr_thread(target=td5gServices).start()], width=22)
    # SOFTWARE FUNCTION INTERFACE
    softwareFrame = LabelFrame(root, text="TD5G Diagnostic Tool Options", padx=5, pady=5)
    softwareFrame.configure(bg='ghost white')
    softwareBtn1 = Button(softwareFrame, text="Settings", command=placeholder, width=22)
    softwareBtn2 = Button(softwareFrame, text="Help / Manual", command=placeholder, width=22)
    softwareBtn3 = Button(softwareFrame, text="Quit", command=root.destroy, width=22)
    # OUTPUT FRAME
    outputFrame = LabelFrame(root, text="Diagnostic Output", padx=5, pady=5)
    outputFrame.configure(bg='ghost white')
    outputText = Text(outputFrame, height=50, width=75)
    # GUI ELEMENT POSITIONING
    dvrFrame.grid(column=0, row=0, padx=5, pady=5)
    dvrBtn1.pack()
    dvrBtn2.pack()
    dvrBtn3.pack()
    dvrBtn4.pack()
    networkFrame.grid(column=0, row=1, padx=5, pady=5)
    networkBtn1.pack()
    networkBtn2.pack()
    networkBtn3.pack()
    networkBtn4.pack()
    serverFrame.grid(column=0, row=2, padx=5, pady=5)
    serverBtn1.pack()
    serverBtn2.pack()
    serverBtn3.pack()
    serverBtn4.pack()
    serverBtn5.pack()
    tdServicesFrame.grid(column=0, row=3, padx=5, pady=5)
    tdServiceBtn1.pack()
    tdServiceBtn2.pack()
    tdServiceBtn3.pack()
    tdServiceBtn4.pack()
    softwareFrame.grid(column=0, row=4, padx=5, pady=5)
    softwareBtn1.pack()
    softwareBtn2.pack()
    softwareBtn3.pack()
    outputFrame.grid(column=1, row=0, rowspan=5, padx=5, pady=5)
    outputText.pack()

    root.mainloop()
