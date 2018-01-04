#!/usr/bin/python
class OfxPort:
    ''' This is a port attached to an Openflow switch ofx . The mode of this port set to CONTROLL  '''
    def CreateCPort(self,prefix, no):
			for i in range(1, no+1):
				print '\tport { \n\t\tid="' + prefix + str(i) + '"\n\t\tmode="CONTROL"\n\t } '
			
