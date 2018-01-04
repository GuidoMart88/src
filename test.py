#!/usr/bin/python
'''
k = 6
c = (k/2)**2  = 9 
loop = k/2 = 3
aggSwitches = c / loop = 3
'''
k = 4
c = (k/2)**2
pods = k
#for pod in range(1,pods+1):
#	for aggsw in range(1,aggSwitches+1):
#		print "Pod is :" + str(pod) + " and agg switch is " + str(aggsw)
subSetOfCore = int(k/2)
aggSwitches = int(k/2)
for pod in range(1,pods+1):
	print "-------POD-----" + str(pod)
	base = 1
	ind = 1
	for aggSw in range(1,aggSwitches+1):
		base =  int(ind)
		for i in range(1,subSetOfCore+1):
			print 'FromAggSw' + str(aggSw) + 'Pod' + str(pod) + 'ToCoreSw' + str(ind)
                	ind = int(base) + int(i)

