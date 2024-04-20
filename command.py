from constant import *
from utils import *
from initialize import *
from add_block import *
import check_block
import show_block
import remove_block
import verify_block


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
    check_block.checkout(item_id, password)

def checkin(item_id, password):
    """
    Checkin an item to the blockchain.
    """
    check_block.checkin(item_id, password)

def show_cases():
    """
    Show all cases in the blockchain.
    """
    show_block.show_cases()

def show_items(case_id):
    """
    Show all items in a case in the blockchain.
    """
    show_block.show_items(case_id)

def show_history(case_id, item_id, num_entries, reverse, password):
    """
    Show the history of a case or an item in the blockchain.
    """
    show_block.show_history(case_id, item_id, num_entries, reverse, password)

def remove(item_id, reason, password):
    """
    Remove an item from the blockchain.
    """
    remove_block.remove(item_id, reason, password)

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
    verify_block.verify()