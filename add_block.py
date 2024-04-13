import os
import struct
import uuid
from hashlib import sha256
from datetime import datetime
from utils import *
from constant import *
from initialize import *

#TODO: add_block is finished for now, move on to checkout and checkin

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

    if password != get_password("CREATOR"):
        print("Invalid password")
        exit(1)


    # Load blockchain data
    with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    for item_id in item_ids:
        # Check if item_id already exists in the blockchain
        if check_item_exists(blockchain_file, item_id):
            print(f"Error: Item ID {item_id} already exists in the blockchain.")
            exit(1)
        # Create block data
        previous_hash = calculate_hash(blockchain_data)
        timestamp = get_timestamp().timestamp()
        state = STATE["checkedin"]
        creator = creator
        owner = 'Police'
        data_length = len(f'Item ID: {item_id}')
        data = f'Item ID: {item_id}'

        # Encrypt case_id and item_id
        encrypted_case_id = encrypt(case_id.encode())
        encrypted_item_id = encrypt(struct.pack("I", int(item_id)))
        print(f"Encrypted item id: {encrypted_item_id}")
        # Pack block data
        packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id,encrypted_item_id, state, creator.encode().ljust(12, b'\0'), owner.encode().ljust(12, b'\0'), data_length) + data.encode()
        # print(sha256(packed_block).hexdigest())
        # Append block to blockchain data
        blockchain_data += packed_block
        print(f"Added item: {item_id}")
        print(f"Status: CHECKEDIN")
        print(f"Time of action: {datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)}")
    
    # Write updated blockchain data to file
    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)

    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)

    print("Item(s) added successfully to the blockchain.")

    

def check_item_exists(blockchain_file, item_id):
    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, _, encrypted_item_id, _, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)
            decrypted_item_id = decrypt(encrypted_item_id)
            if int.from_bytes(decrypted_item_id, "little") == int(item_id):
                return True

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    return False

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