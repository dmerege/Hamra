# HAMRA - Configuration File
# Developed By Daniel Merege - 2015
#--------------------- BEGIN - HAMRA Configuration Area ------------------------

# Network Devices (IP Addresses)
host1 = '172.31.1.100'
host2 = '172.31.2.100'
#host3 = '172.31.3.100' 
#host4 = '172.31.4.100' 
    
# Clusters (Subnet Range IPs)
cluster1 = '172.31.1.0/24'
cluster2 = '172.31.2.0/24'
cluster3 = '172.31.3.0/24'
cluster4 = '172.31.4.0/24'
    
# DataFlow
flow1 = cluster1 + "," + cluster2 #Devices separeted by comma in flow definition (SourceNetwork,DestinationNetwork)
flow2 = cluster2 + "," + cluster1 #Devices separeted by comma in flow definition
flow3 = cluster2 + "," + cluster3 #Devices separeted by comma in flow definition
flow4 = cluster3 + "," + cluster2 #Devices separeted by comma in flow definition
flow5 = cluster3 + "," + cluster4 #Devices separeted by comma in flow definition
flow6 = cluster4 + "," + cluster3 #Devices separeted by comma in flow definition

# Emergency State Flows
idle = [flow1,flow2]
preparedness = [flow1,flow2,flow3,flow4]
warning = [flow1,flow2,flow3,flow4, flow5]
crisis = [flow1,flow2,flow3,flow4, flow5, flow6] 

# Emergency States
emergencyStatesNames = {'i':'Idle', 'p':'Preparedness','w':'Warning','c':'Crisis'}
emergencyStates = {'i':idle, 'p':preparedness, 'w':warning, 'c':crisis}

#--------------------- END - HAMRA Configuration Area --------------------------
    