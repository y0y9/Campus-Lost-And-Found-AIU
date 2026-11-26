from services import item_services
from data_structure.linked_list import LinkedList
from algorithms.sort import merge_sort, merge_sort_category


def to_linked_list(items):
    result = LinkedList()
    for item in items:
        result.insert_end(item)
    return result

def search_item(
    item_id=None,
    description=None,
    category=None,
    date_found=None,
    location_found=None,
    status=None
):

    results = item_services.get_all_items()
    if item_id is not None:
        item = item_services.get_item(item_id)
        if item is None:
            return LinkedList()
        results = [item]

    if description is not None:
        matches = item_services.get_items_by_description(description)
        matching_ids = {item.item_id for item in matches}
        results = [
            item for item in results
            if item.item_id in matching_ids
        ]

    if category is not None:
        matches = item_services.get_items_by_category(category)
        matching_ids = {item.item_id for item in matches}
        results = [
            item for item in results
            if item.item_id in matching_ids
        ]

    if location_found is not None:
        matches = item_services.get_items_by_location(location_found)
        matching_ids = {item.item_id for item in matches}
        results = [
            item for item in results
            if item.item_id in matching_ids
        ]

    if date_found is not None:
        matches = item_services.get_items_by_date(
            start_date=date_found,
            end_date=date_found
        )
        matching_ids = {item.item_id for item in (matches or [])}
        results = [
            item for item in results
            if item.item_id in matching_ids
        ]
    if status is not None:
        results = [
            item for item in results
            if item.status.casefold() == status.casefold()
        ]

    return to_linked_list(results)


def find_possible_items():
    raise NotImplementedError(
        
    )


def get_unresolved():
    all_items = item_services.get_all_items()
    unresolved = [
        item for item in all_items
        if item.status.casefold() == "stored"
    ]
    return to_linked_list(unresolved)


def get_unresolved_by_date():

    all_items = item_services.get_all_items()
    unresolved = [
        item for item in all_items
        if item.status.casefold() == "stored"
    ]

    sorted_items = merge_sort(unresolved)
    return to_linked_list(sorted_items)

def get_unresolved_by_category():
    
    all_items = item_services.get_all_items()
    unresolved = [
        item for item in all_items
        if item.status.casefold() == "stored"
    ]
    sorted_items = merge_sort_category(unresolved)
    return to_linked_list(sorted_items)