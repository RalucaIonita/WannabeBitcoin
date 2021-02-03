from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class PseudoSeeder(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')
        if datagram == "ready":
            addresses = " ".join([str(x) for x in self.clients])
            self.transport.write(addresses.encode('utf-8'), addr)
            self.clients.add(addr)


reactor.listenUDP(9999, PseudoSeeder())
reactor.run()
