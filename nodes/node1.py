import Client
from twisted.internet import reactor

port = 5050
host = "127.0.0.1"

peers = [(host, 5070), (host, 5090)]
db_url = "../databases/db1.txt"
deb_url = "/home/raluca/Desktop/BitcoinWannabe/databases/db1.txt"

node1 = Client.Client(host, port, db_url)
reactor.listenUDP(port, node1)
reactor.run()
