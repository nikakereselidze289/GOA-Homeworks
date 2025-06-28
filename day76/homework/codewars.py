# Sum of odd numbers
def row_sum_odd_numbers(n):
    start = n * n - (n - 1)
    return sum(start + 2 * i for i in range(n))


# 2nd variation
def row_sum_odd_numbers(n):
    start_num = 1
    res = []

    for i in range(1, n+1):
        ls = []
        for x in range(i):
            ls.append(start_num)
            start_num += 2
        res.append(sum(ls))

    return res[-1]


# Printer Errors
def printer_error(s):
    valid = "abcdefghijklm"
    res = 0

    for i in s:
        if i not in valid: res += 1

    return f"{res}/{len(s)}"


# Reverse words
def reverse_words(text):
    str_list=text.split(" ")
    result = []
    for i in str_list:
        result.append(i[::-1])
    return " ".join(result)


# Ones and Zeros
def binary_array_to_number(arr):
    res = ""
    for bit in arr:
        res += str(bit)
    return int(res, 2)


# Number of People in the Bus
def number(bus_stops):
    people = 0
    for on, off in bus_stops:
        people += on
        people -= off
    return people



# Odd or Even?
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"



# The highest profit wins!
def min_max(lst):
    return [min(lst), max(lst)]



