def insert_at_index(my_list, index, item):
    my_list.insert(index, item)
    return my_list

my_list = [1, 2, 3]
index = 1
item = 4
print(insert_at_index(my_list, index, item))
