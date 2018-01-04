#!/usr/bin/python
from hostport import *

class Controller:
	''' This is a controller host class. The CreateCHost function creates a new controller host '''
	
        def CreateCHost(self,HostID,Location, HostPorts):
		hp = HostPort()
                print 'host {'
                print '\tid="' + HostID + '"'
                print '\tlocation="' + Location + '"'
		hp.CreateHPort('eth', HostPorts)
                print '}'



