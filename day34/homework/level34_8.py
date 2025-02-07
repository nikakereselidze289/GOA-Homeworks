def find_maximum(numbers):
    if not numbers:
        return None  
    
    max_number = numbers[0]  
    
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    
    return max_number

num_list = [3, 7, 2, 8, 5, 9, 1]
maximum = find_maximum(num_list)
print("The maximum number is:", maximum)
