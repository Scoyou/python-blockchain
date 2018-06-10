import requests, datetime, time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """Creates a new block in the Blockchain

        :param proof: <int> the proof given by the proof of work algorithm
        :param previous_hash: <str> hash of previous Block
        :return: <dict> new block
        """

        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = [] #reset list of transactions

        self.chain.append(block)
        return block


    def new_transaction(self,sender,recipient,amount):
        """Creates a new transaction that will go into the next mined into the block

        :param sender: <str> address of the sender
        :param recipient: <str> address of the recipient
        :param amount: <int> amount
        :return: <int> the index of the block that will hold this transaction
        """
        self.current_transactions.append(
            {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass
