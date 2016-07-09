import socket
import icmplib


##s = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket.IPPROTO_ICMP)
##host = socket.gethostbyname(socket.gethostname())
##s.bind((host,0))
##s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
##s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
##
##
##def listen():
##  s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
##  s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
##  while 1:
##    data, addr = s.recvfrom(1508)
##    print "Packet from %r: %r" % (addr,data)
##
##
##
### References:
##"""http://stackoverflow.com/questions/8245344/python-icmp-socket-server-not-tcp-udp
##"""


# Open a raw socket listening on all ip addresses
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sock.bind((host, 1))

try :
   while True :
      # receive data
      data = sock.recv(1024)

      # ip header is the first 20 bytes
      ip_header = data[:20]

      # ip source address is 4 bytes and is second last field (dest addr is last)
      ips = ip_header[-8:-4]

      # convert to dotted decimal format
      source = '%i.%i.%i.%i' % (ord(ips[0]), ord(ips[1]), ord(ips[2]), ord(ips[3]))

      print 'Ping from %s' % source
except KeyboardInterrupt :
   print 'Interupted by key'

#References:
"""http://forums.whirlpool.net.au/archive/1473574"""

           
           
