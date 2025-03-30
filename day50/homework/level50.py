try:
    number = float(input("Please enter a number: "))
except ValueError:
    print("Error: That's not a valid number.")

my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[10])
except IndexError:
    print("Error: Index out of range.")

try:
    result = "Hello" + 5
except TypeError:
    print("Error: Cannot add a string and an integer.")
