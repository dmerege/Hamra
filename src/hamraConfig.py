# HAMRA - Configuration File
# Developed By Daniel Merege - 2015
#--------------------- BEGIN - HAMRA Configuration Area ------------------------

# Network Devices (IP Addresses)
switch1 = '127.0.0.1'
switch2 = '127.0.0.2'
switch3 = '127.0.0.3'
switch4 = '127.0.0.4'
host1 = '10.0.0.1'
host2 = '10.0.0.2' 
host3 = '10.0.0.3' 
host4 = '10.0.0.4' 
    
# Clusters
# cluster1 = '10.0.0.0/24' #List with cluster's network devices
# cluster2 = '20.0.0.0/24' #List with cluster's network devices
# cluster3 = '30.0.0.0/24' #List with cluster's network devices
# cluster4 = '40.0.0.0/24' #List with cluster's network devices
    
# DataFlow
flow1 = host1 + "," + host2 #Devices separeted by comma in flow definition
flow2 = host2 + "," + host1 #Devices separeted by comma in flow definition
flow3 = host2 + "," + host3 #Devices separeted by comma in flow definition
flow4 = host3 + "," + host2
flow5 = host3 + "," + host4 #Devices separeted by comma in flow definition
flow6 = host4 + "," + host3

# Emergency State Flows
idle = [flow1,flow2]
preparedness = [flow1, flow2, flow3, flow4]
warning = [flow1, flow2, flow3, flow4, flow5, flow6]
crisis = [] 

# Emergency States
emergencyStatesNames = {'i':'Idle', 'p':'Preparedness','w':'Warning','c':'Crisis'}
emergencyStates = {'i':idle, 'p':preparedness, 'w':warning, 'c':crisis}

#--------------------- END - HAMRA Configuration Area --------------------------
    