from library_file import *

class Automation:
    __port = 22
    __username_mikrotik = 'admin'
    __password_mikrotik = '1qaz2wsx'
    def __init__(self):
        print("Start")
    def ip_(self,ip):
        return (ip)
    def time_stamp(self):
        print(time_stamp)
    
    def remote(self,ip,command):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(ip,self.__port,self.__username_mikrotik,self.__password_mikrotik)
        stdin,stdout,stderr = client.exec_command(command)
        for aaaa in stdout:
            aaaa.strip()
            print(aaaa)
        client.close()

    def showdata(self):
        #print("{}".format(self.ip_))
        print("{}".format(self.__port))
        print("{}".format(self.__username_mikrotik))
        print("{}".format(self.__password_mikrotik))

class Ssh_mikrotik(Automation):
    def __init__(self,ip,command):
        print("Start")
        super().remote(ip,command)
time1 = time.time()
for ip_ssh in ip_mikrotik:
    obj1 = Ssh_mikrotik(ip_ssh,'www.google.com')
    print(ip_ssh)
#obj1.showdata()
time2 = time.time() - time1
print(f"ใช้เวลาในการรัน {time2:0.2f} วินาที")


#obj1 = Automation()
#for a in ip_list:
#    obj1._ssh(a)
#    print('OKOK')




