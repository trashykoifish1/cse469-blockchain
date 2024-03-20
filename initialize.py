# This module is used to initialize the blockchain. If a blockchain already exists, it check if the the inital block is valid or not
import os
import struct
import time
import uuid
from utils import encrypt_aes_ecb
from constant import AES_KEY

def check_initial_block():
    """
    Check if the blockchain file exists and contains a valid initial block.

    Returns:
    - True if the blockchain file exists and contains a valid initial block, False otherwise.
    """
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    if not blockchain_file:
        print("Error: BCHOC_FILE_PATH environment variable not set.")
        exit(1)

    if os.path.exists(blockchain_file):
        # Check if the state of the first block is 'INITIAL'
        try:
            with open(blockchain_file, 'rb') as file:
                # Read the first block head
                initial_block_head = file.read(144)
                if len(initial_block_head) != 144:
                    print("Error: Invalid block size in blockchain file.")
                    exit(1)
                unpacked_block_head = struct.unpack("32s d 32s 32s 12s 12s 12s I", initial_block_head)
                _, _, _, _, state, _, _, _ = unpacked_block_head

                if state.decode().strip('\0') == 'INITIAL':
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error: Failed to read blockchain file - {str(e)}")
            exit(1)
    else:
        return False

def initialize():
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    if check_initial_block():
        print("Blockchain file found with INITIAL block.")
        exit(0)
    else:
        with open(blockchain_file, 'wb') as file:
            # Write an empty initial block to the blockchain file
            initial_block_data = create_initial_block()
            file.write(initial_block_data)
            print("Blockchain file not found. Created INITIAL block.")
            exit(0)
    
def create_initial_block():
    """
    Create data for the initial block.

    Returns:
    - Packed initial block data.
    """
    # Generate block data
    previous_hash = b''  # No previous hash for initial block
    timestamp = time.time()
    case_id = 0  # No case ID for initial block
    item_id = 0  # No item ID for initial block
    state = 'INITIAL'
    creator = ''  # No creator for initial block
    owner = ''  # No owner for initial block
    data_length = len(b'Initial block')
    data = b'Initial block'

    # Encrypt case_id and item_id
    encrypted_case_id = encrypt_aes_ecb(struct.pack("I", case_id), AES_KEY)
    encrypted_item_id = encrypt_aes_ecb(struct.pack("I", item_id), AES_KEY)

    # Create the initial block instance
    packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id, encrypted_item_id, state.encode().ljust(12, b'\0'), creator.encode().ljust(12, b'\0'), owner.encode().ljust(12, b'\0'), data_length) + data

    return packed_block