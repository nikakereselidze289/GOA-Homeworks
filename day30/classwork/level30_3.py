def count_occurrences(main_str, str_to_count):
    count = main_str.count(str_to_count)
    return count

# Example usage:
main_str = input("Enter the main string: ")
str_to_count = input("Enter the string to count: ")

print(f"The string '{str_to_count}' appears {count_occurrences(main_str, str_to_count)} times in the main string.")
