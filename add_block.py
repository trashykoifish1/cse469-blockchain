import os
import struct
import uuid
from hashlib import sha256
from datetime import datetime
from utils import encrypt_aes_ecb, decrypt_aes_ecb
from constant import AES_KEY
from initialize import *

def add_block(case_id, item_ids, creator, password):
    """
    Add a new item to the blockchain.

    Args:
    - case_id: Case identifier (UUID) associated with the item.
    - item_ids: Evidence item identifiers (list of integers) associated with the item.
    - creator: Creator of the item.
    - password: Password for blockchain operations.

    Returns:
    - Success message if item added successfully, error message otherwise.
    """
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    # Authenticate user with password
    # authenticated = authenticate(password)
    # if not authenticated:
    #     return "Error: Authentication failed."
    # Check if initial block exists
    if not check_initial_block():
        # Initialize blockchain
        initialize()

    # Load blockchain data
    with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    for item_id in item_ids:
        # TODO: Check if item_id already exists in the blockchain

        # Create block data
        previous_hash = calculate_hash(blockchain_data)
        timestamp = time.time()
        state = 'CHECKEDIN'
        creator = creator
        owner = 'Police'
        data_length = len(f'Item ID: {item_id}')
        data = f'Item ID: {item_id}'

        # Encrypt case_id and item_id
        encrypted_case_id = encrypt_aes_ecb(struct.pack("I", int(case_id)), AES_KEY)
        encrypted_item_id = encrypt_aes_ecb(struct.pack("I", int(item_id)), AES_KEY)

        # Pack block data
        packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id,encrypted_item_id, state.encode().ljust(12, b'\0'), creator.encode().ljust(12, b'\0'), owner.encode().ljust(12, b'\0'), data_length) + data.encode()
        print(sha256(packed_block).hexdigest())
        # Append block to blockchain data
        blockchain_data += packed_block
    
    # Write updated blockchain data to file
    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)
    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)

    print("Item(s) added successfully to the blockchain.")

    

def calculate_hash(data):
    """
    Calculate the SHA-256 hash of the given data.

    Args:
    - data: Data to hash.

    Returns:
    - SHA-256 hash of the data.
    """
    hasher = sha256()
    hasher.update(data)
    return hasher.digest()