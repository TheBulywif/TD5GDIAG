import os
from datetime import datetime
import pythoncom
import wmi
import diag_log
import opFormat

rep_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
file = f"{rep_path}\\process_report.txt"


class Process:
    def __init__(self, process, pid, state):
        self._procName = process
        self._procPID = pid
        self._procState = state

    @property
    def procName(self):
        print("procName getter method called")
        return self._procName

    @property
    def procPID(self):
        print("procPID getter method called")
        return self._procPID

    @property
    def procState(self):
        print("procState getter method called")
        return self._procState

    # a setter function
    @procName.setter
    def procName(self, var):
        print("procName setter method called")
        self._procName = var

    @procPID.setter
    def procPID(self, var):
        print("procPID setter method called")
        self._procPID = var

    @procState.setter
    def procState(self, var):
        print("procState setter method called")
        self._procState = var


def check_running_processes():
    proc_list = ["TDMonitor.exe", "TDService.exe", "EventsService.exe", "GPSLogConvertor.exe", "httpd.exe",
                 "mysqld.exe", "javaw.exe", "relay266.exe", "QTLogToDB.exe", "mss.exe", "MSSUploadServer.exe",
                 "TeamViewer.exe", "airControl2Server.exe", "extsvr.exe", "tdavlservice2.exe"]
    try:
        f = wmi.WMI()
        header1 = opFormat.center("PROCESS", 20)
        header2 = opFormat.center("ID", 6)
        header3 = opFormat.center("STATE", 7)
        print("| {:<19} | {:<4} | {:<7} |".format(header1, header2, header3))
        for process in f.win32_Process():
            proc = Process
            for var in proc_list:
                data1 = opFormat.center(var, 20)
                data2 = opFormat.center(str("NAN"), 6)
                data3 = opFormat.center("STOPPED", 7)
                if process.Name == var:
                    data1 = opFormat.center(var, 20)
                    data2 = opFormat.center(str(process.processId), 6)
                    data3 = opFormat.center("RUNNING", 7)
                    print("| {:<19} | {:<4} | {:<7} |".format(data1, data2, data3))
    except FileNotFoundError as e:
        diag_log.logger.error(e)
        with open(file, mode='a'):
            pass
        check_running_processes()


if __name__ == "__main__":
    check_running_processes()
