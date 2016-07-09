#https://github.com/mininet/mininet/blob/master/examples/natnet.py
"""
               h0/nat
                 |
                 s0
                 |
       ---------------------
       |                  |
      nat1               nat2
       |                  |
     s1/ap0             s2/ap1
  |    |   |         |    |    |
sta0 sta1 sta2     sta3 sta4  sta5
"""


# set up inet switch
#inetSwitch = self.addSwitch('s0')
s0 = self.addSwitch('s0')
# add inet host
##inetHost = self.addHost('h0')
##self.addLink(inetSwitch, inetHost)
h0 = self.addHost('h0')
self.addLink(s0, h0)

# add local nets
# Add NATs and attach them to s0

nat1 = net.addHost('nat1', cls=NAT, subnet='192.168.1.0/24',
                       inetIntf='nat1-eth0', localIntf='nat1-eth1')
nat2 = net.addHost('nat2', cls=NAT, subnet='192.168.2.0/24',
                       inetIntf='nat2-eth0', localIntf='nat2-eth1')

# connect NAT to inet and local switches
net.addLink(nat1, s0, intfName1='nat1-eth0')
net.addLink(nat, ap0, intfName1='nat1-eth1', params1='ip' : '192.168.1.1/24')
net.addLink(nat2, s0, intfName1='nat2-eth0')
net.addLink(nat, ap1, intfName1='nat2-eth1', params1='ip' : '192.168.2.1/24')

# add host and connect to local switch
sta0 = net.addStation('sta0', ip='192.168.1.100/24',
                    defaultRoute='via 192.168.1.1')
sta1 = net.addStation('sta1', ip='192.168.2.100/24',
                    defaultRoute='via 192.168.2.1')





