# HAMRA - Network Traffic Manager
# Version 1.11.1
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
import time


# Declaration of  HAMRA Network Traffic Manager Class

class NetworkTrafficManager (DynamicPolicy):
    
        
    def __init__(self): 
        """ Method for initialization of the HAMRA's NTM """
        
        self.startTime = time.clock() #Register Start Time of the function
        
        # Global Variables
        self.elapsedTimeInit = 0
        self.elapsedTimeSetState = 0
        self.elapsedTimeUpdatePolicy = 0
        self.simulationId = 1
                    
        print "\n"
        print "Initializing HAMRA Network Traffic Manager" 
        print "Welcome to HAMRA Network Traffic Management - Version 1.11.1"
        print "Developed by Daniel Merege - 2015"
        print "\n"
        
        self.currentState = "None"
        self.activeFlows = {} #List to store the active flows in the current state
        super(NetworkTrafficManager,self).__init__(true)
        self.ui = threading.Thread(target=self.NTM_ui)
        self.ui.daemon = True
        self.ui.start()
        
        self.endTime = time.clock() #Register End Time of the function
        self.elapsedTimeInit = self.endTime - self.startTime #Calculate elapsed time of the function

        
    def setState (self, state):
       
           
        self.startTime = time.clock() #Register Start Time of the function
        
        self.activeFlows = {} #Erase every flow in ActiveFlows dictionary
        self.stateInCharge = hamraConfig.emergencyStates.get(state)
        
        for flow in self.stateInCharge: 
            (str1,str2) = flow.split(',')
            #(source,destination) = (IP(str1),IP(str2))
            (source,destination) = (str1,str2)
            self.activeFlows [(source, destination)] = True #Flow from sourceIP to DestinationIP is active
            
        self.currentState = hamraConfig.emergencyStatesNames.get(state)
        
        self.endTime = time.clock()  #Register End Time of the function
        self.elapsedTimeSetState = self.endTime - self.startTime #Calculate elapsed time of the function
            
   
    def UpdatePolicy (self):
        """ Method for renew the traffic policy in the network """
        
        self.startTime = time.clock() #Register Start Time of the function
        
        self.policy =  union ([match(srcip=source) & match(dstip=destination) 
                              for (source,destination) 
                              in self.activeFlows.keys()])

        print self.policy
             
        self.endTime = time.clock() #Register End Time of the function
        self.elapsedTimeUpdatePolicy = self.endTime - self.startTime #Calculate elapsed time of the function
        
    
    #Save Elapsed Times into Results.txt   
    
    def saveSimulation(self):
        
        self.file.write(str(self.simulationId))
        self.file.write(';') 
        self.file.write(self.currentState)
        self.file.write(';')
        self.file.write(str(self.elapsedTimeInit))
        self.file.write(';')
        self.file.write(str(self.elapsedTimeSetState))
        self.file.write(';')
        self.file.write(str(self.elapsedTimeUpdatePolicy))
        self.file.write('\n')
        
        self.simulationId = self.simulationId + 1
              
    #Initialize Network
    def NTM_ui(self):
        
        #Save Elapsed Times into Results.txt
        self.file = open('/home/mininet/Hamra/src/Simulations/results.txt','w')
        self.file.write('HAMRA Simulation 1.11.1\n')
        self.file.write('Simulation_Id;State;Init_Time;SetState_Time;Update_Time\n')
       
        #Ask the Network Configuration
        while(True):
            print 'Available Network States\n'
            print '\n'
            print hamraConfig.emergencyStatesNames.items()
            print '\n'
                                     
            command = raw_input('Type the first letter of your option, or (q) to Quit Hamra:\n\n')

            if  hamraConfig.emergencyStates.has_key(command):
                self.setState(command)
                self.UpdatePolicy ()
                self.saveSimulation()
                
                
                print '**Current State**\n'
                print self.currentState
                print '\n' 
            elif command == 'q':
                print "Quitting HAMRA"
                os.kill(os.getpid(), signal.SIGINT)
                return          
            else:
                print "Invalid Option. Try Again. \n"
                
            print "Init Time: ", self.elapsedTimeInit, "\n"
            print "Set State Time: ", self.elapsedTimeSetState, "\n"
            print "Update Policy Time: ", self.elapsedTimeUpdatePolicy, "\n"
                
        self.file.close() #Close Simulation File
                   
def main():
    return NetworkTrafficManager() >> flood()
        
    
        
    