
from data_structure import *
from data_structure.bst import BinarySearchTree as BST
from models.item import Item
from datetime import datetime as dt 
import random
from algorithms.sort import *

items_tree = BST()


def random_id_generator(items_tree):
    while True:
        id = random.randint(100000, 999999)
        if items_tree.search(id) is None:
            return id


def add_item(description , category , status , location_found , date_found=None):
    if date_found == None :
        date_found = dt.now()
    
    id = random_id_generator(items_tree)
    item = Item(item_id=id,description=description,
                category=category, location_found=location_found ,
                date_found=date_found, status=status)
    items_tree.insert(item)
    return item


def get_item(item_id):
    item = items_tree.search(item_id=item_id)
    if item == None :
        return None
    return item


def delete_item(item_id):
    return items_tree.delete(item_id=item_id)


def get_all_items():
    all_items = items_tree.in_order()
    return all_items


# def get_items_by_date():
#     all_items = get_all_items()
#     all_items_sorted = merge_sort(all_items)
#     return all_items_sorted


def update_item_status(item_id,new_status):
    new_status = str(new_status).casefold()
    item: Item = get_item(item_id)
    if item is None or (new_status != "stored" and new_status != "claimed" and new_status != "disposed"):
        return False
    
    if new_status == "stored" or new_status == "claimed" or new_status == "disposed":
        item.status = new_status
        return True


def get_items_by_category(category):
    items_list = []
    category = category.casefold()
    all_items = items_tree.in_order()
    for item in all_items:
        if item.category.casefold() == category:
            items_list.append(item)
        else : 
            continue
    return items_list


def get_items_by_location(location:str):
    location = location.lower() 
    items_list = []
    all_items = items_tree.in_order()
    for item in all_items:
        if item.location_found.lower() == location :
            items_list.append(item)
        else:
            continue
    return items_list

def get_items_by_date(start_date=None, end_date=None):
    
    if start_date == None or end_date ==None:
        return None
    all_items = get_all_items()
    
    if start_date is None and end_date is None:
        return merge_sort(all_items)
    items_list = []
    for item in all_items:
        if start_date <= item.date_found <= end_date:
            items_list.append(item)
        else:
            continue
    return items_list


def get_items_by_description(keyword:str):
    all_items = items_tree.in_order()
    items = []
    for item in all_items:
        if keyword.lower() in item.description.lower():
            items.append(item)
    return items


def get_unresolved_items_sorted_by_category():
    all_items = get_all_items()

    items = []
    for item in all_items:
        if item.status == "stored":
            items.append(item)

    return merge_sort_category(items)
