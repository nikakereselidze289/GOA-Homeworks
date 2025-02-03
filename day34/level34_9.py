def filter_positive_numbers(numbers):
    positive_numbers = []
    
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    
    return positive_numbers

num_list = [-10, 15, -3, 7, 0, -1, 5, -6]
positive_list = filter_positive_numbers(num_list)
print("The list of positive numbers is:", positive_list)
