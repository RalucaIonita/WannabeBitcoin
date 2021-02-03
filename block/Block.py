'''
class Header:
    def __init__(self, version, previous_block_hash, timestamp, difficulty_target, nonce):
        self.version = version
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp,
        self.difficulty_target = difficulty_target
        self.nonce = nonce

    def build_header(version, previous_block, difficulty, nonce):
        self.version = version
        self.previous_block_hash = previous_block
        self.timestamp = datetime.now
        self.difficulty_target = difficulty
        self.nonce = nonce


class Block:
    def __init__(self, size, header, transactions_counter, transactions):
        self.size = size
        self.header = header
        self.transactions_counter = transactions_counter
        self.transactions = transactions
'''

from bitcoin import *


class Block:
    def __init__(self, text, nonce, hash):
        self.text = text
        self.nonce = nonce
        self.hash = hash

    def is_acceptable(hash):
        return hash.startswith('000')

    def hash_block(block):
        hash = sha256(block)
        return hash

    def generate_hash(initial_string):
        index = 0
        hash = hash_block(initial_string + str(index))
        while not is_acceptable(hash):
            # get some random shit here
            index += 1
            hash = hash_block(initial_string + str(index))
            # print(hash)
        response = ()
        return hash
