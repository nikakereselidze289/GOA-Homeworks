correct_password = "my_secret"
user_password = input("Enter the password: ")

while user_password != correct_password:
    print("Incorrect password. Try again.")
    user_password = input("Enter the password: ")

print("Access granted!")