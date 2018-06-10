import requests

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        pass

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
