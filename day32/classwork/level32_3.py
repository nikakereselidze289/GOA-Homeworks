def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)

main_string = input("Enter the main string: ")
string_to_split = input("Enter the string to split by: ")

my_split(main_string, string_to_split)
