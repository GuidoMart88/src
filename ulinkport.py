#!/usr/bin/python
class UlinkPort:
    ''' This is an uplink  port attached to a.  '''
    def CreateUlinkPort(self,prefix, no):
			for i in range(1, no+1):
				print '\tport { id="' + prefix + str(i) + '" } '
			
