from Crypto.Cipher import AES
from constant import AES_KEY
import os
import datetime
import struct
import binascii
import uuid
import maya
from datetime import datetime, timezone, timedelta
from hashlib import sha256


def encrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    padded_data = data.ljust((len(data) + 15) // 16 * 16, b'\0')
    encrypted_data = cipher.encrypt(padded_data)
    return binascii.hexlify(encrypted_data)

def decrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    data = binascii.unhexlify(data)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data.rstrip(b'\0')

def get_password(role):
    return os.environ.get(f"BCHOC_PASSWORD_{role}", "")

def get_timestamp():
    return datetime.now().timestamp()

def get_string_timestamp(timestamp):
    display_time = maya.MayaDT.from_datetime(datetime.fromtimestamp(timestamp, tz=timezone.utc))
    display_time = display_time.iso8601()
    return display_time

def get_num_blocks(blockchain_file):
    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    num_blocks = 0
    offset = 0

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, _, _, _, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)
            block_size = 144 + data_length
            offset += block_size
            num_blocks += 1
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    return num_blocks

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

def get_block_from_item_id(blockchain_file, item_id):
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
                return struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    return None

def get_last_block_from_item_id(blockchain_file, item_id):
    try:
        with open(blockchain_file, 'rb') as file:
            blockchain_data = file.read()
    except FileNotFoundError:
        print(f"Error: Blockchain file '{blockchain_file}' not found.")
        exit(1)

    offset = 0
    last_block = None

    while offset < len(blockchain_data):
        try:
            block_header = blockchain_data[offset:offset+144]
            _, _, _, encrypted_item_id, _, _, _, data_length = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)
            decrypted_item_id = decrypt(encrypted_item_id)
            if int.from_bytes(decrypted_item_id, "little") == int(item_id):
                last_block = struct.unpack("32s d 32s 32s 12s 12s 12s I", block_header)

            block_size = 144 + data_length
            offset += block_size
        except struct.error:
            print("Error: Invalid block structure in the blockchain.")
            exit(1)

    return last_block


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

if __name__ == "__main__":
    # For testing purposes
    blockchain_file = os.getenv('BCHOC_FILE_PATH')
    data = uuid.UUID('119482d8-3fbf-4fa8-8948-d2f38d021ae4').bytes
    print(f"Original data : {data}")
    encrypted_data = encrypt(data)
    print(f"Encrypted data: {encrypted_data}")
    decrypted_data = decrypt(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")
    uuid_original = uuid.UUID(bytes=decrypted_data)
    print(f"Decrypted UUID: {uuid_original}")
    timestamp = get_timestamp()
    display_time = get_string_timestamp(timestamp)
    print(f"Current timestamp: {timestamp}")
    print(f"Display time: {display_time}")
    item_id = 1004820154
    encrypted_item_id = encrypt(struct.pack("I", item_id))
    decrypted_item_id = decrypt(encrypted_item_id)
    print(f"Item ID: {item_id}")
    print(f"Encrypted item ID: {encrypted_item_id}")
    print(f"Decrypted item ID: {int.from_bytes(decrypted_item_id, 'little')}")