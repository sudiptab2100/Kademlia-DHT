import multiaddr.validator as vd

class MultiAddr:
    def __init__(self, maddr: str):
        """
        Constructor for the Multiaddr class.
        
        Args:
            maddr (str): The multiaddress string in this '/ip4/10.10.10.10/tcp/62535/QmSudipta' format
        """
        # Initialize the Multiaddr object with the given multiaddress string
        self.maddr = maddr
        if not self.isValid(maddr):
            raise ValueError("Invalid multiaddress")
    
    def isValid(self, maddr):
        ipVersion, ipAddr, transport, port, peerId = list(maddr[1: ].split('/'))
        return vd.isValidIPVersion(ipVersion)\
            and vd.isValidIP(ipAddr)\
            and vd.isValidTransport(transport)\
            and vd.isValidPort(port)\
            and vd.isValidPeerID(peerId)