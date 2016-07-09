#!/usr/bin/python

"""Terminal 1
$ sudo su -
# cd OpenNet
# ./waf_shell.sh
# cd ../../mininet/examples/opennet
# python ap-sta-h-sw-nat3.py
"""
"""Terminal 2
$ cd pyretic
$ sudo fuser -k 6633/tcp
$ python pyretic.py -m p0 pyretic.modules.mac_learner
"""

"""
                           nat--Internet
                            |
                           s0
                            |
       ----------------------------------------------------------------
       |              |          |    |    |    |   |   |   |    |
      nat1           nat2        h0   h1   h2   h3  h4  h5  h6   h7
       |               |
      ap0             ap1
  |    |   |      |    |    |
sta0 sta1 sta2   sta3 sta4  sta5
"""


from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI
#NAT
from mininet.nodelib import NAT
from mininet.topo import Topo

import mininet.ns3
from mininet.ns3 import WifiSegment

import ns.core
import ns.network
import ns.wifi
import ns.csma
import ns.wimax
import ns.uan
import ns.netanim

from mininet.opennet import *

def main():
    net = Mininet()
    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
    natIP="10.0.0.220"
    cpu = 0.1

    wifi = WifiSegment(standard=ns.wifi.WIFI_PHY_STANDARD_80211g)
    #Added for NAT
    hostConfig = {'cpu': cpu, 'defaultRoute': 'via ' + natIP }

    print("Building Switch")
    # About OVSSwitch
    s0 = net.addSwitch('s0', ip=None, protocols=["OpenFlow13"])

    print ("Building APs")
    # About AP
    
    ap0 = net.addAP('ap0', ip=None)
    mininet.ns3.setMobilityModel(ap0, None)
    mininet.ns3.setPosition(ap0, 10, 0, 20)

    ap1 = net.addAP('ap1', ip=None)
    mininet.ns3.setMobilityModel(ap1, None)
    mininet.ns3.setPosition(ap1, 10, 10, 0)

    # Check mininet.node.AP
    if isinstance(ap0, mininet.node.AP):
        print("I'm AP 2")
    if isinstance(ap1, mininet.node.AP):
        print("I'm AP 1")   

    print("Building Hosts")
    # About Host
    #h0 = net.addHost('h0', ip="10.1.1.1")
    h8 = net.addHost('h8', mac='00:00:00:00:00:08', ip="10.0.0.8", **hostConfig)
    h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip="10.0.0.1", **hostConfig)
    h2 = net.addHost('h2', mac='00:00:00:00:00:02', ip="10.0.0.2", **hostConfig)
    h3 = net.addHost('h3', mac='00:00:00:00:00:03', ip="10.0.0.3", **hostConfig)
    h4 = net.addHost('h4', mac='00:00:00:00:00:04', ip="10.0.0.4", **hostConfig)
    h5 = net.addHost('h5', mac='00:00:00:00:00:05', ip="10.0.0.5", **hostConfig)
    h6 = net.addHost('h6', mac='00:00:00:00:00:06', ip="10.0.0.6", **hostConfig)
    h7 = net.addHost('h7', mac='00:00:00:00:00:07', ip="10.0.0.7", **hostConfig)


    
    
    print "Building Stations"
    # About Station
##    sta0 = net.addStation('sta0', ip="10.1.1.5", **hostConfig)
    sta0 = net.addStation('sta0', ip='192.168.1.100/24',
                    defaultRoute='via 192.168.1.1')
    mininet.ns3.setMobilityModel(sta0, None)
    mininet.ns3.setPosition(sta0, 10, 0, 20)

##    sta1 = net.addStation('sta1', ip="10.1.1.6", **hostConfig)
    sta1 = net.addStation('sta1', ip='192.168.1.101/24',
                    defaultRoute='via 192.168.1.1')
    mininet.ns3.setMobilityModel(sta1, None)
    mininet.ns3.setPosition(sta1, 10, 0, 15)

##    sta2 = net.addStation('sta2', ip="10.1.1.7", **hostConfig)
    sta2 = net.addStation('sta2', ip='192.168.1.102/24',
                    defaultRoute='via 192.168.1.1')    
    mininet.ns3.setMobilityModel(sta2, None)
    mininet.ns3.setPosition(sta2, 10, 0, 25)
    
