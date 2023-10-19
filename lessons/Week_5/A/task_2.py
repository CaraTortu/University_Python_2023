
# A
def swap_first_last(l: list) -> list:
    l[0], l[-1] = l[-1], l[0]
    return l

# B 
def rotate_right(n: int, l: list) -> list:
     return l[-n:] + l[:-n]

# C 
def even_replace_with_0(l: list) -> list:
    return list(map(lambda x: x if x % 2 != 0 else 0, l))

# D
def replace_elements_by_largest_n(l: list) -> list:
    # Start list with the first item
    with_largest = [l[0]]

    # Add the maximum of the nodes besides it
    for i in range(1, len(l)-1):
        with_largest.append(max(l[i-1], l[i+1]))

    # Add the last item
    with_largest.append(l[-1])

    # return
    return with_largest

# E
def remove_middle_item(l: list) -> list:
    # remove middle item so now length is odd if it was even and viceversa
    l.pop(len(l)//2)
    
    # If its odd (previously even) delete another one
    if len(l) % 2 != 0:
        l.pop(len(l)//2)

    # Return the list
    return l


# F 
def move_even_to_front(l: list) -> list:
    sorted_list = [[], []]
    for i in range(len(l)):
        if l[i] % 2 == 0:
            sorted_list[0].append(l[i])
            continue

        sorted_list[1].append(l[i])

    return sorted_list[0] + sorted_list[1]

# G 
def second_largest(l: list) -> int:
    return sorted(l)[-2]

# H 
def is_sorted_asc(l: list) -> bool:
    return l == list(sorted(l))

# I 
def adjacent_duplicates(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] == l[i+1]:
            return True

    return False

# J 
def duplicates(l: list) -> bool:
    return adjacent_duplicates(list(sorted(l)))

