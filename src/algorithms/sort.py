def merge_sort(items):

    if len(items) <= 1:
        return items
    
    mid_list = int(len(items)/2)
    left_side = items[0:mid_list]
    right_side = items[mid_list:len(items)]
    
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    
    return merge(left_side,right_side)
def merge(left,right):
    result = []
    i,j=0,0
    
    while i< len(left) and j < len(right):
        if left[i].date_found <= right[j].date_found:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result;




def merge_sort_category(items):
    if len(items) <= 1:
        return items

    mid = len(items)/ 2
    mid = int(mid)
    left = merge_sort_category(items[:mid])
    right = merge_sort_category(items[mid:])

    sorted_items = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i].category.casefold() <= right[j].category.casefold():
            sorted_items.append(left[i])
            i += 1
        else:
            sorted_items.append(right[j])
            j += 1

    while i < len(left):
        sorted_items.append(left[i])
        i += 1

    while j < len(right):
        sorted_items.append(right[j])
        j += 1

    return sorted_items
