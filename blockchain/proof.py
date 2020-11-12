import hashlib
import sys


DIFFICULTY = 18

class ProofOfWork:
    block = None
    target = 0

    def __init__(self,block,target):
        self.block = block
        self.target = target

    def initData(self, nonce):
        data = str(self.block.prevHash) + str(self.block.data + hex(nonce) + hex(DIFFICULTY))
        return data

    def run(self):
        hash = []
        nonce = 0

        while nonce < sys.maxsize:
            data = self.initData(nonce)
            hash = hashlib.sha256(data.encode()).hexdigest()
            print(hash,end='\r')
            intHash = int(hash,16)

            if intHash < self.target:
                break
            else:
                nonce += 1

        print()

        return nonce, hash[:]
    
    def validate(self):
        data = self.initData(self.block.nonce)
        hash = hashlib.sha256(data.encode()).hexdigest()
        intHash = int(hash,16)

        return intHash < self.target

        