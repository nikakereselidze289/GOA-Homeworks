start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    print("The starting number should be less than or equal to the ending number.")
else:
    sum_of_numbers = 0

    for num in range(start, end + 1):
        sum_of_numbers += num

    print("The sum of numbers between", start, "and", end, "is:", sum_of_numbers)
