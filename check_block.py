"""
Checkin/checkout functions
"""

import os
import struct
import uuid
from hashlib import sha256
from datetime import datetime
from utils import *
from constant import *
from initialize import *

#TODO: checkin, checkout is finished for now, move on to show_cases

def checkin(item_id, password):
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    passwords = [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST"), get_password("EXECUTIVE"), get_password("CREATOR")]
    if password not in passwords:
        print("Invalid password")
        exit(1)
    if not check_initial_block():
        # Initialize blockchain
        initialize()
    
    if not check_item_exists(blockchain_file, item_id):
        print(f"Error: Item ID {item_id} does not exist in the blockchain.")
        exit(1)
    else:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
        _, _, encrypted_case_id, encrypted_item_id, state, creator, owner, data_length = get_last_block_from_item_id(blockchain_file, item_id)
        item_id = decrypt(encrypted_item_id)
        item_id = int.from_bytes(item_id, "little")
        case_id = decrypt(encrypted_case_id)
        case_id = uuid.UUID(bytes=case_id)
        if state == STATE["checkedin"]:
            print(f"Error: Item ID {item_id} is already checked in.")
            exit(1)
        else:
            previous_hash = calculate_hash(blockchain_data)
            timestamp = get_timestamp()
            state = STATE["checkedin"]
            data_length = len(f'Item ID: {item_id}')
            data = f'Item ID: {item_id}'
            packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id,encrypted_item_id, state, creator, owner, data_length) + data.encode()
            blockchain_data += packed_block
            print(f"Case: {case_id}")
            print(f"Checked in item: {item_id}")
            print(f"Status: CHECKEDIN")
            print(f"Time of action: {get_string_timestamp(timestamp)}")
                # Write updated blockchain data to file
    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)

    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)

def checkout(item_id, password):
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    passwords = [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST"), get_password("EXECUTIVE"), get_password("CREATOR")]
    if password not in passwords:
        print("Invalid password")
        exit(1)
    if not check_initial_block():
        # Initialize blockchain
        initialize()
    
    if not check_item_exists(blockchain_file, item_id):
        print(f"Error: Item ID {item_id} does not exist in the blockchain.")
        exit(1)
    else:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
        _, _, encrypted_case_id, encrypted_item_id, state, creator, owner, data_length = get_last_block_from_item_id(blockchain_file, item_id)
        item_id = decrypt(encrypted_item_id)
        item_id = int.from_bytes(item_id, "little")
        case_id = decrypt(encrypted_case_id)
        case_id = uuid.UUID(bytes=case_id)
        if state == STATE["checkedout"]:
            print(f"Error: Item ID {item_id} is already checked out.")
            exit(1)
        else:
            previous_hash = calculate_hash(blockchain_data)
            timestamp = get_timestamp()
            state = STATE["checkedout"]
            data_length = len(f'Item ID: {item_id}')
            data = f'Item ID: {item_id}'
            packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id,encrypted_item_id, state, creator, owner, data_length) + data.encode()
            blockchain_data += packed_block
            print(f"Case: {case_id}")
            print(f"Checked out item: {item_id}")
            print(f"Status: CHECKEDOUT")
            print(f"Time of action: {get_string_timestamp(timestamp)}")
    # Write updated blockchain data to file
    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)

    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)


if __name__ == "__main__":
    checkout(1004820154, "P80P")
    checkin(1004820154, "P80P")