from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = time.ctime(time.time())
        self.previous_hash = previous_hash
        self.own_hash ="" #compute_hash(self.index+transactions+timestamp+previous_hash)
        self.nonce = 0

    # def toHash(self):
    #     return self.index+self.transactions+self.timestamp+self.previous_hash
    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = str(self.index)+self.transactions+self.timestamp+self.previous_hash+str(self.nonce)
        # return
        self.own_hash=sha256(block_string.encode()).hexdigest()
    def verificarHash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = str(self.index)+self.transactions+self.timestamp+self.previous_hash+str(self.nonce)
        # return
        return sha256(block_string.encode()).hexdigest()

    def print_bloque(self):
        print("index",self.index)
        print("transactions",self.transactions)
        print("timestamp",self.timestamp)
        print("previous_hash",self.previous_hash)
        print("own_hash",self.own_hash)
        print("nonce",self.nonce)
        return 0
#
class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """

        # seconds passed since epoch
        genesis_block = Block(0, '[]', "0000")
        genesis_block.compute_hash()
        while(not genesis_block.own_hash.startswith("00")):
            genesis_block.nonce+=1
            genesis_block.compute_hash()

        self.chain.append(genesis_block)
    def printChainConfirmed(self):
      for i in self.chain:
          print("-----------")
          i.print_bloque()
    def printUnconfirmed(self):
      for i in self.unconfirmed_transactions:
          i.print_bloque()

    # @property
    # def last_block(self):
    #     return self.chain[-1]
    def add_2future(self, data):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        self.unconfirmed_transactions.append(data)

        return True
    def add_block(self, data):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """

        previous_hash = self.chain[-1].own_hash
        newBlock = Block(self.chain[-1].index+1, data,previous_hash )
        newBlock.compute_hash()
        while(not newBlock.own_hash.startswith("00")):
            newBlock.nonce+=1
            newBlock.compute_hash()
        self.chain.append(newBlock)
        return True

    def searchIndex(self, indice):
        for i in self.chain:
            if i.index==indice:
                return i
        return False
    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index




# bc = Blockchain()
# bc.add_block("aaaaaaaaaaaaaaaa")
# bc.printChainConfirmed()



#
