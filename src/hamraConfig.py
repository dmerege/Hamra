# HAMRA - Configuration File
# Developed By Daniel Merege - 2015
#--------------------- BEGIN - HAMRA Configuration Area ------------------------

# Network Devices (IP Addresses)
host1 = '10.0.0.1'
host2 = '10.0.0.2' 
host3 = '10.0.0.3' 
host4 = '10.0.0.4' 
    
# Clusters (Switches MAC Addresses)
cluster1 = '00:00:00:00:00:01' 
cluster2 = '00:00:00:00:00:02' 
cluster3 = '00:00:00:00:00:03' 
cluster4 = '00:00:00:00:00:04' 
    
# DataFlow
flow1 = cluster1 + "," + cluster2 #Devices separeted by comma in flow definition
flow2 = cluster2 + "," + cluster1 #Devices separeted by comma in flow definition
flow3 = cluster2 + "," + cluster3 #Devices separeted by comma in flow definition
flow4 = cluster3 + "," + cluster2 #Devices separeted by comma in flow definition
flow5 = cluster3 + "," + cluster4 #Devices separeted by comma in flow definition
flow6 = cluster4 + "," + cluster3 #Devices separeted by comma in flow definition

# Emergency State Flows
idle = [flow1,flow2]
preparedness = [flow1, flow2, flow3, flow4]
warning = [flow1, flow2, flow3, flow4, flow5, flow6]
crisis = [flow3, flow4] 

# Emergency States
emergencyStatesNames = {'i':'Idle', 'p':'Preparedness','w':'Warning','c':'Crisis'}
emergencyStates = {'i':idle, 'p':preparedness, 'w':warning, 'c':crisis}

#--------------------- END - HAMRA Configuration Area --------------------------
    