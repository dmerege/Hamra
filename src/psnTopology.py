# HAMRA - PSN Topology for Mininet
# Developed By Daniel Merege - 2015

# PSN Topology for Mininet

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host, OVSSwitch, Controller, RemoteController

class psnTopology(Topo):
    

    def __init__( self, enable_all = True ):
        

        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="172.31.1.100/24",
                          defaultRoute="default")

        h2 = self.addHost("h2",
                          ip="172.31.2.100/24",
                          defaultRoute="default")

        #h3 = self.addHost("h3",
        #                  ip="172.31.3.100/24",
        #                  defaultRoute="default")

        #h4 = self.addHost("h4",
        #                  ip="172.31.4.100/24",
        #                  defaultRoute="default")

       
        s1 = self.addSwitch("s1")
        #s2 = self.addSwitch("s2")
        #s3 = self.addSwitch("s3")
        #s4 = self.addSwitch("s4")
        #s5 = self.addSwitch("s5")
        #s6 = self.addSwitch("s6")
        
        
        
        #self.addLink(s1, s2)
        #self.addLink(s2, s3)
        #self.addLink(s3, s4)
        #self.addLink(s4, s5)
        #self.addLink(s5, s6)
                
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        #self.addLink(h3, s5)
        #self.addLink(h4,s6)
        
              
 
topos = {'psn':(lambda: psnTopology())}
        
