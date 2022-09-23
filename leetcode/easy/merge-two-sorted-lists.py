
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. 
# The list should be made by splicing together 
# the nodes of the first two lists.

# Return the head of the merged linked list.

# Example

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def megre_sorted_lists(list1: list, list2: list):
    merged_list = []
    i = j = 0

    while True:
        if not list1:
            merged_list += list2
            break

        elif not list2:
            merged_list += list2
            break

        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))

    return merged_list


from random import random


list1 = sorted([round(random(), 2) for _ in range(15)])
list2 = sorted([round(random(), 2) for _ in range(15)])


print(megre_sorted_lists(list1, list2))
