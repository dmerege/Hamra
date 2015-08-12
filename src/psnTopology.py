# HAMRA - PSN Topology for Mininet
# Developed By Daniel Merege - 2015

# PSN Topology for Mininet

from mininet.topo import Topo

class PSNTopo(Topo):
    
    def __init__(self):
        
        # Add default members to class.
        super(PSNTopo, self).__init__()
        
        # Adding Switches and Hosts
        self.addSwitch('s1')
        self.addSwitch('s2')
        self.addSwitch('s3')
        self.addSwitch('s4')
        self.addHost('h1', ip='10.0.0.1')
        self.addHost('h2', ip='10.0.0.2')
        self.addHost('h3', ip='10.0.0.3')
        self.addHost('h4', ip='10.0.0.4')
        
      
        # Adding links between swicthes and hosts
        self.addLink ('s1', 's2')
        self.addLink ('s2', 's3')
        self.addLink ('s3', 's4')
        self.addLink ('s1', 'h1')
        self.addLink ('s2', 'h2')
        self.addLink ('s3', 'h3')
        self.addLink ('s4', 'h4')
       
topos = {'psn': PSNTopo}
       
        
        
        
