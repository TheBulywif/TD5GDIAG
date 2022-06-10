import ipaddress
import os
from datetime import datetime
import diag_log
import global_funcs

activeIps = []
rep_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'results.zip')
file = "c:\\program files\\TD5G Diagnostics\\Network Info\\ip_report.txt"


def output(active_ip_list):
    td5g_active_ips = active_ip_list
    tempList = []
    with open(os.path.join(file), 'r+') as f:
        now = datetime.now()
        time = now.strftime("%m/%d/%Y %H:%M:%S")
        f.truncate(0)
        f.write("****TD5G IP Information****")
        f.write("\n")
        f.write(f"****{time}****")
        f.write("\n")
        f.write("\n")
        f.write("| {:<15} | {:<6} | {:<10} |".format('IP', 'STATUS', 'LAST SEEN'))
        for key in td5g_active_ips.items():
            tempList.append(key)
            print(tempList)


def scan():
    network_clients = []
    j = 0
    diag_log.logger.info("Scanning Started... \n")
    ip_list = ['192.168.1.0/24', '192.168.3.0/24', '10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24']
    while j < len(ip_list):
        try:
            i = 0
            ip = ''
            net_addr = ip_list[j]
            ip_net = ipaddress.ip_network(net_addr)
            diag_log.logger.debug(f"Setting IP Network from {ip_net}")
            diag_log.logger.debug(f"net_addr: {net_addr}")
            all_hosts = list(ip_net.hosts())
            for host in all_hosts:
                ip = host
                res = os.popen(f"ping {ip} -n 1 -w 150").read()
                diag_log.logger.debug(f"Command: {res}")
                if "Request timed out" in res:
                    pass
                elif "Destination host unreachable" in res:
                    pass
                else:
                    network_clients.append({'IP': str(ip), 'STATUS': 'ACTIVE'})
                    diag_log.logger.debug(str(ip) + ' ACTIVE\n')
            j += 1
        except KeyboardInterrupt:
            break
        except IndexError as e:
            diag_log.logger.error(e)
    for client in network_clients:
        print(client)


if __name__ == '__main__':
    scan()
