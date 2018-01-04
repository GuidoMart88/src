#!/usr/bin/python

from controller import *
from ofx import *
from host import *

from link import *
from adjacency import * 

def main():

        #Number of switches, switch ports and control mode ports on each switch
        switches=1
        swports =2
        cports = 1

        #Number of hosts per switch and number of ports per host
        hosts = 2
        hports = 1

        # Number of controller hosts , and number of ports per controller	
        chosts =1
        chports =3


        location =raw_input("Enter the location :") 
        controllerIP = raw_input("Enter the IP Address :")  or "10.10.10.10"
        ofxIP = raw_input("Enter fabric IPv4 address for switch  : ")

        controller = Controller()
        switch = Ofx()	
        host = Host()	

        link = Link()
        adjacency = Adjacency()

        print "\n\n\n\ntype FlatTopology{"
        print  "description = \"Flat Network Topology with one controller, one switch and two hosts\""

	
        for swNo in range(1, switches+1):
                OfxID ="ofxSwitch" + str(swNo)
                #ofxIP = raw_input("Enter fabric IPv4 address for " + str(OfxID) + ":  ") 
                ofxSMask = "255.255.255.0"
                cListenPort = "9966"
                switch.CreateOfx(OfxID,location,ofxIP,ofxSMask,cListenPort, controllerIP , swports, cports)

        for chostNo in range(1,chosts+1):
                hname = 'controller' + str(chostNo)
                controller.CreateCHost(hname, location ,chports)

        for hostNo in range(1,hosts+1):
                hname = 'host' + str(hostNo)
                host.CreateHost(hname , location, hports)

        link.CreateLink('link1')
	
        for s in range(1, hosts, 2):
                hname1 = 'host' + str(s)
                hname2 = 'host' + str(s+1)
                adjacency.CreateAdjacency(hname1,'port1', 'link1', 'src')
                adjacency.CreateAdjacency(hname2,'port1', 'link1', 'dst')
        print "}"

main()
