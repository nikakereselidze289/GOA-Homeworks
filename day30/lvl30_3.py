def convert_to_uppercase(string_list):
    return [string.upper() for string in string_list]

lowercase_strings = ["hello", "world", "python"]
uppercase_strings = convert_to_uppercase(lowercase_strings)

print(uppercase_strings)