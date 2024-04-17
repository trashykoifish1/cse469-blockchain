import os
# Constants
AES_KEY = b'R0chLi4uLi4uLi4='
STATE = {
    "init": b"INITIAL\0\0\0\0\0",
    "checkedin": b"CHECKEDIN\0\0\0",
    "checkedout": b"CHECKEDOUT\0\0"
}

blockchain_file = os.getenv('BCHOC_FILE_PATH')
