import os
import struct
from utils import *
from constant import *
from initialize import *

def remove(item_id, reason, password):
    blockchain_file = os.getenv('BCHOC_FILE_PATH')

    if password != get_password("CREATOR"):
        print("Invalid password")
        exit(1)

    if reason not in ["DISPOSED", "DESTROYED", "RELEASED"]:
        print("Invalid reason. Reason must be one of: DISPOSED, DESTROYED, or RELEASED.")
        exit(1)


    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    encrypted_item_id = encrypt(struct.pack("I", int(item_id)))
    last_block = None
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, _, block_encrypted_item_id, state, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            if block_encrypted_item_id == encrypted_item_id:
                last_block = blockchain_data[offset:offset+144+data_length]

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    if last_block is None:
        print(f"Error: Item ID {item_id} not found in the blockchain.")
        exit(1)

    _, _, _, _, state, _, _, _ = struct.unpack("32s d 32s 32s 12s 12s 12s I", last_block[:144])
    state = state.decode().strip('\0')

    if state != "CHECKEDIN":
        print(f"Error: Item ID {item_id} is not in the CHECKEDIN state.")
        exit(1)

    previous_hash = calculate_hash(last_block)
    timestamp = get_timestamp()
    encrypted_case_id = last_block[40:72]
    state = reason.ljust(12, '\0').encode()
    creator = last_block[112:124]
    owner = last_block[124:136]
    data_length = 0
    data = ''
    packed_block = struct.pack("32s d 32s 32s 12s 12s 12s I", previous_hash, timestamp, encrypted_case_id, encrypted_item_id, state, creator, owner, data_length) + data.encode()

    blockchain_data += packed_block

    try:
        with open(blockchain_file, 'wb') as file:
            file.write(blockchain_data)
    except Exception as e:
        print(f"Error: Failed to write blockchain file - {str(e)}")
        exit(1)

    print(f"Item ID {item_id} removed from the blockchain.")
    print(f"Reason: {reason}")