correct_username = "user123"
correct_password = "my_secret"

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect username or password. Please try again.")
