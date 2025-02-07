def find_char_index(string, char):
    return string.find(char)

string = input("Enter a string: ")
char = input("Enter the character to find: ")

index = find_char_index(string, char)

if index != -1:
    print(f"The character '{char}' is found at index: {index}")
else:
    print(f"The character '{char}' was not found.")
