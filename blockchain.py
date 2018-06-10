import hashlib, json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask

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

    def proof_of_work(self, last_proof):
        """Simple Proof of Work algorithm

        -Find a number p such that hash(pp') contains four leading 0's, where p is the previous p'
        -p is the previous proof, and p' is the new proof
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validates the proof. Does hash(last_proof, proof) contain 4 leading zeroes?

        :param last_proof: <int> Previous proof
        :param proof: <int> current proof
        :return bool:  True if correct, False if not
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):
        """Creates a sha-256 hash of a Block

        :param block: <dick> Block
        :return: <str>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        return self.chain[-1]


#instantiate the node
app = Flask(__name__)
#generate globally unique address for the node
node_identifier = str(uuid4()).replace('-', '')
#instatiate blcokchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
