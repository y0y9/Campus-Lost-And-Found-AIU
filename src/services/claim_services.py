from data_structure.queue import Queue
from data_structure.linked_list import LinkedList
from models.claim import Claim
from models.item import Item
import random
from data_structure.bst import BinarySearchTree as BST
from datetime import datetime
from services.item_services import get_all_items, update_item_status, get_item

claim_queue = Queue()
claim_tree = BST(key_attr="claim_id")
claim_history = LinkedList()


'''
queue for requests, adding a claim request or remove
tree for searching about request
'''

def generate_claim_id():
    while True :
        claim_id = random.randint(100000,999999)
        if claim_tree.search(claim_id) is None:
            return claim_id

def create_claim(item_id, user_id, claim_date=None):
    
    if item_id is None or user_id is None:
        return None
    
    item = get_item(item_id)
    
    if item is None or item.status.casefold() != "stored":
        return None
    
    # TODO: Validate user using UserService // comment down 
    if claim_date is None:
        claim_date = datetime.now()
        
    claim_id = generate_claim_id()
    
    claim = Claim(
        claim_id=claim_id,
        item_id=item_id,
        user_id=user_id,
        claim_date=claim_date,
        status="pending"
    )
    
    inserted = claim_tree.insert(claim)
    if not inserted:
        return None
    claim_queue.enqueue(claim)
    add_history_event(
        claim_id,
        "claim_created",
        None,
        "pending",
        performed_by=user_id
    )
    return claim
    """
    create_claim function must ensure that the user/user_id  exist
    or else it returns None
    will be added after (user_service.py)
    """

def get_claim_by_id(claim_id : int):
    return claim_tree.search(claim_id)


def get_all_claims():
    claims = claim_tree.in_order()
    return claims

def get_claim_by_item(item_id):
    claims_results = LinkedList()
    all_claims = claim_tree.in_order()
    for claim in all_claims:
        if claim.item_id == item_id:
            claims_results.insert_end(claim)
    
    return claims_results

def get_claim_by_user(user_id):
    
    if user_id is None :
        return False
    
    all_claims = get_all_claims()
    claims = LinkedList()
    
    for claim in all_claims:
        if claim.user_id == user_id:
            claims.insert_end(claim)
    
    return claims


def process_next_claim(staff_id=None):
    claim = claim_queue.dequeue()
    if claim is None:
        return None
    
    old_status = claim.status
    claim.status = "under_review"
    
    add_history_event(
        claim.claim_id,
        "review_started",
        old_status,
        claim.status,
        performed_by=staff_id
    )
    return claim


def verify_claim(claim_id, staff_id=None):

    claim = get_claim_by_id(claim_id)
    
    if claim is None or claim.status != "under_review":
        return False
    item = get_item(claim.item_id)
    
    if item is None or item.status != "stored":
        return False
    
    old_claim_status = claim.status
    old_item_status = item.status
    
    success = update_item_status(item.item_id, "claimed")
    if not success:
        return False
    
    claim.status = "verified"
    
    add_history_event(
        claim_id,
        "claim_verified",
        old_claim_status,
        claim.status,
        performed_by=staff_id,
        item_old_status=old_item_status,
        item_new_status="claimed"
    )
    return True

def reject_claim(claim_id, staff_id=None , reason = None):
    claim = get_claim_by_id(claim_id)
    
    if claim is None or claim.status.lower() == "under_review":
        return False

    old_status = claim.status 
    claim.status  = "rejected"
    
    # add history event 
    add_history_event(
        claim_id,
        "claim_rejected",
        old_status,
        claim.status,
        performed_by=staff_id,
        details=reason
    )
    
    return True 

def add_history_event(claim_id, action, old_status=None, new_status=None, 
                    performed_by=None, details=None, item_old_status=None, item_new_status=None):
    
    claim = get_claim_by_id(claim_id=claim_id)
    
    if claim is None :
        return False 
    
    event = {
        "claim_id": claim_id,
        "item_id": claim.item_id,
        "action": action,
        "old_status": old_status,
        "new_status": new_status,
        "performed_by": performed_by,
        "timestamp": datetime.now(),
        "details": details,
        "item_old_status": item_old_status,
        "item_new_status": item_new_status
    }
    claim_history.insert_end(event)
    return True

def get_claim_by_history(claim_id):
    results = LinkedList()
    
    for event in claim_history:
        if event["claim_id"] == claim_id:
            results.insert_end(event)
    
    return results;

