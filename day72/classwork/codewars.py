# Shortest Word
def find_short(s):
    s=s.split()
    lenghts=[]
    for i in s:
        lenghts.append(len(i))
    return min(lenghts)

# String ends with?
def solution(text, ending):
    return text.endswith(ending)

# Mumbling
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# 2nd variation
def accum(st):
    res = []

    for i in range(len(st)):
        chr = st[i]
        new_str = chr*(i+1)
        res.append(new_str.capitalize())

    return "-".join(res)


# Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    # Sort the numbers in ascending order
    numbers.sort()
    # Return the sum of the first two numbers
    return numbers[0] + numbers[1]


# Complementary DNA
def DNA_strand(dna):
    complementary_dna = ""
    
    for nucleotide in dna:
        if nucleotide == 'A':
            complementary_dna += 'T'
        elif nucleotide == 'T':
            complementary_dna += 'A'
        elif nucleotide == 'C':
            complementary_dna += 'G'
        elif nucleotide == 'G':
            complementary_dna += 'C'
    
    return complementary_dna


# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    return sum(range(min(a, b), max(a,b)+1))

# Friend or Foe
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res


# Credit Card Mask
def maskify(cc):
    if len(cc) <= 4:
        return cc
    return '#' * (len(cc) - 4) + cc[-4:]


# Binary Addition
