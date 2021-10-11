def maximum(li):
    largest = li[0]
    for item in li[1:]:
        if largest < item:
            largest = item

    return largest


def minimum(li):
    smallest = li[0]
    for item in li[1:]:
        if smallest > item:
            smallest = item
    
    return smallest