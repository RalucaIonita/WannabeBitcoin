class Input:
    def __init__(self, prev_transaction_hash, previous_txout_index, scriptSig):
        self.previous_transaction_hash = prev_transaction_hash
        self.previous_index = previous_txout_index
        self.sign = scriptSig
