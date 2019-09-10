import datetime as date
import block

def mine(last_block):
    nonce = 0
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is the #" + str(this_index) + " block!"
    this_hash = last_block.hash
    this_nonce = nonce
    new_block = block.Block(this_index, this_timestamp, this_data, this_hash, nonce)
    while new_block.hash[:2] != "00":
        nonce += 1
        new_block = block.Block(this_index, this_timestamp, this_data, this_hash, nonce)
    return new_block
