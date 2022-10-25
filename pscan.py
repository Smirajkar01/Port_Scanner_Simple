import sys
import socket
import requests
from datetime import datetime

target = input(str('Enter the Target IP Address: ')) 

print("_" * 50)
print("Beginning to scan Target: ",target)
print("Scan started at: ", str(datetime.now()))
print("_" * 50)

#begin script 
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #uses ipv4 and it is a TCP socket. \
        socket.setdefaulttimeout(0.5)

        #return the open port to the user

        result = s.connect_ex((target,port))
        if result == 0: 
            print("[*] Port ",port," is open!")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting the port scanner, Goodbye.")
    sys.exit()

except socket.error: 
    print("\ Host not responding :(")
    sys.exit()


