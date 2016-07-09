#!/usr/bin/python

"""Terminal 1
$ sudo su -
# cd OpenNet
# ./waf_shell.sh
# cd ../../mininet/examples/opennet
# python ap2-sta-switch-host.py
"""
"""Terminal 2
$ cd pyretic
$ sudo fuser -k 6633/tcp
$ python pyretic.py -m p0 pyretic.modules.mac_learner
"""

from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI

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

    wifi = WifiSegment()

    print "Building APs"
    # About AP
    ap0 = net.addAP('ap0', ip="10.1.1.3")
    mininet.ns3.setMobilityModel(ap0, None)
    mininet.ns3.setPosition(ap0, 0, 0, 0)
    wifi.addAp(ap0, channelNumber=11, ssid="opennet_ap")

    ap1 = net.addAP('ap1', ip="10.1.1.4")
    mininet.ns3.setMobilityModel(ap1, None)
    mininet.ns3.setPosition(ap1, 10, 10, 10)
    wifi.addAp(ap1, channelNumber=1, ssid="opennet_ap2")

    # Check mininet.node.AP
    if isinstance(ap0, mininet.node.AP):
        print("I'm an AP")
    if isinstance(ap1, mininet.node.AP):
        print("I'm an AP also")    

    print "Building Stations"
    # About Station
    sta0 = net.addStation('sta0', ip="10.1.2.1")
    mininet.ns3.setMobilityModel(sta0, None)
    mininet.ns3.setPosition(sta0, 0, 0, 0)
    wifi.addSta(sta0, channelNumber=11, ssid="opennet_ap")

    sta1 = net.addStation('sta1', ip="10.1.2.2")
    mininet.ns3.setMobilityModel(sta1, None)
    mininet.ns3.setPosition(sta1, 0, 0, 5)
    wifi.addSta(sta1, channelNumber=11, ssid="opennet_ap")

    sta2 = net.addStation('sta2', ip="10.1.2.3")
    mininet.ns3.setMobilityModel(sta2, None)
    mininet.ns3.setPosition(sta2, 0, 5, 0)
    wifi.addSta(sta2, channelNumber=11, ssid="opennet_ap")

    sta3 = net.addStation('sta3', ip="10.1.3.1")
    mininet.ns3.setMobilityModel(sta3, None)
    mininet.ns3.setPosition(sta3, 10, 10, 10)
    wifi.addSta(sta3, channelNumber=1, ssid="opennet_ap2")

    #Check mininet.node.Station
    if isinstance(sta0, mininet.node.Station):
        print("I'm a station")

    if isinstance(sta1, mininet.node.Station):
        print("I'm a station also")

    print("****Preparing to list devices***")

    print("APs list: {0}\nSTAs list: {1}\n".format(wifi.aps, wifi.stas))

    print("Building Switch")
    # About OVSSwitch
    s0 = net.addSwitch('s0')

    print("Building Hosts")
    # About Host
    h0 = net.addHost('h0', ip="10.1.1.1")
    h1 = net.addHost('h1', ip="10.1.1.2")

    print("Building Links")
    # Ignore warning message: "defaultIntf: warning: h0 has no interfaces"
    net.addLink(s0, h0)
    net.addLink(s0, h1)
    net.addLink(s0, ap0)
    net.addLink(s0, ap1)

    print("Switches list: {0}\nHosts list: {1}\n".format(net.switches, net.hosts))

    info('***Starting Network***\n')
    mininet.ns3.start()
    net.start()
    
    info( 'Testing network connectivity\n' )
    h0.cmdPrint( 'ping 10.1.1.2 -c3' )
    sta0.cmdPrint('ping -c2 ' + sta3.IP())
    sta1.cmdPrint('ping -c2 ' + sta3.IP())

    CLI(net)

    mininet.ns3.stop()
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()
