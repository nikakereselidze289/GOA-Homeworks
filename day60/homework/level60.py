# The Wide-Mouthed frog!
def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"


# Get Nth Even Number
def nth_even(n):
    return (n - 1) * 2



# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in st)



# 5 without numbers !!
def unusual_five():
    return len("abcde")



# Add Length
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]
