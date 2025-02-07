def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

main_list = [1, 2, 3, 4]
item_to_insert = 5

manual_append(main_list, item_to_insert)
print(main_list)
