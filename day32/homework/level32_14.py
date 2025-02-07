def insert_at_beginning(my_list, item):
    my_list.insert(0, item)
    return my_list

my_list = [2, 3, 4]
item = 1
print(insert_at_beginning(my_list, item))
