my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = int(input("შეიყვანეთ რიცხვი: "))

if 0 <= index < 10:
    print("ელემენტი ამ ინდექსზე:", my_list[index])

elif -10 <= index <= -1:
    print("ელემენტი ამ ინდექსზე:", my_list[index])
else:
    print("შეიყვანეთ სწორი ინდექსი.")


list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for num in list1:
    print("გამრავლებული 2-ზე:", num * 2)
    print("გაყოფილი 2-ზე:", num / 2)
    print()

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for num in list1:
    print(num * 2, num / 2)
