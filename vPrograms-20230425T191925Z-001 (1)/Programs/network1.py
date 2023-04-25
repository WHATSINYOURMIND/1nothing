#Know the IP Address of any server
from socket import *
h='www.google.co.in'
try:
    a=gethostbyname(h)
    print("IP Address=",a)
except gaierror:#get address information
    print("Exception Occurs...")
    
