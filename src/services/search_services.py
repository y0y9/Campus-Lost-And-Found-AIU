from services import item_services
from data_structure.linked_list import LinkedList
from algorithms.sort import merge_sort, merge_sort_category


def search_item(
    item_id=None,
    description=None,
    category=None,
    date_found=None,
    location_found=None,
    status=None
):

    results = LinkedList()

    # Get all items initially
    all_items = item_services.get_all_items()

    # Use ItemService search methods
    if item_id is not None:
        item = item_services.get_item(item_id)

        if item is None:
            return results

        all_items = [item]

    if description is not None:
        matches = item_services.get_items_by_description(description)
        matching_ids = {item.item_id for item in matches}

        all_items = [
            item for item in all_items
            if item.item_id in matching_ids
        ]

    if category is not None:
        matches = item_services.get_items_by_category(category)
        matching_ids = {item.item_id for item in matches}

        all_items = [
            item for item in all_items
            if item.item_id in matching_ids
        ]

    if location_found is not None:
        matches = item_services.get_items_by_location(location_found)
        matching_ids = {item.item_id for item in matches}

        all_items = [
            item for item in all_items
            if item.item_id in matching_ids
        ]

    if date_found is not None:
        matches = item_services.get_items_by_date(
            start_date=date_found,
            end_date=date_found
        )

        matching_ids = {item.item_id for item in (matches or [])}

        all_items = [
            item for item in all_items
            if item.item_id in matching_ids
        ]

    if status is not None:
        all_items = [
            item for item in all_items
            if item.status.casefold() == status.casefold()
        ]

    for item in all_items:
        results.insert_end(item)

    return results


def find_possible_items():
    raise NotImplementedError(
        "To be implemented by the team leader"
    )


def get_unresolved():

    result = LinkedList()

    all_items = item_services.get_all_items()

    for item in all_items:
        if item.status.casefold() == "stored":
            result.insert_end(item)

    return result


def get_unresolved_by_date():

    result = LinkedList()

    all_items = item_services.get_all_items()

    unresolved = []

    for item in all_items:
        if item.status.casefold() == "stored":
            unresolved.append(item)

    sorted_items = merge_sort(unresolved)

    for item in sorted_items:
        result.insert_end(item)

    return result


def get_unresolved_by_category():

    result = LinkedList()

    all_items = item_services.get_all_items()

    unresolved = []

    for item in all_items:
        if item.status.casefold() == "stored":
            unresolved.append(item)

    sorted_items = merge_sort_category(unresolved)

    for item in sorted_items:
        result.insert_end(item)

    return result