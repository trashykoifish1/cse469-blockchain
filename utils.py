from Crypto.Cipher import AES


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