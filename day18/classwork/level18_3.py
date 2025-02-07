num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
total = 0

if num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            print(i)
            total += i
else:
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)
            total += i

print("ჯამი:", total)
