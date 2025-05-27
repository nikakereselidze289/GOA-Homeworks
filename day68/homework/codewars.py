# Disemvowel Trolls
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

# Square Every Digit
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))


# Highest and Lowest
def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"

# 2nd variation
def high_and_low(numbers):
    nums = numbers.split()
    int_nums = []

    for i in nums: int_nums.append(int(i))

    return f"{max(int_nums)} {min(int_nums)}"

# 3rd variation
def high_and_low(numbers):
    nums = [int(i) for i in numbers.split(" ")]
    return f"{max(nums)} {min(nums)}"


# List Filtering
def filter_list(l):
    res = []

    for i in l:
        if type(i)!=str:
            res.append(i)

    return res

# 2nd variation
def filter_list(l):
    return [i for i in l if type(i)!=str]


# Descending Order
def descending_order(num):
    num_str = str(num)
    sorted_digits = sorted(num_str, reverse=True)
    sorted_str = ''.join(sorted_digits)
    return int(sorted_str)


#  You're a square!
import math

def is_square(n):
    if n < 0:
        return False
    return math.isqrt(n) ** 2 == n

# Get the Middle Character
def get_middle(s):
    length = len(s)
    
    if length % 2 == 1:
        return s[length // 2]
    else:
        return s[(length // 2) - 1: (length // 2) + 1]



# Isograms
def is_isogram(string):
    string = string.lower()
    
    seen_chars = set()
    
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True



# Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# Jaden Casing Strings
def to_jaden_case(string):
    # Split the string into words, capitalize each word, and then join them back into a string
    return ' '.join([word.capitalize() for word in string.split()])
