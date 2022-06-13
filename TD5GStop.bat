@ECHO OFF
ECHO TD5G Services Stop - MSS
ECHO Written By Mark Louprette - Updated 6-13-22
cd c:\SmartSvrApps\TD II Tools
ECHO ***SHUTTING DOWN ALL TOUCHDOWN APPLICATIONS***
Taskkill /IM server.exe /F
Taskkill /IM MSSUploadServer.exe /F
Taskkill /IM mss.exe /F
Taskkill /IM GPSLogConvertor.exe /F
Taskkill /IM QTLogToDB.exe /F
Taskkill /IM EventsService.exe /F
Taskkill /IM TDService.exe /F
Taskkill /IM tdavlservice2.exe /F
Taskkill /IM TDMonitor.exe /F
ECHO *** SHUTTING DOWN APACHE***
net stop apache2.4
ECHO ***SHUTTING DOWN MySQL***
net stop mysql