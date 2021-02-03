import Client
from twisted.internet import reactor

port = 5070
host = "127.0.0.1"

peers = [(host, 5050), (host, 5090)]
db_url = "../databases/db2.txt"
deb_url = "/home/raluca/Desktop/BitcoinWannabe/databases/db2.txt"

node1 = Client.Client(host, port, db_url)
reactor.listenUDP(port, node1)
reactor.run()
