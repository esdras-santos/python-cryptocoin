from blockchain import block 
from blockchain import blockchain
import sys


class CommandLine:
    blockchain = blockchain.Blockchain

    def printUsage(self):
        print("Usage:")
        print(" add -block BLOCK_DATA - add a block to the chain")
        print(" print - Prints the blocks in the chain")

    def validateArgs(self):
        if len(sys.argv) < 2:
            self.printUsage()
            sys.exit()


def main():
    chain = block.initBlockchain()


    for blocks in chain.blocks:
        print("Previous Hash: ",blocks.prevHash)
        print("Data in Block: ",blocks.data)
        print("Hash: ",blocks.hash)

        pow = block.Block.newProof(blocks)
        print("PoW: ",pow.validate())
        print()
        
main()


print("number: ",len(sys.argv))

