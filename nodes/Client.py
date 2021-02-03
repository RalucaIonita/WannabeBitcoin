from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == "localhost":
            host = "127.0.0.1"

        self.id = host, port
        self.peers = None
        self.seeder = '127.0.0.1', 9999
        print("Node " + str(host) + " : " + str(port) + " is up!")

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.seeder)

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')
        if not self.peers:
            number = int(input("How many clients would you like to connect to?"))
            self.peers = []
            for i in range(number):
                print("Choose a client:\n", datagram)
                address = input("Write address: "), int(input("Write port: "))
                self.peers.append(address)
            reactor.callInThread(self.send_message)
        else:
            print(str(addr) + " : " + str(datagram))

    def send_message(self):
        while True:
            input_txt = input("##")
            for peer in self.peers:
                self.transport.write(input_txt.encode('utf-8'), peer)
