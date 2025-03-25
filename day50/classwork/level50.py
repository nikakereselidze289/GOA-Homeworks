# TypeError-ის მაგალითი:
num = 10

try:
    print(num + "5")
except TypeError as e:
    print(f"TypeError მოხდა: {e}")




# მომხმარებლის მიერ შემოტანილი მონაცემების მიღება და შეცდომების დამუშავება:
try:
    user_input = input("გთხოვთ შეიტანოთ თქვენი სახელი: ")
    
    if not user_input:
        raise ValueError("სახელი არ შეიძლება იყოს ცარიელი!")

    print(f"თქვენი სახელი: {user_input}")

except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"დაფიქსირდა შეცდომა: {e}")

