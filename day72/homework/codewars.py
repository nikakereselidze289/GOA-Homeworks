# Regex validate PIN code
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    if not pin.isdigit():
        return False
    return True


# Is this a triangle?
def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a



# Two to One
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


# Categorize New Member
def open_or_senior(data):
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]




# Find the next perfect square!
import math

def find_next_square(sq):
    root = math.isqrt(sq)  
    if root * root == sq:
        return (root + 1) ** 2
    else:
        return -1
