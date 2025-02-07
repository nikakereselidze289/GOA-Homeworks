# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter the operator (+, -, *, /): ")

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Invalid operator"

# print("Result:", result)


# second option
# Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation. Display the result and end the program.
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
operator = input("Choose one operator: +, -, *, /, **, %  ")

if operator == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("გაყოფა 0-ზე არ შეიძლება")
    else:
        print(num1, "/", num2, "=", num1/num2)
elif operator == "**":
    print(num1, "**", num2, "=", num1**num2)
elif operator == "%":
    print(num1, "%", num2, "=", num1%num2)
else:
    print("Wrong operator")
