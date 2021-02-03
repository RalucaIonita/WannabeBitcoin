import Client
from twisted.internet import reactor

port = 5090
host = "127.0.0.1"

node1 = Client.Client(host, port)
reactor.listenUDP(port, node1)
reactor.run()
