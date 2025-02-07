def remove_one_element(my_list, index):
    if 0 <= index < len(my_list):
        my_list.pop(index)
    else:
        print("ინდექსი არასწორია.")
    
    print(my_list)

my_list = [1, 2, 3, 4, 5]
remove_one_element(my_list, 2)