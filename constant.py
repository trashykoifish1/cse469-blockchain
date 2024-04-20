import os
# Constants
AES_KEY = b'R0chLi4uLi4uLi4='
STATE = {
    "init": b"INITIAL\0\0\0\0\0",
    "checkedin": b"CHECKEDIN\0\0\0",
    "checkedout": b"CHECKEDOUT\0\0"
}
DEL = {
    "disposed": b"DISPOSED\0\0\0\0",
    "destroyed": b"DESTROYED\0\0\0",
    "released": b"RELEASED\0\0\0\0"

}

blockchain_file = os.getenv('BCHOC_FILE_PATH')
