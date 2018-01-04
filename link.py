#!/usr/bin/python
from linkport import *
class Link:
	def CreateLink(self, LinkID):
		lp = LinkPorts()
		print "link {"
		print '\tid="' + str(LinkID)  + '"'
		lp.CreateLPorts()
		print '}'


