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
        for case_id in case_ids:
            print(case_id)

def show_items(case_id):
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    # passwords = [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST"), get_password("EXECUTIVE"), get_password("CREATOR")]
    # if password not in passwords:
    #     print("Invalid password")
    #     exit(1)

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
                if item_id not in item_ids:
                    item_ids.append(item_id)

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    if len(item_ids) == 0:
        print(f"No items found for case ID: {case_id}")
    else:
        for item_id in item_ids:
            print(item_id)


def show_history(case_id, item_id, num_entries, reverse, password):
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

    if case_id:
        case_id_int = uuid.UUID(case_id).int
        case_id_bytes = case_id_int.to_bytes((case_id_int.bit_length() + 7) // 8, 'big')
        encrypted_case_id = encrypt(case_id_bytes)
    else:
        encrypted_case_id = None

    if item_id:
        encrypted_item_id = encrypt(struct.pack("I", int(item_id)))
    else:
        encrypted_item_id = None

    blocks = []
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, timestamp, block_encrypted_case_id, block_encrypted_item_id, state, creator, owner, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            if (encrypted_case_id is None or block_encrypted_case_id == encrypted_case_id) and \
               (encrypted_item_id is None or block_encrypted_item_id == encrypted_item_id):
                if state != STATE['init']:
                    decrypted_case_id = decrypt(block_encrypted_case_id)
                    decrypted_item_id = decrypt(block_encrypted_item_id)
                    case_id = uuid.UUID(bytes=decrypted_case_id)
                    item_id = int.from_bytes(decrypted_item_id, "little")
                else:
                    case_id = '00000000-0000-0000-0000-000000000000'
                    item_id = '0'
                blocks.append((case_id, item_id, state.decode().strip('\0'), timestamp, creator.decode().strip('\0'), owner.decode().strip('\0')))

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    if reverse:
        blocks.reverse()

    if num_entries is not None:
        blocks = blocks[:num_entries]

    if len(blocks) != 0:
        for block in blocks:
            case_id, item_id, state, timestamp, creator, owner = block
            print(f"Case: {case_id}")
            print(f"Item: {item_id}")
            print(f"Action: {state}")
            print(f"Time: {get_string_timestamp(timestamp)}")
            print()