##    sta3 = net.addStation('sta3', ip="10.1.1.8", **hostConfig)
    sta3 = net.addStation('sta3', ip='192.168.2.100/24',
                    defaultRoute='via 192.168.2.1')
    mininet.ns3.setMobilityModel(sta3, None)
    mininet.ns3.setPosition(sta3, 10, 10, 0)
    
    sta4 = net.addStation('sta4', ip='192.168.2.101/24',
                    defaultRoute='via 192.168.2.1')
    mininet.ns3.setMobilityModel(sta4, None)
    mininet.ns3.setPosition(sta4, 10, 10, 5)
    
    sta5 = net.addStation('sta5', ip='192.168.2.102/24',
                    defaultRoute='via 192.168.2.1')
    mininet.ns3.setMobilityModel(sta5, None)
    mininet.ns3.setPosition(sta5, 10, 10, 10)
    #Check mininet.node.Station
    if isinstance(sta0, mininet.node.Station):
        print("I'm station 0")       
    if isinstance(sta1, mininet.node.Station):
        print("I'm station 1")        
    if isinstance(sta2, mininet.node.Station):
        print("I'm station 2")        
    if isinstance(sta3, mininet.node.Station):
        print("I'm station 3")
    if isinstance(sta4, mininet.node.Station):
        print("I'm station 4")
    if isinstance(sta5, mininet.node.Station):
        print("I'm station 5")   
        
    print("****Preparing to list devices***")
    print("APs list: {0}\nSTAs list: {1}\n".format(wifi.aps, wifi.stas))

    wifi.addAp(ap0, channelNumber=6, ssid="opennet_0")
    wifi.addSta(sta0, channelNumber=6, ssid="opennet_0")
    wifi.addSta(sta1, channelNumber=6, ssid="opennet_0")
    wifi.addSta(sta2, channelNumber=6, ssid="opennet_0")
    wifi.addAp(ap1, channelNumber=11, ssid="opennet_1")
    wifi.addSta(sta3, channelNumber=11,  ssid="opennet_1")
    wifi.addSta(sta4, channelNumber=11,  ssid="opennet_1")
    wifi.addSta(sta5, channelNumber=11,  ssid="opennet_1")    

    #Building NATs
    print("Building NAT")
    nat = net.addHost('nat', cls=NAT, mac='00:00:00:00:00:20', ip=natIP, inNamespace=False)
    nat1 = net.addHost('nat1', cls=NAT, mac='00:00:00:00:00:09', ip='10.0.0.9', subnet='192.168.1.0/24',
                       inetIntf='nat1-eth0', localIntf='nat1-eth1', **hostConfig)
    nat2 = net.addHost('nat2', cls=NAT, mac='00:00:00:00:00:10', ip='10.0.0.10', subnet='192.168.2.0/24',
                       inetIntf='nat2-eth0', localIntf='nat2-eth1', **hostConfig)

    print("Building Links")
    # Ignore warning message: "defaultIntf: warning: h0 has no interfaces"
    #add NAT link s0->nat, nat1->s0, nat2->s0, h0->s0, and h1->s0
    net.addLink(s0, nat)
    net.addLink(s0, nat1, intfName1='nat1-eth0')
    net.addLink(s0, nat2, intfName1='nat2-eth0')
    net.addLink(s0, h8)
    net.addLink(s0, h1)
    net.addLink(s0, h2)
    net.addLink(s0, h3)
    net.addLink(s0, h4)
    net.addLink(s0, h5)
    net.addLink(s0, h6)
    net.addLink(s0, h7)
    # ap0->na1 and ap1->nat2
    net.addLink(nat1, ap0, intfName1='nat1-eth1', params1={'ip' : '192.168.1.1/24'})
    net.addLink(nat2, ap1, intfName1='nat2-eth1', params1={'ip' : '192.168.2.1/24'})

##    print("Switches list: {0}\nHosts list: {1}\n".format(net.switches, net.hosts))

    info('***Starting Network***\n')
    mininet.ns3.start()
    net.start()
    
    info( 'Testing network connectivity\n' )
##    print ( '\n\nTesting h0 -> h1 \n\n' )
##    h0.cmdPrint( 'ping 10.1.1.2 -c2' )
##    print ( '\n\nTesting h0 -> sta0 \n\n')
##    h0.cmdPrint( 'ping 10.1.1.5 -c2' )    
##    print ( '\n\nTesting h0 -> sta1 \n\n')
##    h0.cmdPrint( 'ping 10.1.1.6 -c2' )
##    print ( '\n\nTesting h0 -> sta2 \n\n')
##    h0.cmdPrint( 'ping 10.1.1.7 -c2' )    
##    print ( '\n\nTesting h0 -> sta3 \n\n')
##    h0.cmdPrint( 'ping 10.1.1.8 -c2' )
##    print ( '\n\nTesting sta0 -> sta3 \n\n')    
##    sta0.cmdPrint('ping -c2 ' + sta3.IP())
##    sta0.cmdPrint('ping -c2 ' + sta2.IP())   
##    sta0.cmdPrint('ping -c2 ' + sta3.IP())

    CLI(net)

    mininet.ns3.stop()
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()
