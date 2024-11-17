print("First person:")
name=input("insert name: ")
surname=input("insert surname: ")
age=int(input("insert age: "))

print("\nSecond person:")

name1=input("insert name: ")
surname1=input("insert surname: ")
age1=int(input("insert age: "))

print("\nThird person:")

name2=input("insert name: ")
surname2=input("insert surname: ")
age2=int(input("insert age: "))

print(f"\n{name} {surname}'s age is {age}")
print(f"{name1} {surname1}'s age is {age1}")
print(f"{name2} {surname2}'s age is {age2}")

print(f"arithmetic average of ages: {(age + age1 + age2) / 2}")




