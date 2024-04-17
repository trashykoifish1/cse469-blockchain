### DON'T USE THIS FILE, USE THIS FOR REFERENCE ONLY ###


import os
import sys
import struct
import uuid
import hashlib
import datetime
import base64
from Crypto.Cipher import AES

# Constants
INITIAL_BLOCK = {
    "Prev_hash": b"\0" * 32,
    "Timestamp": 0,
    "Case_id": b"0" * 32,
    "Evidence_id": b"0" * 32,
    "State": b"INITIAL\0\0\0\0",
    "Creator": b"\0" * 12,
    "Owner": b"\0" * 12,
    "D_length": 14,
    "Data": b"Initial block\0"
}

STATE = {
    "init": b"INITIAL\0\0\0\0",
    "checkedin": b"CHECKEDIN\0\0",
    "checkedout": b"CHECKEDOUT\0"
}

# AES key
AES_KEY = b"R0chLi4uLi4uLi4="

# Block structure format string
BLOCK_FORMAT = "32s d 32s 32s 12s 12s 12s I"

# Get the blockchain file path from the environment variable
BLOCKCHAIN_FILE = os.environ.get("BCHOC_FILE_PATH", "blockchain.dat")

def encrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    padded_data = data.ljust((len(data) + 15) // 16 * 16, b'\0')
    return cipher.encrypt(padded_data)

def decrypt(data):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data.rstrip(b'\0')

def get_timestamp():
    return datetime.datetime.now(datetime.timezone.utc)

def pack_block(block):
    return struct.pack(BLOCK_FORMAT,
                       block["Prev_hash"],
                       block["Timestamp"],
                       block["Case_id"],
                       block["Evidence_id"],
                       block["State"],
                       block["Creator"],
                       block["Owner"],
                       block["D_length"]) + block["Data"]

def unpack_block(packed_block):
    unpacked_data = struct.unpack(BLOCK_FORMAT, packed_block[:struct.calcsize(BLOCK_FORMAT)])
    return {
        "Prev_hash": unpacked_data[0],
        "Timestamp": unpacked_data[1],
        "Case_id": unpacked_data[2],
        "Evidence_id": unpacked_data[3],
        "State": unpacked_data[4],
        "Creator": unpacked_data[5],
        "Owner": unpacked_data[6],
        "D_length": unpacked_data[7],
        "Data": packed_block[struct.calcsize(BLOCK_FORMAT):]
    }

def get_password(role):
    return os.environ.get(f"BCHOC_PASSWORD_{role}", "")

def add_evidence(case_id, item_ids, creator, password):
    if password != get_password("CREATOR"):
        print("Invalid password")
        sys.exit(1)

    for item_id in item_ids:
        print(case_id.encode())
        block = {
            "Prev_hash": b"\0" * 32,
            "Timestamp": get_timestamp().timestamp(),
            "Case_id": encrypt(case_id.encode()),
            "Evidence_id": encrypt(struct.pack("I", item_id)),
            "State": STATE["checkedin"],
            "Creator": creator.encode(),
            "Owner": b"\0" * 12,
            "D_length": 0,
            "Data": b""
        }

        with open(BLOCKCHAIN_FILE, "ab") as f:
            packed_block = pack_block(block)
            block["Prev_hash"] = hashlib.sha256(packed_block).digest()
            f.write(pack_block(block))

        print(f"Added item: {item_id}")
        print(f"Status: CHECKEDIN")
        print(f"Time of action: {datetime.datetime.fromtimestamp(block['Timestamp'], tz=datetime.timezone.utc)}")

def checkout_evidence(item_id, password):
    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if decrypt(block["Evidence_id"]) == struct.pack("I", item_id):
                if block["State"] != STATE["checkedin"]:
                    print("Item is not checked in")
                    sys.exit(1)

                if password not in [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST")]:
                    print("Invalid password")
                    sys.exit(1)

                block["State"] = STATE["checkedout"]
                block["Timestamp"] = get_timestamp().timestamp()
                block["Owner"] = password.encode()

                with open(BLOCKCHAIN_FILE, "r+b") as f:
                    f.seek(-struct.calcsize(BLOCK_FORMAT) - block["D_length"], os.SEEK_END)
                    packed_block = pack_block(block)
                    block["Prev_hash"] = hashlib.sha256(packed_block).digest()
                    f.write(pack_block(block))

                print(f"Case: {uuid.UUID(bytes=decrypt(block['Case_id']))}")
                print(f"Checked out item: {item_id}")
                print(f"Status: CHECKEDOUT")
                print(f"Time of action: {datetime.datetime.fromtimestamp(block['Timestamp'], tz=datetime.timezone.utc)}")
                return

    print("Item not found")
    sys.exit(1)

def checkin_evidence(item_id, password):
    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if decrypt(block["Evidence_id"]) == struct.pack("I", item_id):
                if block["State"] != STATE["checkedout"]:
                    print("Item is not checked out")
                    sys.exit(1)

                if password not in [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST")]:
                    print("Invalid password")
                    sys.exit(1)

                block["State"] = STATE["checkedin"]
                block["Timestamp"] = get_timestamp().timestamp()
                block["Owner"] = b"\0" * 12

                with open(BLOCKCHAIN_FILE, "r+b") as f:
                    f.seek(-struct.calcsize(BLOCK_FORMAT) - block["D_length"], os.SEEK_END)
                    packed_block = pack_block(block)
                    block["Prev_hash"] = hashlib.sha256(packed_block).digest()
                    f.write(pack_block(block))

                print(f"Case: {uuid.UUID(bytes=decrypt(block['Case_id']))}")
                print(f"Checked in item: {item_id}")
                print(f"Status: CHECKEDIN")
                print(f"Time of action: {datetime.datetime.fromtimestamp(block['Timestamp'], tz=datetime.timezone.utc)}")
                return

    print("Item not found")
    sys.exit(1)

def show_cases(password):
    if password != get_password("EXECUTIVE"):
        print("Invalid password")
        sys.exit(1)

    cases = set()
    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            cases.add(uuid.UUID(bytes=decrypt(block["Case_id"])))

    for case in cases:
        print(case)

def show_items(case_id, password):
    if password != get_password("EXECUTIVE"):
        print("Invalid password")
        sys.exit(1)

    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if uuid.UUID(bytes=decrypt(block["Case_id"])) == case_id:
                print(struct.unpack("I", decrypt(block["Evidence_id"]))[0])

def show_history(case_id=None, item_id=None, num_entries=None, reverse=False, password=None):
    if password not in [get_password("POLICE"), get_password("LAWYER"), get_password("ANALYST")]:
        print("Invalid password")
        sys.exit(1)

    history = []
    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if (case_id is None or uuid.UUID(bytes=decrypt(block["Case_id"])) == case_id) and \
               (item_id is None or struct.unpack("I", decrypt(block["Evidence_id"]))[0] == item_id):
                history.append(block)

    if reverse:
        history.reverse()

    if num_entries is not None:
        history = history[:num_entries]

    for block in history:
        print(f"Case: {uuid.UUID(bytes=decrypt(block['Case_id']))}")
        print(f"Item: {base64.b64encode(decrypt(block['Evidence_id'])).decode()}")
        print('Action: {}'.format(block['State'].rstrip(b'\0').decode()))
        print(f"Time: {datetime.datetime.fromtimestamp(block['Timestamp'], tz=datetime.timezone.utc)}")
        print()

def remove_evidence(item_id, reason, owner=None, password=None):
    if password != get_password("CREATOR"):
        print("Invalid password")
        sys.exit(1)

    if reason not in ["DISPOSED", "DESTROYED", "RELEASED"]:
        print("Invalid reason")
        sys.exit(1)

    if reason == "RELEASED" and owner is None:
        print("Owner information is required for RELEASED reason")
        sys.exit(1)

    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if decrypt(block["Evidence_id"]) == struct.pack("I", item_id):
                if block["State"] != STATE["checkedin"]:
                    print("Item is not checked in")
                    sys.exit(1)

                block["State"] = reason.encode() + b"\0" * (12 - len(reason))
                block["Timestamp"] = get_timestamp().timestamp()
                block["Owner"] = owner.encode() if owner else b"\0" * 12

                with open(BLOCKCHAIN_FILE, "r+b") as f:
                    f.seek(-struct.calcsize(BLOCK_FORMAT) - block["D_length"], os.SEEK_END)
                    packed_block = pack_block(block)
                    block["Prev_hash"] = hashlib.sha256(packed_block).digest()
                    f.write(pack_block(block))

                print(f"Removed item: {item_id}")
                print(f"Reason: {reason}")
                if owner:
                    print(f"Owner: {owner}")
                print(f"Time of action: {datetime.datetime.fromtimestamp(block['Timestamp'], tz=datetime.timezone.utc)}")
                return

    print("Item not found")
    sys.exit(1)

def init_blockchain():
    if not os.path.exists(BLOCKCHAIN_FILE):
        print(BLOCKCHAIN_FILE)
        with open(BLOCKCHAIN_FILE, "wb") as f:
            packed_block = pack_block(INITIAL_BLOCK)
            f.write(packed_block)
        print("Blockchain file not found. Created INITIAL block.")
    else:
        with open(BLOCKCHAIN_FILE, "rb") as f:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if block == INITIAL_BLOCK:
                print("Blockchain file found with INITIAL block.")
            else:
                print("Blockchain file found with INITIAL block.")
                sys.exit(1)

def verify_blockchain():
    prev_hash = b"\0" * 32
    transaction_count = 0
    state = "CLEAN"
    bad_block = None
    parent_block = None
    double_checked = set()

    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            transaction_count += 1

            if block["Prev_hash"] != prev_hash:
                state = "ERROR"
                bad_block = base64.b64encode(hashlib.sha256(pack_block(block)).digest()).decode()
                parent_block = base64.b64encode(prev_hash).decode()
                break

            if transaction_count > 1:
                evidence_id = decrypt(block["Evidence_id"])
                if evidence_id in double_checked:
                    state = "ERROR"
                    bad_block = base64.b64encode(hashlib.sha256(pack_block(block)).digest()).decode()
                    break
                double_checked.add(evidence_id)

                if block["State"] in [STATE["checkedout"], STATE["checkedin"]] and any(
                    b["State"].startswith(b"DISPOSED") or b["State"].startswith(b"DESTROYED") or b["State"].startswith(b"RELEASED")
                    for b in get_evidence_history(evidence_id)
                ):
                    state = "ERROR"
                    bad_block = base64.b64encode(hashlib.sha256(pack_block(block)).digest()).decode()
                    break

            if hashlib.sha256(pack_block(block)).digest() != block["Prev_hash"]:
                state = "ERROR"
                bad_block = base64.b64encode(hashlib.sha256(pack_block(block)).digest()).decode()
                break

            prev_hash = hashlib.sha256(pack_block(block)).digest()

    print(f"Transactions in blockchain: {transaction_count}")
    print(f"State of blockchain: {state}")
    if state == "ERROR":
        print(f"Bad block: {bad_block}")
        if parent_block:
            print(f"Parent block: {parent_block}")
        else:
            print("Parent block: NOT FOUND")

def get_evidence_history(evidence_id):
    history = []
    with open(BLOCKCHAIN_FILE, "rb") as f:
        while True:
            block_data = f.read(struct.calcsize(BLOCK_FORMAT))
            if not block_data:
                break

            block = unpack_block(block_data + f.read(struct.unpack("I", block_data[-4:])[0]))
            if decrypt(block["Evidence_id"]) == evidence_id:
                history.append(block)
    return history

def main():
    if len(sys.argv) < 2:
        print("Usage: python bchoc.py <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init_blockchain()
    elif command == "add":
        case_id = None
        item_ids = []
        creator = None
        password = None
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-c":
                case_id = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "-i":
                item_ids.append(int(sys.argv[i + 1]))
                i += 2
            elif sys.argv[i] == "-g":
                creator = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "-p":
                password = sys.argv[i + 1]
                i += 2
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)
        if case_id is None or not item_ids or creator is None or password is None:
            print("Missing required options for add command")
            sys.exit(1)
        add_evidence(case_id, item_ids, creator, password)
    elif command == "checkout":
        item_id = None
        password = None
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-i":
                item_id = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "-p":
                password = sys.argv[i + 1]
                i += 2
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)
        if item_id is None or password is None:
            print("Missing required options for checkout command")
            sys.exit(1)
        checkout_evidence(item_id, password)
    elif command == "checkin":
        item_id = None
        password = None
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-i":
                item_id = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "-p":
                password = sys.argv[i + 1]
                i += 2
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)
        if item_id is None or password is None:
            print("Missing required options for checkin command")
            sys.exit(1)
        checkin_evidence(item_id, password)
    elif command == "show":
        subcommand = sys.argv[2]
        if subcommand == "cases":
            password = None
            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == "-p":
                    password = sys.argv[i + 1]
                    i += 2
                else:
                    print("Invalid option: {}".format(sys.argv[i]))
                    sys.exit(1)
            if password is None:
                print("Missing required options for show cases command")
                sys.exit(1)
            show_cases(password)
        elif subcommand == "items":
            case_id = None
            password = None
            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == "-c":
                    case_id = uuid.UUID(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == "-p":
                    password = sys.argv[i + 1]
                    i += 2
                else:
                    print("Invalid option: {}".format(sys.argv[i]))
                    sys.exit(1)
            if case_id is None or password is None:
                print("Missing required options for show items command")
                sys.exit(1)
            show_items(case_id, password)
        elif subcommand == "history":
            case_id = None
            item_id = None
            num_entries = None
            reverse = False
            password = None
            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == "-c":
                    case_id = uuid.UUID(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == "-i":
                    item_id = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == "-n":
                    num_entries = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == "-r":
                    reverse = True
                    i += 1
                elif sys.argv[i] == "-p":
                    password = sys.argv[i + 1]
                    i += 2
                else:
                    print("Invalid option: {}".format(sys.argv[i]))
                    sys.exit(1)
            if password is None:
                print("Missing required options for show history command")
                sys.exit(1)
            show_history(case_id, item_id, num_entries, reverse, password)
    elif command == "remove":
        item_id = None
        reason = None
        owner = None
        password = None
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-i":
                item_id = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] in ["-y", "--why"]:
                reason = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "-o":
                owner = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "-p":
                password = sys.argv[i + 1]
                i += 2
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)
        if item_id is None or reason is None or password is None:
            print("Missing required options for remove command")
            sys.exit(1)
        remove_evidence(item_id, reason, owner, password)
    elif command == "verify":
        verify_blockchain()
    else:
        print("Invalid command: {}".format(command))
        sys.exit(1)

if __name__ == "__main__":
    main()