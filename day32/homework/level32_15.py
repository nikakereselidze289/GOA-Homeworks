def insert_at_end(my_list, item):
    my_list.insert(len(my_list), item)
    return my_list

my_list = [1, 2, 3]
item = 4
print(insert_at_end(my_list, item))
