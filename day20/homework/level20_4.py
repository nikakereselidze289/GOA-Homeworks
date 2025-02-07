start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

while start > end:
    print("The starting number should be less than or equal to the ending number.")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

sum_of_numbers = sum(range(start, end + 1))

print(f"The sum of numbers between {start} and {end} is: {sum_of_numbers}")
