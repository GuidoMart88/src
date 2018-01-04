#!/usr/bin/python
from hostport import *
from ofxport import *
from ulinkport import *
class Ofx:
	''' This is an openflow enabled switch   class. The CreateOfx function creates a new switch '''
	
        def CreateOfx(self,OfxID,Location,ofxIP,ofxSMask,cListenPort, controllerIP , HostPorts, ControllerPorts):
		
		ulp = UlinkPort()
		hp = HostPort()
		op = OfxPort()
                print 'ofx {'
                print '\tid="' + OfxID + '"'
                print '\tlocation="' + Location + '"'
		print '\tfabricIPv4="' + ofxIP + '"'
		print '\tfabricSubnetMaskv4="' + ofxSMask + '"'
		print '\tcontrollerPort="' + str(cListenPort) + '"'
		print '\tcontrollerPv4="' + controllerIP + '"'
		ulp.CreateUlinkPort('ulp', 1)
		hp.CreateHPort('p', HostPorts)
		op.CreateCPort('pControl',ControllerPorts)
                print '}'


