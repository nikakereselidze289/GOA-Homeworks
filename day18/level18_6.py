correct_password = "Goa best"
incorrect_count = 0

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Password correct!")
        break
    else:
        incorrect_count += 1
        print("Incorrect password. Try again.")
        
print("Number of incorrect attempts:", incorrect_count)
