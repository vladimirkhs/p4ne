#
# Lab 2-2
#
from flask import Flask
from ipaddress import IPv4Interface
import re
import glob
import socket

TXT = glob.glob("C:\\Users\\resu\\Desktop\\seafile\\Seafile\\p4ne_training\\config_files\\*.txt")
othr = "ip address 192.178.1.1 255.255.255.0"
IPADDRESS = []
IFACE = []
HOSTNAME = []

def stline(othr):
    oth = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", othr)
    if oth:
        return {"ip":IPv4Interface(str(oth.group(1)) + "/" + str(oth.group(2)))}
    oth = re.match("^interface (.+)", othr)
    if oth:
        return {"int":oth.group(1)}
    oth = re.match("^hostname (.+)", othr)
    if oth:
        return {"host":oth.group(1)}
    return {"Other line",}

for x in TXT:
    f = open(x)
    d = f.readlines()
    for s in d:
        line = stline(s)
        if "ip" in line:
            IPADDRESS.append(line)
        if "int" in line:
            IFACE.append(line)
        if "host" in line:
            HOSTNAME.append(line)

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Это краткая справка об использовании: <BR>" \
           "<BR><A href='http://127.0.0.1/config'>Cведения об именах всех хостов, для которых есть кофигурационные файлы</A>" \
           "<BR><A href='http://127.0.0.1/config/hostname'>Cведения об IP адресах этого хоста</A>" \

@app.route('/config')
def page1():
    return str(HOSTNAME)

@app.route('/config/hostname')
def page2():
    return str(socket.gethostbyname_ex(socket.gethostname())[2])

if __name__ == '__main__':
    app.run(port=80, debug=True)



