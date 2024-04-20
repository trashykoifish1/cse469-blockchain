import os
import struct
from utils import *
from constant import *
from initialize import *

def verify():
    blockchain_file = os.getenv('BCHOC_FILE_PATH')

    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    num_blocks = 0
    prev_hash = None
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            prev_block_hash, _, _, _, state, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            block_size = 144 + data_length
            block_data = blockchain_data[offset:offset+block_size]
            block_hash = calculate_hash(block_data)

            if num_blocks == 0:
                if prev_block_hash != b'\0' * 32:
                    print("Error: Invalid previous hash in the genesis block.")
                    exit(1)
            else:
                if prev_block_hash != prev_hash:
                    print(f"Error: Invalid previous hash in block {num_blocks}.")
                    exit(1)

            prev_hash = block_hash
            offset += block_size
            num_blocks += 1

            state = state.decode().strip('\0')
            if state in ["DISPOSED", "DESTROYED", "RELEASED"]:
                if offset < len(blockchain_data):
                    next_block_header = blockchain_data[offset:offset+144]
                    next_state = next_block_header[100:112].decode().strip('\0')
                    if next_state != state:
                        print(f"Error: Invalid state transition in block {num_blocks}.")
                        exit(1)

        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    print(f"Blockchain verification completed. {num_blocks} blocks verified.")
    print("Blockchain is valid.")