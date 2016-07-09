#Packet sniffer in python
#For Linux
 
from scapy.all import *
import os

print os.listdir('sys/class/net/')
interface = os.listdir('/sys/class/net/')[1]
print interface

while True: 
    p = sniff(iface=interface, timeout=10, count=5)
    print p.summary()
    print p
