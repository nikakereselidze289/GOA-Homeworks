def append_multiple_to_list(my_list, items):
    my_list.extend(items)
    return my_list

my_list = [1, 2, 3]
items = [4, 5, 6]
print(append_multiple_to_list(my_list, items))
