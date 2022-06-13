@ECHO OFF
ECHO TD5G Start Services
ECHO Written By Mark Louprette - Updated 6-13-2022
cd c:\SmartSvrApps\TD II Tools
ECHO ***STARTING MySQL***
net start mysql
ECHO ***STARTING Java 14***
"C:\Program Files (x86)\Java\jdk1.6.0_10\binjava.exe" -jar c:\resin-3.1.0\lib\resin.jar start
ECHO ***STARTING Touchdown Applications***
cd C:\SmartSvrApps
ECHO STARTING server.exec
start server.exe
ECHO STARTING QTLogToDB.exe
start QTLogToDB.exe
ECHO STARTING GPSLogConvertor.exe -background
start GPSLogConvertor.exe -background
ECHO STARTING MSSUploadServer.exe
start MSSUploadServer.exe
ECHO STARTING hstart.exe /NOCONSOLE "C:\SmartSvrApps\mss.exe"
start hstart.exe /NOCONSOLE "C:\SmartSvrApps\mss.exe"
ECHO STARTING TDMonitor.exe
start TDMonitor.exe
ECHO STARTING TDService.exe
start TDService.exe
ECHO STARTING EventsService.exe
start EventsService.exe
ECHO **STARTING Apache***
net start apache2.4