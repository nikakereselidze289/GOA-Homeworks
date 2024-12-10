correct_pas = "Goa best"
count = 0
user_password = input("Enter password: ")

while user_password != correct_pas:
    count += 1
    user_password = input("Enter password: ")
print("Correct password!")
print("You needed", count, "tries")