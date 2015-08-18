# HAMRA - Configuration File
# Developed By Daniel Merege - 2015
#--------------------- BEGIN - HAMRA Configuration Area ------------------------

# Network Devices (IP Addresses)
host1 = '10.0.0.1'
host2 = '20.0.0.1' 
host3 = '30.0.0.1' 
host4 = '40.0.0.1' 
    
# Clusters (Switches IDs)
cluster1 = '10.0.0.0/24'
cluster2 = '20.0.0.0/24'
cluster3 = '30.0.0.0/24'
cluster4 = '40.0.0.0/24'
    
# DataFlow
flow1 = cluster1 + "," + cluster2 #Devices separeted by comma in flow definition (SourceNetwork,DestinationNetwork)
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
    