# Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None



# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return string.swapcase()



# Correct the mistakes of the character recognition software
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s



# Is it a palindrome?
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]  



# Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"



# Student's Final Grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0



# Sum The Strings
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)
