# 1. User Input Number Division
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 2. List Index Access
def access_list_index():
    my_list = [10, 20, 30, 40, 50]
    try:
        index = int(input("Enter an index to access (0-4): "))
        print(f"Value at index {index}: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# 3. Dictionary Key Access
def access_dict_key():
    my_dict = {"apple": 1, "banana": 2, "cherry": 3}
    key = input("Enter a key to access: ")
    try:
        print(f"Value for '{key}': {my_dict[key]}")
    except KeyError:
        print("Error: Key not found in dictionary.")

# 4. Convert String to Integer
def convert_to_integer():
    user_input = input("Enter a number to convert to integer: ")
    try:
        number = int(user_input)
        print(f"Converted number: {number}")
    except ValueError:
        print("Error: Invalid number format.")

# 5. Function as Argument – Greeting
def say_hello():
    print("Hello! Have a great day.")

def greet(func):
    print("Calling the greeting function:")
    func()

# 6. Return a Function – Multiplier
def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor

# Example usage
if __name__ == "__main__":
    print("\n1. Division")
    divide_numbers()
    
    print("\n2. List Index Access")
    access_list_index()
    
    print("\n3. Dictionary Key Access")
    access_dict_key()
    
    print("\n4. Convert String to Integer")
    convert_to_integer()
    
    print("\n5. Function as Argument")
    greet(say_hello)
    
    print("\n6. Return a Function – Multiplier")
    times_three = multiplier(3)
    print(f"3 multiplied by 4 is: {times_three(4)}")
