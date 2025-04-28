# 2
add_five = lambda x: x + 5

# 3
multiply = lambda x, y: x * y

# 4
is_even = lambda x: x % 2 == 0

# 5
c_to_f = lambda c: list(map(lambda x: (x * 9/5) + 32, c))

# 6
starts_with_A = lambda s: s.startswith('A')

numbers = [10, 20, 30, 40, 50]
words = ['apple', 'banana', 'cherry']
names = ['Alice', 'Bob', 'Charlie']
temperatures_c = [0, 25, 100]
mixed_numbers = [45, 55, 60, 30, 80]

# 7
add_ten = list(map(lambda x: x + 10, numbers))

# 8
to_upper = list(map(lambda s: s.upper(), words))

# 9
word_lengths = list(map(lambda s: len(s), words))

# 10
squares = list(map(lambda x: x ** 2, numbers))

# 11
int_to_str = list(map(lambda x: str(x), numbers))

# 12
greet_names = list(map(lambda name: "Hello " + name, names))

# 13
subtract_five = list(map(lambda x: x - 5, numbers))

# 14
multiply_by_three = list(map(lambda x: x * 3, numbers))

# 15
c_to_f_map = list(map(lambda c: (c * 9/5) + 32, temperatures_c))

# 16
greater_than_50 = list(map(lambda x: x > 50, mixed_numbers))
#17
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 18
greater_than_10 = list(filter(lambda x: x > 10, numbers))

# 19
long_words = list(filter(lambda x: len(x) > 5, words))

# 20
non_empty_strings = list(filter(lambda x: x != '', words))

# 21
positive_numbers = list(filter(lambda x: x > 0, more_numbers))

# 22
names_starting_with_A = list(filter(lambda name: name.startswith('A'), names))

# 23
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))

# 24
words_with_e = list(filter(lambda word: 'e' in word, words))

# 25
no_none_values = list(filter(lambda x: x is not None, mixed_list))

# 26
less_or_equal_50 = list(filter(lambda x: x <= 50, more_numbers))
