import paramiko
import os


class ProcessExecutor:

    def __init__(self, server, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        client.connect(server, username=username, password=password)
        self.client = client

    def getProcessFormServer(self):
        output = []
        stdin, stdout, stderr = self.client.exec_command('ps aux | less')
        for line in stdout:
            output.append(line)
        return output;

    def uploadProcessListToServer(self, processList):
        file = open("process.txt", "w+")
        for i in processList:
            file.write(i)
        file.close()
        sftp_client = self.client.open_sftp()
        sftp_client.put("process.txt", "process.txt")
        sftp_client.close()
        os.remove("process.txt")

    def dispose(self):
        self.client.close()
