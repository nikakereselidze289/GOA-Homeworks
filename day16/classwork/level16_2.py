correct_password = "mypassword"
counter = 0

while user_input != correct_password:
    user_input = input("გთხოვთ შეიყვანოთ პაროლი: ")
    counter += 1

print("access granted")
print(f"პაროლი {counter} ჯერ შეიყვანეთ")
