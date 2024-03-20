import os
import struct
import time
import uuid
from Crypto.Cipher import AES
from utils import encrypt_aes_ecb, decrypt_aes_ecb
from initialize import initialize
from add_block import add_block



def add(case_id, item_id, creator, password):
    """
    Add a new item to the blockchain.

    Args:
    - case_id: Case identifier (UUID) associated with the item.
    - item_id: Evidence item identifier (integer) associated with the item.
    - creator: Creator of the item.
    - password: Password for blockchain operations.

    Returns:
    - Success message if item added successfully, error message otherwise.
    """
    add_block(case_id, item_id, creator, password)


def checkout(item_id, password):
    """
    Checkout an item from the blockchain.
    """
    pass

def checkin(item_id, password):
    """
    Checkin an item to the blockchain.
    """
    pass

def show_cases(password):
    """
    Show all cases in the blockchain.
    """
    pass

def show_items(case_id, password):
    """
    Show all items in a case in the blockchain.
    """
    pass

def show_history(case_id, item_id, num_entries, reverse, password):
    """
    Show the history of a case or an item in the blockchain.
    """
    pass

def remove(item_id, reason, password):
    """
    Remove an item from the blockchain.
    """
    pass

def init():
    """
    Initialize the blockchain.

    Returns:
    - Success message if initialization is successful, error message otherwise.
    """
    initialize()

def verify():
    """
    Verify the integrity of the blockchain.
    """
    pass