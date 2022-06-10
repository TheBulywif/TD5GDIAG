import diag_log
import global_funcs
import platform
import psutil
import subprocess
import os
global svrName
td5gServer = platform.uname()
rep_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
file = f"{rep_path}\\system_report.txt"


def get_sys_info():
    try:
        svrName = td5gServer.node
        osType = td5gServer.system
        osRelease = td5gServer.release
        osVersion = td5gServer.version
        svrBit = td5gServer.machine
        svrCpu = td5gServer.processor
        svrRam = psutil.virtual_memory()
        systemInfo = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        write_sys_info(systemInfo)
    except Exception as e:
        diag_log.logger.error(e)


def write_sys_info(systemInfo):
    try:
        info = []
        for item in systemInfo:
            info.append(str(item.split("\r")[:-1]))
        for i in info:
            with open(file, 'a') as f:
                f.write(i[2:-2])
                f.write("\n")
            # diag_log.logger.info(i[2:-2])
    except FileNotFoundError as e:
        diag_log.logger.error(e)
        with open(file, mode='a'):
            pass
        write_sys_info(systemInfo)


if __name__ == "__main__":
    get_sys_info()
