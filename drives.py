import shutil
import os
import diag_log
from datetime import datetime
rep_path = "c:\\program files\\TD5G Diagnostics\\Network Info\\"
file = "network_map.txt"

def drive_diag():
    root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
    file = "drive_report.txt"
    path = os.path.join(root, file)
    diag_log.logger.info("LOOKING FOR DRIVES")
    diag_log.logger.info("                            ")
    drives = [chr(x) + ":\\" for x in range(65, 91) if os.path.exists(chr(x) + ":\\")]
    diag_log.logger.info("DRIVES FOUND: ")
    try:
        with open(os.path.join(path), 'r+') as f:
            now = datetime.now()
            time = now.strftime("%m/%d/%Y %H:%M:%S")
            f.truncate(0)
            f.write("****TD5G Drive Information****")
            f.write("\n")
            f.write(f"****{time}****")
            f.write("\n")
            f.write("\n")
            f.write("| {:<5} | {:<6} | {:<5} | {:<6} | {:<2} | {:<6}".format('Drive', 'Total', 'Used', 'Empty',
                                                                             '%', 'Notes'))
            f.write("\n")
            for drive in drives:
                diag_log.logger.info(drive)
                usage = shutil.disk_usage(drive)
                total = usage[0] / (1024 ** 3)
                total = int(total)
                used = usage[1] / (1024 ** 3)
                used = int(used)
                remaining = usage[2] / (1024 ** 3)
                remaining = int(remaining)
                percent = (remaining / total) * 100
                percent = int(percent)
                if percent < 30:
                    note = "****WARNING | LOW DISK SPACE****"
                else:
                    note = " "
                f.write("| {:<5} | {:<6} | {:<5} | {:<6} | {:<2} | {:<6}".format(drive, total, used, remaining,
                                                                                 percent, note))
                f.write("\n")
    except FileNotFoundError as e:
        diag_log.logger.error(e)
        with open(os.path.join(rep_path, file), mode='a'):
            pass
        drive_diag()
    except Exception as e:
        diag_log.logger.error(e)
