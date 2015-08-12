# HAMRA - Network Traffic Manager
# Version 1.0
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
        print "Welcome to HAMRA Network Traffic Management - Version 1.0"
        print "Developed by Daniel Merege - 2015"
        print "\n"
        self.currentState = "None"
        self.activeFlows = {} #List to store the active flows in the current state
        super(NetworkTrafficManager,self).__init__(true)
        self.ui = threading.Thread(target=self.NTM_ui)
        self.ui.daemon = True
        self.ui.start()
        
    def setState (self, state):
        """ Method for network configuration when the emergency's state is Idle """
        
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        self.stateInCharge = hamraConfig.emergencyStates.get(state)
        
        for flow in self.stateInCharge: 
            (str1,str2) = flow.split(',')
            (source,destination) = (IP(str1),IP(str2))
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.UpdatePolicy ()
        
        self.currentState = hamraConfig.emergencyStatesNames.get(state)
        print '**Current State**\n'
        print self.currentState
        print '\n'      
           
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
            print 'Available Network States\n'
            print '\n'
            print hamraConfig.emergencyStatesNames.items()
            print '\n'
                
            command = raw_input('Type the first letter of your option, or (q) to Quit Hamra:\n\n')

            if  hamraConfig.emergencyStates.has_key(command):
                self.setState(command)
            elif command == 'q':
                print "Quitting HAMRA"
                os.kill(os.getpid(), signal.SIGINT)
                return          
            else:
                print "Invalid Option. Try Again. \n"
        
def main():
    return NetworkTrafficManager() >> flood()
        
    
        
    