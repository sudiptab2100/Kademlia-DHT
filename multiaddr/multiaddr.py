import multiaddr.validator as vd

class MultiAddr:
    def __init__(self, maddr: str):
        """
        Args:
            maddr (str): The multiaddress string in this '/ip4/10.10.10.10/tcp/62535/QmSudipta' format
        """
        self.maddr = maddr
        if not self.isValid(maddr):
            raise ValueError("Invalid multiaddress")
        
        self.ipVersion, self.ipAddr, self.transport, self.port, self.peerId = list(maddr[1: ].split('/'))
    
    def __str__(self):
        return self.maddr
    
    def isValid(self, maddr):
        ipVersion, ipAddr, transport, port, peerId = list(maddr[1: ].split('/'))
        return vd.isValidIPVersion(ipVersion)\
            and vd.isValidIP(ipAddr)\
            and vd.isValidTransport(transport)\
            and vd.isValidPort(port)\
            and vd.isValidPeerID(peerId)