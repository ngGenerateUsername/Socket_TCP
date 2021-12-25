import socket 
#shell to clien

    
if __name__ == '__main__':
    ip = "0.0.0.0"
    port = 8086

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    s.bind((ip,port))
    s.listen(2)
    print("Waiting for Connection......")
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


