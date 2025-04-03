# Double Char
def double_char(s):
    return ''.join(c * 2 for c in s)


# Parse nice int from char problem
def get_age(age):
    return int(age[0])



# The Feast of Many Beasts
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# Array plus array
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


# Grasshopper - Check for factor
def check_for_factor(base, factor):
    return base % factor == 0
