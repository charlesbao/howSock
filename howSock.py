# encoding=utf8
import requesocks as requests
import re
import time

class socks:
    dict = {}
    i = 0
    showProxiesValue = False
    session = None
    header = ''
    changeSockValue = True

    def get(self,url,timeout = 5):
        try:
            self.session.proxies = {'http': 'socks5://'+self.dict['ip'][self.i]+':'+self.dict['port'][self.i],'https': 'socks5://'+self.dict['ip'][self.i]+':'+self.dict['port'][self.i]}
            if self.showProxiesValue:
                print self.session.proxies
            contents = self.session.get(url,timeout=timeout).content
        except:
            self.changeIp()
            return self.get(url,timeout)
        else:
            return contents

    def post(self,url,data,timeout = 5):
        try:
            self.session.proxies = {'http': 'socks5://'+self.dict['ip'][self.i]+':'+self.dict['port'][self.i],'https': 'socks5://'+self.dict['ip'][self.i]+':'+self.dict['port'][self.i]}
            if self.showProxiesValue:
                print self.session.proxies
            contents = self.session.post(url,data,timeout=timeout).content
        except:
            self.changeIp()
            return self.post(url,data,timeout)
        else:
            return contents

    def getSock(self):
        try:
            contents = requests.get('http://www.cz88.net/proxy/socks5.shtml',timeout = 5).content
        except:
            time.sleep(60)
            return self.getSock()
        ip = re.findall('''class="ip">(.+?)</div>''',contents,re.S)[1:]
        port = re.findall('''class="port">(.+?)</div>''',contents,re.S)[1:]
        try:
            contents = requests.get('http://www.cz88.net/proxy/socks5_2.shtml',timeout = 5).content
        except:
            time.sleep(60)
            return self.getSock()
        ip2 = re.findall('''class="ip">(.+?)</div>''',contents,re.S)[1:]
        port2 = re.findall('''class="port">(.+?)</div>''',contents,re.S)[1:]
        ip += ip2
        port += port2
        self.dict['ip'] = ip
        self.dict['port'] = port
        if len(self.dict['ip']) == 0:
            time.sleep(60)
            return self.getSock()
        else:
            return True

    def setProxies(self,ip,port):
        if type(ip) == list:
            self.dict['ip'] = ip
            self.dict['port'] = port
            self.i = 0
        elif type(ip) == str:
            self.dict['ip'] = [ip]
            self.dict['port'] = [port]
            self.i = 0

    def showProxies(self,bool = True):
        self.showProxiesValue = bool

    def changeIp(self):
        self.i += 1
        if(self.i > len(self.dict['ip'])):
            if self.changeSockValue == True:
                self.getSock()
            self.i = 0

    def changeSock(self,bool = False):
        self.changeSockValue = bool

    def setIpIndex(self,val = 0):
        self.i = val

    def printIpIndex(self):
        print self.i

    def printSock5(self):
        print self.dict

    def updateHeader(self,header):
        self.session.headers.update(header)

    def __init__(self,header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}):
        self.session = requests.session()
        self.updateHeader(header)
        self.getSock()