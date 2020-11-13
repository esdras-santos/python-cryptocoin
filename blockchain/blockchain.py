from blockchain import block
import pickledb


dbPath = "./tmp/blocks/blockchain.db"

class Blockchain:

    def __init__(self,lastHash,db):
        self.lastHash = lastHash
        self.database = db

    def addBlock(self, data):
        lastHash = self.database.get("lh")
        newBlock = block.createBlock(data,lastHash)
        self.database.set("lh",newBlock.hash)
        self.lastHash = newBlock.hash
        self.database.dump()

    def iterator(self):
        iter = BlockchainIterator(self.lastHash,self.database)
        return iter

class BlockchainIterator:
    
    def __init__(self,currentHash, database):
        self.currentHash = currentHash
        self.database = database

    def next(self):
        encodedBlock = self.database.get(self.currentHash)
        blk = block.deserialize(encodedBlock)
        self.currentHash = blk.prevHash
        return blk


def initBlockchain():
    lastHash = []
    db = pickledb.load(dbPath,False)
    if db.exists("lh"):
        print("No existing blockchain found")
        genesis = block.genesis()
        print("genesis proved")
        db.append(genesis.hash, genesis.serialize())
        db.append("lh",genesis.hash)
        lastHash = genesis.hash
        db.dump()
    else:
        lastHash = db.get("lh")

    blockchain = Blockchain(lastHash,db)
    return blockchain