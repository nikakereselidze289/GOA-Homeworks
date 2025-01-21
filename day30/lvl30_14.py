def get_lengths(string_list):
    return [len(string) for string in string_list]

strings = ["apple", "banana", "cherry"]
lengths = get_lengths(strings)
print(lengths)
