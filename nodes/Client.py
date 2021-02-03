from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import json
from Block import Block
from threading import Event




class Client(DatagramProtocol):



    def __init__(self, host, port, db_url):
        if host == "localhost":
            host = "127.0.0.1"

        self.db_url = db_url
        self.id = host, port
        self.peers = None
        self.seeder = '127.0.0.1', 9999
        self.CurrentBlock = None
        print("Node " + str(host) + " : " + str(port) + " is up!")

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.seeder)

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')

        print(datagram + "****************")
        if not self.peers:
            number = int(input("How many clients would you like to connect to?"))
            self.peers = []
            for i in range(number):
                print("Choose a client:\n", datagram)
                address = input("Write address: "), int(input("Write port: "))
                self.peers.append(address)
            reactor.callInThread(self.send_message)
        else:
            #hai cu block-urile

            #check
            if datagram != "":
                deserialized_block  = json.loads(datagram)
                received_block = Block(deserialized_block["text"], deserialized_block["nonce"], deserialized_block["hash"])
                print("Received block: ")
                print(received_block)

                computed_block = Block("", "", "")
                computed_block.build_block(received_block.text)

                print("Checking received block is valid...")
                if computed_block.check_valid_block(received_block):
                    print("Block is valid.")
                    print("Adding to database...")
                    received_block.add_to_db(self.db_url)
                else:
                    print("Block is invalid. Block has not been added.")

            #new block
            text = Block.get_hashing_text()
            self.CurrentBlock = Block("", "", "")
            self.CurrentBlock.build_block(text)

            print(str(addr) + " : " + str(datagram))
            print("Computed: " + str(json.dumps(self.CurrentBlock.__dict__)))


    def send_message(self):
        while True:
            if self.CurrentBlock is None:
                input_txt =""
            else:
                input_txt = str(json.dumps(self.CurrentBlock.__dict__))

            Event().wait(5)
            for peer in self.peers:
                self.transport.write(input_txt.encode('utf-8'), peer)
                print("Sent + " + str(input_txt.encode('utf-8')))
