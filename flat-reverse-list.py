l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(l):
    flattened = []
    for item in l:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

print(flatten_list(l))


l2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(l2):
    reversed_list = []
    for item in l2[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

print(reverse_list(l2))