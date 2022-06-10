import os


def apache_on():
    os.system('cmd /c net start httpd.exe')


def apache_off():
    os.system('cmd /c net stop httpd.exe')


def mysql_on():
    os.system('cmd /c net start mysqld.exe')


def mysql_off():
    os.system('cmd /c net stop mysqld.exe')
    os.system('cmd /c TaskKill /IM mysqld.exe /F')


def java_on():
    os.system('cmd /c "C:\\Program Files (x86)\\Java\\jdk1.6.0_10\\bin\\java.exe" '
              '-jar c:\\resin-3.1.0\\lib\\resin.jar start')


def java_off():
    os.system('cmd /c TaskKill /IM javaw.exe /F')


def monitor_on():
    os.system('cmd /c start C:\\SmartSvrApps\\TDMonitor.exe')


def monitor_off():
    os.system('cmd /c TaskKill /IM TDMonitor.exe /F')


def server_on():
    os.system('cmd /c start c:\\SmartSvrApps\\Server.exe')


def server_off():
    os.system('cmd /c TaskKill /IM server.exe /F')


def qtlogtodb_on():
    os.system('cmd /c start C:\\SmartSvrApps\\QTLogToDB.exe')


def qtlogtodb_off():
    os.system('cmd /c TaskKill /IM QTLogToDB.exe /F')


def gps_on():
    os.system('cmd /c start C:\\SmartSvrApps\\GPSLogConvertor.exe -background')


def gps_off():
    os.system('cmd /c TaskKill /IM GPSLogConvertor.exe /F')


def mss_on():
    os.system('cmd /c start C:\\SmartSvrApps\\hstart.exe /NOCONSOLE "C:\SmartSvrApps\mss.exe"')
    os.system('cmd /c start C:\\SmartSvrApps\\MSSUploadServer.exe')


def mss_off():
    os.system('cmd /c TaskKill /IM MSSUploadServer.exe /F')
    os.system('cmd /c TaskKill /IM mss.exe /F')


def tdservice_on():
    os.system('cmd /c start C:\\SmartSvrApps\\TDService.exe')


def tdservice_off():
    os.system('cmd /c TaskKill /IM TDService.exe /F')


def eventsservice_on():
    os.system('cmd /c start C:\\SmartSvrApps\\EventsService.exe')


def eventsservice_off():
    os.system('cmd /c TaskKill /IM EventsService.exe /F')


def relay266_on():
    os.system('cmd /c start c:\\relay266\\relay266.exe')


def relay266_off():
    os.system('cmd /c TaskKill /IM relay266.exe /F')


def tdval_on():
    os.system('cmd /c start c:\\SmartSvrApps\\tdavlservice2.exe')


def tdval_off():
    os.system('cmd /c TaskKill /IM tdavlservice2.exe /F')
