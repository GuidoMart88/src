#!/usr/bin/python
class HostPort:
    ''' This is a port attached to a host.  '''
    def CreateHPort(self,prefix, no):
			for i in range(1, no+1):
				print '\tport { id="' + prefix + str(i) + '" } '
			
