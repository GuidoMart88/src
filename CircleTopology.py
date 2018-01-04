#!/usr/bin/python

from controller import *
from ofx import *
from host import *

from link import *
from adjacency import * 

def main():

        #Number of switches, switch ports and control mode ports on each switch
        EdgeSwitchIPs = []
        switches = input("Enter the number of  switches you want : ") or 2

        for i in range(1, switches+1):
                ofxIP = raw_input("Enter fabric IPv4 address for switch " + str(i) + " : ")
                EdgeSwitchIPs.append(ofxIP)
        switches= len(EdgeSwitchIPs)

        swports =4
        cports = 1

        #Number of hosts per switch and number of ports per host
        hosts = 2
        hports = 1

        # Number of controller hosts , and number of ports per controller	
        chosts =1
        chports =3


        location =raw_input("Enter the location :") 
        controllerIP = raw_input("Enter the Controller's IP Address :")  or "10.10.10.10"


        controller = Controller()
        switch = Ofx()	
        host = Host()	

        link = Link()
        adjacency = Adjacency()

        print "\n\n\n\ntype CircleTopology{"
        print  "description = \"Circular Network  Topology with one controller,  multple edge switches and multiple hosts\""

        #Create  switches	
        for swNo in range(switches):
                OfxID ="ofxSwitch" + str(swNo +1)
                ofxSMask = "255.255.255.0"
                cListenPort = "9966"
                switch.CreateOfx(OfxID,location,EdgeSwitchIPs[swNo],ofxSMask,cListenPort, controllerIP , swports, cports)
        #Create Controller 
        for chostNo in range(1,chosts+1):
                hname = 'controller' + str(chostNo)
                portsOnController = switches +1    # one root switch + edge switches
                controller.CreateCHost(hname, location ,portsOnController)
        #Create hosts on each switch	
        for swNo in range(1, switches+1):
                for hostNo in range(1,hosts+1):
                        hname = 'Host' + str(hostNo) + 'OnSw' +  str(swNo)
                        host.CreateHost(hname , location, hports)
        #Create links per switch and host
        for swNo in range(1, switches+1):
                for hostNo in range(1,hosts+1):
                        linkName = 'Link' + 'Sw' +  str(swNo)+  'ToHost' + str(hostNo)
                        link.CreateLink(linkName)
        #Create links between switches
        for swNo in range(1, switches+1):
                linkName = 'Link' +   str(swNo)
                link.CreateLink(linkName)


        # Adjacency between each switch and host
        for swNo in range(1, switches+1):
                OfxID ="ofxSwitch" + str(swNo)
                for hostNo in range(1,hosts+1):
                        hname = 'Host' + str(hostNo) + 'OnSw' +  str(swNo)
                        linkName = 'Link' + 'Sw' +  str(swNo)+  'ToHost' + str(hostNo)
                        adjacency.CreateAdjacency(hname,'port1',linkName,'src')
                        intf = "p" + str(hostNo) 
                        adjacency.CreateAdjacency (OfxID,intf,linkName,'dst')  

        # Adjacency between switches
        for swNo in range(1, switches+1):
                OfxID ="ofxSwitch" + str(swNo)
                linkName = 'Link' +  str(swNo)
                if (swNo == switches):
                        nextSwitch = 1
                else:
                        nextSwitch = int(swNo) + 1
                nextSName = "ofxSwitch" +  str(nextSwitch)
                adjacency.CreateAdjacency(OfxID,'p4',linkName,'src')
                adjacency.CreateAdjacency(nextSName,'p3',linkName,'dst')


		



        print "}"

main()
