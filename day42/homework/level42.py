# 3) Create a dictionary with at least five key-value pairs and print all the keys using the keys() method.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer', 'hobby': 'Reading'}
print("Keys:", my_dict.keys())

# 4) Create a dictionary and print all the values using the values() method.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'London'}
print("Values:", my_dict.values())

# 5) Create a dictionary and print all key-value pairs using the items() method.
my_dict = {'name': 'Bob', 'age': 22, 'city': 'Paris'}
print("Key-Value Pairs:", my_dict.items())

# 6) Iterate over a dictionary using the items() method and print each key with its corresponding value.
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 7) Create a dictionary and check if a specific key exists using the in operator.
my_dict = {'name': 'Eve', 'age': 28, 'city': 'Berlin'}
if 'name' in my_dict:
    print("The key 'name' exists in the dictionary.")

# 8) Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.
my_dict = {'name': 'David', 'age': 35, 'city': 'Madrid'}
age = my_dict.get('age', 'Key not found')
print("Age:", age)
city = my_dict.get('country', 'Key not found')
print("Country:", city)

# 9) Add a new key-value pair to an existing dictionary and print the updated dictionary.
my_dict = {'name': 'Sara', 'age': 26}
my_dict['city'] = 'Tokyo'
print("Updated Dictionary:", my_dict)

# 10) Remove a key-value pair from a dictionary using the pop() method and print the updated dictionary.
my_dict = {'name': 'Tom', 'age': 40, 'city': 'Sydney'}
my_dict.pop('city')
print("Updated Dictionary after pop:", my_dict)

# 11) Update an existing dictionary with another dictionary using the update() method.
my_dict = {'name': 'Grace', 'age': 31}
update_dict = {'city': 'Rome', 'job': 'Artist'}
my_dict.update(update_dict)
print("Updated Dictionary after update:", my_dict)

# 12) Create a dictionary and print its length using the len() function.
my_dict = {'name': 'Leo', 'age': 29, 'city': 'Berlin', 'job': 'Teacher'}
print("Length of Dictionary:", len(my_dict))

# 13) Write a function that returns the sum of all numeric values in a dictionary.
def sum_numeric_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

my_dict = {'a': 5, 'b': 10, 'c': 3}
print("Sum of numeric values:", sum_numeric_values(my_dict))

# 14) Clear all elements from a dictionary using the clear() method and print the result.
my_dict = {'name': 'Nina', 'age': 24, 'city': 'Amsterdam'}
my_dict.clear()
print("Dictionary after clear:", my_dict)

# 15) Create dictionary about your information, use at least 10 key-value pairs
my_info = {
    'name': 'ChatGPT',
    'age': 0,
    'profession': 'AI Assistant',
    'location': 'Virtual',
    'languages': ['English', 'Spanish', 'French'],
    'hobbies': ['Writing', 'Coding', 'Learning'],
    'favorite_color': 'Blue',
    'year_created': 2023,
    'version': 'GPT-4',
    'creator': 'OpenAI'
}
print("My Information:", my_info)
