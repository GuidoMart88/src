#!/usr/bin/python
from hostport import *
class Host:
	''' This is a generic host class. The CreateHost function creates a new host '''
	
        def CreateHost(self,HostID,Location, HostPorts):
		hp = HostPort()
                print 'host {'
                print '\tid="' + HostID + '"'
                print '\tlocation="' + Location + '"'
		hp.CreateHPort('port', HostPorts)
                #print '\tport { id="eth' + str(HostPorts) + '" }'
                print '}'



