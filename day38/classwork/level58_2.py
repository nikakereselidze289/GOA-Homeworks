def no_duplicates(user_list):
    return list(set(user_list))

print(no_duplicates([1, 2, 3, 4, 4, 5, 6, 6]))
print(no_duplicates(['apple', 'banana', 'apple', 'orange', 'banana']))
print(no_duplicates([True, False, True, True, False]))
