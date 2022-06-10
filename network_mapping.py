import diag_log
import nmap3
import nmap
import os
from datetime import datetime

rep_path = "c:\\program files\\TD5G Diagnostics\\Network Info\\"
file = "network_report.txt"


def prep_doc():
    try:
        with open(os.path.join(rep_path, file), 'r+') as f:
            now = datetime.now()
            time = now.strftime("%m/%d/%Y %H:%M:%S")
            f.truncate(0)
            f.write("****TD5G Network Information****")
            f.write("\n")
            f.write(f"****{time}****")
            f.write("\n")
            f.write("\n")
            f.write("| {:<18} | {:<18} |".format('IP', 'SUBNET'))
            f.write("\n")
    except FileNotFoundError as e:
        diag_log.logger.error(e)
        with open(os.path.join(rep_path, file), mode='a'):
            pass
        prep_doc()


def ping_scan():
    nm = nmap3.NmapScanTechniques()
    scan_list = ['10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24', '192.168.1.0/24', '192.168.3.0/24']

    for item in scan_list:
        hosts = []
        nmap = nmap3.Nmap()
        nm = nmap3.NmapScanTechniques
        scan = nm.nmap_subnet_scan(nmap, item)
        print(scan)


if __name__ == "__main__":
    ping_scan()
