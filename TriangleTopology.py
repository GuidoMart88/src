#!/usr/bin/python
from controller import *
from ofx import *
from host import *
from link import *
from adjacency import * 

def main():

	#Number of hosts per switch and number of ports per host
	hosts = 3
	hports = 2
	
	# Number of controller hosts , and number of ports per controller	
	chosts =1
	chports =3

	locations = []
	for lno in range(1,4):
		myloc = raw_input("Enter the location for host" + str(lno) + " :")
		locations.append(myloc)	

	controller = Controller()
 	host = Host()	
	link = Link()
	adjacency = Adjacency()

	print "\n\n\n\ntype Triagle{"
	print  "description = \"Tree topology with three hosts\""
	for hostNo in range(1,hosts+1):
		hname = 'Host' + str(hostNo)
		ind = int(hostNo) - 1 
		location = locations[ind]
		host.CreateHost(hname , location, hports)
	#Create links per host
	for hostNo in range(1,hosts+1):
		linkName = 'Link' +  str(hostNo)
		link.CreateLink(linkName)

	# Adjacency between each switch and host
	for hostNo in range(1,hosts+1):
		hname = 'Host' + str(hostNo)
		linkName = 'Link' +  str(hostNo)
		if (hostNo == hosts):
			nextHost = 1
		else:
			nextHost = int(hostNo) + 1
		nextHname = 'Host' + str(nextHost)
		adjacency.CreateAdjacency(hname,'port2',linkName,'src')
		adjacency.CreateAdjacency(nextHname,'port1',linkName,'dst')




	print "}"

main()
