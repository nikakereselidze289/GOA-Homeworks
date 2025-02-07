name = input("Enter your name: ")
choice = input("Enter 'u' for uppercase or 'l' for lowercase: ")

if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("Wrong information.")
