from blockchain import block 


def main():
    chain = block.initBlockchain()

    chain.addBlock("First Block after Genesis")
    chain.addBlock("Second Block after Genesis")
    chain.addBlock("Third Block after Genesis")

    for blocks in chain.blocks:
        print("Previous Hash: ",blocks.prevHash)
        print("Data in Block: ",blocks.data)
        print("Hash: ",blocks.hash)

        pow = block.Block.newProof(blocks)
        print("PoW: ",pow.validate())
        print()
        
main()
