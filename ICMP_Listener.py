#ref: http://stackoverflow.com/questions/8245344/python-icmp-socket-server-not-tcp-udp
#ref: http://code.activestate.com/recipes/439224-data-over-icmp/


import socket
import struct
import binascii
##from struct import *


def listen():
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    while 1:
        data, addr = s.recvfrom(1508)
        #print s.recvfrom(1508)
        if addr == ('10.0.0.40',0):
            print "\nValues: ", data[28:]
        else: print addr

listen()




