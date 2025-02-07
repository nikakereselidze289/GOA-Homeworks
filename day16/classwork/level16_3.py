my_num = 7
counter = 0
user_input = 0

while user_input != my_num:
    user_input = int(input("გამოიცანით რიცხვი (1-დან 10-მდე): "))
    counter += 1

print("you guessed")
print(f"ცდა {counter} იყო საჭირო")
