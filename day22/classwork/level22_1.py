my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

index = int(input("შემოიტანეთ რიცხვი: "))

if 0 <= index < len(my_list):
    print("ელემენტი:", my_list[index])
elif len(my_list) * -1 <= index <= -1:
    print("ელემენტი:", my_list[index])
else:
    print("არასწორი ინდექსი!")
