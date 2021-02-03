from bitcoin import *
import json
import uuid


class Block:
    lastBlock = ""

    def __init__(self, text, nonce, hash):
        self.text = text
        self.nonce = nonce
        self.hash = hash

    def build_block(self, text):
        self.text = text
        index = 0
        # hashing
        hash = sha256(text + str(index))
        while not hash.startswith("000"):
            index += 1
            hash = sha256(text + str(index))
        self.nonce = index
        self.hash = hash

    def check_valid_block(self, block):
        if self.hash == block.hash and self.text == block.text and self.nonce == block.nonce:
            return True
        return False

    def add_to_db(self, db_url):
        Block.lastBlock = str(json.dumps(self.__dict__)).replace("\\", "")
        print("Last block:")
        print(Block.lastBlock)
        file = open(db_url, "a")
        file.write(self.lastBlock)
        file.close()
        print("Wrote in file")

    @staticmethod
    def get_hashing_text():
        if Block.lastBlock == "":
            string = str(uuid.uuid4())
            print(string)
            return string
        else:
            return Block.lastBlock
