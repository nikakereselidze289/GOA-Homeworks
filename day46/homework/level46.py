# 2) Generate a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]

# 3) Generate a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]

# 4) Create a list of all even numbers between 1 and 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# 5) Generate a list of the first letters of each word in a given list of words
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]

# 6) Create a list comprehension that converts all words in a given list to uppercase
upper_words = [word.upper() for word in words]

# 7) Generate a list of numbers from 1 to 50 that are divisible by 3
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]

# 8) Extract words with more than 4 letters from a given list of words
long_words = [word for word in words if len(word) > 4]

# 9) Convert a list of temperature values in Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

# 10) Find all prime numbers between 1 and 100
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]

# 11) Extract words from a given sentence that contain at least one vowel and are longer than 5 characters
sentence = "This is an example sentence for testing purposes"
words_in_sentence = sentence.split()
long_vowel_words = [word for word in words_in_sentence if len(word) > 5 and any(vowel in word for vowel in "aeiou")]

# 12) Generate a sequence of Fibonacci numbers up to the 20th term
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, 20)]
