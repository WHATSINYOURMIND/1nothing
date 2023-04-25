#Client Side Application
import socket
host='127.0.0.1'#Loopback IP
port=9000 #1024-65535
s=socket.socket()
s.connect((host,port))
s1=input("Enter Message=")
while s1!='EXIT':
    s.send(s1.encode())#String to byte
    s2=s.recv(1024)
    print("From Server:",s2.decode())#Byte to string
    s1=input("Enter Message=")
s.close()


    
    



