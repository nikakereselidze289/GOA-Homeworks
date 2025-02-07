def manual_len(my_list):
    length = 0
    for _ in my_list:
        length += 1
    return length

my_list = [1, 2, 3, 4, 5]
print(manual_len(my_list))
