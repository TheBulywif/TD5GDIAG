import sys
import diag_log
import os
from datetime import datetime
from zipfile import ZipFile
import diag_log


def center(a, b):
    var = ""
    x = len(a)
    i = 0
    while i < ((b - x) / 2):
        var += " "
        i += 1
    i = 0
    var += a
    while i < ((b - x) / 2):
        var += " "
        i += 1
    while len(var) != b:
        if len(var) > b:
            var = var[:-1]
        if len(var) < b:
            var += " "
    return var


def set_recursion():
    diag_log.logger.debug("SETTING RECURSION LIMIT: 1500")
    sys.setrecursionlimit(1500)


def check_path(path):
    try:
        if path.__contains__(".txt"):
            with open(os.path.join(path), 'r+') as f:
                now = datetime.now()
                time = now.strftime("%m/%d/%Y %H:%M:%S")
                f.truncate(0)
                f.write(f"****TD5G {path}****")
                f.write("\n")
                f.write(f"****{path}****")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("\n")
        else:
            if os.path.exists(path):
                diag_log.logger.debug(f"{path} EXISTS")
            else:
                diag_log.logger.debug(f"{path} DOES NOT EXIST")
                os.makedirs(path)
    except PermissionError as e:
        diag_log.logger.error(f"Permission Error: {e}")
    except FileNotFoundError as e:
        diag_log.logger.error(f"FileNotFoundError: {e}")
        with open(path, mode='a'):
            pass
        check_path(path)


def initializeDirectories():
    files = ["system_report.txt",
             "process_report.txt",
             "drive_report.txt"]
    root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
    diag_log.logger.info(f"Beginning TD5GDIAG Initialization")
    check_path(root)
    for file in files:
        check_path(os.path.join(root, file))


def init_td5g():
    initializeDirectories()
    diag_log.init_logger()


def open_results():
    root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
    files = [f"system_report.txt",
             f"process_report.txt",
             f"drive_report.txt"]
    for file in files:
        osCommandString = f"notepad.exe {os.path.join(root, file)}"
        os.system(osCommandString)
