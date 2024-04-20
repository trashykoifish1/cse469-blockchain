from Crypto.Cipher import AES
import base64
import binascii

# Define the secret key and convert it from base64
AES_KEY = b'R0chLi4uLi4uLi4='

# Convert the integer to bytes
data = 2094523412
data_to_encrypt = data.to_bytes(4, 'big')

# Initialize AES cipher in ECB mode with the secret key
cipher = AES.new(AES_KEY, AES.MODE_ECB)

# Encrypt the data
encrypted_data = cipher.encrypt(data_to_encrypt)

# Convert encrypted bytes to hex representation
encrypted_hex = binascii.hexlify(encrypted_data).decode('utf-8')

print("Encrypted Hex:", encrypted_hex)
