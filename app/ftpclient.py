from ftplib import FTP_TLS

class FtpClient(FTP_TLS):
    def connectToServer(self, server, username, password, port):
        self.connect(server, int(port))

        if(username != None and password != None):
            self.login(username, password)
        else:
            self.login()
            self.prot_p()

    def list(self):
        data = []
        self.dir(data.append)
        item = []

        for line in data:
            x = line.split("   ") #permissions
            item.append(x[0])
            data.append(item)

        return data
