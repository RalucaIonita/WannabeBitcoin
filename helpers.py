from bitcoin import *
# from btclib import *


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
    return hash


generate_hash("banane")
