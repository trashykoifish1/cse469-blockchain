from Crypto.Cipher import AES
from constant import AES_KEY
import os
import datetime
import struct

def encrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    padded_data = data.ljust((len(data) + 15) // 16 * 16, b'\0')
    return cipher.encrypt(padded_data)

def decrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    data = data.strip(b'\0')
    decrypted_data = cipher.decrypt(data)
    return decrypted_data.rstrip(b'\0')

def get_password(role):
    return os.environ.get(f"BCHOC_PASSWORD_{role}", "")

def get_timestamp():
    return datetime.datetime.now(datetime.timezone.utc)

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

if __name__ == "__main__":
    dec_1 = decrypt(b"3\xb0\xd5o9)u\x81\xbb9\xec&\x84S$\xf1")
    dec_2 = decrypt(b'3\xb0\xd5o9)u\x81\xbb9\xec&\x84S$\xf1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    print(int.from_bytes(dec_1, byteorder='little'))
    print(int.from_bytes(dec_2, byteorder='little'))


def encrypt_aes_ecb(data, key):
    """
    Encrypt data using AES ECB mode.

    Args:
    - data: Data to be encrypted.
    - key: AES key for encryption.

    Returns:
    - Encrypted data.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(data.ljust(16, b'\0'))  # AES requires data to be 16 bytes
    return encrypted_data

def decrypt_aes_ecb(encrypted_data, key):
    """
    Decrypt data encrypted with AES ECB mode.

    Args:
    - encrypted_data: Data encrypted with AES ECB.
    - key: AES key used for encryption.

    Returns:
    - Decrypted data.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b'\0')
    return decrypted_data