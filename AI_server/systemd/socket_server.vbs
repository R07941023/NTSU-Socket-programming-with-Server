set ws=WScript.CreateObject("WScript.Shell") 
ws.Run "conda activate cuda10_mayavi_pyqt5 && cd C:\Windows\System32\socket && python socket_server.py",0