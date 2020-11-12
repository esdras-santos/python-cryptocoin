from blockchain import block
import pickledb


dbPath = "./tmp/blocks/blockchain.db"

class Blockchain:
    blocks = []

    def __init__(self,block):
        self.blocks.append(block)

    def addBlock(self, data):
        prevBlock = self.blocks[len(self.blocks)-1]
        new = block.createBlock(data,prevBlock.hash)
        self.blocks.append(new)

def initBlockchain():
    db = pickledb.load(dbPath,False)
    if db.exists("lh"):
        print("No existing blockchain found")
        genesis = block.genesis()
        print("genesis proved")
        db.append(genesis.hash, genesis.serialize())
        db.append("lh",genesis.hash)
        lastHash = genesis.hash
        db.dump()
