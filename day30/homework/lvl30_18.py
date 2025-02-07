string = input("Enter a string: ")
index = string.lower().find("hello")

if index != -1:
    print(f"The word 'hello' first appears at index: {index}")
else:
    print("The word 'hello' was not found.")
