import os
import struct
import uuid
from datetime import datetime
from utils import *
from constant import *
from initialize import *
from hashlib import sha256

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

    # Encrypt case_id
    case_id = uuid.UUID(case_id).int
    case_id = case_id.to_bytes((case_id.bit_length() + 7) // 8, 'big')
    encrypted_case_id = encrypt(case_id)

    for item_id in item_ids:
        # Check if item_id already exists in the blockchain
        if check_item_exists(blockchain_file, item_id):
            print(f"Error: Item ID {item_id} already exists in the blockchain.")
            exit(1)
        # Create block data
        previous_hash = calculate_hash(blockchain_data)
        timestamp = get_timestamp()
        state = STATE["checkedin"]
        creator = creator
        owner = ''
        data_length = 0
        data = ''

        # Encrypt item_id
        item_id = int(item_id)
        item_id_bytes = item_id.to_bytes(16, 'big')
        encrypted_item_id = encrypt(item_id_bytes)
        # Pack block data
        packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id,encrypted_item_id, state, creator.encode().ljust(12, b'\0'), owner.encode().ljust(12, b'\0'), data_length) + data.encode()
        # print(sha256(packed_block).hexdigest())
        # Append block to blockchain data
        blockchain_data += packed_block
        print(f"Added item: {item_id}")
        print(f"Status: CHECKEDIN")
        print(f"Time of action: {get_string_timestamp(timestamp)}")
    
    # Write updated blockchain data to file
    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)

    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)

    print("Item(s) added successfully to the blockchain.")


