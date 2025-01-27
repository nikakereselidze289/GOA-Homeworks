def append_all_elements(list1, list2):
    list1.extend(list2)
    return list1

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(append_all_elements(list1, list2))
