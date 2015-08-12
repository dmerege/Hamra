# HAMRA - Network Traffic Manager
# Version 0.5
# Developed By Daniel Merege - 2015

# Importation of Pyretic Classes

from pyretic.lib.corelib import *
from pyretic.lib.std import *

#Import Hamra Configuration File
import hamraConfig 

# Importation of Python Classes
import os
import signal
import threading

 
# Declaration of  HAMRA Network Traffic Manager Class

class NetworkTrafficManager (DynamicPolicy):
    
        
    def __init__(self): 
        """ Method for initialization of the HAMRA's NTM """
        
        print "Initializing HAMRA Network Traffic Manager" 
        print "Welcome to HAMRA Network Traffic Management - Version 0.5"
        print "Developed by Daniel Merege - 2015"
        print "\n"
        self.currentState = "None"
        self.activeFlows = {} #List to store the active flows in the current state
        super(NetworkTrafficManager,self).__init__(true)
        self.ui = threading.Thread(target=self.NTM_ui)
        self.ui.daemon = True
        self.ui.start()
        
    
    def IdleState (self):
        """ Method for network configuration when the emergency's state is Idle """
             
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        
        for flow in hamraConfig.idle:
            (str1,str2) = flow.split(',')
            (source,destination) = (IP(str1),IP(str2))
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.UpdatePolicy ()
        self.currentState = "Idle" #Change the Current State to Idle
        print self.currentState
    
    
    def PreparednessState (self):
        """ Method for network configuration when the emergency's state is Preparedness """
        
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        
        for flow in hamraConfig.preparedness:
            (str1,str2) = flow.split(',')
            (source,destination) = (IP(str1),IP(str2))
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.UpdatePolicy ()
        self.currentState = "Preparedness" #Change the Current State to Preparedness
        print self.currentState
        
    def WarningState (self):
        """ Method for network configuration when the emergency's state is Warning """
        
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        
        for flow in hamraConfig.warning:
            (str1,str2) = flow.split(',')
            (source,destination) = (IP(str1),IP(str2))
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.UpdatePolicy ()
        self.currentState = "Warning" #Change the Current State to Warning
        print self.currentState
        
    def CrisisState (self):
        """ Method for network configuration when the emergency's state is  """
        
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        
        for flow in hamraConfig.crisis:
            (str1,str2) = flow.split(',')
            (source,destination) = (IP(str1),IP(str2))
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.UpdatePolicy ()
        self.currentState = "Crisis" #Change the Current State to Crisis
        print self.currentState
            
     
    def UpdatePolicy (self):
        """ Method for renew the traffic policy in the network """
        
        self.policy =  union ([match(srcip=source) & match(dstip=destination) 
                              for (source,destination) 
                              in self.activeFlows.keys()])

        print self.policy
        
        
        
    #Initialize Network
    def NTM_ui(self):
        
        #Ask the Network Configuration
        while(True):
            command = raw_input('Type for: (i)dle, (p)reparedness , (w)arning , (c)risis , (e)xit\n\n')

            if   command == 'i':
                self.IdleState()
            elif command == 'p':
                self.PreparednessState()
            elif command == 'w':
                self.WarningState()
            elif command == 'c':
                self.CrisisState()
            elif command == 'e':
                print "Quitting HAMRA"
                os.kill(os.getpid(), signal.SIGINT)
                return          
            else:
                print "Invalid Option. Try Again. \n"
        
def main():
    return NetworkTrafficManager() >> flood()
        
    
        
    