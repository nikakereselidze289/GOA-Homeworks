def sum_divisible_by_three(start, end):
    total_sum = 0
    
    for number in range(start, end + 1):
        if number % 3 == 0:
            total_sum += number
    
    return total_sum

result = sum_divisible_by_three(1, 100)
print("The sum of all numbers divisible by 3 from 1 to 100 is:", result)
