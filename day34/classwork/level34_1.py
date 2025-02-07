def manual_remove(main_list, indexes_list):
    indexes_list.sort(reverse=True)
    
    for index in indexes_list:
        if 0 <= index < len(main_list):
            del main_list[index]
    
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]

print(manual_remove(main_list, indexes_list))
