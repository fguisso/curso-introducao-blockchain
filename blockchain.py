import genesis
import miner

blockchain = [genesis.create_genesis_block()]
previous_block = blockchain[0]

blocks_size = 5

for i in range(0, blocks_size):
    block_to_add = miner.mine(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}".format(block_to_add.hash))
    print("Nonce: {}".format(block_to_add.nonce))
    print("Previous Hash: {}".format(block_to_add.previous_hash))
    print("Data: {}\n".format(block_to_add.data))
