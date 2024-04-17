import os
import struct
import uuid
from utils import *
from constant import *
from initialize import *

#show cases, show items, show history

def show_cases():
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    case_ids = set()
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, encrypted_case_id, _, _, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)
            if encrypted_case_id != b'0' * 32:
                decrypted_case_id = decrypt(encrypted_case_id)
                case_id = uuid.UUID(bytes=decrypted_case_id)
                case_ids.add(case_id)
            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    if len(case_ids) == 0:
        print("No cases found in the blockchain.")
    else:
        print("Cases in the blockchain:")
        for case_id in case_ids:
            print(case_id)

def show_items(case_id, password):
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    passwords = [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST"), get_password("EXECUTIVE"), get_password("CREATOR")]
    if password not in passwords:
        print("Invalid password")
        exit(1)

    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    case_id_bytes = uuid.UUID(case_id).bytes
    encrypted_case_id = encrypt(case_id_bytes)

    item_ids = []
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, block_encrypted_case_id, encrypted_item_id, _, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            if block_encrypted_case_id == encrypted_case_id:
                decrypted_item_id = decrypt(encrypted_item_id)
                item_id = int.from_bytes(decrypted_item_id, "little")
                item_ids.append(item_id)

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    if len(item_ids) == 0:
        print(f"No items found for case ID: {case_id}")
    else:
        print(f"Items for case ID: {case_id}")
        for item_id in item_ids:
            print(item_id)
