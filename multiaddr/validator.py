def isValidIPVersion(ipV: str) -> bool:
    ipVersions = ['ip4']
    return ipV in ipVersions

def isValidIP(ipAddr: str) -> bool:
    return all(num.isdigit() and 0 <= int(num) <= 255 for num in ipAddr.split('.')) and len(ipAddr.split('.')) == 4

def isValidTransport(transport: str) -> bool:
    transports = ['tcp']
    return transport in transports

def isValidPort(port: str | int) -> bool:
    return 0 <= int(port) <= 65535

def isValidPeerID(peerId: str) -> bool:
    return True