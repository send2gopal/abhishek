from ProcessExecutor import ProcessExecutor
from time import sleep

lclient = ProcessExecutor("IP", "username", "Password")
lserver = ProcessExecutor("IP", "username", "Password")


while True:
    process = lclient.getProcessFormServer()
    lserver.uploadProcessListToServer(process)
    print("File created at Server")
    sleep(5)

lclient.dispose()
lserver.dispose()
