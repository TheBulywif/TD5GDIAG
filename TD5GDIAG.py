import threading
import diag_log
import drives
import global_funcs
import processes
import system_info
import mail
import os

if __name__ == "__main__":
    root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
    try:
        diag_log.init_logger()
        global_funcs.set_recursion()
        global_funcs.init_td5g()
        diag_log.logger.debug("INIT func_list && thread_list")
        diag_log.logger.info("                            ")
        func_list = [processes.check_running_processes, drives.drive_diag, system_info.get_sys_info]
        thread_list = []
        for func in func_list:
            diag_log.logger.debug(f"INIT THREAD FOR ({func})")
            thread = threading.Thread(target=func)
            diag_log.logger.debug(f"ADD THREAD FOR ({func}) to thread_list")
            diag_log.logger.info("                            ")
            thread_list.append(thread)
        for thread in thread_list:
            diag_log.logger.debug(f"START ({thread})")
            diag_log.logger.info("                            ")
            thread.start()
        for thread in thread_list:
            diag_log.logger.debug(f"JOIN ({thread})")
            diag_log.logger.info("                            ")
            thread.join()
        diag_log.end_log()
        mail.send_diagnostic_report()
        # global_funcs.open_results()
    except PermissionError as e:
        diag_log.logger.debug(e)

