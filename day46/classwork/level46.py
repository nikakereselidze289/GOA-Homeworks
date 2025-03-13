# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

# თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით
def custom_range(start_point, end_point, step_size, comparison_value):
    return [num for num in range(start_point, end_point, step_size) if num > comparison_value]

print(custom_range(0, 20, 2, 10))   
print(custom_range(5, 30, 5, 15))   
print(custom_range(10, 50, 10, 20)) 


# Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by either 3 or 5, but not both.
result = [num for num in range(1, 101) if (num % 3 == 0) != (num % 5 == 0)]
print(result)



# Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 (a palindromic number reads the same forward and backward).
palindromic_numbers = [number for number in range(10, 201) if str(number) == str(number)[::-1]]
print(palindromic_numbers)
