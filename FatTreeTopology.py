#!/usr/bin/python
from controller import *
from ofx import *
from host import *
from link import *
from adjacency import * 
def main():
        k = int(raw_input("Enter the value of k between 2 , 4 and 6 ") or 2)
        kList = [2,4,6]
        if not k in kList:
                k =2
        NoOfPods = k
        CoreSwitches = int((k/2)**2)
        # Aggregation switches per pod
        AggSwitches = int(k/2) 
        # Edge switches per pod
        Edgeswitches = int(k/2) 
        TotalAggSwitches = int(k/2) * k
        TotalEdgeswitches = int(k/2) *k
        # Number of ports on each switch
        swports = k
        # Controller ports on each switch
        cports = 1
        #Number of hosts per switch and number of ports per host
        hosts = int(k/2)
        hports = 1	
        # Number of controller hosts , and number of ports per controller	
        chosts =1
        #chports =3
        portsOnController = CoreSwitches + TotalAggSwitches + TotalEdgeswitches     # Sum of core , aggregation adn edge switches
        PortsPerCoreSwitch =  k
        subSetOfCore = int(k/2)
        #Number of switches, switch ports and control mode ports on each switch
        EdgeSwitchIPs = []
        CoreSwitchIPs = []
        AggSwitchIPs  = []
        #Collect IP addresses for all Core switches
        for i in range(1, CoreSwitches+1):
                ofxIP = raw_input("Enter fabric IPv4 address for core switch " + str(i) + " : ") or  "10.10.10.10"
                CoreSwitchIPs.append(ofxIP)
	# Colelct IP addresses for all Aggregation Switches in all pods
        for i in range(1, TotalAggSwitches+1):
                ofxIP = raw_input("Enter fabric IPv4 address for Aggregation switch " + str(i) + " : ") or "10.10.10.10"
                AggSwitchIPs.append(ofxIP)
        # Collect IP addresses for all Edge Switches in all pods
        for i in range(1, TotalEdgeswitches+1):
                ofxIP = raw_input("Enter fabric IPv4 address for edge switch " + str(i) + " : ") or "10.10.10.10"
                EdgeSwitchIPs.append(ofxIP)
        location =raw_input("Enter the location :") 
        controllerIP = raw_input("Enter the Controller's IP Address :")  or "10.10.10.10"
        # Instantiate Controller , Switch , link and adjacency
        controller = Controller()
        switch = Ofx()	
        host = Host()	
        link = Link()
        adjacency = Adjacency()
        print "\n\n\n\ntype KArrayFatTreeTopology{"
        print  "description = \"KArray Fat Tree Network Topology with one controller, multiple  core ,aggregation and edge switches and multiple hosts\""
        # Create Core Switches
        for swNo in range(CoreSwitches):
                ROfxID ="CoreOfxSwitch" + str(swNo+1) 
                ofxSMask = "255.255.255.0"
                cListenPort = "9966"
                switch.CreateOfx(ROfxID,location,CoreSwitchIPs[swNo],ofxSMask,cListenPort, controllerIP , PortsPerCoreSwitch, cports)
        # Create Aggregation switches in each pod
        for pod in range(1, NoOfPods+1):
                for agSwno in range(AggSwitches):
                        OfxID ="AggOfxSwitch" + str(agSwno +1) + 'InPOD' + str(pod)
                        ofxSMask = "255.255.255.0"
                        cListenPort = "9966"
                        switch.CreateOfx(OfxID,location,AggSwitchIPs[agSwno],ofxSMask,cListenPort, controllerIP , swports, cports)
        #Create Edge switches in each pod	
        for pod in range(1, NoOfPods+1):
                for swNo in range(Edgeswitches):
                        OfxID ="EdgeOfxSwitch" + str(swNo +1)  + 'InPOD' + str(pod)
                        ofxSMask = "255.255.255.0"
                        cListenPort = "9966"
                        switch.CreateOfx(OfxID,location,EdgeSwitchIPs[swNo],ofxSMask,cListenPort, controllerIP , swports, cports)
        #Create Controller
        for chostNo in range(1,chosts+1):
                hname = 'controller' + str(chostNo)
                controller.CreateCHost(hname, location ,portsOnController)
        #Create hosts on each Edge switch in each pod
        for pod in range(1, NoOfPods+1):
                for swNo in range(1, Edgeswitches+1):
                        for hostNo in range(1,hosts+1):
                                hname = 'Host' + str(hostNo) + 'OnEdgeSwitch' +  str(swNo) + 'InPOD' + str(pod)
                                host.CreateHost(hname , location, hports)



        ####LINKS
        #Create Links between Core and Aggregation switches

        for pod in range(1,NoOfPods+1):
                base = 1
                ptr = 1
                for aggSw in range(1,AggSwitches+1):
                        base =  int(ptr)
                        for indx in range(1,subSetOfCore+1):
                                linkName =  'FromAggSw' + str(aggSw) + 'Pod' + str(pod) + 'ToCoreSw' + str(ptr)
                                link.CreateLink(linkName)
                                ptr = int(base) + int(indx)
	
        #Create Link between Aggregation switch and Edge switches
        for pod in range(1, NoOfPods+1):
                for aSwNo in range(1,AggSwitches+1):
                        for eSwNo in range(1,Edgeswitches+1):
                                linkName = 'FromAggSwitch' +  str(aSwNo)+  'ToEdgeSwitch' + str(eSwNo) + 'InPOD' + str(pod)
                                link.CreateLink(linkName)
                                                
        #Create links between edge switch and hosts in each pod
        for pod in range(1, NoOfPods+1):
                for swNo in range(1, Edgeswitches+1):
                        for hostNo in range(1,hosts+1):
                                linkName = 'FromEdgeSwitch' +  str(swNo)+  'ToHost' + str(hostNo) + 'OnEdgeSW' + str(swNo) + 'OfPod' + str(pod)
                                link.CreateLink(linkName)





        ### ADJACENCIES
        #Adjacencies between CORE Switches and Aggregation switches in each POD
        for pod in range(1,NoOfPods+1):
                base = 1
                ptr = 1
                for aggSw in range(1,AggSwitches+1):
                        base =  int(ptr)
                        for indx in range(1,subSetOfCore+1):
                                linkName =  'FromAggSw' + str(aggSw) + 'Pod' + str(pod) + 'ToCoreSw' + str(ptr)
                                coreSName = "CoreOfxSwitch" + str(ptr) 
                                coreSPort = 'p' + str(pod)
                                agSName ="AggOfxSwitch" + str(aggSw) + 'InPOD' + str(pod)
                                agSPort = 'p' + str(indx)
                                adjacency.CreateAdjacency(agSName,agSPort,linkName,'src')
                                adjacency.CreateAdjacency(coreSName,coreSPort,linkName,'dst')
                                ptr = int(base) + int(indx)	


        #Adjacencies between aggregation and Edge switches in each POD
        for pod in range(1, NoOfPods+1):
                for aSwNo in range(1,AggSwitches+1):
                        spidx = (k/2)
                        for eSwNo in range(1,Edgeswitches+1):
                                linkName = 'FromAggSwitch' +  str(aSwNo)+  'ToEdgeSwitch' + str(eSwNo) + 'InPOD' + str(pod)
                                agSName ="AggOfxSwitch" + str(aSwNo) + 'InPOD' + str(pod)
                                spidx = spidx +1
                                agSPort = 'p' + str(spidx)
                                egSName = "EdgeOfxSwitch" + str(eSwNo)  + 'InPOD' + str(pod)
                                egSPort = 'p' + str(aSwNo)
                                adjacency.CreateAdjacency(agSName,agSPort,linkName,'src')
                                adjacency.CreateAdjacency(egSName,egSPort,linkName,'dst')



		
        # Adjacency between each Edgeswitch and host in each pod
        for pod in range(1, NoOfPods+1):
                for eSwNo in range(1, Edgeswitches+1):
                        spidx = (k/2)
                        for hostNo in range(1,hosts+1):
                                linkName = 'FromEdgeSwitch' +  str(eSwNo)+  'ToHost' + str(hostNo) + 'OnEdgeSW' + str(eSwNo) + 'OfPod' + str(pod)
                                egSName = "EdgeOfxSwitch" + str(eSwNo)  + 'InPOD' + str(pod)
                                spidx = spidx +1
                                egSPort = 'p' + str(spidx)
                                hname = 'Host' + str(hostNo) + 'OnEdgeSwitch' +  str(eSwNo) + 'InPOD' + str(pod)
                                hport = 'port1'
                                adjacency.CreateAdjacency(egSName,egSPort,linkName,'src')
                                adjacency.CreateAdjacency(hname,hport,linkName,'dst')

	



        print "}"

main()
