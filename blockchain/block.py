import hashlib
from blockchain import proof
import pickle


class Block:
    hash = []
    data = []
    prevHash = []
    nonce = 0

    def __init__(self, data, prevHash,nonce):
        self.data = data
        self.prevHash = prevHash
        self.nonce = nonce

    def newProof(self):
        target = 1
        target = target << 256 - proof.DIFFICULTY
        pow = proof.ProofOfWork(self,target)
        return pow

    def serialize(self):
        encoder = pickle.dumps(self)
        return encoder

def deserialize(data):
    block = pickle.loads(data)
    return block   

def createBlock(data,prevHash):
    block = Block(data,prevHash,0)
    pow = Block.newProof(block)
    nonce, hash = pow.run()

    block.hash = hash[:]
    block.nonce = nonce

    return block 

def genesis():
    return createBlock("Genesis", " ")


