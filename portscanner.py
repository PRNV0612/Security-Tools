import socket
import termcolor
import os

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()


print('''
.______     ______   .______     .___________.    _______.  ______     ___      .__   __. .__   __.  _______ .______      
|   _  \   /  __  \  |   _  \    |           |   /       | /      |   /   \     |  \ |  | |  \ |  | |   ____||   _  \     
|  |_)  | |  |  |  | |  |_)  |   `---|  |----`  |   (----`|  ,----'  /  ^  \    |   \|  | |   \|  | |  |__   |  |_)  |    
|   ___/  |  |  |  | |      /        |  |        \   \    |  |      /  /_\  \   |  . `  | |  . `  | |   __|  |      /     
|  |      |  `--'  | |  |\  \----.   |  |    .----)   |   |  `----./  _____  \  |  |\   | |  |\   | |  |____ |  |\  \----.
| _|       \______/  | _| `._____|   |__|    |_______/     \______/__/     \__\ |__| \__| |__| \__| |_______|| _| `._____|
                                                       BY PRNV0612                                                                                                                 
 ''')
def scan(host,ports):
    print("-"*50)
    print(f"Target IP: {host}")
    print("-"*50)
    for port in range(1,ports):
        scan_port(host,port)


def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.connect((ipaddress,port))
        print(termcolor.colored(("[+] Port opened on ",str(port)),"red"))
    except: 
        pass


targets=input("[*] Enter Targets To Scan(separate using ,):")
ports=int(input("[*] Enter Number of Ports to be Scanned:"))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"),"green"))
    for ip in targets.split(','):
        scan(ip.strip(' '),ports)
else:
    scan(targets,ports)