def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check_even_odd(num_list)
