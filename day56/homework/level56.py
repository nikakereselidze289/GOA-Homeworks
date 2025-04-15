# Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None



# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return string.swapcase()



# Correct the mistakes of the character recognition software
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s



# Is it a palindrome?
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]  



# Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"



# Student's Final Grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0



# Sum The Strings
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)


# Expressions Matter
def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)

# I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"
    
    
    
# Reverse List Order
def reverse_list(l):
    res = []
    for i in range(len(l)-1, -1, -1): res.append(l[i])
    return res


# Count Odd Numbers below n
def odd_count(n):
    return n//2


# Difference of Volumes of Cuboids
def find_difference(a, b):
    return abs((a[0]*a[1]*a[2]) - (b[0]*b[1]*b[2]))


# Welcome!
def greet(language):
    all_lang = [ 
        ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
    ]
    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"

# Drink about
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"



# Sort and Star
def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]


# Grasshopper - Messi Goals
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# Short Long Short
def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
    
    
# My head is at the wrong end!
def fix_the_meerkat(arr):
    arr.reverse()
    return arr


# Find Multiples of a Number
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]


# Unfinished Loop - Bug Fixing #1
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1  # 🔧 Fix: increment i
    return res











# 2) Print your name
print("John Doe")

# 3) Print a favorite quote
print('"The only limit to our realization of tomorrow is our doubts of today."')

# 4) Print multiple lines (short poem)
print("Roses are red,")
print("Violets are blue,")
print("Coding is fun,")
print("Especially with you.")

# 5) Print a simple math result
print("2 + 3 =", 2 + 3)

# 6) Print a shape with symbols (triangle)
print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print("Converted number:", num_int)

# 8) Add two floats
float1 = 3.5
float2 = 2.5
result = float1 + float2
print("Sum of floats:", result)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
greeting = str1 + " " + str2
print("Concatenated string:", greeting)

# 10) Print data types
a = 10           # int
b = "Python"     # str
c = 3.14         # float

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

# 11) User input and type conversion
age = input("Enter your age: ")
next_year_age = int(age) + 1
print("Next year, you will be", next_year_age)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year’s age
age = input("How old are you? ")
next_year_age = int(age) + 1
print("Next year, you will be", next_year_age)

# 14) Simple calculator: addition
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print("The sum is:", sum_result)

# 15) Favorite color
favorite_color = input("What is your favorite color? ")
print("Your favorite color is", favorite_color + "!")

# 16) Check if the user is tall enough
height = int(input("What is your height in cm? "))
if height > 150:
    print("You are tall enough!")
else:
    print("You are not tall enough.")

# 17) Print numbers from 1 to 5 using a for loop
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
string = "Python"
for letter in string:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for num in range(1, 11):
    total += num
print("The sum of numbers from 1 to 10 is:", total)

# 20) Print a multiplication table (1 to 5) for the number 2
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")

# 21) Print all even numbers between 2 and 20
for num in range(2, 21, 2):
    print(num)

# 22) Print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1
    
    # 23) Sum of numbers 1 to 5 using a while loop
i = 1
sum_numbers = 0
while i <= 5:
    sum_numbers += i
    i += 1
print("Sum of numbers from 1 to 5:", sum_numbers)

# 24) Count down from 10 to 1 using a while loop
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print all odd numbers between 1 and 10 using a while loop
i = 1
while i <= 10:
    if i % 2 != 0:  # Check if the number is odd
        print(i)
    i += 1

# 26) Ask for user input until they enter "exit"
while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break

# 27) Print all elements of a list
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)

# 28) Find the length of a list
my_list = ["apple", "banana", "cherry"]
print("Length of the list:", len(my_list))

# 29) Access a specific element from the list (second element, index 1)
my_list = [10, 20, 30, 40]
print("The second element is:", my_list[1])

# 30) Add an element to the list
my_list = ["apple", "banana", "cherry"]
my_list.append("date")
print("Updated list:", my_list)

# 31) Remove an element from the list
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")  # Removing 'banana'
print("List after removal:", my_list)

# 32) Create a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]
print("List of squares:", squares)

# 33) Create a list of even numbers using list comprehension
even_numbers = [x for x in range(2, 11, 2)]  # From 2 to 10 inclusive
print("List of even numbers:", even_numbers)

# 34) Filter odd numbers from a list using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in numbers if x % 2 != 0]
print("List of odd numbers:", odd_numbers)

# 35) Convert a list of strings to uppercase using list comprehension
strings = ["hello", "world", "python"]
uppercase_strings = [s.upper() for s in strings]
print("List of uppercase strings:", uppercase_strings)

# 36) Create a list of numbers squared if they are divisible by 2
numbers = [1, 2, 3, 4, 5, 6]
squared_if_divisible_by_2 = [x**2 for x in numbers if x % 2 == 0]
print("Squared numbers divisible by 2:", squared_if_divisible_by_2)

# 37) Function to greet a user
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# 38) Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

sum_result = add_two_numbers(5, 7)
print("Sum of 5 and 7:", sum_result)

# 39) Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(10)
print("10 is", result)

# 40) Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 8)
print("Area of the rectangle (5x8):", area)

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

reversed_str = reverse_string("hello")
print("Reversed string:", reversed_str)

# 42) Create and print a tuple
my_tuple = (42, "apple", 3.14)
print("Tuple:", my_tuple)

# 43) Access an element in a tuple (second element, index 1)
my_tuple = (10, 20, 30, 40)
print("Second element:", my_tuple[1])

# 44) Find the length of a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Length of the tuple:", len(my_tuple))

# 45) Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# 46) Check if an item exists in a tuple
my_tuple = (10, 20, 30, 40)
if 20 in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {10, "apple", 3.14}
print("Set:", my_set)

# 48) Check if an element is in a set
my_set = {10, "apple", 3.14}
if "apple" in my_set:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
my_set = {10, "apple", 3.14}
my_set.add("banana")  # Adding 'banana' to the set
print("Updated set:", my_set)

# 50) Remove an element from a set
my_set = {10, "apple", 3.14}
my_set.remove("apple")  # Removing 'apple' from the set
print("Updated set after removal:", my_set)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Union of set1 and set2
print("Union of sets:", union_set)

# 52) Create and print a dictionary
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)

# 53) Access a value by key
my_dict = {"name": "Alice", "age": 25}
print("Value associated with 'name':", my_dict["name"])

# 54) Add a new key-value pair to a dictionary
my_dict = {"name": "Alice", "age": 25}
my_dict["city"] = "New York"  # Adding a new key-value pair
print("Updated dictionary:", my_dict)









# CODE WARS

# Basic variable assignment
a = "code"  
b = "wa.rs" 
name = a + b  

# get character from ASCII Value
def get_char(c):
    return chr(c)




