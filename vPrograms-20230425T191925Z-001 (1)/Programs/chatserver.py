#Server Side Application
import socket
host='127.0.0.1'#Loopback IP
port=9000 #1024-65535
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()#Client ke sath connection establish karega
print("Client Connected...")
while True:
    s1=c.recv(1024)
    if not s1:
        break
    print("From Client:",str(s1.decode()))
    s2=input("Enter Message=")
    c.send(s2.encode())
c.close()
