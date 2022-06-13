@ECHO OFF
ECHO TD5G Services Restart
ECHO Written By Mark Louprette - Updated 6-13-22
cd c:\SmartSvrApps\TD5GTools
ECHO ***SHUTTING DOWN ALL TOUCHDOWN APPLICATIONS***
Taskkill /IM server.exe /F
Taskkill /IM MSSUploadServer.exe /F
Taskkill /IM mss.exe /F
Taskkill /IM GPSLogConvertor.exe /F
Taskkill /IM QTLogToDB.exe /F
Taskkill /IM EventsService.exe /F
Taskkill /IM TDService.exe /F
Taskkill /IM tdavlservice2.exe /F
TaskKill /IM TDMonitor.exe /F
Taskkill /IM javaw.exe /F
ECHO *** SHUTTING DOWN APACHE***
net stop apache2.4
ECHO ***SHUTTING DOWN MySQL***
net stop mysql
ECHO ***RESTARTING MySQL***
net start mysql
ECHO ***Restarting Java 14***
"C:\Program Files (x86)\Java\jdk1.6.0_10\binjava.exe" -jar c:\resin-3.1.0\lib\resin.jar start
ECHO ***RESTARTING Touchdown Applications***
cd C:\SmartSvrApps
ECHO start server.exec
start server.exe
ECHO start QTLogToDB.exe
start QTLogToDB.exe
ECHO start GPSLogConvertor.exe -background
start GPSLogConvertor.exe -background
ECHO start MSSUploadServer.exe
start MSSUploadServer.exe
ECHO start hstart.exe /NOCONSOLE "C:\SmartSvrApps\mss.exe"
start hstart.exe /NOCONSOLE "C:\SmartSvrApps\mss.exe"
ECHO start TDMonitor.exe
start TDMonitor.exe
ECHO start TDService.exe
start TDService.exe
ECHO start EventsService.exe
start EventsService.exe
ECHO **RESTARTING Apache***
net start apache2.4