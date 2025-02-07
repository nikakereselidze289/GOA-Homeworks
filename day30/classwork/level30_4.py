def manual_swapcase(input_str):
    swapped_str = ''
    for char in input_str:
        if char.islower():
            swapped_str += char.upper()
        elif char.isupper():
            swapped_str += char.lower()
        else:
            swapped_str += char
    return swapped_str

input_str = input("Enter a string: ")
print("String after swapcase:", manual_swapcase(input_str))
