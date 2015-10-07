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
                          #ip="172.31.3.100/24",
                          #defaultRoute="default")

        #h4 = self.addHost("h4",
                          #ip="172.31.4.100/24",
                          #defaultRoute="default")
          
                          

       
        s1 = self.addSwitch("s1")
        #s2 = self.addSwitch("s2")
        #s3 = self.addSwitch("s3")
        #s4 = self.addSwitch("s4")
        #s5 = self.addSwitch("s5")
        #s6 = self.addSwitch("s6")
        #s7 = self.addSwitch("s7")
        #s8 = self.addSwitch("s8")
        #s9 = self.addSwitch("s9")
        #s10 = self.addSwitch("s10")
        #s11= self.addSwitch("s11")
        #s12= self.addSwitch("s12")
        #s13= self.addSwitch("s13")
        #s14= self.addSwitch("s14")
        #s15= self.addSwitch("s15")
        #s16= self.addSwitch("s16")
        #s17= self.addSwitch("s17")
        #s18= self.addSwitch("s18")
        #s19= self.addSwitch("s19")
        #s20= self.addSwitch("s20")
        #s21= self.addSwitch("s21")
        #s22= self.addSwitch("s22")
        #s23= self.addSwitch("s23")
        
               
        #self.addLink(s1, s2, bw=100)
        #self.addLink(s2, s3, bw=100)
        #self.addLink(s3, s4, bw=100)
        #self.addLink(s4, s5, bw=100)
        #self.addLink(s5, s6, bw=100)
        #self.addLink(s6, s7, bw=100)
        #self.addLink(s7, s8, bw=100)
        #self.addLink(s8, s9, bw=100)
        #self.addLink(s9, s10, bw=100)
        #self.addLink(s10, s11, bw=100)
        #self.addLink(s11, s12, bw=100)
        #self.addLink(s12, s13, bw=100)
        #self.addLink(s13, s14, bw=100)
        #self.addLink(s14, s15, bw=100)
        #self.addLink(s15, s16, bw=100)
        #self.addLink(s16, s17, bw=100)
        #self.addLink(s17, s18, bw=100)
        #self.addLink(s18, s19, bw=100)
        #self.addLink(s19, s20, bw=100)
        #self.addLink(s20, s21, bw=100)
        #self.addLink(s21, s22, bw=100)
        #self.addLink(s22, s23, bw=100)
        
    
                
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        #self.addLink(h3, s5)
        #self.addLink(h4,s6)
        
              
 
topos = {'psn':(lambda: psnTopology())}
        
