#!/usr/bin/python
#This tooplogy uses a single switch with given number of hosts. each host has one port each.
# Currently it uses one controller host with one controller port connected to switch

from controller import *
from ofx import *
from host import *

from link import *
from adjacency import * 

def main():
	print "FlatTopologyWithSingleSwitch    {"
	print '\tdescription="This topology uses a single switch with two hosts connected to it"'
	print '\tid="TwoHostsSingleSwitch"'
	#Number of switches, switch ports and control mode ports on each switch
	switches=1
	swports =2
	cports = 1
	
	#Number of hosts per switch and number of ports per host
	#hosts = input("Please enter required number of hosts ; ")
	#if (hosts <=1):
	#	hosts =2  
	hosts = 2
	hports = 1
	
	# Number of controller hosts , and number of ports per controller	
	chosts =1
	chports =1


	location ="USA"

	#controllerIP = raw_input("Please enter the controller IP (default:10.10.10.100): ") or "10.10.10.100"
	controllerIP = "10.10.10.100"
		
        controller = Controller()
	switch = Ofx()	
 	host = Host()	
	
	link = Link()
	adjacency = Adjacency()


	
	for swNo in range(1, switches+1):
		OfxID ="ofxSwitch" + str(swNo)
		ofxIP = "10.10.10.50"
		#ofxIP = raw_input("Enter fabric IPv4 address for " + str(OfxID) + " (default: 10.10.10.50) :  ") or  "10.10.10.50"
		ofxIP =  "10.10.10.50"
		ofxSMask = "255.255.255.0"
		cListenPort = "9966"
 		switch.CreateOfx(OfxID,location,ofxIP,ofxSMask,cListenPort, controllerIP , swports, cports)

	for chostNo in range(1,chosts+1):
		hname = 'controller' + str(chostNo)
		controller.CreateCHost(hname, location ,chports)

	for hostNo in range(1,hosts+1):
		hname = 'host' + str(hostNo)
		host.CreateHost(hname , location, hports)


	link.CreateLink('ofx2controller')
	link.CreateLink('ofx2host1')
	link.CreateLink('ofx2host2')

	
        #for s in range(1, 6+1):

 	adjacency.CreateAdjacency('controller1','eth1', 'ofx2controller', 'src')
	adjacency.CreateAdjacency('ofxswitch1','pControl1', 'ofx2controller', 'dst')
	
 	adjacency.CreateAdjacency('host1','eth1', 'ofx2host1', 'src')
        adjacency.CreateAdjacency('ofxswitch1','p1', 'ofx2host1', 'dst')

	adjacency.CreateAdjacency('host2','eth1', 'ofx2host2', 'src')
        adjacency.CreateAdjacency('ofxswitch1','p2', 'ofx2host2', 'dst')
	print "}"
if __name__ == "__main__":
	main()
